---
id: trademarkia
name: Trademarkia
description: Use when you have a `name`, brand, or `employer-org` and want trademark filings — returns marks with owner/applicant name, address, attorney, and filing dates across US/EU/UK/CA.
url: https://www.trademarkia.com/
category: search-engines
path:
- search-engines
bestFor: Free trademark search by mark or by owner name to tie a person/company to brands, with the owner's name, address, and filing history.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- address
- employer-org
status: live
pricing: freemium
costNote: Trademark search (12M+ marks) is free; the paid side is Trademarkia's registration/legal filing services, not the search.
opsec: passive
opsecNote: Passive — you search a public trademark database; no subject is notified. Owner names and addresses in filings are public record; standard clean-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Search is drawn from official trademark-office records (USPTO and equivalents); the underlying filings are authoritative public records, though Trademarkia itself is a commercial law-firm platform.
missingPersonsRelevance: medium
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- european-trademark-search
- international-trademark-search
aliases:
- trademarkia.com
tags:
- toddington
- curated-directory
- trademark
- business
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Trademarkia

> A free, friendly front end to official trademark records — search a brand or, more usefully for OSINT, an owner's name to surface the marks they've filed, complete with name, address, and attorney.

## When to use
You have a `name`, a brand, or an `employer-org` and want to connect a person or company to registered trademarks. The **owner search** is the OSINT angle: trademark filings are public records that list the applicant's real name and address (and often their attorney), so they can confirm that a subject owns a business/brand, reveal a home or business address, and surface filing dates that anchor a timeline. Covers US (4M+), plus Canada, EU, and UK.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.trademarkia.com/ and use the free search.
2. Search by **mark name** to find who owns a brand, or by **owner/applicant name** to list all marks a person/company has filed.
3. Open a record for the owner's name and address, filing/registration dates, status, goods/services class, and representing attorney.
4. Ignore the upsell to paid registration services — the search and record view are free.
5. Pivot: an owner `address` feeds property/people search; the `employer-org`/brand feeds corporate-registry lookups; the attorney or filing date adds corroboration/timeline.

## Inputs → Outputs
- **In:** a `name`, brand, or `employer-org`
- **Out:** trademark records — owner `name` and `address`, associated `employer-org`, filing dates, status, and attorney
- **Empty/negative result looks like:** no marks for a name/brand means nothing is registered under it in the covered offices — many individuals/businesses hold no trademarks, so absence says little about the person.

## Gotchas & OpSec
- **Verify at the source:** for a decisive claim, confirm the filing on the official office (USPTO TESS/equivalent) — Trademarkia is a convenient mirror, not the authority.
- Owner addresses in filings can be a business, agent, or old address — corroborate before treating as a residence.
- The site heavily promotes paid filing services; keep to the free search.

## Overlaps ("do both")
- Pairs with `[[european-trademark-search]]` / `[[international-trademark-search]]` and corporate registries — Trademarkia is the quick name→marks lookup; the official offices confirm it, and registries add the company-ownership layer.

## Trust & verifiability
`trust: trusted` — its search reflects official trademark-office filings, which are authoritative public records; the platform is commercial, so confirm critical entries at the government source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trademarkia |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → name, address, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
