# CLAUDE.md — David Malawey YouTube Wiki

This file is the schema for this wiki. Every Claude session should read it before doing anything else. Co-evolve it with the user as conventions settle.

## Purpose

A personal wiki for David Malawey's YouTube channel, built with the [LLM Wiki pattern](https://github.com/). Transcripts pulled from YouTube via the Claude Chrome extension are the raw sources. The LLM reads each transcript and maintains a structured, interlinked markdown knowledge base covering videos, people, tools, materials, techniques, projects, and series.

The channel focuses on hobbyist / craft / how-to content.

## Architecture

Three layers:

- `raw/transcripts/` — source transcripts. **Immutable.** Read but never modify.
- `wiki/` — LLM-generated, interlinked markdown pages. The LLM owns this layer.
- `CLAUDE.md` (this file) — the schema.

Out-of-scope layers (do not ingest, do not link from the wiki):

- `scratch/` — scratchpad for the YouTube channel-surface skill family. Holds test harvests (About tabs, shorts, playlists, schema dumps, community posts, etc.) that the skill is *capable* of producing but that the Malawey KB does not consume. Treat as if it isn't there during ingest, query, and lint workflows. See `scratch/README.md` for its own conventions.
- `skill-dev/` — SKILL.md drafts, shared schemas, and research docs for the `yt-channel-inventory`, `yt-transcript-fetch`, `yt-channel-about` skill family. Source of truth before a skill is packaged into a `.skill` archive. Also ignored by all KB workflows.

Navigation aids at the project root:

- `index.md` — catalog of every wiki page with one-line summaries. Updated on every ingest.
- `log.md` — chronological, append-only record of ingests, queries, and lint passes.

## Directory layout

```
raw/
  transcripts/
    YYYY-MM-DD_<slug>.md       # one file per video, named by upload date

wiki/
  overview.md                   # rolling synthesis of the wiki
  videos/<slug>.md              # one page per transcript
  entities/
    people/<slug>.md            # David, guests, referenced figures
    tools/<slug>.md             # specific tools used or discussed
    materials/<slug>.md         # wood, metal, resin, etc.
    brands/<slug>.md            # manufacturers, suppliers
    projects/<slug>.md          # specific builds / creations featured
    places/<slug>.md            # workshops, venues, shops
  concepts/<slug>.md            # recurring techniques, philosophies, safety practices
  series/<slug>.md              # playlists or multi-video arcs

scratch/                        # IGNORED by KB workflows (ingest / query / lint)
  inventory/                    # channel-inventory JSONs for non-Malawey creators
  about/                        # About-tab raw dumps (description, links, total views)
  shorts/                       # Shorts-tab harvests
  playlists/                    # Playlists-tab harvests
  community/                    # Community-tab posts / polls / images
  live-streams/                 # past live broadcasts harvested separately from VOD
  schema-dumps/                 # ytInitialData / JSON-LD / RSS samples
  comments-stub/                # reserved for future yt-comments-fetch skill
```

Create entity subfolders on demand — no need to pre-create empty folders.

## File naming

- All slugs are kebab-case, ASCII only.
- Video page slug matches its transcript slug (minus the date prefix). Transcript `2026-03-14_building-a-forge.md` → video page `wiki/videos/building-a-forge.md`.
- Entity slugs should be the canonical common name (`angle-grinder`, not `dewalt-dw4-angle-grinder`).

## Frontmatter standards

All wiki pages start with YAML frontmatter.

**Video page:**
```yaml
---
type: video
title: "Building a Forge from Scratch"
video_id: "abc123"
url: "https://youtu.be/abc123"
published: 2026-03-14
duration: "22:15"
series: "[[forge-build]]"   # optional
tags: [blacksmithing, forge, build]
ingested: 2026-04-23
---
```

**Entity page:**
```yaml
---
type: entity
kind: tool           # one of: person | tool | material | brand | project | place
aliases: []
first_seen: "[[videos/building-a-forge]]"
tags: []
source_count: 1
---
```

**Concept page:**
```yaml
---
type: concept
aliases: []
tags: []
source_count: 1
---
```

