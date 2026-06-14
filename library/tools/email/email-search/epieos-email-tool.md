---
id: epieos-email-tool
name: Epieos Email Tool
description: Use when you have an email address and want to reverse it into linked Google/Gravatar profiles and registered online accounts — returns social-profile, name, metadata.
url: https://tools.epieos.com/email.php
category: email
path:
- email
- email-search
bestFor: Reverse-email lookup exposing Google account, Gravatar, and registered services.
input: Email address
output: Linked Google profile, Gravatar, and accounts on many services
selectorsIn:
- email
selectorsOut:
- social-profile
- name
- metadata
status: live
pricing: freemium
costNote: Free interactive web lookup (limited); deeper/bulk reports and API are paid Epieos plans.
opsec: passive
opsecNote: Passive reconnaissance across many sites and Google's public account data; the target is not notified. Queries hit Epieos servers, so use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Epieos is a widely used, reputable OSINT service in the email/Google-account space; results are well-regarded among practitioners.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- holehe
- ghunt
- email-reputation
aliases:
- Epieos email lookup
tags:
- email
- reverse-email
- google-account
source: arf-seed
lastVerified: ''
enrichment: full
---

# Epieos Email Tool

> Reverse-email lookup that turns an address into linked Google/Gravatar profiles and a map of services where the address is registered — one of the strongest single-step email pivots.

## When to use
You have an `email` and want maximum identity context fast: a connected Google account (name, profile photo, reviews/maps activity exposure), a Gravatar, and which third-party services the address has accounts on. In missing-persons work this can yield a name, photo, and live online footprint from just an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to tools.epieos.com/email.php.
2. Enter the `email` and submit (no login for the basic lookup).
3. Read the panels: Google account info (if a Google/Gmail address), Gravatar profile, and the grid of services where the address is registered.
4. Pivot: a recovered `name`/photo feeds image and people searches; registered `social-profile` hits feed `[[holehe]]`; for deep Google exploitation move to `[[ghunt]]`.

## Inputs → Outputs
- **In:** `email`
- **Out:** `social-profile` (registered services), `name` (from Google/Gravatar), `metadata` (account IDs, profile photo, activity hints)
- **Empty/negative result looks like:** no Google/Gravatar match and an empty/all-negative service grid — thin footprint or a non-Google provider.

## Gotchas & OpSec
- Best signal comes from Gmail/Google-linked addresses; non-Google addresses return less.
- Free tier is rate-limited; heavy or bulk use needs a paid Epieos plan/API.
- OpSec: passive — the target is not alerted, but your queries hit Epieos. Use a sock-puppet browser/clean IP.

## Overlaps ("do both")
- Pairs with `[[holehe]]` (broader account enumeration), `[[ghunt]]` (deeper Google-account dig), and `[[email-reputation]]` (risk/profile summary) — each catches what the others miss.

## Trust & verifiability
`trust: trusted` — Epieos is a well-established, practitioner-recommended OSINT service; its email/Google-account results are accurate and widely cited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | epieos-email-tool |
| category | email |
| selectorsIn → selectorsOut | email → social-profile, name, metadata |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
