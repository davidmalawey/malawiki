# Log

Chronological, append-only record of ingests, queries, and lint passes.
Entry format: `## [YYYY-MM-DD] <kind> | <subject>` where kind ∈ {ingest, query, lint, schema}.

## [2026-04-23] acquire | More than you ever wanted to know about tape

- Saved: `raw/transcripts/2024-07-17_more-than-you-ever-wanted-to-know-about-tape.md`
- Source: YouTube https://www.youtube.com/watch?v=W0sAR_jI4b8
- Published: 2024-07-17 | Duration: 1:10:39 | Views: 174,242 | Likes: 9,142
- 631 unique transcript segments extracted via localStorage bridge (2 × get_page_text, split at 315/316)
- 28 chapters captured (0:00 introduction → 69:08 broad poly tape)
- Ready for ingest (wiki page creation)

## [2026-04-23] acquire | Label supplies to multiply results

- Saved: `raw/transcripts/2024-08-31_label-supplies-to-multiply-results.md`
- Source: YouTube https://www.youtube.com/watch?v=B1QqAZeEfes
- Published: 2024-08-31 | Duration: 24:10 | Views: 190,981 | Likes: 9,006
- 208 unique transcript segments extracted via localStorage bridge (single get_page_text call)
- 17 chapters captured (0:00 Guaranteed Savings → 21:30 secrets in Manuals)
- Ready for ingest (wiki page creation)

## [2026-04-23] acquire | Aluminum Extrusions Fundamentals

- Saved: `raw/transcripts/2025-09-03_aluminum-extrusions-fundamentals.md`
- Source: YouTube https://www.youtube.com/watch?v=cLrIE6ltErE
- Published: 2025-09-03 | Duration: 34:20 | Views: 191,235 | Likes: 6,160
- 321 unique transcript segments extracted via DOM, written in 9-line batches
- 13 chapters captured (0:00 intro → 28:40 Solidworks Frame Design)
- Ready for ingest (wiki page creation)

## [2026-04-23] acquire | More about USB than you ever wanted to know

- Saved: `raw/transcripts/2024-07-25_more-about-usb-than-you-ever-wanted-to-know.md`
- Source: YouTube https://www.youtube.com/watch?v=9c9-YUSbgYs
- Published: 2024-07-25 | Duration: 57:46 | Views: 281,880 | Likes: 6,239
- 521 transcript segments extracted via DOM (`ytd-transcript-segment-renderer`), written in batches
- 17 chapters captured (0:00 intro → 53:48 wireless charger)
- Ready for ingest (wiki page creation)

## [2026-04-23] schema | Wiki scaffolded

Initial scaffolding created.
- `CLAUDE.md` — schema defining ingest / query / lint workflows, directory layout, frontmatter, and linking conventions.
- `index.md` — empty catalog.
- `log.md` — this file.
- `raw/transcripts/` — intake directory for YouTube transcripts.
- `wiki/overview.md` — stub synthesis page.
- `wiki/{videos,entities,concepts,series}/` — page directories (each with a short README).

Channel focus: hobbyist / craft / how-to.
Ingest style: auto-ingest with minimal confirmation — log and report are the review surface.
Page types enabled: video summaries, entities (people/tools/materials/brands/projects/places), concepts, series.

## [2026-04-23] inventory | @davidmalawey — 224 videos cataloged

- Channel: David Malawey (UCwirLDXiN1ybgPyIDNt85PA) — 100K subscribers
- Tabs detected: Home · Videos · Shorts · Podcasts · Playlists · Posts — tabs absent: Live · Store
- Videos found: 224 long-form VODs (header said "630 videos" — delta = Shorts + Podcasts + Playlists-as-items + header overcounts)
- Method: `/youtubei/v1/browse` continuation API (8 pages, 30×7 + 14) after scroll-based harvest stalled on backgrounded tab
- Artifacts: `inventory/@davidmalawey.json` (172K, 224 entries, schema-valid), `inventory/@davidmalawey.md` (6K summary with Top 20 / Oldest 5 / Newest 5)
- 5 videos already in `raw/transcripts/` (in_kb=true): W0sAR_jI4b8, B1QqAZeEfes, cLrIE6ltErE, 9c9-YUSbgYs, pN-rh6UwR_A
- Remaining: 219 unfetched
- Top-3 by views: "More about USB than you ever wanted to know" (281K) · "Aluminum Extrusions Fundamentals" (191K) · "Label supplies to multiply results" (190K)
- Oldest videos from 2018 (7 years ago); newest from 1 month ago — channel spans early SCUTTLE robot tutorials → deep engineering how-to
- Schema updates applied: added `Podcasts` and `Posts` to tabs_detected enum (Malawey has both), added `description_snippet` field to channel object
- Skill lesson: backgrounded-tab throttling defeats DOM-scroll harvesting. `/youtubei/v1/browse` with scraped continuation token bypasses visibility throttling entirely — this should be the skill's default.

## [2026-04-23] profile | @davidmalawey — full channel harvest

- Skills run: yt-channel-structured-data, yt-channel-about (partial — no modal), yt-channel-shorts, yt-channel-podcasts, yt-channel-playlists, yt-channel-posts, yt-channel-featured
- Method: innertube-browse-api for all tab walks
- **Header count demystified**: 630 videos = 224 long-form + 406 shorts (exact)
- Totals: 224 videos · 406 shorts · 1 podcast · 8 playlists · 10 community posts · 3 home shelves
- **Top shorts by views**: "carbide tooling changes the game" (5.4M), "USB-C can replace alkaline batteries" (3.3M), "Caution! circuits destroy regular drill bits" (2.2M) — shorts are where Malawey's reach concentrates
- Structured-data captured: 19 meta tags, 8 og:* (+ 8 og:video:tag), 9 itemprop, 23 link rels, 0 JSON-LD
- Attribution link: qr.net/openlabproject · RSS: explicit from channelMetadataRenderer.rssUrl
- About modal (joined-date, total-views) NOT captured this pass — requires UI click. Full description + external-link text is in channelMetadataRenderer.description and parseable.
- Artifacts: `profile/@davidmalawey.json`, `profile/@davidmalawey.md`, `scratch/shorts/@davidmalawey/2026-04-23.json`, `scratch/community/@davidmalawey/...`, `scratch/podcasts/...`, `scratch/playlists/...`, `scratch/schema-dumps/@davidmalawey/2026-04-23_structured-data.json`
- Schema v2.0.0 introduced (channel-profile.schema.json) — extends v1.0.0 (channel-inventory).

## [2026-04-23] rss | @davidmalawey — 15 entries fetched

- Source: `https://www.youtube.com/feeds/videos.xml?channel_id=UCwirLDXiN1ybgPyIDNt85PA` (from `channelMetadataRenderer.rssUrl`)
- Method: Chrome fetch (bash egress to youtube.com is blocked — cowork-egress-blocked)
- **All 15 entries are Shorts** — every `<link rel="alternate">` href is `/shorts/<id>`. Malawey's recent uploads (2026-03-18 → 2026-04-23, ~5 weeks) are exclusively short-form.
- Fields RSS exposes beyond what we had: exact ISO-8601 publish timestamps, exact view counts, `media:starRating count` (total ratings = ~ likes proxy), `media:description` (creator-written — often absent on shorts).
- **For the Malawey long-form KB, RSS adds no publish-date pinning this cycle** — none of the 15 are long-form. Useful fallback when the channel mixes formats or for monitoring new drops.
- Artifacts: `profile/rss/2026-04-23.json` (enriched with classified short/long flag), `profile/rss/2026-04-23.md` (human summary)
- Most-liked in this window: "Never bend a key again" (1,684 ratings) and "Sticky Tack Life Hack" (1,562 ratings) — neither correlates perfectly with view count. The views leader is also "Never bend a key again" (24,770).

## [2026-04-24] skills | description optimization + packaging

- 12 skills packaged as .skill archives (all in KB root, installable via Cowork plugins)
- New: yt-channel-rss added to the family (fetches 15-entry Atom feed with exact dates + view counts + short/long classifier)
- Description optimization attempted via scripts.run_loop — baseline showed 0% recall on 5 priority skills (classic undertriggering)
- Full auto-loop couldn't complete in this sandbox (subprocess lifetime < 45s bash timeout)
- Applied skill-creator's "be pushy" guidance MANUALLY to the 5 priority skills (profile/rss/inventory/transcript-fetch/about):
  - Expanded trigger-phrase lists with casual variants ("give me the top 10", "what's the bio", "who is this creator")
  - Added "Use this skill PROACTIVELY whenever..." language per the skill-creator docs
  - Called out skill-vs-skill disambiguation (rss vs inventory, profile vs about, transcript-fetch vs inventory)
  - Included handle-less phrasings (many users say "this channel" / "this video" without naming the handle)
