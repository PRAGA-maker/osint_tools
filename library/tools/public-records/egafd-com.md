---
id: egafd-com
name: egafd.com
description: Use when you have a `name`/stage name or `image` of a European female adult-film performer and want to identify or cross-reference them — returns confirmed `name`, aliases and `associate` links.
url: https://www.egafd.com/fora/viewforum.php?f=4
category: public-records
path:
- public-records
bestFor: Identifying continental-European female adult-film performers and their aliases via a specialist database/forum.
selectorsIn:
- name
- image
- physical-description
selectorsOut:
- name
- associate
status: live
pricing: free
costNote: Free to read; the forum has restricted posting (moderated/closed to new members), so treat it as read-only reference.
opsec: passive
opsecNote: Reading the database/forum is passive and does not notify anyone. It is an adult-industry site — access it from an isolated sock-puppet browser, expect adult content, and handle any identification with care given the sensitivity and potential exploitation context. Do not register or post from an attributable identity.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running niche community database (European Girls Adult Film Database) with dedicated identification threads; contributor-sourced, so entries are enthusiast-curated rather than authoritative.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- European Girls Adult Film Database
- EGAFD
tags:
- professionlicensing
- Profession & Licensing Sites
- adult-industry
- identification
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# egafd.com

> The European Girls Adult Film Database and its identification forum — a specialist reference for putting a real/stage name to a continental-European female adult performer.

## When to use
You have a `name`, stage name, `image`, or `physical-description` of a woman appearing in European adult content and need to identify her, resolve her aliases, or cross-reference filmography. This is a narrow but sometimes decisive resource: in exploitation, trafficking, or missing-persons cases where a subject appears in adult media, EGAFD's contributor-driven identification threads can link a stage name to other aliases and to associated people/studios that mainstream tools won't surface.

## How to use it (`bestInteractionPattern`: web-manual)
1. From an isolated sock-puppet browser, open https://www.egafd.com/ and its forum (`/fora/`); the linked section (`viewforum.php?f=4`) is one of the identification/discussion fora.
2. Search or browse by performer name/alias, nationality, or thread; the forum organises "who is this" identification requests and performer discussions.
3. Read matching threads and any linked database entry for confirmed `name`, alternate stage names, nationality, and film/studio associations.
4. Because posting is restricted, use it read-only — do not register to ask; instead corroborate a candidate ID elsewhere.
5. Pivot: a confirmed real name feeds `[[familytree]]` / court records; a face feeds reverse-image and face-search tools.

## Inputs → Outputs
- **In:** `name`/stage name, `image`, `physical-description`
- **Out:** confirmed/candidate `name` + aliases, `associate` links (studios, co-performers, other stage names)
- **Empty/negative result looks like:** no thread or database entry matches — the performer isn't European-focused, isn't catalogued here, or the description is too generic. Absence proves nothing about identity.

## Gotchas & OpSec
- Human-in-the-loop: **manual-review** — identification is analyst-driven, matching photos/descriptions to entries; there is no automated lookup.
- OpSec: passive to read, but this is adult/NSFW and ethically sensitive. Use an isolated browser, never an attributable account, and handle findings with victim-sensitive care.
- Contributor-sourced: entries and IDs can be wrong or contested. Corroborate any real-name attribution before acting.

## Overlaps ("do both")
- Pairs with `[[familytree]]` and reverse-image/face tools — EGAFD resolves the stage-name/alias layer; those confirm the real identity and location.

## Trust & verifiability
`trust: unverified` — a real, active specialist database, but enthusiast-curated and unofficial. Treat every identification as a lead requiring independent confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | egafd-com |
| category | public-records |
| selectorsIn → selectorsOut | name, image, physical-description → name, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
