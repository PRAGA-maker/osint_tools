---
id: followerwonk
name: Followerwonk
description: Use when you have a Twitter/X `username` and want audience/bio analytics and account-overlap comparison — returns follower demographics and associated accounts.
url: https://followerwonk.com/
category: social-networks
path:
- social-networks
- twitter
- search
bestFor: Analyzing a Twitter/X account's followers and comparing two accounts to surface shared connections and audience overlap.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: degraded
pricing: freemium
costNote: Free tier allows limited bio search and basic analysis after login; deep follower analytics, comparisons and exports require a paid plan.
opsec: passive
opsecNote: Uses public profile/follower data via a third-party analytics service; the target is not notified. You must log in, so the account ties activity to you — use a research login.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established Twitter-analytics product (Moz lineage). Depth depends on X's API access, which has tightened since 2023, so historical coverage may be reduced.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- epieos
aliases:
- Follower Wonk
tags:
- twitter
- x
- social-analytics
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Followerwonk

> Twitter/X audience analytics: profile a `username`'s followers, search bios, and compare two accounts to expose shared connections.

## When to use
You have a subject's Twitter/X `username` and want to understand their network rather than their tweets: who follows them, where those followers cluster (location/timezone/activity), and — most usefully for investigations — which accounts two handles have in common. Bio search also lets you find accounts by keywords people put in their profiles (employer, city, role), turning a `name`/attribute into candidate `username`s.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://followerwonk.com/ and log in (free account for basic use).
2. **Analyze** a `username` to profile its followers/following: location map, active hours, bio word cloud, social authority.
3. **Compare** two usernames to see follower overlap — the shared-connection view is the strongest OSINT signal (find who links two people).
4. **Search bios** for keywords to surface accounts matching an attribute.
5. Pivot: shared/overlap accounts become new `associate` leads; a bio-search hit becomes a new `username` to run through profile tools.

## Inputs → Outputs
- **In:** `username` (or bio keywords)
- **Out:** `social-profile` analytics (follower demographics, activity, bio word cloud), `associate` (shared connections via account comparison)
- **Empty/negative result looks like:** thin or missing analytics / "unable to fetch." Post-2023 X API limits can cap how much follower data loads, so a sparse result may reflect API throttling, not a small account.

## Gotchas & OpSec
- Human-in-the-loop: login required; the richest features (deep follower pulls, comparisons, exports) are gated behind paid plans.
- **Status is degraded-risk:** X's API changes since 2023 have reduced what many third-party analytics tools can retrieve; verify current depth before relying on completeness.
- Twitter/X only — no value for other platforms.
- OpSec: passive; the subject isn't alerted. Log in with a research account.

## Overlaps ("do both")
- Pairs with `[[epieos]]` — Epieos maps an email/phone to accounts; Followerwonk then profiles and cross-compares the Twitter account you land on.
- Do alongside native X advanced search, which finds the *content* Followerwonk's audience analytics ignore.

## Trust & verifiability
`trust: community` — a well-known commercial analytics tool, but its coverage is bounded by X's API access, which has tightened; treat follower/overlap figures as indicative and confirm key connections directly on-platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | followerwonk |
</content>
