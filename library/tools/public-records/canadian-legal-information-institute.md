---
id: canadian-legal-information-institute
name: Canadian Legal Information Institute (CanLII)
description: Use when you have a `name` and want Canadian court/tribunal decisions or legislation mentioning them — returns document-id case citations and associate/address context.
url: https://www.canlii.org/en/
category: public-records
path:
- public-records
bestFor: Full-text search of Canadian case law and legislation to find a person named as a party, witness, or subject in court/tribunal decisions.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: free
costNote: Free to search and read the full text of decisions and statutes; funded by Canadian law societies. No account required for public search.
opsec: passive
opsecNote: A public legal-research database — searching does not notify anyone named in a case, and CanLII only sees your query/IP. Note CanLII applies noindex/anti-scraping so cases are less exposed to general search engines; that's a benefit for the subject, not a barrier to your manual search. Use a sock-puppet browser for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Federation of Law Societies of Canada; authoritative primary-source court decisions and legislation.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- supremecourt-uk
- courtlistener
- canlii-database
aliases:
- CanLII
- canlii.org
tags:
- court
- legal
- case-law
- canada
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Canadian Legal Information Institute (CanLII)

> The free, authoritative database of Canadian court and tribunal decisions and legislation — searchable full-text, so a person's name in any published judgment surfaces.

## When to use
You have a `name` with a Canadian nexus and want to know whether they appear in litigation, tribunal rulings, family/estate proceedings, or regulatory decisions. Court records are dense identity sources: a decision can confirm addresses, relationships (`associate`s — co-parties, family, business partners), employment, financial disputes, and a documented timeline. CanLII covers the Supreme Court of Canada down through federal, provincial, and many administrative tribunals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.canlii.org/en/ and use the full-text search box.
2. Search the target `name` in quotes; add a jurisdiction filter (province/court) or a keyword (city, company) to cut noise from common names.
3. Open matching decisions and read for the person's role (party, witness, deceased in an estate matter), plus any addresses, relatives, and organizations named.
4. Note the neutral citation (`document-id`, e.g. `2023 ONSC 1234`) for your record.
5. Pivot: co-parties/relatives named become `associate` leads; an estate/probate matter can confirm a death; a company named feeds corporate-registry lookups.

## Inputs → Outputs
- **In:** `name` (optionally + jurisdiction/keyword)
- **Out:** case citations (`document-id`), the person's role and details in the decision, `associate` links (co-parties, family, counsel), sometimes `address`/employer context
- **Empty/negative result looks like:** no hits — the person may simply have no published Canadian decision (most legal matters never produce a searchable judgment), so absence is weak evidence.

## Gotchas & OpSec
- Coverage is *published decisions* only — settled, sealed, publication-banned, or lower-volume matters may never appear; a clean search ≠ no legal history.
- Common names generate false positives; always disambiguate with jurisdiction, dates, or a second identifier before attributing a case to your subject.
- Publication bans (common in family/youth/criminal matters) may anonymize parties as initials — respect these legally and ethically.
- OpSec: passive — no one is notified by your search.

## Overlaps ("do both")
- Pairs with [[courtlistener]] (US case law) and [[supremecourt-uk]] (UK) — use the jurisdiction-appropriate database; CanLII is the Canadian equivalent.

## Trust & verifiability
`trust: trusted` — operated by the Federation of Law Societies of Canada, serving primary-source decisions and statutes. The documents are authoritative; the analytic risk is misattribution on common names, not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-legal-information-institute |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
