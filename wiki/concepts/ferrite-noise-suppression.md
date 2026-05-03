---
type: concept
aliases: [ferrite core, ferrite bead]
tags: [electronics, emi, usb]
source_count: 1
---

# Ferrite noise suppression

## Definition

A ferromagnetic sleeve (the lump on a good USB or monitor cable) presents high impedance to common-mode high-frequency current, suppressing EMI on data lines.

## How David uses it

In [[videos/more-about-usb-than-you-ever-wanted-to-know]], David slices open a printer's bundled USB cable and explains the ferrite lump as part of a two-layer defense: **shielding blocks noise, ferrite kills noise**. He then slices open a cheap cable advertising a "ferrite core" and finds the sleeve is plain rubber. Simple test: real ferrite is magnetic. Rubber isn't.

Sold cables that use real ferrite are typically the ones bundled with printers or USB-B peripherals where 10+ feet of serial cable becomes an antenna.

## Appears in

- [[videos/more-about-usb-than-you-ever-wanted-to-know]]
