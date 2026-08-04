---
id: slash
name: Slash
description: Use when you have a `username` or `email` and want to sweep 180+ social platforms and forums at once — returns matching social-profiles plus scraped names, locations and contact hints.
url: https://github.com/redc86/slash
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: One-shot username/email enumeration across a very wide list of sites, with bio/contact scraping on hits.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
- name
- geolocation
status: live
pricing: free
costNote: Free and open-source (MPL-2.0). No paid tier; you self-host and run it locally.
opsec: active
opsecNote: It fires HTTP requests directly at each platform's profile URL, so those sites can see your IP/user-agent hitting many usernames in a burst. Run through a VPN/proxy and treat the check as observable; also, a match only proves the handle exists, not that it belongs to your subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community Python project (~700 stars); accuracy depends on per-site detection rules that rot as sites change. Verify every hit manually.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- slash osint
tags:
- username-enumeration
- account-discovery
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Slash

> A Sherlock-style username hunter that checks a handle across 180+ platforms and 30+ forums, then scrapes bios/contact data from the hits.

## When to use
You have a `username` (or `email`) and want a fast, broad map of where else that identity appears online — a first pivot when a subject is known by a handle and you need to find their other accounts, forum activity, or leaked contact details to expand the picture.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/redc86/slash && cd slash && pip install -r requirements.txt`.
2. Run `python slash.py <username-or-email>`.
3. Read the output: confirmed profile URLs per platform, plus any scraped name/location/phone/email/education pulled from those bios.
4. Manually open each claimed hit — the same handle on two sites is not proof of the same person.
5. Pivot: confirmed profiles feed platform-specific tools; a scraped `email`/`phone` feeds email/phone OSINT; a scraped `name` feeds people-search.

## Inputs → Outputs
- **In:** `username` or `email`.
- **Out:** `social-profile` URLs across many platforms, plus scraped `name`, `geolocation`, and contact strings from matched bios.
- **Empty/negative result looks like:** "not found" for a platform (or an all-negative run) — common for handles that are rare, newly created, or blocked behind login walls; absence is not proof.

## Gotchas & OpSec
- **Active/observable:** hammering 180+ sites with one username is noisy; rate-limits and false "found" results from soft-404 pages are common.
- Detection rules drift as sites change their markup — expect both false positives and missed accounts; corroborate before acting.
- Bio scraping can surface stale data (old locations/jobs); date-check anything you rely on.

## Overlaps ("do both")
- Run alongside a second enumerator so gaps in one site-list are covered by the other; a full OSINT platform like `[[prism]]` can orchestrate username checks plus domain/email modules in one place.

## Trust & verifiability
`trust: community` — an open-source enumerator whose value is the breadth of its site list, but every hit is a lead to verify by hand, never a confirmed identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slash |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email → social-profile, name, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
