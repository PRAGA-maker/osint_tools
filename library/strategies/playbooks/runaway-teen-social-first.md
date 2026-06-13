---
id: runaway-teen-social-first
name: playbook-runaway-teen-social-first
description: Use for a likely-runaway minor with a social footprint — an ordered, social-media-first sequence that exploits how heavily teens leak selectors online while respecting the heightened safety bar for minors.
type: playbook
phase: triage
pivotFrom: [name, username, social-profile, image]
pivotTo: [geolocation, associate, social-profile, any]
platforms: [instagram, tiktok, snapchat, discord, telegram]
summary: A runaway teenager is the case type most favorable to social-first OSINT — minors live on Instagram, TikTok, Snapchat, and Discord, and they leak location, associates, and recent activity constantly, often continuing to post after leaving. This playbook orders the work to exploit that: confirm the subject's accounts, mine recent posts for a current-location and last-known-activity signal, triangulate through friends, and build a timeline — all passively, all routed to the proper authority, with the minor-safety bar raised throughout.
missingPersonsRelevance: high
whenToUse: A minor is missing, likely voluntarily (runaway), and has an active social-media presence or known handles.
steps:
  - INTAKE — confirm age (minor), the time/place last seen, the seed selectors, and that "found" means a current location/proof-of-life routed to authorities. Raise the safety bar.
  - Confirm the subject's own accounts — enumerate known handles, disambiguate to the real person; teens reuse handles heavily (`[[username-reuse-enumeration]]`).
  - Mine RECENT activity first — a runaway often keeps posting; the newest post is the freshest location/timeline signal. Reverse-image any photos (`[[pattern-reverse-image-everything]]`).
  - Triangulate through friends — the close circle (best friends, a partner) often knows or reveals where they went; read their PUBLIC posts (`[[pivot-network-triangulation]]`).
  - Build the last-known-activity timeline — order posts, check-ins, and tags; the goal is the most recent confirmed point (`[[pattern-timeline-anchoring]]`).
  - Report to authorities ONLY — never contact the teen or friends, never publish; minors raise the bar further (`[[phase-reporting]]`, `[[phase-opsec]]`).
signals:
  - A post-disappearance post or story gives a fresh location or proof of life.
  - Friends' public content triangulates a current city or a place they're staying.
pitfalls:
  - Contacting the teen or their friends to "help" — tips them off, endangers them, and contaminates the case (see `[[antipattern-contaminating-the-subject]]`).
  - Publishing anything about a minor publicly — a serious safety and legal failure.
  - Forcing a lookalike teen account as the subject — common handles and young-user churn make false matches easy (`[[antipattern-forcing-the-match]]`).
toolsUsed: [whatsmyname-web, instagram-search, snapchat-map, yandex-images]
evidence: []
trust: trusted
relatedStrategies: [username-reuse-enumeration, pivot-network-triangulation, pattern-timeline-anchoring, antipattern-contaminating-the-subject, phase-opsec]
tags: [playbook, runaway, minor, social, high-yield]
source: ""
---

# Playbook: Runaway teen, social-first

## When this applies
A minor is missing, the circumstances suggest they left voluntarily (a runaway), and they have — or you have handles into — an active social-media presence. This is the single most social-first-favorable case type, because teenagers live on Instagram, TikTok, Snapchat, and Discord and leak selectors constantly. Critically, a runaway frequently **keeps posting** after leaving, which makes recent activity gold.

## The minor-safety bar (read first)
Because the subject is a minor, the safety and legal bar is raised throughout: strictly passive, **no contact** with the subject or their friends, **nothing published**, and findings routed only to law enforcement or the sponsoring search org. This frames every step below. See `[[phase-opsec]]` and `[[phase-reporting]]`.

## The ordered sequence
1. **Intake.** Confirm age, last-seen time/place, the seed selectors, and the "found" definition (a current location / proof of life handed to authorities). `[[phase-intake]]`.
2. **Confirm their accounts.** Enumerate known handles and disambiguate to the real subject — teens reuse handles heavily, so one confirmed handle usually unlocks several. `[[username-reuse-enumeration]]`.
3. **Mine recent activity first.** Sort by newest. A runaway's latest post or story is the freshest location and proof-of-life signal — far more actionable than their back-catalogue. Reverse-image every photo (`[[pattern-reverse-image-everything]]`) and read backgrounds for place (`[[pivot-image-to-geolocation]]`).
4. **Triangulate through friends.** The close circle — best friend, partner, the group chat regulars — frequently knows where they went and leaks it in *public* posts. Read the network passively. `[[pivot-network-triangulation]]`.
5. **Build the timeline.** Order everything dated; the target is the most recent confirmed activity. `[[pattern-timeline-anchoring]]`.
6. **Report to authorities only.** Privately, with provenance and confidence. Never contact, never publish. `[[phase-reporting]]`.

## The big failure modes
- **Contacting the teen or their friends** "to help" — tips them off, can endanger them, contaminates the case. `[[antipattern-contaminating-the-subject]]`.
- **Publishing anything** about a minor — serious safety/legal failure.
- **Forcing a lookalike account** — teen platforms churn and handles collide; verify before you commit. `[[antipattern-forcing-the-match]]`.

---
## Metadata
| field | value |
|---|---|
| type | playbook |
| phase | triage → pivot → reporting |
| platforms | instagram, tiktok, snapchat, discord, telegram |
| MP relevance | high |
| tools | whatsmyname-web, instagram-search, snapchat-map, yandex-images |
