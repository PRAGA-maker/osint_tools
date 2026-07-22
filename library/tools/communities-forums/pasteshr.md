---
id: pasteshr
name: PasteShr
description: Use when you have a `name`, `email`, or `username` and want to find leaked/dumped text (credentials, dox, lists) posted to this pastebin — returns `email`, `phone`, `password`.
url: https://www.pasteshr.com/
category: communities-forums
path:
- communities-forums
bestFor: Surfacing dumped text (leaks, dox, combolists) hosted on PasteShr that mentions a selector, via external search.
selectorsIn:
- name
- email
- username
selectorsOut:
- email
- phone
- password
status: live
pricing: free
costNote: Free paste-hosting site; reading pastes needs no account.
opsec: passive
opsecNote: Reading a paste is passive. Do not create an account or post; treat any credentials you find as evidence to report, never to test or reuse.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An anonymous public paste host with no editorial control — content is user-submitted, unverified, and frequently removed or expired.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- pastebin-com
- pastebin-osint-harvester
aliases:
- pasteshr.com
tags:
- pastebins
- leaks
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# PasteShr

> A public pastebin-style text host — worth checking as one more place a leak, combolist, or dox mentioning your subject may have been dropped.

## When to use
You are sweeping paste sites for a selector — a `name`, `email`, `username`, or a breach-related term — and want to include PasteShr in the pass. Pastebins are where credential dumps, doxes, and leaked lists get posted, so a hit can expose an `email`, `phone`, `password`, or associated accounts tied to the subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. PasteShr has no reliable on-site search, so query it externally: `site:pasteshr.com "<selector>"` in your search engine of choice.
2. Open any matching paste directly (URLs look like `pasteshr.com/<id>`).
3. Read the dumped text for identifiers tied to your subject (emails, phones, usernames, hashed/plaintext passwords, associated accounts).
4. Pivot: an exposed `email`/`username` feeds account-existence and breach tools; never reuse or test any credential — record it and move on.

## Inputs → Outputs
- **In:** `name` / `email` / `username` (searched via an external engine)
- **Out:** `email`, `phone`, `password`, and associated account references found inside pastes
- **Empty/negative result looks like:** no indexed pastes for the term — many pastes are unlisted, short-lived, or removed, so absence is not proof nothing was ever posted.

## Gotchas & OpSec
- Pastes are ephemeral and often deleted — capture (screenshot/hash) anything relevant immediately.
- Content is unverified and may be fabricated or recycled from old breaches; corroborate before relying on it.
- Handle exposed credentials as evidence only; testing or reusing them is unlawful and burns your OpSec.

## Overlaps ("do both")
- Pairs with `[[pastebin-com]]` and `[[pastebin-osint-harvester]]` — run the same selector across multiple paste hosts, since a dump on one is often not mirrored on the others.

## Trust & verifiability
`trust: community` — an anonymous, uncurated paste host; treat every paste as an unverified claim and confirm identifiers independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pasteshr |
| category | communities-forums |
| selectorsIn → selectorsOut | name, email, username → email, phone, password |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
