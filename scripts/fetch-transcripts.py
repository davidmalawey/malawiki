#!/usr/bin/env python3
"""
fetch-transcripts.py — host-side transcript ingestion via yt-dlp

Why this exists:
  The yt-transcript-fetch Cowork skill works from a Chrome extension on
  Anthropic's sandboxed host. As of 2026-04-24, YouTube tightened pot-token
  enforcement on the legacy transcript engagement panel, so the in-sandbox
  Chrome path now succeeds only for videos in the (~2-3% sampled) modern-
  panel rollout cohort. yt-dlp running on YOUR machine, with its actively-
  maintained pot-token handling, bypasses all of that.

What this script does:
  - Accepts one or more YouTube video IDs (or watch URLs)
  - Calls yt-dlp to fetch ONLY the auto-generated English captions + video
    metadata (no audio, no video, no thumbnails — fast, ~200 KB per video)
  - Parses the .vtt output into [MM:SS] segments matching the existing
    raw/transcripts/*.md format used by the wiki ingest workflow
  - Writes the transcript file with full frontmatter (title, channel,
    published date, duration, view count at capture time, etc.)
  - Verifies the channel matches the KB's active creator (boundary check)
    before writing — same posture as the in-skill version

Requirements:
  - Python 3.9+
  - yt-dlp installed:  pip install -U yt-dlp
  - Network access to youtube.com (i.e., not running in the Anthropic sandbox)

Usage:
  # One video by ID
  python scripts/fetch-transcripts.py W0sAR_jI4b8

  # One video by URL
  python scripts/fetch-transcripts.py 'https://www.youtube.com/watch?v=W0sAR_jI4b8'

  # Many videos at once (each captured serially, channel boundary checked)
  python scripts/fetch-transcripts.py W0sAR_jI4b8 cLrIE6ltErE B1QqAZeEfes

  # From a file (one ID/URL per line)
  python scripts/fetch-transcripts.py --from-file targets.txt

  # Pull every long-form video in the inventory that's not already in raw/transcripts/
  python scripts/fetch-transcripts.py --catch-up

  # Override the KB root (default: parent dir of this script's folder)
  python scripts/fetch-transcripts.py --kb-root /path/to/YT-David-Malawey-KB W0sAR_jI4b8

Output:
  - raw/transcripts/YYYY-MM-DD_<slug>.md   (one per video)
  - log.md                                  (appends an entry per run)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# --- Configuration ---------------------------------------------------------

# Boundary identifier — only writes transcripts for videos whose channelId
# matches. Set to None to disable the check (e.g. when porting this script
# to another KB).
KB_CHANNEL_ID = "UCwirLDXiN1ybgPyIDNt85PA"  # @davidmalawey
KB_CHANNEL_NAME = "David Malawey"

# --- Helpers ---------------------------------------------------------------

VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
WATCH_URL_RE = re.compile(r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([A-Za-z0-9_-]{11})")


def normalize_to_video_id(token: str) -> str | None:
    """Accept '0_Ab3MyVxiE', a watch URL, or a shorts URL — return the bare 11-char ID."""
    token = token.strip()
    if VIDEO_ID_RE.match(token):
        return token
    m = WATCH_URL_RE.search(token)
    return m.group(1) if m else None


def slugify(title: str) -> str:
    """Kebab-case ASCII slug for filenames."""
    s = title.lower()
    s = re.sub(r"['’]", "", s)            # strip apostrophes
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s[:80] or "untitled"


def parse_vtt(vtt_text: str) -> list[tuple[str, str]]:
    """Parse a .vtt file into [(timestamp_label, text), ...].

    Timestamps are normalized to MM:SS or H:MM:SS (no fractional seconds).
    Consecutive duplicate text blocks (yt-dlp's stale-frame artifact) are
    deduplicated.
    """
    out: list[tuple[str, str]] = []
    last_text = None
    block_lines: list[str] = []
    cur_start: str | None = None
    for line in vtt_text.splitlines():
        line = line.strip()
        if not line:
            if cur_start and block_lines:
                txt = " ".join(block_lines).strip()
                # Strip <c> color/karaoke markup that yt-dlp leaves in
                txt = re.sub(r"<[^>]+>", "", txt)
                # Collapse repeated whitespace
                txt = re.sub(r"\s+", " ", txt)
                if txt and txt != last_text:
                    out.append((cur_start, txt))
                    last_text = txt
            cur_start, block_lines = None, []
            continue
        # Cue header line: "00:00:01.234 --> 00:00:04.567 ..."
        if "-->" in line:
            start = line.split("-->")[0].strip()
            # Convert HH:MM:SS.fff to H:MM:SS or MM:SS
            t = start.split(".")[0]               # drop fractional secs
            h, m, s = t.split(":")
            cur_start = (f"{int(h)}:{m}:{s}" if int(h) else f"{int(m)}:{s}")
            block_lines = []
            continue
        # Skip metadata: WEBVTT header, NOTE comments, numeric cue indices
        if line in ("WEBVTT", "Kind: captions", "Language: en"):
            continue
        if line.startswith(("WEBVTT", "NOTE", "STYLE")) or line.isdigit():
            continue
        # Otherwise this is caption text
        if cur_start:
            block_lines.append(line)
    # Flush trailing block
    if cur_start and block_lines:
        txt = " ".join(block_lines).strip()
        txt = re.sub(r"<[^>]+>", "", txt)
        txt = re.sub(r"\s+", " ", txt)
        if txt and txt != last_text:
            out.append((cur_start, txt))
    return out


def yt_dlp_call(video_id: str, work_dir: Path) -> dict:
    """Run yt-dlp once. Returns parsed JSON metadata + path to the .vtt file."""
    work_dir.mkdir(parents=True, exist_ok=True)
    # Templated filenames so we can predict the output paths
    out_tpl = str(work_dir / f"{video_id}.%(ext)s")
    # Invoke via the running interpreter's `python -m yt_dlp` so we work
    # whether or not the `yt-dlp` console-script is on PATH.
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--skip-download",            # captions/metadata only, no video
        "--write-auto-sub",            # ASR-generated captions
        "--sub-lang", "en",
        "--sub-format", "vtt",
        "--write-info-json",           # full metadata to <id>.info.json
        "--no-warnings",
        "-o", out_tpl,
        f"https://www.youtube.com/watch?v={video_id}",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except FileNotFoundError:
        sys.exit("ERROR: yt_dlp module not importable.  Install with:  pip install -U yt-dlp")
    except subprocess.TimeoutExpired:
        return {"error": "timeout (120s)"}
    if result.returncode != 0:
        return {"error": result.stderr.strip().splitlines()[-1] if result.stderr else "unknown yt-dlp error"}

    info_path = work_dir / f"{video_id}.info.json"
    vtt_path = work_dir / f"{video_id}.en.vtt"
    if not info_path.exists():
        return {"error": "info.json missing"}
    info = json.loads(info_path.read_text(encoding="utf-8"))
    if not vtt_path.exists():
        return {"error": "no English auto-captions for this video", "info": info}
    return {"info": info, "vtt_text": vtt_path.read_text(encoding="utf-8")}


def render_transcript_md(info: dict, segments: list[tuple[str, str]], chapters: list[tuple[str, str]]) -> str:
    """Render a transcript markdown file matching raw/transcripts/ format."""
    upload_date = info.get("upload_date", "")           # YYYYMMDD
    iso_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}" if len(upload_date) == 8 else ""
    duration_sec = int(info.get("duration", 0))
    h, rem = divmod(duration_sec, 3600)
    m, s = divmod(rem, 60)
    duration_label = f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

    # Frontmatter
    lines: list[str] = ["---"]
    lines.append(f"title: \"{info.get('title', '').replace(chr(34), chr(39))}\"")
    lines.append(f"url: \"https://www.youtube.com/watch?v={info['id']}\"")
    lines.append(f"video_id: \"{info['id']}\"")
    lines.append(f"channel: \"{info.get('uploader', '')}\"")
    lines.append(f"channel_id: \"{info.get('channel_id', '')}\"")
    lines.append(f"channel_url: \"{info.get('channel_url', '')}\"")
    lines.append(f"published: {iso_date}")
    lines.append(f"duration: \"{duration_label}\"")
    lines.append(f"duration_sec: {duration_sec}")
    lines.append(f"views: {info.get('view_count') or 0}")
    lines.append(f"likes: {info.get('like_count') or 0}")
    lines.append(f"category: \"{(info.get('categories') or ['unknown'])[0]}\"")
    keywords = info.get("tags") or []
    lines.append(f"keywords: {json.dumps(keywords)}")
    lines.append(f"thumbnail_url: \"https://i.ytimg.com/vi/{info['id']}/maxresdefault.jpg\"")
    lines.append(f"is_live: false")
    lines.append(f"was_live: {str(bool(info.get('was_live'))).lower()}")
    lines.append(f"is_upcoming: false")
    lines.append(f"source: \"yt-dlp via fetch-transcripts.py\"")
    lines.append(f"acquired: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}")
    lines.append(f"transcript_segments: {len(segments)}")
    lines.append(f"chapters_count: {len(chapters)}")
    desc = (info.get("description") or "").strip()
    lines.append(f"has_description: {str(bool(desc)).lower()}")
    lines.append(f"has_comments: false")
    lines.append("---")
    lines.append("")

    if desc:
        lines.append("## Description")
        lines.append("")
        lines.append(desc)
        lines.append("")

    if chapters:
        lines.append("## Chapters")
        lines.append("")
        for ts, label in chapters:
            lines.append(f"- {ts} {label}")
        lines.append("")

    lines.append("## Transcript")
    lines.append("")
    for ts, text in segments:
        lines.append(f"[{ts}] {text}")
    lines.append("")
    lines.append("## Comments")
    lines.append("")
    lines.append("<!-- reserved for yt-comments-fetch skill; intentionally empty. -->")
    return "\n".join(lines) + "\n"


def extract_chapters(info: dict) -> list[tuple[str, str]]:
    """yt-dlp's info.json has chapters with start_time (seconds) + title."""
    out: list[tuple[str, str]] = []
    for c in (info.get("chapters") or []):
        sec = int(c.get("start_time", 0))
        h, rem = divmod(sec, 3600)
        m, s = divmod(rem, 60)
        ts = f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"
        out.append((ts, c.get("title", "").strip()))
    return out


def already_in_kb(kb_root: Path, video_id: str) -> Path | None:
    """Return the existing transcript file path if this video_id is already captured."""
    for p in (kb_root / "raw" / "transcripts").glob("*.md"):
        try:
            head = p.read_text(encoding="utf-8", errors="ignore")[:2000]
        except OSError:
            continue
        if re.search(r'^video_id:\s*"?' + re.escape(video_id) + r'"?', head, re.M):
            return p
    return None


def fetch_one(video_id: str, kb_root: Path, work_dir: Path) -> dict:
    """Process one video. Returns a status dict for logging."""
    existing = already_in_kb(kb_root, video_id)
    if existing:
        return {"id": video_id, "status": "skipped-already-in-kb", "path": str(existing)}

    print(f"  → fetching {video_id}", flush=True)
    result = yt_dlp_call(video_id, work_dir)
    if "error" in result and "info" not in result:
        return {"id": video_id, "status": "yt-dlp-error", "error": result["error"]}
    info = result["info"]
    if KB_CHANNEL_ID and info.get("channel_id") != KB_CHANNEL_ID:
        return {"id": video_id, "status": "boundary-mismatch",
                "got": info.get("channel_id"), "expected": KB_CHANNEL_ID}
    if "vtt_text" not in result:
        return {"id": video_id, "status": "no-captions", "title": info.get("title", "")}

    segments = parse_vtt(result["vtt_text"])
    if not segments:
        return {"id": video_id, "status": "empty-after-parse", "title": info.get("title", "")}
    chapters = extract_chapters(info)

    md = render_transcript_md(info, segments, chapters)
    upload_date = info.get("upload_date", "")
    iso_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}" if len(upload_date) == 8 else "0000-00-00"
    slug = slugify(info.get("title", "untitled"))
    out_path = kb_root / "raw" / "transcripts" / f"{iso_date}_{slug}.md"
    out_path.write_text(md, encoding="utf-8")
    return {"id": video_id, "status": "ok", "path": str(out_path),
            "segments": len(segments), "chapters": len(chapters), "title": info.get("title", "")}


