---
id: best-phone-lookup
name: Best Phone Lookup
description: Use when researching a US phone number — but note this domain is now a parked redirector, not a working lookup; prefer a live reverse-phone tool instead.
url: http://phonesearch.us/login.php
category: phone
path:
- phone
bestFor: (Defunct) was a login-gated US reverse phone lookup; the domain is now parked.
selectorsIn:
- phone
selectorsOut:
- name
- address
status: down
pricing: free
costNote: No functioning service to price — the domain now serves a parked/redirect ad page.
opsec: passive
opsecNote: Reaching the page hits a parking/ad-router service (parklogic) that fingerprints the browser; do not enter any query data.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: untrustworthy
trustNote: phonesearch.us now resolves to a parked-domain ad redirector (router.parklogic.com), not the original "Best Phone Lookup" tool; treat as defunct/abandoned.
missingPersonsRelevance: low
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- phonesearch.us
- Best Phone Lookup
tags:
- phone
- reverse-lookup
- defunct
source: metaosint
lastVerified: '2026-06-13'
enrichment: full
---

# Best Phone Lookup

> Formerly a login-gated US reverse phone lookup at phonesearch.us — the domain is now a parked ad-redirector and no longer a usable OSINT tool.

## When to use
Effectively: don't. If you arrived here looking to resolve a US `phone` number to a `name`/`address`, route to a working alternative (see Overlaps). This entry exists so the agent recognizes the dead site and pivots rather than wasting effort on a login wall.

## How to use it (`bestInteractionPattern`: web-manual)
1. Navigating to http://phonesearch.us/login.php returns HTTP 200 but the body is a "Redirecting…" parking page that POSTs to `router.parklogic.com` and runs ad-block/browser fingerprinting.
2. There is no functioning login or lookup form serving real reverse-phone data.
3. Pivot immediately to a live tool below.

## Inputs → Outputs
- **In:** `phone` (intended)
- **Out:** none usable — `name`/`address` were the historical outputs, but the service no longer returns them.
- **Empty/negative result looks like:** the entire site — a parking/redirect page is what you get, every time.

## Gotchas & OpSec
- Status `down`: domain is parked. The original "login.php" implies it always required an account, but there is nothing real behind it now.
- Do not submit any subject data; the page is an ad-router that fingerprints visitors.
- OpSec: treat as hostile/abandoned infrastructure — use a clean browser if you must visit, but you should not need to.

## Overlaps ("do both")
- Replace with `[[advanced-background-checks]]` (free US reverse phone lookup) and `[[carrier-lookup]]` (US carrier/line type); for non-US use country directories like `[[canada411-ca]]` or `[[britishphonebook-com]]`.

## Trust & verifiability
`trust: untrustworthy` — verified 2026-06-13 that phonesearch.us now serves a parked-domain ad redirector rather than the listed tool. Marked `status: down`; excluded from active use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | best-phone-lookup |
| category | phone |
| selectorsIn → selectorsOut | phone → (none — defunct) |
| pricing / cost | free (no service) |
| trust | untrustworthy |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (was login-gated) |
