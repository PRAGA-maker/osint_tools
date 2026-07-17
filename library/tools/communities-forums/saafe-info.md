---
id: saafe-info
name: SAAFE.info
description: Use when a subject is connected to UK/Ireland sex work and you want a peer-support forum whose "Warnings & Wasters" board names dangerous clients — returns forum posts, `username`s, and warning threads.
url: https://saafe.info/main/index.php
category: communities-forums
path:
- communities-forums
bestFor: Reading the SAAFE peer-support forum and its client-warnings board for leads on people tied to UK/Ireland sex work.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free community forum run by and for sex workers; reading public boards is free, some areas may require a free account.
opsec: active
opsecNote: This is a safety resource for a vulnerable, criminalised community. Treat it with extreme care and ethical restraint. Do NOT register or post with any traceable identity, do NOT contact members, and do NOT scrape or repost warning-board content — doing so can endanger real people. Read only what is public, minimise footprint, and use a sock-puppet browser session. Only pursue this when it genuinely serves the welfare of the subject.
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
bestInteractionPattern: web-manual
trust: community
trustNote: A genuine, long-running peer-support forum (Support And Advice For Escorts); content is anonymous user posts and warnings — unverified, and posted for member safety rather than as vetted fact.
missingPersonsRelevance: medium
coverage:
- uk
- ie
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Support And Advice For Escorts
- saafe forum
tags:
- forum
- sex-work
- safety
- community
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# SAAFE.info

> A peer-support forum run by and for sex workers in the UK/Ireland, including a "Warnings & Wasters" board flagging dangerous or fraudulent clients — a sensitive, welfare-first source to be handled with great care.

## When to use
Only when a subject is genuinely connected to UK/Ireland sex work and the investigation serves their welfare (e.g. locating or safeguarding a missing person in that community, or understanding a warning that names a dangerous individual). The forum's public threads can surface a persona's `username`, self-disclosed details, and — on the Warnings board — reports naming or describing dangerous clients (`associate`s in a safeguarding sense). This is a lead source about risk, not a people-search database.

## How to use it (`bestInteractionPattern`: web-manual)
1. Browse the public boards from https://saafe.info/ in a clean, sock-puppet browser session. Ignore the session token in any harvested link.
2. Read the relevant board (general advice, or "Warnings & Wasters" for client-danger reports); use on-site navigation rather than aggressive searching.
3. Note only what is publicly posted — a `username`, a described individual, a location or time reference — and corroborate elsewhere before treating it as fact.
4. Do not register, post, message members, or copy warning content out. If a section needs login, weigh carefully whether it is ethical and necessary before creating a puppet account.
5. Pivot cautiously: a reused `username` can be checked across platforms; a named dangerous individual can be cross-referenced in public records — always with the community's safety in mind.

## Inputs → Outputs
- **In:** a `username`/`name` plausibly tied to UK/Ireland sex work.
- **Out:** public forum posts, `username`s, and warning threads naming/describing individuals (`social-profile`/`associate` leads).
- **Empty/negative result looks like:** no matching persona or thread — the handle isn't used here; this is a niche, access-limited community. Absence means nothing broader.

## Gotchas & OpSec
- Human-in-the-loop / legal-and-ethical gate: this community is vulnerable and criminalised in places. Careless use can cause real harm — proceed only with a clear welfare justification.
- Content is anonymous and unverified; warnings are posted for safety, not as adjudicated fact. Never republish or weaponise them.
- Active by nature of login-gated areas — never touch it from a real identity, and never contact members.

## Overlaps ("do both")
- Any lead here must be corroborated with public records or platform checks; treat SAAFE as context, not evidence, and keep the subject's safety central.

## Trust & verifiability
`trust: community` — an authentic peer-support forum. Its content is unverified user experience shared for protection; use it to understand risk and generate cautious leads, never as a standalone factual source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | saafe-info |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, legal-gate) |
