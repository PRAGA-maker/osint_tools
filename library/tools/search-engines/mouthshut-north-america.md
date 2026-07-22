---
id: mouthshut-north-america
name: MouthShut
description: Use when you have a `username` or `name` and want a subject's consumer reviews and reviewer profile — returns `social-profile`, posting history and disclosed location/purchase detail.
url: http://www.mouthshut.com
category: search-engines
path:
- search-engines
bestFor: Finding a person's consumer-review profile and history on a large (India-centric) reviews platform.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to read reviews and public reviewer profiles; an account is only needed to post.
opsec: passive
opsecNote: Reading and dorking public reviews/profiles is passive and invisible to the reviewer. Do not register or reply from an attributable identity if you need to interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, long-running (India-centric) consumer-review site; reviews and profile detail are user-generated self-report, useful as leads.
missingPersonsRelevance: medium
coverage:
- in
auth: none
api: false
localInstall: false
registration: false
aliases:
- MouthShut.com
- mouthshut.com
tags:
- reviews
- social-network
- india
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# MouthShut

> A large consumer-review community (India-centric) — reviewer profiles and review histories can leak a subject's location, purchases, services used and reused handle.

## When to use
You have a `username` or `name` and want a review footprint. On MouthShut, a reviewer profile aggregates a person's reviews of products, businesses and services; those reviews often disclose their city, what they bought/used, local businesses they frequent, and a writing style — useful for placing an Indian subject geographically, recovering a reused handle, or corroborating consumption patterns.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use MouthShut's search, or Google-dork it: `site:mouthshut.com "<username or name>"`.
2. Open the reviewer's profile and read their review history — products/services, dates, and any location or personal detail volunteered.
3. Note reused handles and any linked profiles.
4. Pivot: a reused `username` feeds cross-platform enumeration; a reviewed local business narrows `geolocation`; timestamps date the subject's activity.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (reviewer profile + reviews), reused `username`, disclosed location/purchase detail
- **Empty/negative result looks like:** no profile or dork hits — the handle isn't used here (likely unless the subject is an active reviewer, often India-based).

## Gotchas & OpSec
- India-centric; lower yield for other regions despite the "North America" label in this entry.
- Reviews are self-reported and can be incentivised/fake; corroborate before attributing.
- Passive to read; posting is attributable — sock puppet only.

## Overlaps ("do both")
- Pairs with other review platforms (Google/Trustpilot) and cross-platform username tools — MouthShut adds an India-heavy review angle; those broaden the reviewer footprint.

## Trust & verifiability
`trust: community` — a legitimate large review site; content is user self-report, so treat profile disclosures as leads to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mouthshut-north-america |
| category | search-engines |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
