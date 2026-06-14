---
id: peepmail
name: Peepmail
description: Use when you have a person's name and their company domain and want to guess likely work email patterns — legacy Samy Kamkar demo, almost certainly defunct.
url: http://www.samy.pl/peepmail
category: email
path:
- email
bestFor: Guessing corporate email address patterns from a name + domain (historical).
selectorsIn:
- name
- employer-org
- domain
selectorsOut:
- email
status: down
costNote: Free demo project; the hosted service has long been non-functional.
pricing: free
opsec: passive
opsecNote: Pattern-guessing is computed from public naming conventions; no contact with the subject. (Service likely dead, so moot.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Peepmail is an old Samy Kamkar (samy.pl) demo that inferred corporate email formats from a name and company. It has not worked reliably in years; treat as historical reference.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- peepmail
tags:
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Peepmail

> A historical Samy Kamkar demo that guessed corporate email patterns from a name and company — long defunct; use a modern email-finder instead.

## When to use
Conceptually: you have a `name` and an `employer-org`/`domain` and want a likely work `email` (e.g. first.last@company.com). In practice the service is down — use a maintained alternative.

## How to use it (`bestInteractionPattern`: web-manual)
1. The legacy page is at samy.pl/peepmail; expect it to be non-functional.
2. For live pattern-finding, use `[[nymeria-io]]` or `[[omail-io]]`, or infer the company's format from a known employee and apply it to the subject's name.

## Inputs → Outputs
- **In:** `name`, `employer-org`, `domain`
- **Out:** `email` (pattern guess, unverified)
- **Empty/negative result looks like:** the page fails to load or returns nothing — the expected state today.

## Gotchas & OpSec
- Almost certainly defunct; do not rely on it.
- Any guessed email must be verified (deliverability/breach check) — guesses are frequently wrong.
- OpSec: passive (computation only).

## Overlaps ("do both")
- Superseded by `[[nymeria-io]]`, `[[omail-io]]`, and `[[pipl]]` for live email discovery.

## Trust & verifiability
`trust: unverified` — historical demo, retained for provenance; not a working tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peepmail |
| category | email |
| selectorsIn → selectorsOut | name, employer-org, domain → email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
