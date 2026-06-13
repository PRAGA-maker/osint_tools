---
id: opsec
name: phase-opsec
description: Use throughout — protect the investigation, the investigator, and above all the subject; the cross-cutting discipline that keeps you passive and keeps you from tipping anyone off.
type: pattern
phase: opsec
pivotFrom: [any]
pivotTo: [any]
summary: OpSec is not a phase you do once — it's a constraint that rides every other phase. Three things to protect, in priority order: the subject (don't tip them off, don't endanger them, don't dox them publicly), the investigation (don't leave footprints that burn a source or get you blocked), and the investigator (don't expose your real identity to a potentially hostile target). The default posture is passive: look without touching. Most opsec failures are the moment someone logs in, follows, or messages "just to see more."
missingPersonsRelevance: high
whenToUse: Always — before every action ask "does this touch the subject or leave a footprint?"
steps:
  - Default to passive — viewing public data leaves far fewer traces than logging in, following, or messaging. Prefer the contactless path every time.
  - When login is unavoidable, use a sock-puppet/research account that is in no way linked to your real identity or to the subject's network.
  - Never follow, friend, like, message, or join from a real or subject-linked account — these notify the target and contaminate the case (see `[[antipattern-contaminating-the-subject]]`).
  - Mind your egress — view counts, "seen" receipts, story views, and platform "people you may know" graphs can leak your interest to the target.
  - Protect the subject in output — route findings privately to the proper authority, never publish personal data; the bar is higher for minors.
signals:
  - Every action you've taken is one a passive observer could have taken — no notifications were generated on the target side.
  - Your research identity and your real identity are cleanly separated with no crossover.
pitfalls:
  - Logging in with your personal account to "just check" — view receipts, story views, and PYMK suggestions leak you to the target.
  - Following or messaging the subject or an associate — instant contamination and possible danger to the subject.
  - Publishing the subject's location or identity publicly — endangers them and destroys the investigation's legitimacy.
toolsUsed: [sock-puppet-generator]
trust: trusted
relatedStrategies: [antipattern-contaminating-the-subject, phase-reporting, phase-intake, platform-instagram]
tags: [core, opsec, safety, cross-cutting]
source: ""
---

# Phase: OpSec (cross-cutting)

## The move
Protect three things, in order: **the subject**, **the investigation**, **the investigator**. OpSec isn't a stage — it's a filter every action passes through. Before you click, ask: does this touch the subject, and does it leave a footprint?

## Passive by default
The single most important habit is looking without touching. Viewing public content is low-trace; logging in, following, liking, messaging, joining, or story-viewing is high-trace and frequently *notifies the target*. The whole tree is built around contactless pivots for this reason — almost everything worth having is reachable passively. When a pivot tempts you toward engagement "to see more," that's the signal to stop, not proceed.

## When you must log in
Some platforms gate everything behind an account. Use a **sock puppet** — a research persona with no link to your real identity and no overlap with the subject's network — and assume the account itself is observable. A puppet that follows the subject is still contamination; the puppet protects *your identity*, not the subject from being tipped off.

## Mind the egress
Platforms leak the observer, not just the observed. Story/Reel view lists, "seen" receipts, profile-view notifications, and "People You May Know" / "Who viewed your profile" graphs can surface your interest to the target — especially if you browsed from a real or weakly-separated account. Know which platform leaks what (`platforms/` notes flag these).

## Protecting the subject in output
The subject is the top priority. Findings go privately to the **proper authority**, never into a public post. Don't publish a location, an identity, or a photo. If the subject is a minor, the bar is higher still. This connects straight to `[[phase-reporting]]` and is the positive form of `[[antipattern-contaminating-the-subject]]`.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | opsec |
| pivot | any → any |
| MP relevance | high |