**Series page:**
```yaml
---
type: series
title: "Forge Build"
started: 2026-02-01
status: ongoing       # ongoing | complete
tags: []
episode_count: 0
---
```

## Linking

- Use Obsidian-style wiki links everywhere: `[[entities/tools/angle-grinder|angle grinder]]`.
- Linking is two-way: if a video mentions an entity, the entity page gets that video added under "Appears in". Do not leave one-way references.
- Prefer linking over re-explaining. If a technique already has a concept page, link to it instead of describing it inline.

## Page templates

**Video summary page** — use these sections, skip any that don't apply:
- Overview (2-3 sentences)
- Key takeaways (bullet list)
- Techniques demonstrated (links to concept pages)
- Tools used (links)
- Materials used (links)
- Projects (links)
- People mentioned (links)
- Notable quotes / timestamps (optional)
- Related videos

**Entity page:**
- Short description (1-2 sentences)
- Details (type-specific — specs for tools, properties for materials, bio for people, etc.)
- Appears in (bulleted list of video links)
- Related entities / concepts

**Concept page:**
- Definition
- How it's used (what videos demonstrate it, in what context)
- Variations / sub-techniques
- Related concepts
- Appears in

**Series page:**
- Premise (what the series is building toward)
- Episodes (ordered list of video links)
- Open threads (what's unresolved)
- Related concepts / projects

## Ingest workflow (auto-ingest, minimal confirmation)

When the user drops a transcript into `raw/transcripts/` and says "ingest" (or equivalent):

1. Read the transcript.
2. Extract title, URL, published date, duration from the transcript header. If any are missing, make one request for the missing fields — don't ask field-by-field.
3. Create `wiki/videos/<slug>.md` using the video page template.
4. Scan for entities. For each:
   - Exists → increment `source_count`, append to "Appears in", merge any new facts into the body.
   - Doesn't exist → create a stub with frontmatter and a 1-2 sentence description.
5. Do the same for concepts (techniques, themes).
6. If the video fits an existing series, update the series page's episode list. If it looks like the start of a new series, propose one in your report but don't auto-create without confirmation.
7. Update `index.md` with any new pages.
8. Append an entry to `log.md`:
   ```
   ## [YYYY-MM-DD] ingest | <video title>
   - Created: wiki/videos/<slug>.md
   - Created entities: [[tools/x]], [[materials/y]]
   - Updated: [[concepts/z]] (source_count 3 → 4)
   ```
9. Report to the user: one-paragraph recap, then a bulleted list of pages touched. No approval prompts during ingest — the log and report are the review surface.

## Query workflow

1. Read `index.md` first to find candidate pages.
2. Drill into them; synthesize an answer.
3. Cite specific wiki pages in the answer.
4. If the answer itself is reusable (a comparison, a timeline, a synthesis), offer to file it back as a new wiki page.
5. Append to `log.md`: `## [YYYY-MM-DD] query | <question>`.

## Lint workflow

When the user says "lint" or "health check":

1. Orphan pages — pages with zero inbound wiki-links.
2. Stubs that have enough `source_count` to deserve fleshing out.
3. Contradictions — claims on one page inconsistent with another.
4. Missing pages — concepts or entities referenced repeatedly but without a page.
5. Stale claims — newer transcripts superseding older summaries.
6. Report findings. Don't auto-fix unless the user says so.
7. Log: `## [YYYY-MM-DD] lint | <summary>`.

## Hard rules

- Never modify `raw/transcripts/`.
- Every new wiki page must have valid frontmatter.
- Every reference to an entity or concept in prose must be a wiki link.
- Update `index.md` in the same turn as creating or renaming pages — do not let it drift.
- Convert relative dates to absolute dates in log entries (today is the ingest date).
- **Ignore `scratch/` and `skill-dev/` entirely** during ingest, query, and lint. Do not read, link, or catalog anything under them. Files there belong to the skill-development layer, not the wiki.

## Co-evolution

This schema is not frozen. If you notice a pattern the schema doesn't cover — a new entity subtype, a recurring page shape, a useful tag convention — propose an update to this file alongside the ingest report.
