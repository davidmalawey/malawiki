# Raw transcripts

This directory holds the source transcripts pulled from David Malawey's YouTube channel. **Files here are immutable** — Claude reads them but never modifies them.

## Intake format

One markdown file per video. Name the file by upload date + kebab-case slug:

```
YYYY-MM-DD_<slug>.md
```

Example: `2026-03-14_building-a-forge.md`

## File structure

Each transcript file should start with a small header block so Claude can auto-extract metadata on ingest:

```markdown
---
title: "Building a Forge from Scratch"
url: "https://www.youtube.com/watch?v=abc123"
video_id: "abc123"
published: 2026-03-14
duration: "22:15"
channel: "David Malawey"
---

# Transcript

[0:00] ...
[0:12] ...
```

If the Chrome extension outputs a different shape, that's fine — Claude will read whatever's in the file and fill in gaps on ingest, asking once for anything it can't infer.

## Workflow

1. Pull the transcript via the Claude Chrome extension while on the video page.
2. Save it to this directory with the naming convention above.
3. In a Claude session opened at the project root, say "ingest <slug>" (or just "ingest the new transcript").
4. Claude reads `CLAUDE.md`, processes the transcript, and updates the wiki.
