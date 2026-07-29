---
id: jstor
name: JSTOR
description: Use when you have a `name` or topic and want scholarly articles, books, or primary sources authored by or about a subject — returns academic publications and archival materials.
url: https://www.jstor.org
category: search-engines
path:
- search-engines
bestFor: Searching a subject's academic authorship or finding archival/primary-source material by topic.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Free registered accounts get limited monthly reads plus open/Creative-Commons content and free search; full access to paywalled articles needs an institutional subscription or purchase.
opsec: passive
opsecNote: You search a public academic index — no subject selector is exposed to the target. Fully passive. A free personal account ("register & read") is enough for most triage; use a sock-puppet email if you prefer not to tie the account to yourself.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: JSTOR is an authoritative, long-established scholarly digital library operated by ITHAKA; content is peer-reviewed/archival and citable.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- google-scholar
aliases:
- JSTOR
tags:
- academic-resources-and-grey-literature
- scholarly-search
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# JSTOR

> An authoritative digital library of scholarly journals, books, and primary sources — search a person's academic authorship, or research a topic through peer-reviewed and archival material.

## When to use
Your subject has (or may have) an academic footprint — a researcher, academic, or someone who published or was written about. Search JSTOR by `name` to find their articles/books, which expose affiliations (`employer-org`), co-authors (`associate`), dates, and a paper trail placing them in institutions and networks. Also useful for the archival side: its primary sources (Independent Voices alternative press, Artstor images, maps) can corroborate historical or place-based leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.jstor.org and search the `name` (use quotes; try name variants and initials).
2. Filter by author, date, discipline; open results — abstracts and metadata are visible even when full text is paywalled.
3. Read author affiliations and co-authors to extract `employer-org` and `associate` links.
4. For full text: use open/CC content freely, or a free "register & read" account for limited monthly reads; paywalled items need institutional access.
5. Pivot: an affiliation dates the subject to an institution; co-authors become new leads.

## Inputs → Outputs
- **In:** `name` (author) or topic
- **Out:** publications with affiliations (`employer-org`), co-authors (`associate`), dates
- **Empty/negative result looks like:** no authored works — the person may not be an academic, published under a variant name, or in venues JSTOR doesn't index. Cross-check `[[google-scholar]]`.

## Gotchas & OpSec
- **Freemium paywall:** search and metadata are free; many full texts require subscription/purchase — rely on abstracts and open content for triage.
- Common-name ambiguity — disambiguate by field/affiliation before attributing authorship.
- OpSec: **passive** — nothing about your target is disclosed; a free account (optionally sock-puppet) unlocks limited reads.

## Overlaps ("do both")
- Pairs with `[[google-scholar]]` — Google Scholar is broader and free-full-text-friendly for discovery; JSTOR adds authoritative archival depth and primary sources. Search both to catch works each misses.

## Trust & verifiability
`trust: trusted` — a curated, citable scholarly archive; metadata and publications are authoritative and verifiable against the original journals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jstor |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
