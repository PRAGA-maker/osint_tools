---
id: open-secrets
name: OpenSecrets
description: Use when you have a `name` and want US political-money and financial-disclosure records — returns campaign contributions, lobbying ties, and (for officials) personal-finance disclosures with `employer-org` and `address` clues.
url: https://www.opensecrets.org/
category: search-engines
path:
- search-engines
bestFor: Tracing a US person's political donations, lobbying links, and financial disclosures.
selectorsIn:
- name
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free public database run by the non-profit OpenSecrets (formerly Center for Responsive Politics). Bulk data/API access may require a free key, but web lookups are open.
opsec: passive
opsecNote: You browse a public transparency database; the subject is not contacted. Fully passive. Use a VPN for hygiene if you don't want the research tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Non-partisan non-profit compiling data from official FEC, Senate, and disclosure filings; widely cited by journalists and researchers, with sourcing to primary records.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- political-moneyline
aliases:
- Open Secrets
- Center for Responsive Politics
- opensecrets.org
tags:
- toddington
- curated-directory
- specialty-search
- campaign-finance
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# OpenSecrets

> The non-partisan money-in-politics database — campaign contributions, lobbying, and officials' personal-finance disclosures, aggregated from official filings and searchable by name.

## When to use
You have a US subject's `name` and want to exploit political-money transparency data. Individual **donor** records list the contributor's name, city/state (`address` clue), employer, and occupation (`employer-org`) with each donation — a rich, name-searchable source that often confirms location and employment. For public officials and candidates, personal financial disclosures reveal assets, income sources, and business ties (`associate` links). Strong when a subject has any donor or official footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.opensecrets.org/.
2. Use **Donor Lookup** to search the `name`; results show each contribution with the donor's city/state, employer, and occupation.
3. For officials/candidates, open their profile and the **Personal Finances** section for disclosed assets, income, and affiliations.
4. Explore lobbying and organization pages to map who's connected to whom.
5. Pivot: employer/occupation → company records and professional-network tools; city/state → people-search to resolve a full `address`; disclosed business ties → `associate` mapping.

## Inputs → Outputs
- **In:** `name` (US subject)
- **Out:** donation records (with `employer-org`, occupation, city/state `address` clue), lobbying links, official financial disclosures (`associate`)
- **Empty/negative result looks like:** no donor records / no official profile — the person hasn't made itemized federal contributions and isn't a covered official. This is common; absence isn't meaningful. Small/unitemized donations may not appear.

## Gotchas & OpSec
- US-focused and **federal-leaning**; state/local money is patchier (some states have separate databases).
- Donor employer/occupation fields are self-reported on the filing and can be blank or stale.
- Common names collide; use the reported city/state and employer to disambiguate before attributing.
- OpSec: **passive** — public data, no target contact.

## Overlaps ("do both")
- Pairs with [[political-moneyline]] and the FEC's own site — overlapping but differently-organized campaign-finance data; cross-check to catch records one presentation misses.

## Trust & verifiability
`trust: trusted` — a long-established non-partisan non-profit sourcing from official FEC/Senate/disclosure filings; figures are dependable and traceable to primary records, though presentation is aggregated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-secrets |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
