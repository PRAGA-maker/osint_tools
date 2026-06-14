---
id: pastebin-com
name: pastebin.com
description: Use when you have an email, username, or name and want to search public pastes for leaked dumps, contact data, or mentions — returns leaked credentials, linked accounts, and associates.
url: https://pastebin.com/
category: email
path:
- email
bestFor: Finding leaked dumps and mentions of an identifier in public text pastes.
selectorsIn:
- email
- username
- name
- domain
selectorsOut:
- email
- username
- social-profile
- phone
- associate
status: live
costNote: "Free to read public pastes. On-site search is limited; a Google site:pastebin.com search is more effective. Pastebin Pro and the scraping API are paid."
pricing: freemium
opsec: passive
opsecNote: Reading public pastes (especially via search engines) is passive and reveals nothing to the subject. Do not paste sensitive data yourself.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Pastebin is the canonical public paste host; long used by OSINT investigators to find leaked credential dumps and doxes. The site is real; individual pastes are unverified user content.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Pastebin
tags:
- email
- Email Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# pastebin.com

> The web's main public paste host — a frequent dumping ground for leaked credentials, contact lists, and doxes searchable by email, username, or name.

## When to use
You have an `email`, `username`, `name`, or `domain` and want to check whether it appears in a public dump or paste — leaked passwords, combo lists, contact sheets, or a dox that exposes linked accounts and associates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Best path: search engines — `site:pastebin.com "target@email.com"` (and variants) finds more than on-site search.
2. Optionally use Pastebin's own search box, but its index is partial.
3. Open matching pastes; extract leaked emails, usernames, phones, and named associates.
4. Pivot found `username`/`email` to `[[osint-rocks]]` and breach checks (`[[osintcat]]`).

## Inputs → Outputs
- **In:** `email`, `username`, `name`, `domain`
- **Out:** `email`, `username`, `social-profile`, `phone`, `associate`
- **Empty/negative result looks like:** no indexed pastes — note that pastes are often removed, so absence isn't proof of nothing ever existing.

## Gotchas & OpSec
- Many sensitive pastes are deleted/unlisted; coverage is incomplete. Combine with paste-aggregators and cached copies.
- Paste content is unverified user data — corroborate before acting.
- OpSec: passive when reading via search engines; never paste investigative data to the site.

## Overlaps ("do both")
- Pairs with `[[osintcat]]` / `[[osint-lolarchiver-com-2]]` (structured breach DBs) — pastes catch dumps those may miss, and vice versa.

## Trust & verifiability
`trust: trusted` — the platform is canonical and widely used in OSINT; treat each paste as unverified user content to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pastebin-com |
| category | email |
| selectorsIn → selectorsOut | email, username, name, domain → email, username, social-profile, phone, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
