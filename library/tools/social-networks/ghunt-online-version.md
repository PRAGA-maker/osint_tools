---
id: ghunt-online-version
name: GHunt Online Version
description: Use when you have an `email` (Gmail/Google account) and want to enumerate the linked Google profile — returns name, profile/cover images, Google ID, Maps reviews, and calendar/timezone hints.
url: https://gmail-osint.activetk.jp/
category: social-networks
path:
- social-networks
bestFor: Enriching a Gmail address into its public Google account profile without installing GHunt.
selectorsIn:
- email
selectorsOut:
- name
- image
- social-profile
- geolocation
status: live
pricing: free
costNote: Free hosted front-end for the GHunt framework; no account or payment. Onion mirror offered for anonymous access.
opsec: active
opsecNote: The lookup calls Google's own account/profile endpoints on the target's address via a third-party server run by ActiveTK. It relies on the operator's Google auth, and you are trusting a third party with the target email. Use a sock-puppet context; prefer running GHunt locally with your own cookies for sensitive cases.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run hosted wrapper around mxrch's open-source GHunt; convenient but you depend on a third party's server and its Google session staying valid.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- activetk
- ghunt
- epieos
- darkweb-archive
aliases:
- gmail-osint.activetk.jp
- GHunt web
tags:
- Social Media
- Google
- gmail
- email-enrichment
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# GHunt Online Version

> A hosted, no-install front-end for GHunt: paste a Gmail address and get back the public Google account behind it — name, photos, Google ID, Maps reviews, and activity hints.

## When to use
You have an `email` that is (or might be) a Google account and you want to confirm the person behind it and pull their public Google footprint without setting up GHunt and Google cookies locally. A hit gives you a `name`, profile and cover `image` (reverse-image pivots), the stable Google user ID, public Google Maps reviews (which leak `geolocation` — places the subject visited/reviewed), and calendar/timezone signals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gmail-osint.activetk.jp/ (or its onion mirror) in a sock-puppet browser.
2. Enter the target `email` in Gmail form and submit.
3. Read the report: whether the address maps to a Google account, the display `name`, profile/cover `image` URLs, the numeric Google ID, linked Google services, public Maps reviews, and timezone/last-activity hints.
4. Feed the profile `image` into reverse-image search and the Maps review locations into geolocation work; the Google ID is a stable key for correlating across other Google surfaces.
5. If the hosted instance is rate-limited/down or the case is sensitive, run the local GHunt tool with your own authenticated cookies instead.

## Inputs → Outputs
- **In:** `email` (Gmail / Google account)
- **Out:** `name`, `image` (profile + cover), `social-profile` (Google ID/services), `geolocation` (public Maps reviews)
- **Empty/negative result looks like:** "no Google account" / empty profile — the address is not a Google account, or the profile is fully private; not proof the email is unused.

## Gotchas & OpSec
- OpSec: this is **active** — the query hits Google's endpoints for the target address (via the host's session). Prefer a sock puppet; assume the third-party operator can log the emails you submit.
- Hosted instances break when the operator's Google cookies expire — a "session invalid" error is the tool's problem, not evidence about the target.
- Google has tightened these endpoints over time; some fields (e.g. calendar) may be blank even for real accounts.

## Overlaps ("do both")
- Pairs with `[[epieos]]` (which also resolves Gmail → Google profile plus other services) and `[[ghunt]]` (the local CLI) — cross-check results, since a hosted wrapper and a locally-authenticated run can return different completeness.

## Trust & verifiability
`trust: community` — it wraps the well-regarded open-source GHunt, but you rely on a third party's server and Google session; verify the returned name/photo independently before acting on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghunt-online-version |
| category | social-networks |
| selectorsIn → selectorsOut | email → name, image, social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
