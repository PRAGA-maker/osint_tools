---
id: data-ddosecrets-search
name: DDoSecrets Search (Library of Leaks)
description: Use when you have a `name`, `email` or `domain` and want to find it inside published leaked/hacked datasets — returns matching documents and their source dataset.
url: https://search.ddosecrets.com/data/
category: public-records
path:
- public-records
bestFor: Full-text searching millions of leaked/hacked documents published in the public interest for a name, email, or organisation.
selectorsIn:
- name
- email
- domain
selectorsOut:
- email
- name
- document-id
status: live
pricing: free
costNote: Free; DDoSecrets is a non-profit and states cost should never be a barrier to access.
opsec: passive
opsecNote: Searching is passive and does not touch your subject. But the underlying material is hacked/leaked data — handling, storing and acting on it carries legal and ethical constraints that vary by jurisdiction and your authorisation. Treat any hit as a lead to verify against lawful sources, and follow your engagement's legal-gate rules.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: community
trustNote: Run by Distributed Denial of Secrets, an established transparency non-profit; the datasets are authentic leaks but are unvetted primary material — corroborate before relying on any single record.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Library of Leaks
- DDoSecrets search
- Distributed Denial of Secrets
tags:
- leaks
- public-records
- breach-data
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# DDoSecrets Search (Library of Leaks)

> A searchable index over millions of leaked and hacked documents published by DDoSecrets — type a name, email or domain and see which datasets mention it.

## When to use
You have a `name`, `email`, or `employer-org`/`domain` and want to know whether it appears in the large corpus of leaked/hacked material DDoSecrets has published (government leaks, corporate breaches, etc.). Useful for surfacing a subject's mentions in datasets you couldn't otherwise search, but strictly as a lead-generation step given the sensitive provenance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the search interface (search.ddosecrets.com / the Library of Leaks).
2. Enter a `name`, `email`, `domain`, or keyword and run the full-text search across indexed datasets.
3. Review hits — each links to the document and the source dataset it came from.
4. Note the dataset provenance and date; treat the content as an unverified lead.
5. Corroborate any actionable finding against a lawful primary source before using it, and follow your legal/ethical constraints on handling leaked data.

## Inputs → Outputs
- **In:** `name`, `email`, or `domain`/keyword
- **Out:** matching documents (`document-id`), the `email`/`name` context around them, and the source dataset
- **Empty/negative result looks like:** no matches — the selector isn't in the indexed leaks; it says nothing about the person's real-world footprint.

## Gotchas & OpSec
- **Legal-gate:** this indexes hacked/leaked data. What you may lawfully access, retain and act on depends on your jurisdiction and authorisation — do not treat a hit as usable evidence without clearing that gate.
- Content is unvetted primary material and can be forged, partial, or out of date — corroborate.
- OpSec: searching is passive; the risk is in handling the results, not the query.

## Overlaps ("do both")
- Overlaps with breach-notification services (HaveIBeenPwned et al.) which tell you *that* an email was breached; DDoSecrets lets you read *what* is in the published datasets. Use breach checkers first, this for depth.

## Trust & verifiability
`trust: community` — a reputable transparency non-profit hosts authentic leaks, but individual records are unverified primary sources; always corroborate before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | data-ddosecrets-search |
