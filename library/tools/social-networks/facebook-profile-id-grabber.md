---
id: facebook-profile-id-grabber
name: Facebook Profile Id Grabber
description: Use when you have a Facebook profile (vanity URL or open page) and want its stable numeric profile ID — returns the numeric ID that unlocks graph-search and survives name/URL changes.
url: https://osint.support/chrome-extensions/2019/09/01/facebook-profile-id-grabber.html
category: social-networks
path:
- social-networks
bestFor: Extracting the numeric Facebook profile ID behind a vanity username, for stable tracking and graph-based searches.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free browser extension / method.
opsec: passive
opsecNote: Reading a profile's public numeric ID does not notify the target. However, if you view the profile while logged into a personal Facebook account you risk appearing in "people you may know"/leaving a footprint — use a sock-puppet account and browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Community OSINT technique/extension; it simply reads a value Facebook exposes, so the ID it returns is authoritative — but vet any extension's permissions before installing.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- lookup-id-com
- graph-tips
aliases:
- Facebook Profile ID Grabber
- Facebook numeric ID finder
tags:
- facebook
- facebook-graph
- browser-extension
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Facebook Profile Id Grabber

> A one-click way to get the stable numeric ID behind a Facebook profile — the identifier that survives username/display-name changes and unlocks graph-based searches.

## When to use
You have a Facebook profile (a vanity URL like `facebook.com/zuck`, or an open page) and want its **numeric profile ID**. The numeric ID is the durable key to a person on Facebook: it doesn't change when they rename their vanity URL or display name, it lets you re-find a profile that changed its handle, and it's the input for Facebook graph-search URLs (photos-of, posts-by, places-visited). Getting it is the first step in serious Facebook OSINT.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension (per the osint.support write-up) into a **sock-puppet browser profile** — review its permissions first.
2. Log into a sock-puppet Facebook account and open the target profile.
3. Click the extension (or right-click) to grab and copy the numeric profile ID.
4. Record the numeric ID alongside the current vanity URL and display name.
5. Pivot: feed the ID into graph-search URLs and tools like [[graph-tips]]; if the person later changes their handle, `facebook.com/<numeric-id>` still resolves to them.

## Inputs → Outputs
- **In:** `social-profile` (a Facebook profile URL/page)
- **Out:** `social-profile` — the stable numeric profile ID for that account
- **Empty/negative result looks like:** no ID returned — the profile is unavailable/blocked to your session, or the extension can't read the page (deleted/deactivated account, or you're not able to view it).

## Gotchas & OpSec
- **Vet the extension** before installing — grant it the minimum, and prefer a disposable browser profile; if unsure, use a web method like [[lookup-id-com]] instead.
- Numeric ID is stable; vanity URL and display name are not — always record the ID.
- OpSec: view targets only from a sock-puppet Facebook account to avoid "people you may know" blowback.

## Overlaps ("do both")
- Pairs with [[lookup-id-com]] (a no-install web page that returns the same numeric ID) and [[graph-tips]] (turns the ID into ready-made graph-search queries) — get the ID however is safest, then exploit it.

## Trust & verifiability
`trust: community` — the ID it returns is a value Facebook itself exposes, so it's authoritative; the only caution is extension hygiene (permissions/source), which a web-based alternative sidesteps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-profile-id-grabber |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
