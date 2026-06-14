---
id: infostealers-info
name: infostealers.info
description: Use when you have an email/username/domain and want to search infostealer malware logs for that subject — returns exposure confirmation and associated identifiers.
url: https://infostealers.info/en/search
category: email
path:
- email
bestFor: Searching stolen infostealer logs by email, username, or domain.
selectorsIn:
- email
- username
- domain
selectorsOut:
- email
- username
- domain
- metadata
status: live
pricing: freemium
costNote: Free search returns existence/preview; full credential and host records require a paid plan.
opsec: passive
opsecNote: Query runs server-side against a third-party stealer-log index; subject is not notified. Use a research-only account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Listed on uk-osint.net under Hacked/Breached Account Sites. Commercial stealer-log search; record provenance is stolen data, individual results unverified. Treat hits as leads.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- InfoStealers
tags:
- hackedaccounts
- Hacked / Breached Account Sites
- infostealer-logs
source: uk-osint
lastVerified: ''
enrichment: full
---

# infostealers.info

> The search endpoint of InfoStealers — query stolen infostealer-malware logs by email, username, or domain.

## When to use
You hold a subject's `email`, `username`, or a `domain` and want to check whether their machine/accounts were captured by infostealer malware (RedLine, Raccoon, Vidar, etc.). A hit can reveal additional accounts the person used on the same device and confirm activity around a date — valuable for reconstructing a missing person's digital footprint. This is the live query box for [[infostealers]].

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://infostealers.info/en/search.
2. Enter the `email`, `username`, or `domain`.
3. Run the search; a positive result confirms presence and may preview dataset/source. Full log contents (passwords, cookies, host fingerprint) are paid.
4. Pivot: take any newly surfaced emails/usernames into [[leakcheck]], [[intelligence-x-2]], or social-profile lookups.

## Inputs → Outputs
- **In:** `email`, `username`, `domain`
- **Out:** existence flag plus associated `email`/`username`/`domain` and log `metadata` (dataset, date) on paid tiers
- **Empty/negative result looks like:** zero matches — no stealer log indexed, not a guarantee of no compromise.

## Gotchas & OpSec
- Human-in-the-loop: usable detail is paywalled; free tier mainly confirms existence.
- OpSec: passive, leaks nothing to the subject; still use a sock puppet. Stolen-log records are sensitive and jurisdiction-dependent — handle lawfully.

## Overlaps ("do both")
- Pairs with [[leakradar]] because both index stealer logs but ingest different feeds; a subject may appear in only one.

## Trust & verifiability
`trust: unverified` — commercial stealer-log aggregator listed by a third-party OSINT directory; provenance is criminal data dumps and individual records are not independently confirmed. Corroborate before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infostealers-info |
| category | email |
| selectorsIn → selectorsOut | email, username, domain → email, username, domain, metadata |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
