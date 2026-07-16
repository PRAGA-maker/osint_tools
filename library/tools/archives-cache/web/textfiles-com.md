---
id: textfiles-com
name: Textfiles.com
description: Use when a `name`, `username` or `email` may appear in 1980s–90s BBS/hacker text-file culture — returns document-id and username leads from legacy archives.
url: https://textfiles.com/
category: archives-cache
path:
- archives-cache
- web
bestFor: Searching legacy BBS, zine, and hacker-scene text archives for old handles, real names, and contact info.
selectorsIn:
- username
- name
- email
selectorsOut:
- document-id
- username
- email
status: live
pricing: free
costNote: Free to browse and read; no account. A read-only historical archive maintained by Jason Scott.
opsec: passive
opsecNote: Read-only browsing of a static public archive; nothing is submitted to any subject and there is no interaction. Standard web-access logging only; a VPN is optional.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, well-known archive curated by Jason Scott (also of the Internet Archive); the files are faithfully preserved historical artefacts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- textfiles.com
- Textfiles
tags:
- archive
- historical
- bbs
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# Textfiles.com

> A preserved archive of 1980s–90s BBS, zine, and underground-scene text files — a place to find old handles, real names, and contact details from the pre-web era.

## When to use
A niche but occasionally decisive resource: when your subject has deep roots in early computer/hacker/BBS culture, their old `username`/handle, real `name`, or period `email`/address may survive in a text file here (member lists, zine credits, philes, message dumps). Because these documents predate modern privacy norms, they sometimes tie a modern handle to a long-standing pseudonym or an early real-name attribution.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://textfiles.com/ and browse by topic directory, or
2. Use a `site:textfiles.com <handle or name>` query in a search engine (the site has no strong built-in full-text search).
3. Read matching files for handles, credits, greetz lists, and contact blocks that name or link identities.
4. Pivot: an old handle → username enumeration across platforms; a real name found beside a handle → attribution lead; note the file as a `document-id` source for provenance.

## Inputs → Outputs
- **In:** `username`/handle, `name`, or period `email`
- **Out:** archived text files (`document-id`) containing handles (`username`), names, and old `email`/contact details.
- **Empty/negative result looks like:** no file mentions the term — expected for the vast majority of modern subjects; this only helps for people with genuine early-scene history.

## Gotchas & OpSec
- Very low hit rate for ordinary/modern subjects — only worth it when there's a real BBS/hacker-scene angle.
- No robust on-site search; drive it with an external `site:` search engine query.
- Content is decades old; a name/handle match is a historical lead to corroborate, not current fact.

## Overlaps ("do both")
- Pairs with username-enumeration and general archive tools — Textfiles covers the pre-web underground specifically, which mainstream archives index poorly.

## Trust & verifiability
`trust: trusted` — a faithfully preserved, well-known historical archive; the documents are authentic artefacts, though what they *claim* about a person is unverified period content.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | textfiles-com |
| category | archives-cache |
| selectorsIn → selectorsOut | username, name, email → document-id, username, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
