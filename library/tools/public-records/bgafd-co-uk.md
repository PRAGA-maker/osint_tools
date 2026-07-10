---
id: bgafd-co-uk
name: bgafd.co.uk
description: Use when you need to identify a British adult-film performer by stage name and resolve aliases/physical description — a niche performer database returning `name`, aliases and `physical-description`.
url: http://www.bgafd.co.uk
category: public-records
path:
- public-records
bestFor: Identifying/disambiguating a British female adult-film performer and resolving stage-name aliases.
selectorsIn:
- name
selectorsOut:
- name
- physical-description
- associate
status: live
pricing: free
costNote: Free reference database; no account to search/browse.
opsec: passive
opsecNote: Read-only browsing of a public performer database; no individual is queried or notified. Handle results with discretion — this concerns adult-industry identities and sexual history, which are sensitive personal data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing, single-topic fan/reference database (the British Girls Adult Film Database); community-compiled, so aliases and details are unofficial and may be incomplete or dated.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- BGAFD
- British Girls Adult Film Database
tags:
- performer-database
- alias-resolution
- adult-industry
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# bgafd.co.uk

> The British Girls Adult Film Database — a niche reference for identifying British female adult-film performers and resolving their stage-name aliases.

## When to use
You are trying to identify a person who appears in British adult media, or to connect a stage name to other aliases and biographical/physical detail. BGAFD indexes ~2,800 performers and ~21,500 titles, so it can turn a single stage name into a set of aliases (`associate`/alternate `name`s) and a `physical-description`, which may help confirm an identity, link personas, or corroborate that a subject worked in the industry. Treat this as sensitive and use it only for legitimate identification purposes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.bgafd.co.uk.
2. Browse/search by performer `name` (A–Z index), by film title, or check the "unknown performers" section.
3. Read the performer page: known aliases/alternate stage names, filmography, and physical description details.
4. Corroborate any alias link before relying on it — this is community-compiled.
5. Pivot: an alias `name` feeds username/people-search; a `physical-description` supports photo/face comparison.

## Inputs → Outputs
- **In:** performer stage `name` (or film title)
- **Out:** alternate `name`s/aliases, `physical-description`, filmography (`associate` links between personas)
- **Empty/negative result looks like:** no performer/title match — the person isn't in this UK-scoped database (they may be non-British, more recent, or simply uncatalogued). Absence is not evidence of anything.

## Gotchas & OpSec
- **Sensitive data**: adult-industry identity and sexual history — use strictly for legitimate identification, mind data-protection and dignity, and store findings carefully.
- UK female performers only; community-compiled, so coverage/aliases can be incomplete or dated.
- OpSec: **passive** — a public database read.

## Overlaps ("do both")
- Complements reverse-image/face tools — BGAFD resolves a stage name to aliases and description, while a reverse-image search on a still can connect the same person across other media.

## Trust & verifiability
`trust: community` — a long-standing but unofficial fan-compiled database; treat aliases and details as leads to corroborate, especially given the sensitivity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bgafd-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → name, physical-description, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
