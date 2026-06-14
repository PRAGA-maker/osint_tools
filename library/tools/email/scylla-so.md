---
id: scylla-so
name: Scylla.so
description: Use when you want to search an email/username against leaked-breach records — Scylla was a breach-data search engine with intermittent availability.
url: https://scylla.so/
category: email
path:
- email
bestFor: Searching breach/leak datasets by email, username, or other fields to find exposed records and linked accounts.
selectorsIn:
- email
- username
selectorsOut:
- name
- username
- phone
- metadata-exif
status: degraded
pricing: freemium
costNote: Free search interface historically; availability has been intermittent (the original Scylla.sh was taken down; .so is a successor/mirror of uncertain provenance).
opsec: passive
opsecNote: Passive lookup against leak databases — no contact with the subject. Operator/provenance is uncertain; use a VPN and never enter your own credentials.
humanInLoop: false
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: Successor/mirror of the original Scylla breach search engine, which was seized. Current operator and data integrity are unverified; site availability is intermittent. Treat results as leads requiring corroboration.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Scylla
- scylla.sh
tags:
- breach
- leak-search
- credentials
source: osint4all
lastVerified: ''
enrichment: full
---

# Scylla.so

> Scylla is a breach-data search engine — query an `email` or `username` across leaked datasets to surface exposed records. Provenance is uncertain and availability is intermittent.

## When to use
You have a subject's `email` or `username` and want to search leak corpora for exposed records (linked names, phones, other usernames). Useful as one of several breach engines to cross-check, given each indexes different datasets. Expect the site to be flaky or offline at times.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open scylla.so over a VPN / clean browser; it may be slow, behind a CAPTCHA, or down.
2. Enter the email or username (Scylla historically supported field-scoped queries like `email:` / `username:`).
3. Review returned leaked records; note linked `name`, `phone`, `username`.
4. Pivot recovered identifiers to social-profile and people-search tools — and corroborate, since data integrity is unverified.

## Inputs → Outputs
- **In:** `email` or `username`
- **Out:** leaked records — `name`, `username`, `phone`, source-breach metadata (`metadata-exif`).
- **Empty/negative result looks like:** no records, or the site failing to load (frequent for this domain).

## Gotchas & OpSec
- Human-in-the-loop: may present a CAPTCHA; the site is often unavailable.
- OpSec: passive toward the subject, but the operator is unknown and the data is leaked — use a VPN, do not log in with real credentials, and handle any exposed data lawfully.

## Overlaps ("do both")
- Cross-check with `[[scatteredsecrets-com]]` and other breach engines; corpora and uptime differ, so confirm any hit in a second source.

## Trust & verifiability
`trust: unverified` — successor/mirror of a seized service with unknown current ownership and unverified data integrity; intermittent availability. Use only as a lead source, never as proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scylla-so |
| category | email |
| selectorsIn → selectorsOut | email, username → name, username, phone, metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
