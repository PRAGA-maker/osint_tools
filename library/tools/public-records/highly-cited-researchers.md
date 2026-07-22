---
id: highly-cited-researchers
name: Highly Cited Researchers (Clarivate)
description: Use when you have a researcher's `name` or an institution and want to confirm their field, affiliation, and standing — returns `employer-org` (institution), country, and research area.
url: https://hcr.clarivate.com
category: public-records
path:
- public-records
bestFor: Verifying an academic's institution, country, and research field against Clarivate's annual Highly Cited Researchers list.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: The searchable list is free to browse; the underlying Web of Science data behind it is a paid Clarivate product, but the HCR directory itself is public.
opsec: passive
opsecNote: A public directory lookup; searching a name touches only Clarivate's list and never reaches the person. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Clarivate (Web of Science) using citation analysis; inclusion is a reliable signal of research standing, though it only covers the highly-cited top tier, not researchers generally.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- HCR Clarivate
- hcr.clarivate.com
tags:
- toddington
- academic
- researchers
- verification
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Highly Cited Researchers (Clarivate)

> Clarivate's annual roll of the world's most-cited scientists — a quick way to confirm a named academic's institution, country, and field.

## When to use
You have a researcher's `name` (or an `employer-org`/institution) and want to verify their academic standing and current affiliation, or enumerate the top-cited researchers at an institution or in a field. In an investigation this corroborates a claimed academic identity, pins a subject to an institution and country, and helps disambiguate common names by research area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://hcr.clarivate.com.
2. Search by researcher `name`, or filter by institution, country/region, and research field.
3. Read the entry: name, primary affiliation (`employer-org`), country, and the category/field they were recognized in, plus the award year(s).
4. Pivot: the confirmed institution and field feed university directory, `[[linkedin]]`, and scholarly-profile (ORCID, Google Scholar) lookups to build out the person.

## Inputs → Outputs
- **In:** `name` or `employer-org`/institution
- **Out:** `employer-org` (affiliation), country, research field, recognition year — a verified `name`↔institution↔field link
- **Empty/negative result looks like:** no entry — the person simply isn't on the highly-cited list (the vast majority of researchers aren't). Absence says nothing about whether they're a real or active academic; it only means they aren't in the top-cited tier.

## Gotchas & OpSec
- Coverage is the elite top tier only; most legitimate academics never appear. Use it to confirm, not to rule out.
- Affiliation reflects the year of listing; a person may since have moved institutions.
- OpSec: passive directory lookup; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with `[[linkedin]]`, ORCID, and Google Scholar to flesh out a confirmed academic, and with university staff directories to find current contact/affiliation.

## Trust & verifiability
`trust: trusted` — a reputable Clarivate publication built on Web of Science citation data; inclusion is authoritative for standing, but remember it captures only the highly-cited elite as of each annual edition.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | highly-cited-researchers |
| category | public-records |
