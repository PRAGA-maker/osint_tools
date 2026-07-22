---
id: copyright-search
name: Copyright Search
description: Use when you have a `domain`, `name` or `employer-org` and want to see copyright/DMCA complaints tied to it — returns complainant/sender details and targeted URLs.
url: https://www.lumendatabase.org/topics/22
category: search-engines
path:
- search-engines
bestFor: Finding DMCA/copyright takedown notices naming a site, person, or company as sender or target.
selectorsIn:
- domain
- name
- employer-org
selectorsOut:
- employer-org
- domain
- name
status: live
pricing: free
costNote: Free, publicly searchable research database (Lumen, hosted at Harvard's Berkman Klein Center). No account needed to search; some personal details in notices are redacted.
opsec: passive
opsecNote: You search a third-party research archive, not the sender or target — nobody is notified. Standard passive browsing; a VPN keeps the query itself private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Lumen is a well-established academic transparency project (Harvard Berkman Klein Center) archiving takedown notices submitted by Google and others; entries are real notices, not user claims.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- lumen
aliases:
- Lumen copyright complaints
- DMCA notice search
tags:
- toddington
- curated-directory
- specialty-search
- dmca
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Copyright Search

> Lumen's copyright/DMCA topic view — a searchable archive of takedown notices that can tie a person or company to the sites they run, host, or tried to erase.

## When to use
You have a `domain`, `name`, or `employer-org` and want to know whether it appears in copyright/DMCA takedown notices — as the sender (who complained), the target (whose URLs were removed), or the principal behind either. Notices reveal relationships that are otherwise hidden: which URLs a rights-holder claims, which sites a person operates, and who is fighting to remove content — useful for mapping infrastructure and attribution.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Lumen copyright topic at https://www.lumendatabase.org/topics/22 (or search the whole database at lumendatabase.org).
2. Search by `domain`, sender/target `name`, or `employer-org`/brand.
3. Read matching notices: sender (complainant), the principal/rights-holder, the targeted URLs, and dates.
4. Pivot: the list of targeted URLs often enumerates a subject's sites/accounts; the sender details tie a brand or law firm to a person or company.

## Inputs → Outputs
- **In:** `domain`, `name`, or `employer-org`
- **Out:** notice sender/principal (`name`/`employer-org`), targeted `domain`s/URLs, dates
- **Empty/negative result looks like:** no matching notices — the entity simply isn't in the archive (most content is never subject to a filed notice), so absence proves nothing.

## Gotchas & OpSec
- Lumen archives notices **submitted to it** (heavily Google-sourced) — it is broad but not exhaustive; a null result is common.
- Personal data in notices is partly redacted, and the *claims* in a notice are the sender's assertions, not adjudicated facts.
- OpSec: fully passive — searching discloses nothing to sender or target.

## Overlaps ("do both")
- Pair with `[[lumen]]` for the full multi-topic database and with WHOIS/reverse-IP — takedown notices name the sites and parties, while infrastructure lookups confirm who actually owns them.

## Trust & verifiability
`trust: trusted` — an authoritative academic archive of real notices; the entries are genuine, with the caveat that a notice's allegations are unproven and coverage is not complete.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | copyright-search |
| category | search-engines |
| selectorsIn → selectorsOut | domain, name, employer-org → employer-org, domain, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
