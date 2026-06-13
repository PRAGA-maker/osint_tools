---
id: enrichment
name: phase-enrichment
description: Use once a lead is confirmed — go deep on that one node to extract every selector and fact it holds before you move on.
type: pattern
phase: enrichment
pivotFrom: []
pivotTo: []
summary: Where the pivot phase grows the graph breadth-first, enrichment deepens a single confirmed node. You've verified this account/person is the subject; now you mine it exhaustively — every post, every tagged photo, every linked account, the follower graph, the bio links, the historical activity — converting one confirmed selector into a dense cluster of new ones. Enrichment is depth-first by design, which is only safe AFTER verification has locked the node to the subject.
missingPersonsRelevance: high
whenToUse: After a selector is confirmed (not a candidate) and you want to extract maximum signal from it.
steps:
- Confirm the node is verified, not a candidate — enrichment amplifies whatever you feed it, including errors.
- Mine the profile fully — bio links, pinned/old posts, tagged photos, location tags, "about" fields, linked accounts, joined-date.
- Walk the close network one hop — family/best-friend accounts often hold the photos and check-ins the subject hid (see `[[pivot-network-triangulation]]`).
- Pull historical state — Wayback/cache for deleted bios and posts; old posts often pre-date the privacy lockdown.
- Build the timeline from what you find — last-known-activity, recurring locations, routine (see `[[pattern-timeline-anchoring]]`).
signals:
- The single confirmed node is spawning many new selectors that keep cohering (same person, consistent timeline/location).
- You're finding the same fact from two independent places inside the cluster — self-corroboration that strengthens confidence.
pitfalls:
- Enriching an UNVERIFIED node — you build a rich, confident profile of the wrong person.
- Stopping at the live profile and skipping archives — the most useful posts are often the deleted/old ones.
- Drifting into active engagement (following, messaging) to see more — that's contamination (see `[[antipattern-contaminating-the-subject]]`).
toolsUsed:
- wayback-machine
trust: trusted
relatedStrategies:
- phase-pivot
- phase-verification
- pivot-network-triangulation
- pattern-timeline-anchoring
tags:
- core
- depth
source: ''
---

# Phase: Enrichment

## The move
Go deep on one node. Pivot grows the graph wide; enrichment drills one **confirmed** node to bedrock — every post, photo, tag, link, follower, and archived version — turning a single verified selector into a dense cluster of new ones.

## Why it comes after verification
Enrichment is depth-first, and depth-first amplifies whatever you point it at. Point it at a verified node and you get a rich true picture; point it at a candidate and you get a rich *false* one. The verification gate (`[[phase-verification]]`) is what makes going deep safe.

## What to mine
- **The profile itself** — bio links, "about" fields, pinned and oldest posts, location tags, joined-date, linked/cross-posted accounts.
- **The close network, one hop** — a private subject often appears in a relative's or best friend's public photos and check-ins. This is `[[pivot-network-triangulation]]`.
- **History** — Wayback and platform cache recover deleted bios, old handles, and posts that pre-date a privacy lockdown. The richest selectors are frequently the ones the subject later removed.

## Build the timeline as you go
Enrichment is where the last-known-activity timeline takes shape: recurring locations, posting cadence, routine. Feed it straight into `[[pattern-timeline-anchoring]]`.

## The discipline
Stay passive. The temptation to follow or message "to see more" is real and is exactly how you contaminate a case — see `[[antipattern-contaminating-the-subject]]`. Everything worth having on a public-leaning subject is reachable without contact.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | enrichment |
| pivot | any → any |
| MP relevance | high |
