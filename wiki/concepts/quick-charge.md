---
type: concept
aliases: [QC, Quick Charge protocol]
tags: [usb, power-delivery, charging]
source_count: 2
---

# Quick Charge (QC)

## Definition

Qualcomm's pre-USB-PD fast-charging protocol that negotiates a 9V (or higher) supply on an otherwise-5V USB port by signaling over the data pins. If the charger sees a compliant request, it boosts; otherwise it defaults to 5V.

## How David uses it

In [[videos/more-about-usb-than-you-ever-wanted-to-know]], David characterizes QC as the "exception to the rule" that standard USB ports are always 5V. He admits his treatment isn't rigorous and warns viewers not to treat it as ground truth — full USB-PD coverage is deferred to a future video.

**Practical warning**: QC is dangerous on a shared splitter. If one connected device requests 9V, the whole bus may jump to 9V, frying any legacy 5V device on the same splitter. Outside of dedicated single-port chargers, David recommends avoiding QC entirely.

The one place David finds QC genuinely useful is wireless charging, where a 4-wire cable + QC-aware charger yields ~20 W instead of the ~5 W you get on a 2-wire power-only cable.

## Related

- [[concepts/ferrite-noise-suppression]]
- [[concepts/instrument-resolution]]

## Appears in

- [[videos/more-about-usb-than-you-ever-wanted-to-know]]
- [[videos/build-a-battery-adapter-to-power-the-whole-lab]]