- All 12 descriptions validated: under the 1024-char cap, no angle brackets, valid frontmatter
- Baseline eval set saved at outputs/trigger-evals/ for re-running optimization in a longer session (run_loop.py works fine for single skills up to ~3 min; just can't chain 5 within bash 45s timeout here)

## [2026-04-24] investigation | late-2025 transcript bug — diagnosis, no fix

Attempted to close the yt-transcript-fetch gap for videos uploaded after ~Oct 2025 (test target: lcV9Wvxn6qk, "Build a battery adapter to power the whole Lab", Nov 2025).

**Paths tried, all rejected:**

1. **Direct timedtext URL** from `ytInitialPlayerResponse.captions.captionTracks[0].baseUrl` (signed with signature/sparams/expire params) → HTTP 200 with empty body across fmt variants (json3, srv3, vtt, plain).
2. **`api/timedtext?type=list`** unsigned list endpoint → HTTP 200, empty body.
3. **Unsigned `api/timedtext?v=<id>&lang=en&kind=asr&fmt=json3`** → HTTP 200, empty body.
4. **`/youtubei/v1/get_transcript`** POST with the `getTranscriptEndpoint.params` scraped from `engagementPanels[].engagementPanelSectionListRenderer.content.continuationItemRenderer.continuationEndpoint` → HTTP 400 `FAILED_PRECONDITION` across all 5 Innertube client identities (WEB, IOS, ANDROID, WEB_EMBEDDED_PLAYER, TVHTML5).
5. **DOM engagement panel** with `visibilityState='visible'` override, "Transcript" chip click, scroll-into-view, 15-second wait → spinner stays active, `ytd-transcript-segment-renderer` count stays at 0.

**Diagnosis**: YouTube's transcript endpoints now require a `pot` (proof-of-origin) token derived client-side by BotGuard. Static fetches without that token fail. The DOM panel is subject to the same gating — when the browser/tab is flagged or stale, even its internal call fails. Confirmed by re-testing the previously-successful video (W0sAR_jI4b8) mid-session: its DOM path also returned 0 segments, meaning this is a rolling enforcement change, not a per-video-UI change.

**Implications:**

- The 5 transcripts already in `raw/transcripts/` are valuable — may be the only ones we get without a pot-token workaround.
- The prior Sonnet's successful runs (earlier in this session) were on the window before stricter enforcement kicked in.
- The `yt-transcript-fetch` SKILL.md troubleshooting table is updated with the full diagnosis and a "wait for pot-token support" posture.

**Escape hatches not tried (blocked by sandbox):**

- `yt-dlp` from bash — blocked by `cowork-egress-blocked` to youtube.com.
- BotGuard reverse-engineering / pot-token synthesis — out of scope; substantial engineering effort and brittle.
- Asking the user to paste the transcript manually — always works, but defeats automation.

**Task #30 status**: completed with "no fix found". Updated SKILL.md to reflect the current state accurately rather than leave users expecting a working fallback.

## [2026-04-24] experiment | fresh-tab transcript fetch — conclusive diagnosis

Closed both existing Chrome tabs (which had accumulated hours of automated activity). Opened a brand-new tab, navigated directly to i4oJTfp18eg (Design enclosures for electronics, 36K views, not yet in KB). Tried to fetch its transcript.

**Browser fingerprint looked legitimate:**
- `navigator.webdriver` = false
- User agent is normal Chrome (no "headless" string)
- plugins.length = 5
- languages.length = 2
- No chrome.runtime exposed
- **Signed in** (`ytcfg.LOGGED_IN = true`)
- Valid `visitorData` on INNERTUBE_CONTEXT (48 chars)

**What happened:**
- "Show transcript" button clicked successfully
- Engagement panel opened (`visibility = ENGAGEMENT_PANEL_VISIBILITY_EXPANDED`)
- Chip bar rendered with Timeline / Chapters / Transcript
- "Transcript" chip clicked, became selected
- Continuation element scrolled into view explicitly
- Waited up to 12 seconds
- Spinner stayed active indefinitely; 0 segments populated; panel text stayed at just the 3 chip labels
- Reloaded, retried — same result

**Smoking gun:** Monkey-patched `window.fetch` and watched network requests. **No `get_transcript` request was ever fired**, neither by user-simulated click nor by the continuation IntersectionObserver. YouTube's client-side JS is silently refusing to initiate the call. Only two `youtubei/v1/*` requests fired during the full page load + interaction: `log_event` (analytics) and `get_setting_values` (account settings).

**Conclusion:** The transcript-access gate is a **client-side decision** made by YouTube's JS before any network request leaves the browser. Our direct programmatic POST to `/get_transcript` returns `FAILED_PRECONDITION`, but the browser's own JS doesn't even attempt the call. Whatever signal YouTube uses to decide "don't fetch transcript" is firing on this Chrome profile across fresh tabs.

**What this eliminates:**
- Session-state flagging of a specific tab (fresh tab same behavior)
- Visitor-data expiry (fresh visitorData, same behavior)
- Signed-out-user restriction (we're signed in)
- Common bot-detection knobs at navigator level (all clean)

**What it points to:**
- Chrome profile-level flag (would persist across tabs; would require a fresh browser profile to reset)
- Or a global enforcement change YouTube pushed that's currently live

**Verdict for the skill:** `yt-transcript-fetch` is not functional for new transcript captures on this Chrome profile right now. The 5 existing transcripts in `raw/transcripts/` are a stable ground truth; adding more will require either a fresh browser profile, a different host (out-of-sandbox `yt-dlp`), or waiting for the enforcement state to change.

Task #31 completed. Findings logged here and into the yt-transcript-fetch troubleshooting table.

## [2026-04-24] ingest | More than you ever wanted to know about tape

- Created: [[wiki/videos/more-than-you-ever-wanted-to-know-about-tape]]
- Created entities: [[entities/materials/kapton-tape]], [[entities/materials/ptfe-teflon]], [[entities/brands/3m]] (shared with labels video), [[entities/brands/home-depot]]
- Bootstrap of many shared entities: [[entities/materials/aluminum]], [[entities/materials/vinyl]], [[entities/materials/nylon]], [[entities/materials/hdpe]], [[entities/tools/sharpie]], [[entities/tools/circular-saw]]
- Scissors noted inline in the video page but no stub created (fleeting single-mention tool).
- Created concepts: [[concepts/emissivity]], [[concepts/vibration-damping]]
- No series created — standalone reference video.

## [2026-04-24] ingest | More about USB than you ever wanted to know

- Created: [[wiki/videos/more-about-usb-than-you-ever-wanted-to-know]]
- Created entities: [[entities/brands/toyota]] (source_count 0 → 1), [[entities/brands/texas-instruments]], [[entities/brands/arduino]], [[entities/brands/raspberry-pi]], [[entities/tools/usb-power-meter]], [[entities/materials/copper]]
- Merged into existing: [[entities/materials/vinyl]] (source_count 1 → 2)
- Created concepts: [[concepts/ferrite-noise-suppression]], [[concepts/quick-charge]], [[concepts/instrument-resolution]]
- No series created.

## [2026-04-24] ingest | Borrow a Tolerance: Mindset for Designers

- Created: [[wiki/videos/borrow-a-tolerance-mindset-for-designers]]
- Created entities: [[entities/projects/scuttle-robot]], [[entities/brands/grabcad]], [[entities/tools/3d-printer]], [[entities/tools/calipers]], [[entities/tools/ball-bearings]], [[entities/tools/collet]], [[entities/materials/pla]], [[entities/materials/abs]], [[entities/materials/urethane]], [[entities/materials/spring-steel]]
- Merged into existing: [[entities/brands/toyota]] (source_count 1 → 2), [[entities/materials/aluminum]] (source_count 1 → 2), [[entities/materials/nylon]] (source_count 1 → 2), [[entities/materials/hdpe]] (source_count 1 → 2)
- Created concepts: [[concepts/borrowing-tolerances]], [[concepts/screw-as-spring]], [[concepts/print-direction]], [[concepts/plastic-compressibility]], [[concepts/parametric-design]]
- **Proposal** (not auto-created per schema): a SCUTTLE series page may be warranted once 2-3 more SCUTTLE-centric videos are ingested.

## [2026-04-24] ingest | Label supplies to multiply results

- Created: [[wiki/videos/label-supplies-to-multiply-results]]
- Created entities: [[entities/brands/texas-am]], [[entities/places/toyota-georgetown-kentucky]], [[entities/places/texas-am-lab]], [[entities/materials/isopropyl-alcohol]]
- Merged into existing: [[entities/people/david-malawey]] (created this pass, source_count 5 across all 5 videos), [[entities/brands/toyota]] (source_count 2 → 3), [[entities/brands/3m]] (source_count 1 → 2), [[entities/projects/scuttle-robot]] (source_count 1 → 2), [[entities/tools/sharpie]] (source_count 1 → 2), [[entities/tools/3d-printer]] (source_count 1 → 2), [[entities/materials/nylon]] (source_count 2 → 3)
- Created concepts: [[concepts/5s-methodology]], [[concepts/calibrate-the-humans]], [[concepts/free-data]]
- Extended [[concepts/parametric-design]] (source_count 1 → 2)

## [2026-04-24] ingest | Aluminum Extrusions Fundamentals

- Created: [[wiki/videos/aluminum-extrusions-fundamentals]]
- Created entities: [[entities/brands/automation-direct]], [[entities/brands/solidworks]], [[entities/brands/lowes]], [[entities/brands/crayola]], [[entities/tools/miter-saw]], [[entities/materials/paraffin-wax]]
- Merged into existing: [[entities/materials/aluminum]] (source_count 2 → 3), [[entities/brands/amazon]] (source_count across 3 videos), [[entities/brands/home-depot]] (source_count 1 → 2), [[entities/brands/grabcad]] (source_count 1 → 2), [[entities/tools/sharpie]] (source_count 2 → 3), [[entities/tools/circular-saw]] (source_count 1 → 2), [[entities/projects/scuttle-robot]] (source_count 2 → 3)
- Extended [[concepts/parametric-design]] (source_count 2 → 3), [[concepts/screw-as-spring]] (source_count 1 → 2)
- Also refreshed [[wiki/overview]] and [[index]] with all new pages; SCUTTLE series proposal carried forward.

## [2026-04-24] schema | First batch ingest — scaffolding notes

Five-video batch ingest completed. Pattern observations for schema co-evolution:

- Cross-video entity recurrences are concentrated in a small set: [[entities/projects/scuttle-robot|SCUTTLE]] (3 videos), [[entities/brands/toyota|Toyota]] (3), [[concepts/parametric-design|parametric design]] (3), [[entities/materials/aluminum|aluminum]] (3), [[entities/materials/nylon|nylon]] (3), [[entities/tools/sharpie|Sharpie]] (3). These are the wiki's current load-bearing spine.
- Many brands appear once only (Apple, Dremel, Panasonic, LG, Cooler Master, FLIR, JB Weld, Scotch, Gorilla, NASA). Per the lint workflow, stubs will be created if/when these recur.
- Videos are catalog-shaped. Proposed schema addendum: an optional `catalog_size: N` frontmatter field on video pages would make it easier to flag reference-style content (tape = 20 items, USB = dozens of hardware examples, extrusions = 4 nut types + 4 bracket types).
- The [[entities/projects/scuttle-robot|SCUTTLE]] "series" status is ambiguous — not a linear arc but a design-philosophy thread. Hold on creating a series page until a fourth explicitly-SCUTTLE video lands.

## [2026-05-02] acquire | how Hardware Enshitification occurs and how EASILY we can beat it.

- Saved: `raw/transcripts/2026-05-01_how-hardware-enshitification-occurs-and-how-easily-we-can-beat-it.md`
- Source: YouTube https://www.youtube.com/watch?v=GlrpN5RDmSQ
- Published: 2026-05-01 | Duration: 30:26 | Views: 627 | Likes: 67
- 229 transcript segments extracted via DOM
- Ready for ingest (wiki page creation)

## [2026-05-02] investigation | transcript-fetch gate revisited — partial success

The 2026-04-24 diagnosis was **partially superseded**. Findings from today's run:

**Gate is no longer fully closed.** The very newest video on the channel (`GlrpN5RDmSQ`, posted 2026-05-01) was extractable via DOM. We got a clean 229-segment transcript using a click → panel-expand → segment-iterate flow. This contradicts the prior session's "no fix found" conclusion.

**However, gate behavior is video-specific.** Attempts on `W38vuFPvroc` (Chemical Spills, 1 month old), `khiMEj0_Yjo` (Exoskeleton, 2 months old) failed identically: click on "Show transcript" registers, but the engagement panel stays at `ENGAGEMENT_PANEL_VISIBILITY_HIDDEN` and 0 segments populate. Tried multiple click strategies (.click(), PointerEvent sequence, focus + Enter key, click on yt-button-shape wrapper) — none worked. Innertube `/youtubei/v1/get_transcript` still returns `FAILED_PRECONDITION`. Signed timedtext URLs still return HTTP 200 empty body. Same browser profile, fresh tab, signed-in session.

**Two updates that matter for the skill, regardless of gate state:**

1. **DOM selectors changed.** The prior skill counted `ytd-transcript-segment-renderer` — that element name is gone. New structure:
   ```
   transcript-segment-view-model
   ├── div.ytwTranscriptSegmentViewModelTimestamp        ← visible "0:12"
   ├── div.ytwTranscriptSegmentViewModelTimestampA11yLabel  ← skip
   └── span.ytAttributedStringHost                       ← the actual text
   ```
   Extractor: `document.querySelectorAll('transcript-segment-view-model').forEach(seg => { const ts = seg.querySelector('.ytwTranscriptSegmentViewModelTimestamp')?.textContent?.trim(); const txt = seg.querySelector('.ytAttributedStringHost')?.textContent?.trim(); ... })`

2. **Tab visibility throttling needs an explicit override.** Backgrounded tabs don't hydrate engagement panels; on a fresh tab opened via `tabs_create_mcp + navigate`, panels were absent at the 12-second mark until I forced `document.visibilityState = 'visible'` and dispatched a `visibilitychange` event. After that, panels appeared within ~6s.

3. **Output bridging trick.** The MCP `javascript_exec` response truncates around ~1KB, but `get_page_text` returns much more. Build the transcript text with JS, then **replace `document.body` with an `<article>` containing a `<pre>` with sentinel-wrapped text** (using `createElement` / `appendChild` — `innerHTML` is blocked by Trusted Types on YouTube). `get_page_text` then returns the full transcript cleanly.

**Why does the gate fail on older videos?** Unclear. Hypotheses:
- Fresh-content cohort: the newest video may be on a different rollout that hasn't enforced pot-token requirement yet.
- Click handler binding: synthetic clicks may only succeed on specific recently-built page templates.
- Session-state drift: extended automated activity may trigger additional bot-detection flags.

**Recommended next step:** when the user wants more transcripts, retry on whatever the **newest** unsaved video is on the channel. That cohort appears to still be reachable. Older content remains gated until either YouTube's enforcement state shifts again, the user provides a fresh Chrome profile, or we route through `yt-dlp` outside the sandbox.

**Outcome of today's run:** 1 of 5 transcripts captured. The channel inventory shows several promising candidates from the past 1-2 months — those are the next attempts when the gate cooperates.

## [2026-04-24] acquire | Which lubricant is SAFE on RUBBER?

- **TRANSCRIPT IMPORT SUCCEEDED.** Earlier "we're being client-side gated" diagnosis was WRONG.
- Saved: `raw/transcripts/2022-01-09_which-lubricant-is-safe-on-rubber.md`
- Source: YouTube https://www.youtube.com/watch?v=0_Ab3MyVxiE
- Channel: David Malawey (UCwirLDXiN1ybgPyIDNt85PA) ✅ boundary verified
- Published: 2022-01-08 (ISO from microformat) | Duration: 5:30 | Views: 82,698
- Category: Education | ASR captions, no chapters
- 35 transcript segments captured

**The actual fix:** YouTube renamed the transcript panel and elements in late 2025. The skill was looking for the OBSOLETE selectors:

| Old selector (no longer exists)                                  | New selector (current as of 2026-04-24)                                                       |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Panel: `target-id="engagement-panel-searchable-transcript"`      | Panel: `target-id="PAmodern_transcript_view"`                                                  |
| Segment: `ytd-transcript-segment-renderer`                       | Segment: `transcript-segment-view-model`                                                       |
| Timestamp: `.segment-timestamp`                                  | Timestamp: `.ytwTranscriptSegmentViewModelTimestamp:not([class*="A11yLabel"])`                |
| Text: `.segment-text`                                            | Text: `span.ytAttributedStringHost` (inside the view-model)                                    |

The `engagement-panel-searchable-transcript` panel now exists ALONGSIDE `PAmodern_transcript_view` but stays HIDDEN with a perpetually-active spinner — a red herring that consumed several rounds of investigation. The real, populated transcript is in the new panel using the new element type. Spinner-watching on the old panel was useless because that panel's continuation never resolves; the new panel renders synchronously when "Show transcript" is clicked.

**No pot-token bypass needed, no `yt-dlp`, no fresh browser profile.** The path is the same DOM-bridge approach we used originally — just with the updated selectors.

**SKILL.md updated** with the new selectors documented in the troubleshooting table. Repackaged `yt-transcript-fetch.skill`.

Task #32: completed (transcript imported), and as a bonus, task #30 (late-2025 panel bug) is now actually solved — not just diagnosed. Reopening #30 retrospectively is unnecessary; the corrected skill code is in place.

## [2026-04-24] investigation | transcript fetch is rollout-dependent (correcting yesterday's "RESOLVED" claim)

Tried to grab 4 more transcripts. Got 0 of 4. Earlier "RESOLVED" claim was based on a single video and was overstated.

**The real situation:**

YouTube has TWO transcript panels currently in flight, controlled per-video:

| Panel target-id                              | Status                              | Element type for segments              |
|----------------------------------------------|-------------------------------------|----------------------------------------|
| `engagement-panel-searchable-transcript`     | Legacy, pot-token gated → broken    | `ytd-transcript-segment-renderer`      |
| `PAmodern_transcript_view`                   | New rollout, works when populated   | `transcript-segment-view-model`        |

The description-area "Show transcript" button is rendered for both kinds of videos but targets DIFFERENT panels depending on which rollout cohort the video is in:

- Lubricant video (`0_Ab3MyVxiE`): button command targets `PAmodern_transcript_view` → panel auto-populates → 35 segments → **works**
- Adhesive video (`WyM9JtRZuvc`) + 110+ others sampled: button targets `engagement-panel-searchable-transcript` → panel never populates → 0 segments → **broken**

**Sampling rate**: probed 111 of 224 Malawey videos via `/youtubei/v1/next` looking for `PAmodern_transcript_view` in the response's `engagementPanels[]`. **Zero matches.** The lubricant video that worked yesterday is the only known modern-rollout video on this channel — and its modern panel is created at runtime by the web player (not surfaced in the `/next` API response), so even probing won't reliably predict rollout status.

**Why my "fix" worked once**: the lubricant video happened to be in YouTube's experimental cohort that auto-populates the modern panel when the watch page loads. I didn't trigger anything — the panel was already populated when I checked it. For non-rollout videos, no amount of clicking, scrolling, force-setting visibility, or dispatching commands triggers the modern panel to populate. The population is server-controlled by feature flags I can't influence client-side.

**Honest verdict**: the 6 transcripts currently in `raw/transcripts/` (5 from prior Sonnet session, 1 from today's lubricant capture) are the realistic ceiling for this Chrome profile until either (a) YouTube's rollout expands to include more Malawey videos, (b) we use yt-dlp on a host with a working pot-token implementation, or (c) someone manually opens the videos and pastes transcripts.

**SKILL.md updated** with the corrected diagnosis. The "skip_reason: transcript-rollout-pending" flag is now part of the documented posture so the skill stops gracefully on non-rollout videos rather than spinning forever.

**Task #33 status**: completed with 0 transcripts captured. Sample diversity (newest, oldest, mid, 2.5% sampled) suggests <5 candidates total in the rollout across the full inventory.

## [2026-04-24] tooling | scripts/fetch-transcripts.py — yt-dlp escape hatch

Sandbox can't install yt-dlp (proxy blocks pypi.org, files.pythonhosted.org, github.com — only *.anthropic.com / *.claude.com reachable). So the practical answer is "yt-dlp on the user's host machine."

Wrote `scripts/fetch-transcripts.py` (~470 lines) — a host-runnable Python script that:

- Takes video IDs / URLs / list-files / --catch-up (walk inventory)
- Calls yt-dlp to fetch ASR captions + metadata only (no audio/video, ~200 KB per video)
- Parses `.vtt` into `[MM:SS] text` segments matching our existing format
- De-dupes consecutive identical caption lines (yt-dlp's repeat artifact during slow speech)
- Strips `<c>` karaoke markup
- Extracts chapters from `info.json` when present
- Enforces channel boundary against `KB_CHANNEL_ID = UCwirLDXiN1ybgPyIDNt85PA`
- Skips videos already in `raw/transcripts/` unless explicitly named
- Writes the same frontmatter shape as the in-skill version (channel, channel_id, published, duration, views, likes, category, keywords, thumbnail, etc.)
- Appends a structured batch summary to `log.md`

Companion `scripts/README.md` documents install (`pip install -U yt-dlp`) and usage. The yt-transcript-fetch SKILL.md now references this as the escape hatch.

Smoke-tested the script's parser logic in-sandbox (no network, just unit-level tests on the parse_vtt, normalize_to_video_id, slugify, already_in_kb functions). All four pass.

Practical user workflow:
```
pip install -U yt-dlp
cd "C:\Users\Justin\Documents\Claude\Projects\YT - David Malawey KB"
python scripts/fetch-transcripts.py --catch-up --limit 50
```

That should get ~50 new transcripts in one shot, depending on which Malawey videos have captions enabled.

## [2026-05-02] yt-dlp-batch | 5 new transcripts
- Method: yt-dlp on host (bypasses Chrome-extension pot-token gating)
- Targets: 218 | new: 5 | already-in-kb: 0 | no-captions: 0 | errors: 0
  - ✅ W38vuFPvroc | 566 segs | 7 chap | How to Prep for Chemical Spills
  - ✅ 2Hjf48S98fA | 570 segs | 13 chap | Never Fold Clothes Again
  - ✅ Hqk08dc2a_A | 440 segs | 0 chap | This Insole design is healthier, longer-lasting, and cheaper
  - ✅ khiMEj0_Yjo | 1090 segs | 9 chap | Exoskeleton Design & Control of Fastener Torque
  - ✅ Rsz5TlAEIfg | 660 segs | 0 chap | Checking in from Mexico and a free engineering gift for my A

## [2026-05-02] yt-dlp-batch | 50 new transcripts
- Method: yt-dlp on host (bypasses Chrome-extension pot-token gating)
- Targets: 213 | new: 50 | already-in-kb: 0 | no-captions: 0 | errors: 0
  - ✅ YBW1i3gBt6Q | 2644 segs | 7 chap | Innovations underway - Friction Welded PVC, Unistrut Slide m
  - ✅ CvhiSP_6ESQ | 1500 segs | 15 chap | How to design a functional, printable, open source mechanica
  - ✅ n3na6mTBLvA | 1868 segs | 16 chap | Highly Engineered EMT Conduit Parts to Study Before Designin
  - ✅ 1-9dbWSUl7w | 1130 segs | 0 chap | A&M University’s Lab burned down and here’s what I learned.
  - ✅ lcV9Wvxn6qk | 1296 segs | 10 chap | Build a battery adapter to power the whole Lab
  - ✅ ioUWBli_iFU | 986 segs | 0 chap | New Pardigm for Engineering - how we pursue all the dreams
  - ✅ IFo5F24jhug | 958 segs | 0 chap | 10 years of Engineering Labs
  - ✅ -hdVmXMv8F4 | 1300 segs | 0 chap | I met Henry Ford’s grandson, but the Brazilian engineers tau
  - ✅ M7CvLJcEAds | 1598 segs | 11 chap | Expanded PVC for Engineering Designs -  The Easiest Panel in
  - ✅ IvZXdxWh7dg | 886 segs | 9 chap | I applied Toyota Root Cause Analysis to the sticky lids - He
  - ✅ QnAuQ8QLtgs | 928 segs | 0 chap | mechanical design tutorial for a hub
  - ✅ Zrt5EQ3SnGU | 718 segs | 11 chap | Dual Power supply for Electronics Prototyping [FULL TUTORIAL
  - ✅ wKlTQUgUxrs | 1200 segs | 8 chap | Don't suffocate society’s innovators / inside an engineer's 
  - ✅ GBuXDm2Qahw | 726 segs | 0 chap | what GPT5 is doing to open robotics design - better than I i
  - ✅ GhqwwvtWnS8 | 1522 segs | 0 chap | This is why you can’t find a Robotics Job in the USA
  - ✅ iNG-G44Cd5s | 1438 segs | 0 chap | Fully Explained Build: Test Setup, PWM Generator, DC Motor D
  - ✅ tFHB3c5enoA | 1284 segs | 0 chap | Just sharing my thoughts while Nigeria Lab progresses (live 
  - ✅ tt13GCgdD68 | 1550 segs | 0 chap | Make a Frankenstein Power Drill Treadmill Motor Controller, 
  - ✅ gjGNDaH15Ik | 1000 segs | 0 chap | How to Design the Best in the World
  - ✅ gLK1LTlivQw | 1298 segs | 12 chap | Every Engineering Lab needs Rags
  - ✅ WSEPPpp8jB4 | 1806 segs | 0 chap | strategies for lab workspace - design of lab and methods
  - ✅ ZOMu9AFOdCk | 1712 segs | 10 chap | How to Design a 3D Print - (with example, funtional Hinge)
  - ✅ RxruSY_9S3s | 212 segs | 0 chap | Extruder Project Info - ft. Gina, Mechanical Engineer.
  - ✅ KLoevbmQ4mU | 392 segs | 7 chap | We (USA) need to catch up with the Developing World in Engin
  - ✅ W-VgVRYiYqA | 2148 segs | 0 chap | A working model for an Undergrad, Hands-on Engineering Lab i
  - ✅ AueuAd5cjqc | 2546 segs | 10 chap | The Lunchbox PC - building a PC in 2025
  - ✅ AT_6_IGdku4 | 988 segs | 0 chap | We discovered a shape and it’s not a big deal 😝
  - ✅ H6BFeo9z46w | 1004 segs | 9 chap | How real experts change the world using robotics
  - ✅ EF9fIMgCdZw | 680 segs | 9 chap | Embedded Computer users Should Know this Power Issue
  - ✅ wWQ2x0hBkBY | 1282 segs | 11 chap | Excessively technical video about a vacuum adapter
  - ✅ 23hqRMnvwW4 | 2970 segs | 13 chap | A Multidisciplinary Engineering Lab Tour ► all types of actu
  - ✅ UFUxgp7focI | 744 segs | 0 chap | some designs fight thermodynamics, some designs work togethe
  - ✅ NanKGvlNbAQ | 1038 segs | 0 chap | Engineers' Mistakes (DEBUNKED)
  - ✅ _ifndZ6EIx8 | 610 segs | 0 chap | Dear Engineers: NOW is the time to lead.
  - ✅ _VxqJuFoGz4 | 1092 segs | 9 chap | What is a robot? [engineer explains]
  - ✅ mdtxljHxdUA | 1020 segs | 9 chap | Gain 5x more workspace in 12 months (at no net cost)
  - ✅ MOsBIspr6Y0 | 740 segs | 0 chap | Powerful tool anyone can use - from an engineer's perspectiv
  - ✅ aW0wrEVj3Y8 | 1336 segs | 6 chap | Mindset to perform 200% output (an organizing method, uncut)
  - ✅ I_ZlFTuSK4k | 2312 segs | 14 chap | 2024 Steve Jobs Speech Commentary - tech anxiety
  - ✅ VLrEtrU10ow | 850 segs | 13 chap | Build a DIY power supply (a tutorial using openBox)
  - ✅ Xxm6rC0z3ts | 1740 segs | 26 chap | How to Drill a Hole in Metal, Plastic, Wood, and Laminate
  - ✅ 3okGwdE9tRQ | 606 segs | 0 chap | Tradesmen outperform engineers (dialogue from an engineer)
  - ✅ kxGagkzpKZg | 556 segs | 4 chap | Refuel butane torches (a deep dive to solve all the issues)
  - ✅ 31hwwpmNlCo | 2414 segs | 17 chap | Clean up cords & wires in projects (for prototype or product
  - ✅ i4oJTfp18eg | 1554 segs | 14 chap | Design enclosures for electronics (using mechanical mindset)
  - ✅ vaBI-zFmS2k | 2779 segs | 15 chap | More than you ever wanted to know about your home’s internet
  - ✅ ob6ZYFVlByg | 2196 segs | 15 chap | How to choose a̶n̶ a̶d̶h̶e̶s̶i̶v̶e̶  a bond based on materia
  - ✅ -eF5kLdLvU0 | 506 segs | 0 chap | Hack a Soldering Iron with a mechanical engineer
  - ✅ G2JmWiyUJ3s | 1198 segs | 16 chap | Insights in REAL-WORLD battery energy that YOU can verify.
  - ✅ TdTM_QWIA1E | 398 segs | 0 chap | These two GENIUS designers are building our future.

## [2026-05-02] ingest | Batch ingest of 57 transcripts (one-shot)

Seven parallel workers each created ~8 video pages (57 total) and produced manifests; consolidator merged manifests, deduped, created stubs, updated existing entity/concept pages, refreshed index/overview/log.

- Created: 57 video pages in `wiki/videos/` (full list in [[index]]; total wiki video count now 62)
- Created entities: 134 new
  - **People (17)**: [[entities/people/joe-bowers]], [[entities/people/zack-freedman]], [[entities/people/peter-fiber-tech]], [[entities/people/steve-jobs]], [[entities/people/gozie-nzebuka]] (merged Gaius/Gozie/Zabuka aliases), [[entities/people/leonardo-da-vinci]], [[entities/people/angel-paredes]], [[entities/people/joseph-morgan]], [[entities/people/gina]], [[entities/people/william-clay-ford]], [[entities/people/renato]], [[entities/people/dr-nurasmi]], [[entities/people/walt-abi]], [[entities/people/reza-langari]] (merged Lingari/Langari), [[entities/people/elon-musk]], [[entities/people/ibraheem]], [[entities/people/precious]]
  - **Tools (50)**: 18650-cell, 2020-extrusion, 3030-extrusion, anderson-connector, automatic-center-punch, ballistol, beaglebone-y-ai, cnc-router, cordless-drill, cuban-mop, cutting-mat, dc-dc-converter, dc-gearmotor, deburring-tool, din-rail, doodlebug-mop, drill-press, dual-h-bridge-motor-driver, dupont-connector, emg-sensor, emt-conduit, fiber-cleaver, flashforge-creator-pro, forstner-bit, fusion-splicer, h-bridge, handy-box, harmonic-drive, honeywell-hpa300, hook-bracket, limit-switch, multimeter, o-ring, optical-network-terminal, otdr, pinecil, project-box, pwm-signal-generator, rivnut, roomba, scotchbrite, sleeve, soldering-iron, solar-panel, spiral-wrap, step-drill-bit, swiffer, threaded-insert, torque-wrench, treadmill-motor, unistrut, usb-pd-trigger-board, utility-knife, zip-tie
  - **Materials (29)**: acetone, acrylic, beeswax, cardboard, chemsorb, construction-adhesive, contact-cement, cork, duck-cloth, epoxy, expanded-pvc, fiberglass, galvanized-fence-post, heat-shrink, hot-melt-glue, jb-weld, kevlar, lifepo4, optical-fiber, polycarbonate, pvc, pvc-cement, pvc-primer, rubber, silicone, stamped-steel, steel-tubing, super-glue, two-part-epoxy
  - **Brands (20)**: anderson-powerworks, asus, beaglebone, boston-dynamics, canakit, chatgpt, crc, dewalt, flashforge, futo, honeywell, jb-weld-brand, mechanics-inside, molex, mouser, noctua, ridgid, tesla, walmart, wd-40
  - **Projects (24)**: assist-as-needed-exoskeleton, bikini-bracket, doodlebug-mop-build, filament-extruder, futo-filament-extruder, grip-22, hub-zero, labs-need-rags-memo, lunchbox-pc, misl-projects, openair, openarm, openbox, openjar, openlab, open-me-project, openspin, parametric-vacuum-adapter, scuttle-hinge, scuttle-malaysia, scuttle-nigeria, team-zamalik-chili-robot, terminal-v2
  - **Places (13)**: aeri-nigeria, brazil, futo-nigeria, home-depot-cancun, johor-bahru-malaysia, kane-building, lagos-nigeria, malaysia, misl-lab, pic-lab, scuttle-asia-malaysia, singapore, toyota-design-center-saline
- Created concepts: 96 new — actuator-taxonomy, adhesive-datasheet, adhesive-selection-method, ai-as-optimizer, aluminum-extrusion-wiring, analog-to-digital-conversion, battery-chemistry-tradeoffs, battery-protection-circuit, benchmarking-design, bio-signal-meter, bonding-by-porosity, bonding-types, cable-management, cash-swap-psychology, closet-rod-upgrade, connecting-the-dots-backward, connector-corrosion-cycle, cross-disciplinary-humility, data-as-authority, dc-motor-fundamentals, design-by-questions, design-for-manufacturing, din-rail-wiring, discharge-profile, diy-vs-store-bought-cost-comparison, documented-design-as-leverage, dynamics-vs-static-motion, expert-dialogue-gap, feature-tree-naming, fiber-optic-installation, fifo-storage, friction-welding-plastic, fusion-splicing, graceful-degradation, h-bridge-trigger-module, hardware-enshittification, heat-pipe-cooling, imperial-vs-metric-pragmatism, invisible-power-undersupply, kaizen, lab-commonization, leadership-as-bottleneck, leverage-incumbent-engineering, local-maxima, locally-sourced-bom, loop-vs-routine, mechatronics, mistake-vs-improvement, modularity, mortality-as-decision-filter, multidisciplinary-lab-model, multidisciplinary-optimization, o-ring-design, one-handed-access, open-source-hardware-publishing, open-source-knowledge, openlab-philosophy, optical-attenuation, parts-ecosystem-design, parts-library, passive-convection, pdca, peel-vs-shear, press-fit, product-for-stakeholders, psychrometrics, pwm, rag-as-infrastructure, real-estate-thinking, risk-tolerance-vs-abundance, root-cause-analysis, sensor-actuator-controller-loop, share-the-failure, solar-charging, speeds-and-feeds, spill-mitigation-workflow, standardize-mounting-interfaces, standardized-handybox, standardized-thickness, steady-state-heat-conduction, store-as-storage, strain-relief, study-before-designing, supercritical-fluid, surface-preparation, symptom-watch, technology-meeting-needs, thermodynamic-cooperation, three-point-clamping, tolerances, tools-augment-not-replace, torque-evaluation-on-assembled-fastener, training-plus-product, usb-pd-vs-5v-power, vacuum-interface-standards, version-marking, vertical-non-integration, volatile-cleanup-bag, water-resistance, zero-kerf-cutting, blue-tape-purge

Skipped slugs (single fleeting / redundant — left as missing-link targets for future lint):
- People: phil, dr-weinan, oneer, nikki (single fleeting mentions with no rich context)
- Tools: thermal-camera, accelerometer, computer-fan, raspberry-pi-as-tool (would conflict with brands/raspberry-pi — see below), heat-gun, junction-box, waterproof-button, spade-bit, spade-terminal, drill-guide, conical-bit, shop-vacuum, loom, velcro-strap, cable-cuff, cable-clip, cable-tray, grommet, cordless-drill-battery, magnet-base-test-rig, dupont-housings-kit, solar-battery-backup, chase-nipple, closure-plug, compression-connector, threaded-coupling, knockout-seal, angle-connector, inner-lights-timer-switch, handheld-torque-screwdriver, laminating-roller, automatic-light-sensor, chemsorb-shaker, paper-shredder, toolbox-trash-bin, molex-44262, cable-gland, hole-punch, router, jigsaw, fire-blanket, heat-set-insert/heat-set-inserts (alias of threaded-insert), soldering-iron-pinecil (alias of pinecil), anderson-powerpole (alias of anderson-connector), conical-bit/step-drill (aliases of step-drill-bit) — single fleeting mentions or alias duplicates
- Materials: sawdust, paper-shreddings, ca-glue (alias of super-glue) — single fleeting / aliases
- Brands: reiko, akeer (single fleeting)
- Places: openlab (project/place collision — kept project canonical), wta-brazil, metal-am-lab, texas-am-research-lab, texas-am-mobile-robotics-lab, harris-county-iot-lab, toyota-ann-arbor, scuttle-robotics-malaysia (dup of scuttle-asia-malaysia), scuttle-robotics-nigeria (dup of futo-nigeria) — single fleeting or duplicated by canonical entry
- Concepts: dropped a small handful of low-content concepts that overlapped with stronger ones (e.g. version-debossing folded into version-marking; benchmark-driven-design merged into benchmarking-design; debossed/version-numbering-strategy folded into version-marking)

- Updated existing entities: 35 with new "Appears in" entries
  - People: david-malawey (5→62)
  - Projects: scuttle-robot (3→30)
  - Brands: 3m (2→5), amazon (3→19), grabcad (2→13), automation-direct (1→2), raspberry-pi (1→4), solidworks (1→12), texas-am (1→15), toyota (3→14), lowes (1→3), home-depot (2→5), texas-instruments (1→3), arduino (1→2)
  - Places: texas-am-lab (1→13), toyota-georgetown-kentucky (1→5)
  - Tools: 3d-printer (2→27), usb-power-meter (1→6), sharpie (3→4), calipers (1→4), collet (1→2), miter-saw (1→4), circular-saw (2→4), ball-bearings (1→3)
  - Materials: abs (1→16), pla (1→8), nylon (3→5), ptfe-teflon (1→2), aluminum (3→13), copper (1→6), urethane (1→2), hdpe (2→4), d-rail (1→3), isopropyl-alcohol (1→2), vinyl (2→3)
- Updated existing concepts: 10 with new "Appears in" entries
  - parametric-design (3→17), borrowing-tolerances (2→11), print-direction (1→6), plastic-compressibility (1→3), instrument-resolution (1→5), free-data (1→11), calibrate-the-humans (1→8), 5s-methodology (1→8), screw-as-spring (2→3), quick-charge (1→2)

Schema observations / conflicts / proposals:
- **Slug collision flagged**: Multiple manifests proposed `raspberry-pi` as a tool for the actual SBC boards. The existing entity is at `entities/brands/raspberry-pi`. Per consolidator rules, kept the existing brand canonical and folded board references into it (the brand page now appears in 4 videos that mention specific Pi 3/4/5 hardware). A future lint may want to split into `raspberry-pi-foundation` (brand) + `raspberry-pi-board` (tool), but the brand-only model holds for now.
- **Person-canonical merge**: Three batches each named the Nigerian collaborator differently (Dr. Gaius Nzebuka / Dr. Gozie Nzebuka / Dr. Zabuka). Merged under `gozie-nzebuka` with the union of aliases. Same for Dr. Lingari (b6) / Dr. Langari (b7) → `reza-langari`.
- **Place/project collision** flagged for `openlab`: batch6 proposed it as a place (David's current personally-built lab); we already had it as a project (the open-source publication). Kept project canonical; future schema work may add a separate `david-openlab-physical` place if more video footage warrants it.
- **Series-page proposals (NOT auto-created — schema requires confirmation):**
  1. **Open\* family series** — covers OpenBox, OpenLab, OpenJar, OpenSpin, OpenAir, OpenArm, Open ME Project; ~13 videos touch this thread.
  2. **SCUTTLE international tour series** — Nigeria, Malaysia, Mexico, Singapore-Johor; ~10 videos.
  3. **10 years of labs / lab infrastructure series** — labs tour, rags memo, lab fire, workspace design, 5S/kaizen application; 

## [2026-05-02] ingest | Batch 3 — 50 transcripts (2019-2020 SCUTTLE origin backfill)

Seven parallel ingest workers each created 6-9 video pages (50 total) and produced manifests; consolidator merged manifests, deduped, created stubs, updated existing entity/concept pages, refreshed index/overview/log.

- Created: 50 video pages in `wiki/videos/` (full list in [[index]]; total wiki video count now 162)
- Created entities: 44 new
  - **People (1)**: [[entities/people/nextec-capstone-team]]
  - **Tools (25)**: beaglebone-blue, node-red, github-gist, sd-card, hobby-servo, servo-horn, wheel-encoder, sick-tim561-lidar, usb-webcam, gamepad, mpu9250, drill-bit, mqttool, hivemq, jst-zh-connector, vscode, putty, mobaxterm, cloud9, heat-gun, buzzer, rfid-reader, wireless-charging-pad, arduino-mqtt-client-library, flashforge-creator-pro2, simplify-3d, flashprint, solidworks-2020, nvidia-isaac-sdk, nvidia-isaac-sim, ubuntu (note: software items provisionally placed under tools/ — see schema proposal below)
  - **Materials (4)**: solder-paste, diametric-magnet, lipo-battery, petg
  - **Brands (7)**: mr-diy, daiso, cayenne, creality, cytron, nvidia, github
  - **Projects (7)**: scuttle-servo-arm-v1, scuttle-iot-ecosystem, scuttle-wireless-dock, iot-slot-car-racetrack, scuttle-iot-guide, scuttle-conveyor, scuttle-solar
  - **Places (0)**: none new (sedili-besar-malaysia skipped — single 27-second vlog mention)
- Created concepts: 41 new — linux-partition-inspection, sd-card-partition-expansion, tinning-stranded-wire, node-red-flow-export-import, telemetry-via-flat-files, kinematics-sign-check, source-linked-gist, proportional-control, pid-control, runtime-tunable-parameters, closed-loop-feedback, control-oscillation, design-commonization, snap-fit-bearing-mount, counterweight-design, cable-routing-through-structure, layered-software-architecture, standalone-testable-modules, bottom-up-troubleshooting, explicit-signal-labeling, multithreading-as-cooperation, gp1-as-debug-port, apparent-size-ranging, differential-drive-kinematics, rotation-matrix, numerical-integration-of-pose, threshold-switching-control, sensor-calibration, relative-vs-absolute-orientation, mqtt, iot-data-flow, stress-concentration, file-as-ipc, free-upgrades, m2m-iot-communication, poka-yoke, leveraging-physical-testing, manual-feature-recognition, global-variable-driven-pattern, semver-for-hardware, sim-to-real-handoff
- Updated existing entities: ~58 (tools, materials, brands, places, projects) with new "Appears in" entries
- Updated existing concepts: ~40 with new "Appears in" entries; major source_count bumps include scuttle-robot (49→91), david-malawey (112→162)

- **Disambiguation**: BeagleBone Blue (new entity) vs beaglebone-y-ai (existing) — these are different products; both kept. The Y-AI page now lists the 11 new SCUTTLE videos that referenced its slug — those references will be re-pointed to beaglebone-blue in a future lint pass.
- **Two slug-truncation cases flagged for future lint**: `scuttle-robot-multithreading-explained-with-demonstration-speed-control-text-to-` (trailing dash; original title ended `text-to-speech`) and `scuttle-robot-demonstration-for-reading-gpio-input-on-beaglebone-blue-with-l1-gp` (truncated; original title ended `with-l1_gpio.py`). Per the schema, slugs must match transcript filenames — keeping them as-is.
- **Cleanup performed**: 30 entity/concept pages had pre-existing truncated bullet lines (orphan `- [[video` fragments left over from Batch 2 consolidation) — removed in this pass.

- **Series-page candidates flagged (not auto-created)**:
  - SCUTTLE 2019 BeagleBone-era tutorials (~16 episodes — Sep–Nov 2019)
  - SCUTTLE 2020 build / IoT arc (~25 episodes — Aug–Dec 2020)
  - NavigationVectors (Part 1 + Part 2)
  - Adhesive-on-rubber (round 1 + round 2 — predecessor of 2024 selection framework)

- **Schema-co-evolution proposal (deferred for user decision)**:
  - Add `entities/software/` subtype for software-only items (slicers, IDEs, simulators, libraries) — distinct from `entities/tools/` (physical) and `entities/brands/` (vendor).
    Currently affected items: Node-RED, FlashPrint, Simplify3D, NVIDIA Isaac SDK, NVIDIA Isaac Sim, VS Code, MobaXterm, PuTTY, Cloud9, Arduino MQTT client library, Ubuntu.
    Default for this pass: place under `entities/tools/` (the agent's default).

- **Schema observation**: existing `raspberry-pi` is at `entities/brands/` but agents kept treating it as a tool too — the same kind ambiguity surfaces for `beaglebone-blue` (currently under tools, with a separate `beaglebone` brand). The proposed `entities/software/` doesn't solve this; we may need a parallel `entities/devboards/` or just accept the brand/tool overlap for development-board products.

## [2026-05-02] yt-dlp-batch | 33 new transcripts
- Method: yt-dlp on host (bypasses Chrome-extension pot-token gating)
- Targets: 63 | new: 33 | already-in-kb: 0 | no-captions: 27 | errors: 1
  - ❌ ITMb0w3uyeE | no-captions | Parametric Hinge using 1/4in tube
  - ❌ ZBGswS26Dy4 | no-captions | Industrial robotics (MXET400) quick demo, conveyor, UR3e robot.
  - ❌ -C9X-VSfA-4 | no-captions | "Muscle SCUTTLE" demo - Billet aluminum mobile robot & 200kg payload
  - ❌ 0fp0wvpRqL4 | no-captions | SCUTTLE Robot carries a huge rock!
  - ❌ IeKOo-oq3kU | no-captions | Creator Pro 2 in 4K - Up Close Printing - Macro views, simultaneous twin extrusi
  - ❌ M2fa_Sh7yfQ | no-captions | SCUTTLE Robot gets a home in Johor Bahru with Iskandar Space
  - ❌ MXalMrZMsHY | no-captions | SCUTTLE Robot - water bottle demo 30kg payload
  - ❌ 375gYUm2grw | no-captions | when I have no t-slot nut or t-nut available - I make these
  - ❌ FJ-jP9HCqj8 | no-captions | Pleco Steals the Goldfish Pellets
  - ❌ RyGBepeNf7I | no-captions | SCUTTLE Robot - testing 12v LED strip, WS8211, Esp8266, FastLED Library
  - ❌ fdIofRpkFoo | no-captions | SCUTTLE Robot - Beaglebone Blue - power servos from Barrel plug
  - ✅ 5l-xO3AWcM8 | 142 segs | 0 chap | SCUTTLE Robot - Beaglebone Blue setup WPA enterprise WiFi
  - ✅ uYnGog1Pc_8 | 46 segs | 0 chap | SCUTTLE Robot - open loop vs closed loop speed control
  - ✅ qmSQHYQaYrs | 202 segs | 0 chap | SCUTTLE Robot - Send & Receive MQTT messages, display with N
  - ❌ bAQEuIzX3_8 | no-captions | Beaglebone Blue - SCUTTLE - encoders i2c addresses and pullup pins
  - ✅ C7K95wd_ezU | 56 segs | 0 chap | SCUTTLE Robot - check your wifi SSID over USB on Beaglebone 
  - ✅ 0_PJ1xX05Y8 | 90 segs | 0 chap | 3D Printed Laminar Flow Nozzle Construction
  - ✅ F7rsOU_ex5Y | 184 segs | 0 chap | Combine Two Bodies in Solidworks
  - ✅ ntIdRon6oaY | 28 segs | 0 chap | Adhesives for Small Gaps
  - ❌ c8VflTGNItU | no-captions | How to 3D Print a Black Hole
  - ❌ ikl88TbnMBU | no-captions | THE FRUIT SPIKE - Stainless 3D Printed Vegetable Spinner Hex Adapter
  - ✅ kjLAztgDgHw | 150 segs | 5 chap | Introduction to QuantAM - import parts & set up a build
  - ✅ 6gxz8YhA35U | 188 segs | 0 chap | How to Crimp 2.54mm DuPont connectors (macro view)
  - ❌ SigcCpBj0PQ | no-captions | Build the cheapest, fastest sandpaper shelf organizer
  - ✅ VBk1gkTI7PY | 62 segs | 0 chap | Renishaw AM400 - Should this thing be loose?
  - ✅ PZ6i2W_9lJE | 152 segs | 0 chap | SCUTTLE Robot - How to run color_tracking_v1.py computer vis
  - ❌ xK2SHM6fj18 | no-captions | Scuttle Robot - Carrying 90 lbs Payload (41kg)
  - ✅ fwuoglO3J0k | 162 segs | 0 chap | SCUTTLE Robot - using Matlab GUI v1.1
  - ✅ X2x7R6xTDok | 62 segs | 0 chap | Scuttle Robot - secure your beaglebone blue
  - ✅ 4vjoToIsxR4 | 8 segs | 0 chap | Scuttle Robot - Cut i2c circuit board
  - ✅ _ZNiIEPJr7c | 36 segs | 0 chap | Scuttle Robot - i2c bracket v1.2
  - ❌ qaW5Szx5Ebo | yt-dlp-error | ERROR: Unable to download video subtitles for 'en': HTTP Error 429: Too Many Req
  - ✅ yBV0TCLIw5Y | 56 segs | 4 chap | SCUTTLE Robot - fastest way to check battery voltage on beag
  - ❌ WdWj5KSYGlc | no-captions | SCUTTLE Robot - accuracy of the wheel encoders AMS AS5048B
  - ❌ -w6X6w_qcbs | no-captions | SCUTTLE Robot - Beaglebone Blue Problem Powering Servos with 12.0v @ barrel plug
  - ✅ fC4sgXplA3k | 248 segs | 0 chap | Don't destroy your 18650 cells! Use this Analogy to understa
  - ✅ JfYrRua7tiw | 16 segs | 0 chap | Scuttle Robot - Wheel Slip with unlevel chassis
  - ✅ _GyacXFINLY | 46 segs | 0 chap | Scuttle Robot - soldering the i2c bus board
  - ✅ BN1E99_LWlo | 136 segs | 0 chap | Scuttle Robot - assembling wheels and belt.
  - ❌ THejHu2klQM | no-captions | Scuttle Robot - I2C bus board (no audio)
  - ✅ 8o-XcZ3_teM | 226 segs | 4 chap | Scuttle Robot -  Modifying the Wheel Pulley in Solidworks
  - ✅ daPXxpQAJaQ | 176 segs | 0 chap | Scuttle Robot - Gluing the Wheel Pulleys (VERSION 1.0)
  - ✅ 388paGI_ecE | 114 segs | 5 chap | Anatomy Of DuPont Connector (2.54mm Connector), How To Crimp
  - ✅ M9cL-bfdHPk | 16 segs | 0 chap | Epoxy failed on ABS
  - ❌ F0HP_MXiXHo | no-captions | SCUTTLE check for belt meshing
  - ✅ d_CcTHs64qQ | 106 segs | 0 chap | Soldering Leads on 12V DC Motors (18awg) and heat shrink
  - ✅ E7_NHTZwens | 72 segs | 0 chap | Scuttle Wiring - Power Wires Overview
  - ✅ GCT9hjeIvX8 | 176 segs | 0 chap | Scuttle Battery Pack - Crimping Insulated Terminals
  - ✅ A2vBMLaxQs0 | 158 segs | 0 chap | Scuttle Robot - Battery Pack - soldering the bottom side
  - ✅ Fhat7w075Js | 96 segs | 0 chap | Scuttle Battery Pack   heat-set inserts
  - ✅ JS_9AhtAyLg | 110 segs | 0 chap | Scuttle Battery Pack - assembly & wire lengths
  - ✅ wpSIqTLZpCg | 348 segs | 9 chap | SCUTTLE robot hardware overview
  - ❌ Ey4IBEFNfrM | no-captions | Young Pitoca, the Special Silkie
  - ✅ PXD6mWnY9d0 | 370 segs | 9 chap | Scuttle Robot - Printed Parts & Orientations
  - ✅ 9LQHswVGzX0 | 1458 segs | 12 chap | Novel Aquaponics Method 1st Year summary - Suspended Media M
  - ❌ rzFaL1RxEzs | no-captions | SCUTTLE robot Carries 14.1kg payload
  - ❌ ba56mGb3jck | no-captions | My Pet Chickens Jump For Treats
  - ❌ 5kvBgsmHzV4 | no-captions | CocoPe The Silkie Rooster
  - ❌ Ax5LfTU_q4w | no-captions | Spider Tries To Trap A Gecko
  - ❌ D_iBNRZeQ2E | no-captions | Overview - Small Aquaponics Backyard System In Texas
  - ❌ oVL_tSpOYNw | no-captions | Aquaponics overview May 2018


## [2026-05-02] ingest | Batch 4 — 33 transcripts (2018-2019 SCUTTLE origin backfill)

Five parallel ingest workers each created 6-7 video pages (33 total) and produced manifests; consolidator merged manifests, deduped, created stubs, updated existing entity/concept pages, refreshed index/overview/log.

- Created: 33 video pages in `wiki/videos/` (full list in [[index]]; total wiki video count now 195)
- Created entities: 59 new
  - **People (1)**: herbert
  - **Tools (38)**: swirl-filter, reverse-osmosis-di-system, solenoid-valve, aquarium-pump-20w, airstone, wifi-temperature-sensor, scuttle-universal-bracket, scuttle-hardware-kit, hex-key-set, ratcheting-driver, wire-cutters, wire-strippers, insulated-terminal-crimper, rosin-flux-pen, 18650-cell-holder, helping-hands, wheel-pulley, lock-washer, axle-bolt, i2c-bus-board, i2c-bracket, 18650-charger, cell-removal-tool, rc-battery-monitor, m2-screw, matlab, matlab-runtime, scuttle-gui, opencv, python, color-tracking-v1, renishaw-am400, oxygen-sensor, quantam, brush, q-tip, mqtt-websocket-client, notepad-plus-plus
  - **Materials (17)**: expanded-clay-pellets, expanded-shale, landscape-timbers, fishnet, shade-cloth, pea-gravel, 18awg-wire, brass, rosin-flux, lead-tin-solder, skateboard-wheel, argon, stainless-steel, pro-weld, abs-cement, cpvc-cement, foam
  - **Brands (1)**: renishaw
  - **Projects (1)**: laminar-flow-nozzle
  - **Places (1)**: college-station-texas
- Created concepts: 50 new — gravity-overflow-pressure-regulation, glue-free-pvc-assembly, air-pruning, 45-degree-overhang-rule, screw-measurement-conventions, wire-length-specification, insulation-shoulder-as-depth-gauge, one-handed-crimp-rule, just-shy-of-flush-rule, u-shape-strand-prep, heat-the-joint-not-the-solder, rosin-flux-pen-priming, dupont-crimping, connector-anatomy, strip-then-trim, convert-entities, circular-pattern, assembly-sequencing, plastic-as-temporary-fixture, wheel-slip-diagnosis, chassis-leveling, c-rate, series-cell-balancing, cups-of-water-cell-analogy, individual-cell-charging, wrapper-rescue-with-heat-gun, ssh-tab-completion-discovery, sudo-required-utility, live-telemetry-readout, protoboard-grid-cutting, silkscreen-as-fab-guide, clip-onto-extrusion-mounting, pin-clearance-shelf, connector-orientation-for-cable-reach, solvent-welding, gap-filling-adhesion, multibody-modeling, merge-result-toggle, 3d-print-porosity-sealing, journalctl-grep-debug, soft-ap-discovery, ssh-over-usb, mqtt-topic-wildcards, mqtt-quality-of-service, node-red-dashboard, open-loop-control, integral-windup, wpa-enterprise-setup, cloud9-ide-workflow, raw-github-paste
- Updated existing entities: ~70 with new "Appears in" entries (david-malawey +33; scuttle-robot +24; abs +12; beaglebone-blue +9; soldering-iron +4; flush-cutters/htd5-belt/symmetric-not-identical/print-direction/cable-management/squeeze-out-verification/symptom-watch +3; ~30 others +1 or +2)
- Updated existing concepts: ~70 with new "Appears in" entries (crimping +4 to bring it to 8; design-for-3d-printing, parametric-design, study-before-designing, single-pump-aquaponics, leveraging-physical-testing, etc.)

- **Cleanup pass**: removed orphan empty-bullet artifacts from 16 entity/concept pages introduced by prior consolidations (raspberry-pi, calipers, parametric-design, borrowing-tolerances, abs, arduino, copper, ptfe-teflon, urethane, automation-direct, instrument-resolution, free-data, calibrate-the-humans, plastic-compressibility, screw-as-spring, amazon). Fixed orphan `## ` heading in toyota.md. Removed truncated `- [` artifacts in 2020-extrusion.md and 3d-printer.md. Re-counted and corrected `source_count` on 18 cleaned pages (e.g., parametric-design 26 → 22 after re-count + Batch 4 appends).

- **Roster resolution**:
  - **solidworks (brand) is canonical**; solidworks-2020 demoted/redirected. All three video references (`design-a-compliant-clamp-...`, `scuttle-robot-modifying-the-wheel-pulley-...`, `scuttle-robot-printed-parts-orientations`) re-routed from `entities/tools/solidworks-2020` to `entities/brands/solidworks`. The old solidworks-2020.md page rewritten as a deprecation tombstone (could not be deleted via tools — flagged for manual `rm` if user wants the slug fully retired).
  - **texas-am brand vs texas-am-lab place**: WPA enterprise WiFi video (`tamulink-wpa` campus context) routes to `texas-am` (brand, campus-level, institution); the metal-AM lab video routes to `texas-am-lab` (place). Both `how-to-crimp-2-54mm-dupont-connectors-macro-view` and `scuttle-robot-beaglebone-blue-setup-wpa-enterprise-wifi` appended to `texas-am` brand page; `renishaw-am400-should-this-thing-be-loose` and the aquaponics video appended to `texas-am-lab` place page.

- **Series-page candidates flagged (NOT auto-created)**:
  - **SCUTTLE Bench Build (Jan-Feb 2019)** — STRONGEST signal yet, three different ingest workers independently proposed the same series (`scuttle-bench-build-kickoff` / `scuttle-v1-build` / `scuttle-robot-build`). ~13 episodes spanning 2019-01-16 through 2019-02-26, covering printed-parts orientations, hardware kit, battery-pack assembly arc (4 videos), wheel-pulley CAD + glue + assembly (3 videos), I2C bus board build (3 videos). Recommend the user confirm a series page on the next session.
  - **Renishaw AM400 operation** — 2-episode mini-series covering the AM400 loose-assembly inspection and the QuantAM build-prep walkthrough; may overlap with the 2016 thesis arc.
  - **Laminar-flow nozzle design** — explicit June 20-21 2019 two-part build pair (combine-two-bodies-in-solidworks + 3d-printed-laminar-flow-nozzle-construction).

- **Lint flags for future cleanup**:
  - `renishaw-am400-should-this-thing-be-loose` transcript may have an automated-caption mishearing: "two minutes are probably loose" almost certainly should be "two nuts" or "two screws". Per schema, raw transcripts are immutable — flagged here for the next lint pass to consider an annotation in the video page rather than a transcript edit.
  - `concepts/soldering-header-pins` is too narrow as a label for the SCUTTLE motor-soldering content — the new motor-soldering video applies the same technique to motor terminals, not headers. A concept rename to `soldering-stranded-leads` or split-into-two-concepts would be cleaner; deferred for user decision.
  - `entities/tools/solidworks-2020` exists as a tombstone (rewritten with `status: redirected` frontmatter) but the file itself could not be deleted by the consolidator. User can `rm wiki/entities/tools/solidworks-2020.md` to fully retire the slug.
  - Two earlier batch-3 truncated slugs continue to live in the wiki (`scuttle-robot-multithreading-explained-with-demonstration-speed-control-text-to-` and `scuttle-robot-demonstration-for-reading-gpio-input-on-beaglebone-blue-with-l1-gp`); kept as-is per schema.
