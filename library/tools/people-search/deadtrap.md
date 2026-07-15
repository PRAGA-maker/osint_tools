---
id: deadtrap
name: DeadTrap
description: Use when you have a `phone` and want to identify its likely owner, carrier region and linked social/spam footprint — returns name, social-profile, geolocation.
url: https://github.com/kaan-44/DeadTrap
category: people-search
path:
- people-search
bestFor: Enriching an international phone number into owner, carrier/region and social-media footprint from one CLI run.
selectorsIn:
- phone
selectorsOut:
- name
- social-profile
- geolocation
status: live
pricing: free
costNote: MIT-licensed open-source Python tool; free. Needs Python 3 plus Firefox + geckodriver (it drives a browser via Selenium); no paid API keys.
opsec: active
opsecNote: DeadTrap automates Google and social-media queries about the number via a real browser (Selenium). It does not alert the number's owner, but the automated searches are fingerprintable and can trigger Google CAPTCHAs/rate-limits against your IP — run it behind a VPN/clean IP, not from an attributable network.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: cli
trust: community
trustNote: Single-author open-source project (~54 GitHub stars, MIT). Results are aggregated from public web/social sources and are indicative, not authoritative; audit the Python source before running and verify every hit independently.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- Dead Trap
tags:
- people-search
- open-source
- cli
- phone
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# DeadTrap

> A Python CLI that takes a phone number (with country prefix) and aggregates owner, carrier/region, social-media footprint and spam-risk signals from public sources in one pass.

## When to use
You have a `phone` number and want a fast first-pass profile of it: who it likely belongs to, its carrier/region, any social-media accounts registered to or associated with it, and whether it is flagged as spam. Good for opening up a lone phone-number lead before moving to targeted per-platform checks.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/kaan-44/DeadTrap`.
2. On Windows install Firefox + geckodriver first; on Linux run `python3 setup.py`.
3. Set the path in `Style/banner.py` as the README instructs.
4. Run `python3 main.py`, then enter the number **with country prefix** (e.g. `+15551234567`).
5. Read the sectioned output (Info / SocialMedia / spam). Pivot: a surfaced social handle feeds that platform's tooling and `[[social-search-engine]]`; the carrier/region narrows `geolocation`.

## Inputs → Outputs
- **In:** `phone` (E.164, with country prefix)
- **Out:** `name`/owner hints, `social-profile` links tied to the number, `geolocation` (carrier region), spam-risk flag
- **Empty/negative result looks like:** empty sections or a Selenium/geckodriver error — usually a bad number format, a Google CAPTCHA blocking the automated search, or a driver/path misconfiguration rather than proof the number is unused.

## Gotchas & OpSec
- Depends on a working Firefox + geckodriver install; version mismatches are the most common failure.
- Automated Google searches reliably hit CAPTCHAs — expect to intervene or throttle; use a clean IP.
- Output quality varies by country and by what is publicly indexed; treat every result as a lead to confirm.
- OpSec: it queries public sources about the number, not the owner's device, so the target isn't notified — but your automation is fingerprintable.

## Overlaps ("do both")
- Pairs with `[[osintxphone]]` for Mexican numbers (authoritative IFT carrier data) and with a global reputation lookup — DeadTrap casts a wide social net while those give precise carrier/region facts.

## Trust & verifiability
`trust: community` — an open-source, single-author CLI; the tool is real and functioning but the data is scraped from public web/social sources, so verify each finding independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deadtrap |
| category | people-search |
| selectorsIn → selectorsOut | phone → name, social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (captcha) |
