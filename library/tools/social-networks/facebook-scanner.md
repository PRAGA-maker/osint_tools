---
id: facebook-scanner
name: Facebook Scanner (StalkScan)
description: Use when older guides point you to StalkScan for Facebook Graph Search — but it is defunct; returns nothing and you should route to a live workaround instead.
url: https://stalkscan.com
category: social-networks
path:
- social-networks
bestFor: Historical reference only — Facebook Graph Search-style querying of a profile's public interactions (no longer functional).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- associate
status: down
pricing: free
costNote: Was free while it existed; the domain no longer serves a working tool.
opsec: passive
opsecNote: The tool is dead, so there is nothing to query. Do not enter targets into any clone or mirror claiming to be StalkScan — several parked/imitation domains harvest whatever you type. Treat any "StalkScan" prompt that asks for a login or token as hostile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Originally a legitimate tool by researcher Inti De Ceukelaire, but it broke permanently when Facebook killed Graph Search in June 2019; the domain today is not a maintained tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- who-posted-what
- intelligence-x
aliases:
- StalkScan
- stalkscan.com
tags:
- facebook
- defunct
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Facebook Scanner (StalkScan)

> A once-popular Facebook Graph Search front-end that is now dead — kept here so an agent recognises the name and routes to a working alternative instead of wasting a step.

## When to use
Effectively never, as a live tool. You will still see "StalkScan" recommended in older OSINT lists (MetaOSINT and others) as a way to enumerate a Facebook profile's public likes, photos, tagged posts and friends. That capability relied on Facebook Graph Search, which Facebook retired in June 2019. StalkScan's author patched it repeatedly, but Facebook crippled each patch within hours, and the tool has not worked since. Recognise the reference, then pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Do **not** rely on stalkscan.com — it no longer returns Graph Search results, and lookalike domains may be malicious.
2. If you need equivalent Facebook enumeration, hand-build Graph Search-style URLs or use a maintained workaround (e.g. Who Posted What, manual `facebook.com/search` filters).
3. For a profile's numeric ID (still the durable pivot even without Graph Search), use a bulk Facebook ID finder, then work the ID against Facebook's remaining search surfaces.

## Inputs → Outputs
- **In:** `username` / `name` / profile URL (historically)
- **Out:** nothing today; historically `social-profile`, `image`, `associate` links via Graph Search
- **Empty/negative result looks like:** the site failing to load, redirecting, or returning an error/parked page — which is the expected state, not a temporary outage.

## Gotchas & OpSec
- This entry is a tombstone: `status: down`. Don't spend a step trying to make it work.
- Beware imitations: parked or cloned "StalkScan" pages that ask you to log in or paste a token are credential/data harvesters. Never authenticate.

## Overlaps ("do both")
- Replace with `[[who-posted-what]]` for time-bounded Facebook keyword search, and `[[intelligence-x]]` for archived/leaked social content — both are maintained where StalkScan is not.

## Trust & verifiability
`trust: unverified` — the original was a reputable researcher's project, but the domain today serves no maintained tool, so any current content there cannot be trusted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-scanner |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
