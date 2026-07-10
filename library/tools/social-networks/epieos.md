---
id: epieos
name: Epieos
description: Use when you have an `email` or `phone` and want to reverse-lookup the accounts, profiles and Google identity tied to it — returns social-profile, name, username and location hints.
url: https://epieos.com
category: social-networks
path:
- social-networks
bestFor: Reverse email/phone lookup that maps an address or number to connected accounts and a Google profile without alerting the target.
selectorsIn:
- email
- phone
selectorsOut:
- social-profile
- name
- username
- geolocation
status: live
pricing: freemium
costNote: The web email lookup is free with daily usage limits; phone lookups, bulk/history and the API are paid tiers. No payment needed for a single stealth email check.
opsec: passive
opsecNote: Epieos queries third-party services server-side and states it does not notify the target or log queries, so a single lookup is passive from the subject's side. Still run it from a research/sock-puppet context and avoid pasting live case emails into any tool you do not control.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Widely-used, well-regarded third-party OSINT service (Maltego transform hub partner). Results are aggregated from other platforms, so treat each hit as a lead to confirm at the source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- account-live-com
- holehe
aliases:
- Epieos email lookup
- holehe online
tags:
- real-time-search-social-media-search-and-general-social-media-tools
- email
- reverse-lookup
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Epieos

> A reverse email/phone search engine that turns a single address or number into a map of connected accounts and a Google identity — quietly.

## When to use
You have an `email` or `phone` for the subject and want to know what it is connected to: which of 140+ services (Google, Skype, LinkedIn, GitHub, Pinterest, Fitbit, Duolingo, etc.) have an account on it, plus the Google profile — display `name`, profile photo, public Google Maps reviews (which leak `geolocation`), and account creation date. It is one of the fastest first pivots once you have a confirmed contact selector.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://epieos.com and choose the email or phone tab.
2. Enter the subject `email` (or `phone` in full international format) and run the lookup.
3. Read the output:
   - **Accounts found** — a list of services where the address/number is registered (each is a pivot).
   - **Google account** — if the email is a Google account, you get the Gmail display `name`, profile picture, Google ID, and links to public **Maps reviews/photos** that often reveal home city, workplace or travel `geolocation`.
   - Empty result = no connected services surfaced (see below).
4. Pivot: feed discovered `username`/`social-profile` links into the relevant platform tools; use a leaked recovery/second address as a new `email` selector; treat Maps review locations as leads to corroborate.

## Inputs → Outputs
- **In:** `email` or `phone`
- **Out:** `social-profile` (connected accounts), `name` (Google display name), `username`, `geolocation` (from Google Maps reviews/photos)
- **Empty/negative result looks like:** "no account found" / a blank services list. This means nothing surfaced across the checked services — not that the person has no online presence. Re-run with alternate addresses.

## Gotchas & OpSec
- Human-in-the-loop: the free web tier is rate-limited (a handful of lookups); heavier or phone/history use pushes you to the paid plan or the API.
- Results are only as fresh as the underlying services; a service can hide account-existence, producing false negatives.
- OpSec: passive — Epieos states it does not tip off the subject. Still treat the address itself as sensitive and query from a clean context.
- Google Maps review data is a strong, often-overlooked location leak — check it every time.

## Overlaps ("do both")
- Pairs with `[[holehe]]` — holehe brute-checks account existence across sites from the CLI; Epieos adds the Google-profile and Maps-review layer that holehe lacks.
- Pairs with `[[account-live-com]]` — that confirms Microsoft-account existence and leaks masked recovery contacts, complementing Epieos's Google-side view.

## Trust & verifiability
`trust: community` — a mature, reputable third-party service used across the OSINT industry (Maltego integration), but its findings are aggregated from other platforms, so confirm each hit at the source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | epieos |
</content>
</invoke>
