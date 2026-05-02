# Prompt — Acquire one David Malawey transcript

Copy-paste this into a fresh Sonnet session that has the Claude Chrome extension available. It's designed to fetch exactly one transcript, save it to disk in the shape the wiki expects, and then stop and ask whether to do another.

---

You are helping build a YouTube knowledge base for David Malawey's channel. Your job is to acquire **one** transcript, save it to disk in a specific format, then stop and ask whether to do another. Do not batch.

## Destination

Save the transcript file to:

```
C:\Users\Justin\Documents\Claude\Projects\YT - David Malawey KB\raw\transcripts\YYYY-MM-DD_<slug>.md
```

Where:
- `YYYY-MM-DD` is the video's upload date.
- `<slug>` is a kebab-case, ASCII-only slug derived from the video title: lowercase, strip punctuation, join words with `-`. Example: "Building a Forge from Scratch" → `building-a-forge-from-scratch`.

## Steps

1. **Check what's already there.** List files in `C:\Users\Justin\Documents\Claude\Projects\YT - David Malawey KB\raw\transcripts\`. Note which slugs/dates are already saved so you don't duplicate.

2. **Open the channel.** In Chrome, navigate to `https://www.youtube.com/@davidmalawey/videos`. Sort the videos list by "Oldest" so the earliest uploads appear first — this biases the wiki to build chronologically.

3. **Pick one video** that isn't already in `raw/transcripts/`. Default: oldest uploaded video not yet saved. If you have a reason to pick differently (e.g., the oldest video has no transcript available), say so in your final report.

4. **Open the video.** Navigate to that video's page.

5. **Extract the transcript.** Open YouTube's transcript panel (typically: click the "..." menu below the video, then "Show transcript"; or expand the description and scroll to the "Transcript" button). Keep timestamps on — the ingest schema expects `[MM:SS]` or `[H:MM:SS]` at the start of each line. Copy the full transcript text.

6. **Collect metadata:**
   - `title` — full video title
   - `url` — canonical `https://www.youtube.com/watch?v=<id>` URL
   - `video_id` — the YouTube ID
   - `published` — ISO upload date (`YYYY-MM-DD`). YouTube often shows relative dates; hover the date, or check the video description, or read `itemprop="datePublished"` from page source if needed. Infer to best of your ability.
   - `duration` — as shown on the video (`MM:SS` or `H:MM:SS`)

7. **Write the file** to `raw/transcripts/YYYY-MM-DD_<slug>.md` with this exact shape:

   ```markdown
   ---
   title: "<full video title>"
   url: "<canonical URL>"
   video_id: "<id>"
   published: <YYYY-MM-DD>
   duration: "<MM:SS>"
   channel: "David Malawey"
   source: "Claude Chrome extension"
   acquired: <today's date YYYY-MM-DD>
   ---

   # Transcript

   [0:00] first line from YouTube transcript
   [0:12] second line
   ...
   ```

   Paste the transcript verbatim — no summarization, no reformatting, no rephrasing. If YouTube emits lines without timestamps (rare), leave them as-is and add one line above the body: `<!-- Note: transcript lacked explicit timestamps -->`.

8. **Stop and report.** In chat, tell the user:
   - Which video you picked (title + URL) and why that one
   - The saved file path
   - A sanity check: first transcript line, last timestamp, total line count
   - Then ask: **"Want me to grab another?"**

## Hard rules

- Acquire exactly **one** transcript, then stop.
- Do not edit, summarize, or paraphrase the transcript text.
- Do not create or modify anything outside `raw/transcripts/`. The wiki layer (`wiki/`) is maintained by a separate ingest step in a different session.
- Do not invent metadata. If you genuinely can't find a field, leave it blank and add a `note:` in frontmatter explaining what's unverified — don't fabricate.
- If the video has no transcript available on YouTube (auto-generated not enabled), report that, skip it, pick the next-oldest video, and continue.

## Implementation notes (as of 2026-05-02)

YouTube's transcript flow is gated and partially flaky. These tactics work; older skill versions may use stale selectors or assume gates are fully closed.

### DOM selectors (new — old `ytd-transcript-segment-renderer` is gone)

After clicking "Show transcript," each segment is structured as:

```
transcript-segment-view-model
├── div.ytwTranscriptSegmentViewModelTimestamp        ← visible "0:12"
├── div.ytwTranscriptSegmentViewModelTimestampA11yLabel  ← skip (e.g. "12 seconds")
└── span.ytAttributedStringHost                       ← the actual transcript text
```

Extractor:

```js
const segments = [];
document.querySelectorAll('transcript-segment-view-model').forEach(seg => {
  const ts = seg.querySelector('.ytwTranscriptSegmentViewModelTimestamp')?.textContent?.trim();
  const txt = seg.querySelector('.ytAttributedStringHost')?.textContent?.trim();
  if (ts && txt) segments.push(`[${ts}] ${txt}`);
});
```

### Tab visibility override

Backgrounded tabs don't hydrate engagement panels. On a fresh tab, run this before doing anything else and wait ~6s:

```js
Object.defineProperty(document, 'visibilityState', { configurable: true, get: () => 'visible' });
Object.defineProperty(document, 'hidden', { configurable: true, get: () => false });
document.dispatchEvent(new Event('visibilitychange'));
```

### Output bridge (avoid the ~1KB `javascript_exec` cap)

Build the formatted transcript in JS, then replace the body with an `<article>` containing a `<pre>` sentinel-wrapped. Then call `get_page_text` to retrieve the full text. **Use `createElement` / `appendChild` — `innerHTML` is blocked by Trusted Types on YouTube.**

```js
const article = document.createElement('article');
const h1 = document.createElement('h1');
h1.textContent = 'KB Transcript Bridge';
const pre = document.createElement('pre');
pre.id = 'kb-out';
pre.textContent = '===KB-START===\n' + segments.join('\n') + '\n===KB-END===';
article.appendChild(h1);
article.appendChild(pre);
while (document.body.firstChild) document.body.removeChild(document.body.firstChild);
document.body.appendChild(article);
```

### Gate caveat

Some videos still fail at the click step (panel stays HIDDEN, no segments populate) despite identical browser fingerprint. As of 2026-05-02, the channel's **newest** video was reachable; ones from 1-2 months ago were not. If a video fails after one click attempt + 8s wait, skip it and try a more recent video. Don't burn cycles re-trying — the failure mode is server-side, not a click-event-routing problem.

### Bias towards newest, not oldest

The **"oldest first"** advice in the steps above is the *aspirational* policy, but right now it's safer to start from the **newest unsaved video** because that cohort is more likely to clear the transcript gate. If/when the gate state shifts, revert to oldest-first.
