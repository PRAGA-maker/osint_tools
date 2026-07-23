---
id: aa419-fake-sites-database
name: aa419 Fake Sites Database
description: Use when you have a `domain` or an impersonated brand `name` and want to know if it is a catalogued scam/fake site — returns matching fraudulent domains.
url: https://db.aa419.org/fakebankslist.php
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking whether a website is a known advance-fee / fake-bank / scam site in the Artists Against 419 database.
selectorsIn:
- domain
- name
selectorsOut:
- domain
status: live
pricing: free
costNote: Free to search (176,000+ catalogued scam sites). Redistribution of the data is restricted, but interactive lookups are open with no account.
opsec: passive
opsecNote: You query Artists Against 419's own archive, not the scam site, so nothing touches the fraudulent host. Only aa419 sees your search. As with any scam DB, don't then browse the listed live scam URLs from a real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running volunteer anti-fraud project (Artists Against 419); entries are human-curated and generally reliable, though status (active/dead) can lag and coverage skews to advance-fee / fake-financial scams.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Artists Against 419
- aa419 fakebankslist
tags:
- domain-and-ip-research
- scam
- fraud-db
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# aa419 Fake Sites Database

> The Artists Against 419 database — a searchable catalogue of 176,000+ fraudulent websites (fake banks, advance-fee scams, bogus escrow/finance) with the impersonated entity and status of each.

## When to use
You have a `domain` or a suspicious brand `name` and want to know whether it's a *documented* scam — a fake bank, phony investment/escrow site, or advance-fee (419) front. A hit gives you the impersonated entity, when it was catalogued, and its status, which is strong corroboration when assessing a site tied to a fraud or a missing-person-adjacent romance/finance scam.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://db.aa419.org/fakebankslist.php .
2. Use basic search (exact phrase / all words / any word) or advanced search; enter the `domain` or the impersonated brand `name`.
3. Read each result: fraudulent URL, the entity it impersonates, active/inactive status, date added, last updated, and category.
4. Note the "status" but verify freshness — a site marked active may already be down and vice versa.
5. Pivot: a confirmed scam `domain` feeds WHOIS/hosting lookups and clustering to find the operator's other sites; the impersonated brand narrows the scam type.

## Inputs → Outputs
- **In:** `domain`, or impersonated brand/`name`
- **Out:** matching fraudulent `domain`(s) with impersonated entity, status, and dates
- **Empty/negative result looks like:** no match — the site isn't in aa419's catalogue, NOT proof it's legitimate. Their focus is financial/419 fraud; other scam types may be absent.

## Gotchas & OpSec
- Coverage is skewed toward fake-bank / advance-fee / fake-finance scams; general phishing or e-commerce fraud may not appear.
- Status fields can lag reality; treat active/dead as indicative.
- OpSec: **passive** — you search aa419's archive; don't visit the listed live scam URLs from a real identity.

## Overlaps ("do both")
- Complements phishing feeds like `[[https-openphish-com-feed-txt]]` and general scam-site checkers — aa419 is the specialist for financial-impersonation fraud; combine for broader scam coverage.

## Trust & verifiability
`trust: community` — a respected, human-curated volunteer anti-fraud effort. A listing is high-confidence evidence a site was flagged as fraudulent; corroborate current status independently before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aa419-fake-sites-database |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, name → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
