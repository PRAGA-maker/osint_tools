---
id: leakradar
name: LeakRadar
description: Use when you have an email, username, or domain and want to check it against infostealer logs and recent leaks — returns exposure confirmation and linked identifiers.
url: https://leakradar.io/
category: email
path:
- email
bestFor: Monitoring/checking an email, username, or domain against stealer logs and fresh leak feeds.
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
costNote: Free existence/preview check; full credential/host records and monitoring features require a paid plan.
opsec: passive
opsecNote: Server-side query against LeakRadar's leak/stealer-log index; subject not notified. Use a research-only account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: LeakRadar (leakradar.io) is a commercial leak/infostealer-log monitoring service referenced in awesome-osint. Useful for fresh stealer-log coverage; full records paywalled and provenance is stolen data.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases: []
tags:
- email-search-email-check
- infostealer-logs
- data-breach-search-engines
source: awesome-osint
lastVerified: ''
enrichment: full
---

# LeakRadar

> Leak and infostealer-log monitoring service — checks an email, username, or domain against recent stealer logs and leak feeds.

## When to use
You have a subject's `email`, `username`, or `domain` and want coverage of fresh stealer-malware logs and recent leaks that classic breach engines may not yet index. In missing-persons work a stealer-log hit can reveal other accounts the person used on the same device and indicate recent activity. Reach for it to complement database-breach checkers with infostealer-log coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://leakradar.io/ (account for full features).
2. Enter the `email`, `username`, or `domain`.
3. Read the result: which leaks/stealer logs the subject appears in; full record contents (credentials, host data) and monitoring are paid.
4. Pivot: take newly surfaced emails/usernames into [[leakcheck]], [[infostealers-info]], or [[intelligence-x-2]].

## Inputs → Outputs
- **In:** `email`, `username`, `domain`
- **Out:** existence flag, associated `email`/`username`/`domain`, leak/log `metadata` (source, date)
- **Empty/negative result looks like:** no matches — subject absent from their feeds, not proof of no compromise.

## Gotchas & OpSec
- Human-in-the-loop: meaningful detail is paywalled; free use confirms existence.
- OpSec: passive; leaks nothing to the subject. Stealer-log data is sensitive — handle lawfully and use a sock-puppet account.

## Overlaps ("do both")
- Pairs with [[infostealers-info]] (both index stealer logs but ingest different feeds) and [[leakcheck]] (classic database breaches).

## Trust & verifiability
`trust: community` — commercial leak/stealer-log service cited in public OSINT lists; provenance is stolen data and individual records are unverified. Corroborate any actionable lead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leakradar |
| category | email |
| selectorsIn → selectorsOut | email, username, domain → email, username, domain, metadata |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
