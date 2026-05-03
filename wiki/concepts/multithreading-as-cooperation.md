---
type: concept
aliases: ["multithreading not magic"]
tags: []
source_count: 1
---

# Multithreading as cooperation

## Definition

Multithreading is not a magic speed-up tool — it only helps when the bottleneck is wait time (I/O, audio playback, network), not compute. Two threads sharing one CPU don't go faster; they just stop blocking on each other.

## Appears in

- [[videos/scuttle-robot-multithreading-explained-with-demonstration-speed-control-text-to-]]

## Related

- [[concepts/loop-vs-routine]]
- [[concepts/graceful-degradation]]
