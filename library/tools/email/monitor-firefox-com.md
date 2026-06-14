---
id: monitor-firefox-com
name: monitor.firefox.com
description: Use when you have an email address and want to learn which known data breaches it appears in (and what data classes leaked) — returns the breach list for that address.
url: https://monitor.firefox.com/
category: email
path:
- email
bestFor: Checking which public data breaches an email address appears in.
selectorsIn:
- email
selectorsOut:
- metadata-exif
status: degraded
pricing: freemium
costNote: Free breach check; Mozilla Monitor Plus (paid) adds broker-removal scanning. Note the old firefox.com URL now redirects to monitor.mozilla.org.
opsec: passive
opsecNote: Fully passive against the target — you query Mozilla's breach index, not the person. To see full results you submit the email and verify ownership via a code, so use it on addresses you can receive at (your own) or rely on the summary count.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Mozilla Monitor (formerly Firefox Monitor) is an official Mozilla service backed by Have I Been Pwned breach data. Reputable and well documented.
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Firefox Monitor
- Mozilla Monitor
tags:
- hackedaccounts
- Hacked / Breached Account Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# monitor.firefox.com

> Mozilla's breach-exposure checker (formerly Firefox Monitor, now Mozilla Monitor) — tells you which known breaches an email address appears in.

## When to use
You have a confirmed `email` for a missing person or associate and want to know where it was exposed. The breach names reveal which services the person used (e.g. a fitness app, a dating site, a forum), each of which is a pivot toward accounts, usernames, and timeframes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to monitor.firefox.com (redirects to monitor.mozilla.org) and enter the `email`.
2. You get a summary count immediately; to see the full breach list for an address you must verify you control it (email a code) or sign in.
3. Read each breach entry: service name, breach date, and leaked data classes (passwords, phones, DOB, etc.).
4. Pivot: each breached service is a candidate account to search; data classes hint at what other selectors may exist.

## Inputs → Outputs
- **In:** `email`
- **Out:** breach metadata — service names, dates, and leaked data classes (`metadata-exif`-style exposure record)
- **Empty/negative result looks like:** "no breaches found" — means not in the indexed corpus, NOT that the address is clean or unused.

## Gotchas & OpSec
- Full per-breach detail is gated behind ownership verification of the address; for a third party's email you may only get the count or must use HIBP directly.
- Mozelle Monitor reflects only breaches in its (HIBP-derived) index; newer or unindexed leaks won't show.
- Breach presence proves the address existed/was used at some point, not who currently controls it.

## Trust & verifiability
`trust: trusted` — official Mozilla service using Have I Been Pwned data; reputable and transparent about sources. Marked `degraded` only because the legacy firefox.com URL now redirects and full results require verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | monitor-firefox-com |
| category | email |
| selectorsIn → selectorsOut | email → metadata-exif (breach records) |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
