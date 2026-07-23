---
id: searchonymous
name: Searchonymous
description: Use to search Google without your queries being tied to your logged-in Google account — a Firefox add-on that anonymizes Google search while you stay signed in for other services.
url: https://addons.mozilla.org/en-US/firefox/addon/searchonymous
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Separating your investigative Google searches from your logged-in Google identity/history.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: This is investigator-side opsec: it stops Google from personalizing/logging your searches under your account, reducing filter-bubble bias and the trail your queries leave on your profile. It does NOT hide your IP or make you anonymous to Google at the network level — combine with a VPN/sock-puppet browser for real separation. It's a browser extension, so vet its permissions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A small third-party Firefox add-on; useful and long-listed, but community-made — review its requested permissions before installing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Searchonymous
tags:
- opsec
- search-anonymization
- browser-extension
- toddington
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Searchonymous

> A Firefox add-on that de-links your Google searches from your signed-in Google account — search without personalization or search-history logging, while staying logged in for Gmail/Drive.

## When to use
An opsec utility, not a lookup. Reach for it so your investigative Google queries aren't personalized by (or recorded against) your logged-in Google identity. That matters two ways: it reduces the filter-bubble effect that skews results toward your history, giving you more "neutral" search output, and it keeps your case-related searches out of your account's activity trail. Handy when you must stay logged into Google services but want clean, unlogged searching.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Searchonymous from the Firefox Add-ons page (review the permissions it requests).
2. Stay signed into Google as normal — the add-on strips the account association from Google Search requests automatically.
3. Search Google; results are returned without personalization tied to your account.
4. For true separation from Google, layer this with a VPN/proxy and ideally a dedicated sock-puppet browser profile.

## Inputs → Outputs
- **In:** none (a browser setting; no OSINT selector)
- **Out:** de-personalized, unlogged Google search sessions (an opsec effect, not subject data)
- **Empty/negative result looks like:** not applicable — if searches still look personalized, the add-on may be disabled or Google changed behavior; verify it's active.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: it addresses *account-level* logging/personalization only — it does NOT mask your IP or fingerprint. Google still sees the request at the network level; pair with a VPN/puppet browser for real anonymity.
- It's a third-party extension with browser permissions; vet it and keep it updated, as ad-hoc add-ons can break when Google changes its pages.

## Overlaps ("do both")
- Pairs with a VPN/proxy, a sock-puppet browser profile, and private/containerized windows — Searchonymous handles the Google-account linkage while those handle network- and fingerprint-level separation.

## Trust & verifiability
`trust: unverified` — a small, long-listed community add-on that does a narrow job well. Because it's third-party and depends on Google's page structure, confirm it's active and behaving, and don't mistake it for full anonymity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchonymous |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
