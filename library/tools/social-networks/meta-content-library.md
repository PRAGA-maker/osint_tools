---
id: meta-content-library
name: Meta Content Library
description: Use when you have a `name`, `username`, or keyword and (as an approved researcher) want to search all public Facebook/Instagram/Threads posts — returns posts, accounts, and engagement.
url: https://transparency.meta.com/researchtools/meta-content-library
category: social-networks
path:
- social-networks
bestFor: Searching the full public archive of Facebook, Instagram, and Threads posts in near-real-time — for approved academic/nonprofit researchers.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to use, but access is gated to vetted researchers at qualified academic/nonprofit institutions; there is no paid path around the approval requirement.
opsec: passive
opsecNote: Passive toward subjects — you query Meta's archive, not accounts, so no one is notified. But access is tied to your vetted, named researcher identity and use is bound to an approved project scope and Meta's terms; it is not anonymous.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: A first-party Meta research tool serving Meta's own public-content data; authoritative for what it covers, but access-gated and scope-limited by Meta's research program.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: true
relatedTools:
- crowdtangle
- facebook-search-tool
aliases:
- Meta Content Library
- MCL
- Meta transparency research tools
tags:
- bellingcat-toolkit
- facebook
- instagram
- threads
source: bellingcat-toolkit
lastVerified: '2026-07-18'
enrichment: full
---

# Meta Content Library

> Meta's controlled-access research tool — approved researchers can search the full public archive of Facebook, Instagram, and Threads in near-real-time.

## When to use
You are (or work with) a vetted researcher at a qualifying academic or nonprofit institution and need to search public content across Meta's platforms at archive scale — every public post, page, group, and account matching a `name`, `username`, or keyword, with engagement metrics and near-real-time coverage. For missing-persons work this is high-value where access exists: it can surface a subject's public posts, the accounts around them (`associate`), and public activity that ordinary in-app search buries — succeeding CrowdTangle as Meta's research offering.

## How to use it (`bestInteractionPattern`: web-manual)
1. Apply for access via https://transparency.meta.com/researchtools/meta-content-library — approval requires a qualifying institution and an ethics/vetting review (this is the gate).
2. Once approved, use the web Content Library UI (or the associated API) to search by keyword, `name`, `username`, page, or account.
3. Filter by platform (Facebook/Instagram/Threads), date, and content type; read matching public posts with engagement data.
4. Export/analyze within the approved project scope and Meta's terms.
5. Pivot: accounts and interactions found here feed profile-analysis tools; corroborate anything public directly on the platform.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** public posts and `social-profile`s across FB/IG/Threads, plus `associate` links via interactions and engagement metrics
- **Empty/negative result looks like:** no matches — the content is non-public (the library only indexes public content), outside the covered window, or excluded by policy; absence is not proof the subject has no Meta presence.

## Gotchas & OpSec
- **Access-gated:** requires institutional vetting and manual approval — it is not open to the general public or freelance investigators.
- Public content only; private profiles, DMs, and closed groups are out of scope.
- Use is bound to your approved research project and Meta's terms — off-scope use risks access revocation.
- OpSec: passive toward subjects, but fully attributable to your researcher identity.

## Overlaps ("do both")
- Pairs with `[[crowdtangle]]` (its predecessor, now largely retired) and `[[facebook-search-tool]]` (open, no-approval Facebook search techniques) — use those when you lack MCL access, and MCL when you have it for far broader, authoritative coverage.

## Trust & verifiability
`trust: trusted` — first-party Meta data served through an official research program; results are authoritative for public content, though gated access and policy scoping limit who can use it and how.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | meta-content-library |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
