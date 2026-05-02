# scripts/

Host-runnable utilities. These are intended to run on **your machine**, not inside the Anthropic sandbox — the sandbox has restricted egress (only `*.anthropic.com` and `*.claude.com`) and can't reach pypi or YouTube.

## fetch-transcripts.py — yt-dlp escape hatch

What: pulls YouTube auto-captions + metadata for a video (or many) and writes them to `raw/transcripts/YYYY-MM-DD_<slug>.md` in the same format the Chrome-extension skill uses, so the wiki ingest workflow keeps working unchanged.

Why: as of 2026-04-24, YouTube's pot-token (BotGuard) enforcement on the legacy transcript engagement panel made the Cowork Chrome-extension path stop working for ~98% of videos. yt-dlp running on your host has dedicated pot-token handling and bypasses this.

### One-time install

```bash
pip install -U yt-dlp
```

(Python 3.9+ recommended. yt-dlp updates often — `-U` keeps you current with their pot-token workarounds.)

### Common usage

```bash
# from the KB root
cd "C:\Users\Justin\Documents\Claude\Projects\YT - David Malawey KB"

# fetch one video (ID or URL form both work)
python scripts/fetch-transcripts.py W0sAR_jI4b8
python scripts/fetch-transcripts.py 'https://www.youtube.com/watch?v=W0sAR_jI4b8'

# fetch several at once
python scripts/fetch-transcripts.py W0sAR_jI4b8 cLrIE6ltErE B1QqAZeEfes

# fetch from a list file (one ID/URL per line; #-prefixed lines are comments)
python scripts/fetch-transcripts.py --from-file my-targets.txt

# CATCH-UP MODE: walk inventory/@davidmalawey.json and grab every long-form
# video that isn't already in raw/transcripts/. This is the big one.
python scripts/fetch-transcripts.py --catch-up

# limit to N captures per run (good for incremental work)
python scripts/fetch-transcripts.py --catch-up --limit 10

# preview mode — see what would be fetched without writing
python scripts/fetch-transcripts.py --catch-up --dry-run
```

### What gets written

For each successful video:

- `raw/transcripts/YYYY-MM-DD_<slug>.md` — frontmatter + Description + Chapters (if any) + Transcript + empty Comments stub. Same shape the wiki ingest expects.
- One entry appended to `log.md` summarizing the batch with per-video status.

Intermediate yt-dlp output (`<id>.info.json`, `<id>.en.vtt`) lands in `scratch/yt-dlp-work/`. Safe to delete once captures land.

### Channel boundary check

The script enforces `KB_CHANNEL_ID = "UCwirLDXiN1ybgPyIDNt85PA"` (Malawey). Videos belonging to a different channel are reported as `boundary-mismatch` and skipped. Edit the constant at the top of the script if you fork the KB for another creator.

### Why this is faster than fighting the sandbox

- **Sandbox path**: Chrome extension → engagement panel DOM → continuation request → blocked by pot-token gate. ~2-3% success rate.
- **yt-dlp on host**: direct innertube call with pot-token rotation. ~99% success rate. Limited only by YouTube's own throttling (yt-dlp self-paces).

### When to use the Chrome-extension skill instead

- One-off ingest where you're already in a Cowork session
- Capturing transcripts from a channel that's currently in the modern-panel rollout (the lubricant video on Malawey's channel works this way; most don't)
- When you don't want to install Python on your machine

### Output formatting notes

yt-dlp's `.vtt` parsing in this script:
- Strips fractional seconds (cue boundaries land on whole seconds)
- Strips `<c.colorCC>` karaoke/timing markup
- Deduplicates consecutive identical captions (yt-dlp emits the same line in two cues during slow speech)
- Preserves chapter info from `info.json` when present

Auto-captions are lowercase + minimal punctuation (YouTube's ASR limitation, not a script bug). Manually-uploaded captions, when available, come through with proper case and punctuation. The script doesn't try to clean either — the wiki ingest layer can do prose cleanup if needed.