# --- CLI -------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Fetch YouTube transcripts via yt-dlp into the KB format.")
    ap.add_argument("targets", nargs="*", help="Video IDs or watch URLs.")
    ap.add_argument("--from-file", help="Read targets (one per line) from this file.")
    ap.add_argument("--catch-up", action="store_true",
                    help="Process every video in inventory/@<handle>.json that isn't already in raw/transcripts/.")
    ap.add_argument("--kb-root", default=str(Path(__file__).resolve().parent.parent),
                    help="KB root directory (default: parent of scripts/).")
    ap.add_argument("--work-dir", default=None, help="Where to keep yt-dlp's intermediate files (default: kb_root/scratch/yt-dlp-work/).")
    ap.add_argument("--limit", type=int, default=None, help="Stop after N successful captures.")
    ap.add_argument("--dry-run", action="store_true", help="Print what would happen, don't write files.")
    args = ap.parse_args()

    kb_root = Path(args.kb_root).resolve()
    work_dir = Path(args.work_dir) if args.work_dir else (kb_root / "scratch" / "yt-dlp-work")

    # Build the target list
    targets: list[str] = []
    for t in args.targets:
        vid = normalize_to_video_id(t)
        if vid:
            targets.append(vid)
        else:
            print(f"  ! ignoring unrecognized target: {t}", file=sys.stderr)
    if args.from_file:
        for line in Path(args.from_file).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            vid = normalize_to_video_id(line)
            if vid:
                targets.append(vid)
    if args.catch_up:
        inv_path = kb_root / "inventory" / "@davidmalawey.json"
        if not inv_path.exists():
            sys.exit(f"--catch-up needs {inv_path}, which doesn't exist.")
        inv = json.loads(inv_path.read_text(encoding="utf-8"))
        for v in inv.get("videos", []):
            if v.get("video_id"):
                targets.append(v["video_id"])
    # Dedupe, preserve order
    seen: set[str] = set()
    targets = [v for v in targets if not (v in seen or seen.add(v))]
    if not targets:
        sys.exit("No targets given. Pass IDs/URLs, or use --from-file or --catch-up.")

    # Filter out already-in-KB unless explicitly requested via direct args
    direct = set(normalize_to_video_id(t) for t in args.targets if normalize_to_video_id(t))
    work_targets = []
    for v in targets:
        if v in direct:
            work_targets.append(v)  # explicit request; let fetch_one report skipped-already-in-kb
        else:
            if not already_in_kb(kb_root, v):
                work_targets.append(v)
    print(f"Total targets: {len(targets)} | new to fetch: {len(work_targets)} | KB root: {kb_root}", flush=True)

    if args.dry_run:
        for v in work_targets[: args.limit or 10]:
            print(f"  would fetch {v}")
        return 0

    successes = 0
    statuses: list[dict] = []
    for v in work_targets:
        if args.limit and successes >= args.limit:
            break
        s = fetch_one(v, kb_root, work_dir)
        print(f"    {s['status']}{' — ' + s.get('title', '')[:60] if s.get('title') else ''}", flush=True)
        statuses.append(s)
        if s["status"] == "ok":
            successes += 1

    # Summary log entry
    log_path = kb_root / "log.md"
    if log_path.exists():
        entry = [
            "",
            f"## [{datetime.now(timezone.utc).strftime('%Y-%m-%d')}] yt-dlp-batch | {successes} new transcripts",
            f"- Method: yt-dlp on host (bypasses Chrome-extension pot-token gating)",
            f"- Targets: {len(work_targets)} | new: {successes} | already-in-kb: {sum(1 for s in statuses if s['status'] == 'skipped-already-in-kb')} | no-captions: {sum(1 for s in statuses if s['status'] == 'no-captions')} | errors: {sum(1 for s in statuses if s['status'] == 'yt-dlp-error')}",
        ]
        for s in statuses:
            if s["status"] == "ok":
                entry.append(f"  - ✅ {s['id']} | {s['segments']} segs | {s['chapters']} chap | {s['title'][:60]}")
            elif s["status"] in ("yt-dlp-error", "no-captions", "boundary-mismatch"):
                entry.append(f"  - ❌ {s['id']} | {s['status']} | {s.get('error', s.get('title', ''))[:80]}")
        log_path.write_text(log_path.read_text(encoding="utf-8") + "\n".join(entry) + "\n", encoding="utf-8")

    print(f"\nDone. {successes} new transcripts written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
