---
id: numspy-api
name: Numspy-Api
description: Use when you have an Indian mobile `phone` number and want basic subscriber/network details via a simple GET API — returns `name`, carrier, and `address` (state) hints.
url: https://numspy.pythonanywhere.com/
category: phone
path:
- phone
bestFor: Programmatic lookup of Indian (10-digit) mobile numbers — subscriber name, provider, and state — via a JSON GET endpoint.
selectorsIn:
- phone
selectorsOut:
- name
- address
status: degraded
pricing: free
costNote: Free open-source public API (bhattsameer/numspy-api), Flask-hosted on PythonAnywhere. No API key. Free PythonAnywhere hosting means the instance is frequently offline/rate-limited — the root URL may 404 while the /LocateMobile endpoint intermittently works, so treat availability as unreliable.
opsec: active
opsecNote: Remote API calls are logged by the operator and by PythonAnywhere; queries are attributable to your IP. The lookup does not contact or notify the number's owner. Route through a clean IP for sensitive work. Data provenance is opaque (scraped from Indian number-lookup sites), so treat results as leads, not confirmed facts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: unverified
trustNote: Community open-source project scraping unofficial Indian number-info sources; accuracy and uptime are not guaranteed and the data source has historically been unstable.
missingPersonsRelevance: high
coverage:
- in
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Numspy API
- numspy public api
tags:
- phone
- india
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Numspy-Api

> A free, keyless GET API for basic Indian mobile-number details (name, provider, state) — handy when it's up, but flaky free hosting makes it a best-effort lookup.

## When to use
You have a 10-digit Indian mobile `phone` number and want a quick, scriptable read of the subscriber `name`, telecom provider, and circle/state. Fits an early-stage phone workflow for Indian numbers where you want a programmatic (JSON) result to chain into other tools — provided the endpoint is responding.

## How to use it (`bestInteractionPattern`: api)
1. Hit the endpoint with a GET request: `http://numspy.pythonanywhere.com/LocateMobile/<10-digit-number>` (no key, no auth).
2. Parse the JSON: fields typically include Mobile number, Name, Provider, and State.
3. If the root URL 404s or the call times out, the free instance is asleep/offline — retry later or fall back to the Python module (`bhattsameer/numspy`) or another phone tool.
4. Treat outputs as unverified leads.
5. Pivot: a returned `name` feeds people-search; the provider/state (`address` region) narrows geolocation; the number itself feeds messaging-app and breach checks.

## Inputs → Outputs
- **In:** `phone` (Indian 10-digit mobile)
- **Out:** subscriber `name`, telecom provider, circle/state (`address` region)
- **Empty/negative result looks like:** an error/empty JSON, a 404 on the host, or a "not found" payload — meaning the number isn't in the scraped source OR (very often) the free instance is simply down. Absence is not evidence.

## Gotchas & OpSec
- **Uptime is the main failure mode.** PythonAnywhere free apps sleep and rate-limit; expect frequent 404/timeout. Have a fallback ready.
- **India-only.** Non-Indian numbers won't resolve.
- Data is scraped from unofficial lookup sites — names can be stale, wrong, or reflect a prior owner. Always corroborate.
- OpSec: active (your IP queries a third-party API), but the number's owner is not notified.

## Overlaps ("do both")
- Pairs with libphonenumber-style validators and messaging-app presence checks — Numspy attempts a name/carrier from Indian sources, while a validator confirms format/region and app-checks confirm the number is live. Cross-check the carrier/state before trusting the name.

## Trust & verifiability
`trust: unverified` — a community scraper over unofficial Indian number data on flaky free hosting. Never treat a returned name as confirmed; verify against an independent source (e.g. a linked social profile or a second phone tool) before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | numspy-api |
| category | phone |
| selectorsIn → selectorsOut | phone → name, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | api |
| opsec | active |
| human-in-loop | no |
