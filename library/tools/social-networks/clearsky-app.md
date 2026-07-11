---
id: clearsky-app
name: clearsky.app
description: Use when you have a Bluesky `username` (handle) and want block relationships, handle-change history, and account metadata — returns social-profile plus associate/name links.
url: https://clearsky.app/
category: social-networks
path:
- social-networks
bestFor: Auditing a Bluesky handle — who blocks it, which block/starter-pack lists it is on, and its handle-change and registration history.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- associate
status: live
pricing: free
costNote: 100% free and anonymous; no login, signup, or payment required.
opsec: passive
opsecNote: Queries hit ClearSky's own index of the public Bluesky (AT Protocol) firehose, not the target's account, so the subject is not notified. You browse without authenticating, so nothing ties the lookup to you — but the site operator sees your IP; use a VPN/sock-puppet browser if the investigation is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent community-run Bluesky analytics site widely referenced in the Bluesky tooling ecosystem; data is derived from the public AT Protocol firehose and is verifiable against Bluesky itself.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bluesky
aliases:
- ClearSky
- clearsky bluesky
tags:
- bluesky
- BlueSky / BSky Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# clearsky.app

> A free Bluesky analytics site that exposes block relationships, handle history, and account metadata for any public handle without logging in.

## When to use
You have a Bluesky `username` (handle, e.g. `alice.bsky.social`) — or a display `name` you can resolve to one — and want to understand the account beyond what its profile shows: who blocks it, which public block-lists and starter-packs include it, when it registered, and every handle it has used before. This is strong corroboration and pivot material when a subject is active on Bluesky: prior handles are new usernames to search elsewhere, and block/list membership reveals `associate` clusters.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://clearsky.app/ in a normal browser (no account needed).
2. Enter the target's Bluesky handle (or DID) into the search box.
3. Read the results:
   - **Blocking data** — how many and which accounts block this handle, and which accounts it blocks.
   - **Lists** — public moderation/block lists and starter-packs the handle appears on.
   - **History** — registration date, prior handles (handle-change history), and moderation labels.
4. Pivot: feed any prior handle back into username tooling ([[username-search-2]], [[sherlock]]-style checks); use blocklist/list co-membership to build an `associate` map; use the registration date to time-bracket the account.

## Inputs → Outputs
- **In:** `username` (Bluesky handle or DID); a `name` first resolved to a handle
- **Out:** `social-profile` (the Bluesky account and its metadata), prior `name`/handles, `associate` links via block-lists and starter-packs
- **Empty/negative result looks like:** "no data" / an unresolved handle — the account may be deleted, never existed, or the handle is mistyped; it does not prove the person is absent from Bluesky under another handle.

## Gotchas & OpSec
- Handle-change history is the highest-value output: an account you found under one handle may have posted for years under another — search both.
- Block counts are relationship signals, not identity; a large block-list membership often just means the account was mass-added, not that each blocker knows the subject.
- OpSec: passive — no notification reaches the subject. Only your IP is exposed to the ClearSky operator.

## Overlaps ("do both")
- Pairs with generic username tools like [[username-search-2]] because ClearSky resolves the Bluesky-specific history (prior handles, blocks) that cross-platform checkers miss, and those tools then spread the discovered handles across other networks.

## Trust & verifiability
`trust: community` — independent, community-maintained analytics built on the public AT Protocol firehose. Findings are checkable directly against Bluesky, so data-quality risk is low, but it is not an official Bluesky service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | clearsky-app |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
