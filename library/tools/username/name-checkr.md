---
id: name-checkr
name: NameCheckr
description: Use when you have a `username` and want a fast availability check across social networks and domains to see where the handle is taken — returns social-profile presence signals.
url: https://www.namecheckr.com
category: username
path:
- username
bestFor: One-glance check of which social sites and domains a username is registered on.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free web tool; no account.
opsec: passive
opsecNote: Availability checks are made from NameCheckr's side, not yours; targets are not notified. You disclose the handle to the site. As with all availability checkers, "taken" means the name exists — not that it's your subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Convenience availability checker; results are a quick signal, not verified profile confirmation, and its site list is smaller than dedicated enumerators.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname-web
- namechk-2
- sherlock
aliases:
- namecheckr.com
- Name Checkr
tags:
- username-check
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# NameCheckr

> A quick handle-availability checker across popular social networks and domains — a fast first read on where a username is already taken (i.e. registered by someone).

## When to use
You have a `username` and want an at-a-glance map of which major platforms and domains have that handle registered. "Taken" on a site is a lead that your subject *might* have an account there; it's the fastest way to generate a shortlist before deeper, per-site confirmation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.namecheckr.com and enter the username.
2. Read the grid: which social sites and domain TLDs show the handle as taken vs available.
3. For each "taken" site, open the profile URL and confirm it's actually your subject (handles are reused).
4. Because its site list is limited, follow up with a broader enumerator for full coverage.
5. Pivot: confirmed profiles feed content review; a distinctive handle that's taken everywhere strengthens attribution.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` presence signals (taken/available per site + domains)
- **Empty/negative result looks like:** "available" everywhere means the handle is unused on the sites it checks — but it only checks a subset, so run a larger tool before concluding the person has no accounts.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; no target alert.
- Identity trap: "taken" ≠ "your subject." Availability checkers report existence, not ownership — always open and verify the profile.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-web]]` and `[[sherlock]]` — far larger site coverage; use NameCheckr for a quick look and these for depth.
- Pairs with `[[namechk-2]]` — comparable checker; cross-run since site lists differ.

## Trust & verifiability
`trust: community` — a handy but shallow availability checker; treat every "taken" as a lead to open and confirm, not as proof of an account belonging to your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | name-checkr |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
