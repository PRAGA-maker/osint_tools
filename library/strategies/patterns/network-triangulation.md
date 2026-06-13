---
id: network-triangulation
name: pattern-network-triangulation
description: Use as a default instinct — a person is visible through the people around them; when the subject hides, pivot to the network and read it for the selectors the subject won't show.
type: pattern
phase: pivot
pivotFrom: [social-profile, associate, name]
pivotTo: [social-profile, image, geolocation, associate]
platforms: [instagram, facebook, tiktok, snapchat]
summary: Network triangulation is the cross-cutting principle behind the social-profile→associate pivot: privacy is rarely symmetric, so a subject who locks down their own account is usually still visible in the public content of their friends, family, and partners. As a habit of mind it means you never treat a private subject as a dead end — you reflexively ask "who's around them, and what are THEY posting?" The concrete how-to lives in the pivot; this is the doctrine that makes you reach for it.
missingPersonsRelevance: high
whenToUse: Any time the subject's own footprint is thin, private, or stale and you have any thread to a connected person.
steps:
  - Reframe a private subject as a network problem — the question becomes "who's around them?" not "what did they post?".
  - Find any one associate — a tagged account, a frequent commenter, a shared surname, a partner.
  - Read the network's PUBLIC output for the subject's leaked selectors — face in group photos, location in others' check-ins, activity in others' stories.
  - Triangulate — multiple associates' posts converging on a place/time locates the subject more reliably than any single source.
  - Keep it passive and verify the face — observe only; confirm it's the subject before trusting any tag.
signals:
  - You stopped treating a locked profile as a wall and immediately had three new avenues (their three closest people).
  - Independent associates' posts agree on the subject's recent location — triangulated, not single-sourced.
pitfalls:
  - Treating a private subject as un-findable instead of pivoting to the network.
  - Engaging the network (follow/message) and tipping off the subject (see `[[antipattern-contaminating-the-subject]]`).
  - Assuming a person in an associate's photo is the subject without verifying the face.
toolsUsed: [instagram-search, facebook-search]
evidence: []
trust: trusted
relatedStrategies: [pivot-network-triangulation, phase-enrichment, antipattern-contaminating-the-subject, antipattern-tunnel-vision]
tags: [associate, social, network, doctrine, cross-cutting]
source: ""
---

# Pattern: Network triangulation

## The doctrine
A person is visible through the people around them. This is the principle; the step-by-step is the pivot `[[pivot-network-triangulation]]`. The reason it deserves its own pattern is that it's a *default instinct* you want to install: when a subject is private or quiet, you should reflexively reframe the problem from "what did the subject post?" to "who is around the subject, and what are *they* posting?"

## Why privacy is asymmetric
People can lock their own accounts, but they can't lock their friends'. A subject appears in a cousin's birthday album, a partner's geotagged check-in, a best friend's story — all public, none under the subject's control. The network leaks what the subject hides. So a private profile is never a dead end; it's a redirect to the people one hop out.

## Triangulation, literally
The word is precise: you locate the subject by intersecting *multiple* independent associates' public content. One friend's geotagged photo is a lead; three associates' posts converging on the same place and time is a *location*. That convergence is also your verification — independent sources agreeing is exactly the bar `[[phase-verification]]` asks for.

## The two disciplines
- **Passive only.** Reading the network is contactless; *engaging* it (following, messaging, friending an associate) notifies people and can reach the subject. That's `[[antipattern-contaminating-the-subject]]`, and the network is where the temptation peaks.
- **Verify the face.** The person beside your associate is a candidate, not the subject, until confirmed. Don't let a convenient group photo skip the verification step.

This pattern is also the antidote to `[[antipattern-tunnel-vision]]`: when one profile dead-ends, the network is a whole new breadth of leads.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | pivot |
| pivot | social-profile, associate → image, geolocation, associate |
| platforms | instagram, facebook, tiktok, snapchat |
| MP relevance | high |
