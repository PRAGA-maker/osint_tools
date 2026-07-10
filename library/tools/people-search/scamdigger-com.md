---
id: scamdigger-com
name: ScamDigger
description: Use when you have a `name`, `email`, `phone`, or `ip-address` from a suspected romance/dating scammer and want matching documented scam profiles — returns name, email, phone, image, and address leads.
url: http://scamdigger.com/
category: people-search
path:
- people-search
bestFor: Checking a suspected scammer's selectors against a large documented romance-scam profile database.
selectorsIn:
- email
- name
- phone
- ip-address
selectorsOut:
- name
- email
- phone
- address
- image
status: live
pricing: freemium
costNote: Free to search and browse documented scam profiles; community/forum-driven.
opsec: passive
opsecNote: Searches a public crowd-sourced database; no notification reaches anyone. Note the "scammer" photos are usually stolen images of innocent people — an image match tells you a photo is used in scams, not that the depicted person is the scammer.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Crowd-sourced anti-scam archive; entries are user-submitted and much of the core data dates to ~2017, so treat as leads, not verified fact.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- scamsearch-io
- tineye
aliases:
- scamdigger.com
tags:
- Universal Contact Search and Leaks Search
- romance-scam
- catfish
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# ScamDigger

> A crowd-sourced archive of romance/dating-scam profiles, searchable by name, email, phone, or IP — useful for spotting when a person or photo is a known catfish/scam identity.

## When to use
You have a `name`, `email`, `phone`, or `ip-address` tied to an online contact that may be fake (a dating profile, a "relative" reaching a family, a fraudulent intermediary) and want to check it against documented scam identities. In missing-persons contexts this helps flag when someone communicating with the family is a scammer exploiting the case, or when a subject's online romance was a fabricated identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://scamdigger.com/ and search by name, email, phone, or IP.
2. Read matching profiles: aliases, emails, phones, IP addresses, stolen photos, and claimed locations.
3. Critically: the photos are almost always **stolen from innocent people** — a match means "this image is used in scams," which is itself a lead (reverse-image the photo to find the real person whose pictures were taken).
4. Pivot: a reused email/phone feeds contact-OSINT; a scammer photo feeds `[[tineye]]` reverse image search to find the genuine owner.

## Inputs → Outputs
- **In:** `email`, `name`, `phone`, or `ip-address`
- **Out:** `name` (aliases), `email`, `phone`, `address` (claimed), `image` (stolen photos used)
- **Empty/negative result looks like:** no match — the identity isn't in this archive (which skews older and to certain scam types). Absence does not clear the contact; cross-check a live scam database.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; public archive, no alerts.
- Misattribution risk: the depicted people in scam photos are victims, not scammers — never treat an image match as identifying the fraudster.

## Overlaps ("do both")
- Pairs with `[[scamsearch-io]]` — a larger, more current scam database; run it since ScamDigger's data skews to ~2017.
- Pairs with `[[tineye]]` — reverse-image the scam photos to find the real person whose images were stolen.

## Trust & verifiability
`trust: unverified` — crowd-sourced, aging entries; valuable for pattern-matching known scams but every hit is a lead to corroborate, and photos must not be read as identifying the scammer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scamdigger-com |
| category | people-search |
| selectorsIn → selectorsOut | email, name, phone, ip-address → name, email, phone, address, image |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
