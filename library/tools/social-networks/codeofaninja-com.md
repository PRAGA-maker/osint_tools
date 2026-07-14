---
id: codeofaninja-com
name: Find TikTok ID (codeofaninja.com)
description: Use when you have a TikTok `username` and want its stable numeric user ID (`document-id`) — returns the account's permanent ID for use across rename-proof lookups and APIs.
url: https://www.codeofaninja.com/tools/find-tiktok-id/
category: social-networks
path:
- social-networks
bestFor: Converting a TikTok @username into the account's permanent numeric user ID, which survives handle changes and feeds other TikTok tooling.
selectorsIn:
- username
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free web tool; no account or payment.
opsec: passive
opsecNote: The tool queries TikTok's public data for the handle, not the person; the subject is not notified. The site sees the username you enter — use a sock-puppet browser for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small free developer utility that reads TikTok's public account data; the numeric ID it returns is a factual platform value, but the third-party page can break when TikTok changes its APIs.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- here-19
- pixelatomy-com
aliases:
- codeofaninja.com find tiktok id
- TikTok ID finder
tags:
- tiktok
- TikTok Related Sites
- id-resolution
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Find TikTok ID (codeofaninja.com)

> A one-field converter: a TikTok @username in, the account's permanent numeric user ID out — the anchor you need to track someone across handle changes.

## When to use
You have a TikTok `username` and need its stable numeric user ID because: the handle might change (the ID won't), other TikTok OSINT tools/APIs key on the numeric ID, or you want to confirm two handles are (or aren't) the same underlying account. The username is cosmetic; the ID is the durable identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.codeofaninja.com/tools/find-tiktok-id/.
2. Enter the TikTok username without the `@`.
3. Click "Get TikTok ID" and read the returned numeric ID.
4. Pivot: feed the numeric ID into TikTok scrapers/APIs and monitoring tools; re-check it later against a suspected new handle to prove continuity.

## Inputs → Outputs
- **In:** TikTok `username` (no `@`)
- **Out:** the account's permanent numeric user ID (`document-id`)
- **Empty/negative result looks like:** an error or blank ID — the username doesn't exist, is private/banned, or TikTok changed its endpoint and broke the tool; try again or use an alternative ID finder.

## Gotchas & OpSec
- Third-party tools that read TikTok's private-ish endpoints break periodically — a failure may mean the tool is stale, not that the account is gone.
- Confirm the resolved ID belongs to the right person before treating a later handle match as identity continuity.
- OpSec: passive — no interaction with the target account.

## Overlaps ("do both")
- Pairs with `[[here-19]]` (the X equivalent: ID↔handle) and `[[pixelatomy-com]]` (Discord snowflake decoding) — all three exploit that platforms key identity on permanent IDs, not mutable handles.

## Trust & verifiability
`trust: community` — a small free utility returning a factual platform ID; reliable when it works, but verify against a second source if the ID is load-bearing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | codeofaninja-com |
