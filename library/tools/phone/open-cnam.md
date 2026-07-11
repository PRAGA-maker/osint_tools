---
id: open-cnam
name: OpenCNAM (Neustar Caller Name)
description: Use when you have a US `phone` and want the registered caller-ID name (CNAM) for the line — returns the CNAM string (a name), now via Neustar's enterprise API.
url: https://www.opencnam.com
category: phone
path:
- phone
bestFor: Resolving a US phone number to its registered CNAM (caller-ID name) label via API.
selectorsIn:
- phone
selectorsOut:
- name
status: degraded
pricing: freemium
costNote: The old self-serve OpenCNAM free/hobbyist tier is gone — opencnam.com now redirects to Neustar's enterprise "Caller Name Services." Access today generally requires a business account/contract and an API key; there is no easy free individual tier. Author-listed for completeness and to warn that the free tool many OSINT lists reference no longer exists.
opsec: passive
opsecNote: A CNAM lookup is a passive API query against telecom caller-name data; the subject is never contacted or notified. The exposure is to the API provider (Neustar), which logs the query and the number under your account/API key.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: CNAM data itself is telecom-grade, but it reflects the label the line's carrier registered (often a business or the account holder's name, sometimes blank or generic) — not a verified identity.
missingPersonsRelevance: high
coverage:
- us
auth: api-key
api: true
localInstall: false
registration: true
invitationOnly: false
aliases:
- OpenCNAM
- opencnam.com
- Neustar Caller Name Services
tags:
- phone
- cnam
- caller-id
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# OpenCNAM (Neustar Caller Name)

> The classic CNAM (caller-ID name) lookup — a US number in, the carrier-registered name string out. Note: the free self-serve OpenCNAM is gone; it's now Neustar's enterprise API.

## When to use
You have a US `phone` and want the CNAM — the caller-ID name label the line's carrier has on file. For a landline or business line this is often the account holder's or company's name; for a personal mobile it may be blank, a first name, or a generic label. It's a cheap corroborating signal for "whose number is this?", complementing reverse-phone aggregators.

## How to use it (`bestInteractionPattern`: api)
1. Be aware `opencnam.com` now redirects to **Neustar Caller Name Services** — the old free hobbyist tier is retired.
2. Obtain enterprise/API access (business account + API key) from Neustar, or use a CNAM lookup exposed by another telephony provider (Twilio, Telnyx, etc.).
3. Query the number via the API (historically `GET .../phone/<number>?...` returning the CNAM string).
4. Read the returned `name` string; treat blank/`UNKNOWN`/generic labels as "no CNAM on file."
5. Pivot: a returned name → people-search and cross-check against `[[www-spydialer-com]]`; a business name → `[[kompass]]`/registries.

## Inputs → Outputs
- **In:** `phone` (US)
- **Out:** `name` (the CNAM string registered for the line)
- **Empty/negative result looks like:** an empty, `UNKNOWN`, or generic city/carrier label — no useful registered name. CNAM is frequently blank for mobiles, so absence is common and not meaningful.

## Gotchas & OpSec
- The free OpenCNAM many OSINT guides cite no longer exists as a self-serve tool — expect an enterprise gate or use a telephony provider's CNAM endpoint instead.
- CNAM ≠ verified identity: it's a carrier-registered label, easily generic or outdated; corroborate before trusting a name.
- US-focused; CNAM is largely a North American concept.

## Overlaps ("do both")
- Pairs with `[[www-spydialer-com]]` and `[[free-carrier-lookup]]` — carrier-lookup gives line type, SpyDialer attempts an owner from public data, CNAM gives the carrier-registered name; agreement across all three is a strong signal.

## Trust & verifiability
`trust: community` — the data is telecom-sourced but is only the registered label, not a confirmed identity; use it as one corroborating input, and note the free tool is deprecated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-cnam |
| category | phone |
| selectorsIn → selectorsOut | phone → name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
