---
id: fb-lookup-id
name: FB Lookup ID
description: Use when you have a Facebook profile/page/group `social-profile` URL and want its numeric ID — returns the stable numeric Facebook ID for pivoting and graph-style searches.
url: https://lookup-id.com/
category: social-networks
path:
- social-networks
- facebook
- search
bestFor: Resolving a Facebook vanity/profile URL to its permanent numeric ID for reliable pivoting.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free web tool; no account or payment.
opsec: passive
opsecNote: You paste a public Facebook URL into a third-party resolver; the subject is not contacted and nothing is posted. The site sees the URL you look up; use a sock-puppet browser. Do NOT log into Facebook through this site — it only needs the public URL.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A simple third-party utility that reads Facebook's public data to return the numeric ID; harmless in function, but unaffiliated with Facebook and dependent on Facebook's public exposure of IDs.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- lookup-id.com
- Facebook ID lookup
tags:
- facebook
- graph-search
- id-resolution
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# FB Lookup ID

> Turn a Facebook vanity URL into the account's permanent numeric ID — the stable key that survives username changes and unlocks graph-style pivots.

## When to use
You have a Facebook profile, page, or group `social-profile` URL and need its numeric ID. Vanity handles change and profiles get renamed, but the numeric ID is permanent — it's the reliable anchor for Facebook graph-search techniques (finding photos, tagged posts, connections) and for tracking an account across renames in a missing-person/identity workflow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://lookup-id.com/ in a sock-puppet browser.
2. Paste the target's Facebook profile/page/group URL into the box.
3. Submit — it returns the numeric Facebook ID (a long number).
4. Use the ID for pivots: graph-search URL patterns (`facebook.com/<id>`), photo/tagged-content queries, and matching the same person across handle changes.
5. Pivot: the ID anchors further Facebook OSINT; combine with `[[user-searcher]]`-style handle searches elsewhere and `[[reverse-image-search]]` on the profile photo.

## Inputs → Outputs
- **In:** Facebook profile/page/group `social-profile` URL
- **Out:** the numeric Facebook ID (a stable identifier that resolves back to the `social-profile`)
- **Empty/negative result looks like:** an error or no ID — the URL is wrong, the profile is deleted/blocked, or Facebook isn't exposing the ID for that object. Absence is a tool/visibility issue, not proof the profile is gone.

## Gotchas & OpSec
- Facebook has curtailed much graph-search functionality over the years — a valid numeric ID no longer unlocks everything it once did; treat it as an anchor, not a master key.
- Only needs the **public URL** — never authenticate to Facebook through a third-party ID site.
- OpSec: **passive**; the resolver sees your query. Use a sock puppet.

## Overlaps ("do both")
- Pairs with Facebook graph-search helpers and profile-photo `[[reverse-image-search]]` — the numeric ID is the input those pivots need. Resolve the ID here, then run the graph/photo techniques.

## Trust & verifiability
`trust: unverified` — a minimal unaffiliated utility; the ID it returns is verifiable (it resolves back to the same profile), so confirm by loading `facebook.com/<id>`.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fb-lookup-id |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
