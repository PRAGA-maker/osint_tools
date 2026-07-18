---
id: namechecker-org
name: NameChecker.org
description: Use when you have a `username` and want to see which of 190+ social networks it is taken on — returns per-platform taken/available status and profile links.
url: https://www.namechecker.org/
category: username
path:
- username
bestFor: Fanning a single handle across 190+ social/brand platforms to spot where an account already exists.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free, no account; funded as a brand/naming utility so there's no paywall on the availability check.
opsec: passive
opsecNote: Passive toward the subject — the checker queries each platform for handle existence; it does not log into or notify any account. It is built for brand-name checks, so results indicate "taken" not "belongs to your subject" — verify each hit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A naming/branding availability tool, not an OSINT-purpose scraper; "taken" checks can false-positive (reserved/parked handles) and false-negative (rate-limited platforms), so treat results as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- namechk
- sherlock
aliases:
- NameChecker
- namechecker.org
tags:
- username
- account-enumeration
source: inteltechniques-tools
lastVerified: '2026-07-18'
enrichment: full
---

# NameChecker.org

> A brand-name availability checker repurposed for OSINT — enter a handle and see the 190+ platforms where it's already claimed.

## When to use
You have a `username` and want a fast, broad sweep of where that exact handle already exists — Instagram, TikTok, GitHub, Reddit, and 190+ other social/brand sites, plus domains. It's a discovery starting point: platforms showing "taken" are candidate accounts to inspect and tie back to your subject. Because it's built for people picking a brand name, read its output as "this handle is in use somewhere," then confirm each is actually your target.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.namechecker.org/.
2. Enter the exact `username`/handle and run the check.
3. Read the grid: each platform shows available (unclaimed) or taken (an account exists).
4. For each "taken" platform, open the profile URL and check whether it's actually your subject vs. a coincidental namesake.
5. Pivot: confirmed accounts feed profile-analysis and cross-platform correlation; consistent claims across many sites strengthen attribution.

## Inputs → Outputs
- **In:** `username`
- **Out:** per-platform taken/available status and `social-profile`/`username` links where taken
- **Empty/negative result looks like:** "available" everywhere — either the handle genuinely isn't used, or the checker was rate-limited on key platforms; a scarce handle with all-available results warrants a manual re-check on the platforms you care about.

## Gotchas & OpSec
- **"Taken" ≠ "your subject":** popular handles are claimed by many unrelated people — always verify the actual profile.
- Availability checkers can be inaccurate: reserved/parked/banned handles read as "taken," and rate-limited platforms can wrongly read as "available."
- Coverage and per-platform accuracy drift as sites change their signup pages; corroborate important negatives.
- OpSec: passive; no account is logged into or alerted.

## Overlaps ("do both")
- Pairs with `[[namechk]]` (another broad availability checker — cross-run to cover platform gaps) and `[[sherlock]]` (CLI enumeration that returns direct profile URLs for deeper verification).

## Trust & verifiability
`trust: community` — a branding utility, not a forensic tool; its taken/available signals are useful leads but prone to both false positives and negatives, so verify every account directly before attributing it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | namechecker-org |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
