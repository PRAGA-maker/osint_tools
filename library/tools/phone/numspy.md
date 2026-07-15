---
id: numspy
name: Numspy
description: Use when you have an Indian `phone` number and want scripted carrier/region lookup from Python/CLI — returns carrier, circle/region, and number metadata.
url: https://bhattsameer.github.io/numspy/
category: phone
path:
- phone
bestFor: Scripted lookup of Indian mobile-number metadata (operator, telecom circle/region) from a Python module.
selectorsIn:
- phone
selectorsOut:
- phone
- geolocation
status: degraded
pricing: free
costNote: Free open-source Python module (`pip3 install numspy`). No API key for the number-details lookup; the bundled Way2SMS send/schedule features depend on Way2SMS, which is largely defunct, so treat SMS features as unreliable.
opsec: active
opsecNote: The number-details lookup scrapes third-party number-info sites from your machine/IP — those endpoints see your requests. Run it from a VPN/attribution-managed host if you need to stay covert; the target is not contacted by the lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: unverified
trustNote: A hobby OSINT module by developer Sameer Bhatt (bhattsameer); installs cleanly but relies on scraped upstream sources whose accuracy and uptime vary.
missingPersonsRelevance: high
coverage:
- in
auth: none
api: true
localInstall: true
registration: false
aliases:
- numspy python module
tags:
- phone-number-research
- python
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Numspy

> A small Python module that returns metadata for a mobile number (operator, telecom circle/region) via scraping — most reliable for Indian numbers, and best used as a scriptable step in a phone-recon pipeline.

## When to use
You have an Indian `phone` number and want its carrier and telecom circle (region) programmatically — e.g. batching many numbers, or wiring number-metadata into a larger script. It won't name the owner, but operator + circle narrows geography and corroborates whether a number is plausible for a claimed location.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip3 install numspy` (needs Python 3; pulls in requests/BeautifulSoup).
2. In Python, import numspy and call its number-details function with the target number in the expected format.
3. Read the returned fields — operator/carrier and telecom circle/region.
4. Pivot: the circle gives a rough `geolocation`; combine with people-search or messaging-app lookups (e.g. Telegram add-by-number) to move toward identity.

## Inputs → Outputs
- **In:** `phone` (Indian mobile number)
- **Out:** carrier/operator, telecom circle → `geolocation` (region), number validity signal
- **Empty/negative result looks like:** an error or blank fields — usually the scraped upstream changed or is down, or the number is non-Indian/out of the module's coverage; verify with a second phone tool before trusting a null.

## Gotchas & OpSec
- **India-centric**: designed around Indian numbering/operators; low value for other countries.
- **Scraper fragility**: it depends on third-party sites that change or break, hence `status: degraded` — always sanity-check results against another source.
- The bundled Way2SMS SMS-sending features are effectively dead; ignore them for OSINT.
- OpSec: **active** — the lookup hits upstream sites from your IP; use managed attribution for covert work. The subject is never contacted.

## Overlaps ("do both")
- Pairs with other phone-intelligence tools and `[[tginfo-me]]` (Telegram add-by-number) — Numspy gives carrier/region cheaply and at scale; messaging-app checks turn a number into a `social-profile`.

## Trust & verifiability
`trust: unverified` — a useful hobbyist module, but it scrapes sources of variable accuracy and uptime; corroborate carrier/region against a second tool before relying on it in a case.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | numspy |
| category | phone |
| selectorsIn → selectorsOut | phone → phone, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | python-lib |
| opsec | active |
| human-in-loop | no |
