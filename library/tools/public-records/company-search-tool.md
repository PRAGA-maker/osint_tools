---
id: company-search-tool
name: Company search tool
description: Use when you have a company name or an `employer-org`/`associate` link and want to investigate the company and its directors/owners across many registries — returns a form that fans your query out to 10+ corporate databases.
url: https://www.aware-online.com/en/osint-tools/company-search-tool/
category: public-records
path:
- public-records
bestFor: Kicking off a company/UBO investigation by launching the same query into multiple corporate registries and leak databases at once.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Free browser-based helper from Aware Online; no account. It only builds and forwards queries — the destination registries may have their own paywalls (most linked ones are free).
opsec: passive
opsecNote: The tool just constructs links to public registries; the searches you launch hit those registries directly. Use a sock-puppet browser for the onward searches. Passive — the company/directors aren't notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Aware Online, an established OSINT training company; it's a transparent query-builder that forwards to well-known public registries, so the data comes from those authoritative sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Aware Online company search tool
tags:
- company-osint
- corporate-registry
- kyc
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Company search tool

> Aware Online's query-builder that launches one company query into 10+ corporate registries and leak databases at once.

## When to use
You have a company name (an `employer-org`) or a person linked to a business — an employer, a director, a suspected front company connecting to your subject — and you want to investigate the entity and the people behind it (directors, ultimate beneficial owners). This tool saves you re-typing the same query into every registry: it fans it out to Dutch KVK, OpenCorporates, ICIJ Offshore Leaks, gov.uk, Google, Indeed, and more.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.aware-online.com/en/osint-tools/company-search-tool/.
2. Fill in the company/search fields in the form.
3. Click through the generated buttons — each opens that query pre-loaded in a third-party registry/database (OpenCorporates, Offshore Leaks, national chambers of commerce, etc.).
4. Work each result: pull directors/officers, registered `address`es, and beneficial owners; note names as new `associate` leads.
5. Pivot: a director's name feeds people-search; a registered address feeds address/records tools; an offshore hit feeds `[[icij-offshore-leaks]]`.

## Inputs → Outputs
- **In:** `employer-org` (company name) or a person `name` tied to a company
- **Out:** onward searches returning company records, directors/officers (`associate`), registered `address`es, UBO clues
- **Empty/negative result looks like:** the tool always builds the links; "empty" happens on the destination registries (no filing found), often because the entity is in a jurisdiction none of the linked databases cover — try a country-specific registry directly.

## Gotchas & OpSec
- Human-in-the-loop: none in the tool; each linked registry has its own interface, some with rate limits or partial paywalls.
- It's a *launcher*, not a database — record which registry actually returned the data as your source, not this page.
- Coverage skews to NL/UK/EU and the big leak datasets; for other jurisdictions supplement with a local corporate registry.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` and `[[icij-offshore-leaks]]` directly — this tool routes you into them; go deeper in each for full filings and network links.

## Trust & verifiability
`trust: trusted` — built by Aware Online (a known OSINT trainer) and transparent about where it sends you; the actual evidence comes from the authoritative public registries it links, which you should cite individually.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | company-search-tool |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
