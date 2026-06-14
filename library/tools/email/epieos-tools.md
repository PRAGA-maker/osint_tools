---
id: epieos-tools
name: Epieos Tools
description: Use when you have an email or phone number and want Epieos's hub of free reverse-lookup tools (email-to-accounts, reverse phone) — returns social-profile, name, metadata.
url: https://tools.epieos.com
category: email
path:
- email
bestFor: Entry hub for Epieos's free email and phone reverse-lookup tools.
selectorsIn:
- email
- phone
selectorsOut:
- social-profile
- name
- metadata
status: live
pricing: freemium
costNote: Free interactive tools with limits; deeper/bulk lookups and API on paid Epieos plans.
opsec: passive
opsecNote: Passive reverse-lookup hub; queries go to Epieos servers and the target is not notified. Use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Epieos is a reputable, widely-used OSINT service; this is its tools landing page fronting the email and phone lookups.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- epieos-email-tool
- holehe
- ghunt
aliases:
- Epieos
tags:
- email
- phone
- reverse-lookup
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Epieos Tools

> The Epieos tools hub — a single entry point to its free reverse-email and reverse-phone lookups that map an identifier to linked Google/Gravatar profiles and registered accounts.

## When to use
You have an `email` or `phone` and want Epieos's lookups but are starting from the landing page rather than a deep link. From here you reach the email tool (account/Google/Gravatar mapping) and the reverse-phone tool. High-value first stop for both selectors in a missing-persons workup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to tools.epieos.com.
2. Choose the email or phone lookup.
3. Enter the `email`/`phone` and submit.
4. Read the results panels; pivot via `[[epieos-email-tool]]` (deep-linked email tool) for details, then `[[holehe]]`/`[[ghunt]]` to expand accounts.

## Inputs → Outputs
- **In:** `email`, `phone`
- **Out:** `social-profile` (registered services), `name` (Google/Gravatar), `metadata` (account IDs, profile photo, carrier/region for phone)
- **Empty/negative result looks like:** no profile matches and an empty service grid — thin footprint or non-Google address.

## Gotchas & OpSec
- This is the hub; the email-specific skill is `[[epieos-email-tool]]` — use that for the detailed email workflow.
- Free tier is rate-limited; bulk/API requires a paid plan.
- OpSec: passive; target not alerted, but queries reach Epieos — use a sock-puppet browser/clean IP.

## Overlaps ("do both")
- Same vendor as `[[epieos-email-tool]]`; pair with `[[holehe]]` and `[[ghunt]]` for broader/deeper account coverage.

## Trust & verifiability
`trust: trusted` — Epieos is an established, practitioner-recommended OSINT provider; this hub fronts its accurate, widely-used lookups.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | epieos-tools |
| category | email |
| selectorsIn → selectorsOut | email, phone → social-profile, name, metadata |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
