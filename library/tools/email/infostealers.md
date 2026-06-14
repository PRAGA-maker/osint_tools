---
id: infostealers
name: InfoStealers
description: Use when you have an email or username and want to know if it appears in infostealer malware logs — returns exposure confirmation and (paid) credential/host context.
url: https://infostealers.info/en/info
category: email
path:
- email
bestFor: Checking whether an email/username surfaces in stealer-malware (RedLine, Raccoon, etc.) log datasets.
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
costNote: Free existence/preview check; full log records (passwords, cookies, host fingerprints) sit behind paid access.
opsec: passive
opsecNote: Server-side query against a third-party breach/stealer index; nothing is sent to the subject. Use a research-only account/email, not a personal one.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial infostealer-log aggregator referenced in OSINT lists (awesome-osint). Data provenance is stolen credential logs; treat hits as leads, not proof. Legality of accessing full records varies by jurisdiction.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- infostealers.info
tags:
- email-search-email-check
- infostealer-logs
source: awesome-osint
lastVerified: ''
enrichment: full
---

# InfoStealers

> Infostealer-malware log lookup: tells you whether a given email/username/domain shows up in stolen credential logs harvested by stealer malware.

## When to use
You have a subject's `email`, `username`, or a `domain` they use, and you want to know whether their device or accounts were compromised by infostealer malware. A hit can surface other accounts, services, and a rough indication the person was active on a particular machine — useful for confirming a digital footprint or finding fresh leads in a missing-persons workup. This is the `/info` landing/about endpoint; the actual query box is on the `/search` page ([[infostealers-info]]).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://infostealers.info/en/info to read scope/coverage, then go to the search page.
2. Enter the subject `email`, `username`, or `domain`.
3. Read the result: a positive hit names datasets/log batches; full record contents (plaintext passwords, browser cookies, machine fingerprint) require a paid tier.
4. Pivot: feed any newly exposed usernames/emails into [[leakcheck]] or [[intelligence-x-2]], and cross-check breach overlap.

## Inputs → Outputs
- **In:** `email`, `username`, `domain`
- **Out:** existence flag, associated `email`/`username`/`domain`, log `metadata` (dataset, approximate date) on paid tiers
- **Empty/negative result looks like:** "no results" / zero matches — means no stealer log in their index, NOT that the person is clean.

## Gotchas & OpSec
- Human-in-the-loop: the meaningful detail (credentials, host data) is paywalled; free use only confirms existence.
- OpSec: passive lookup, leaks nothing to the subject; still use a sock-puppet account. Stolen-log data is sensitive — handle and store findings carefully and lawfully.

## Overlaps ("do both")
- Pairs with [[leakradar]] and [[leakcheck]] because infostealer-log coverage differs from classic database-breach coverage; a person can appear in one and not the other.

## Trust & verifiability
`trust: community` — commercial aggregator of stolen stealer logs cited in public OSINT lists; reliability of individual records is unverified and provenance is criminal data dumps. Confirm any actionable lead through an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infostealers |
| category | email |
| selectorsIn → selectorsOut | email, username, domain → email, username, domain, metadata |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
