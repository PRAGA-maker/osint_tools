---
id: internect-info
name: internect.info
description: Use when you have a Bluesky handle, DID or AT URI and want to resolve it to the underlying AT Protocol identity — returns the stable `social-profile` (DID) and current `name`/handle mapping.
url: https://internect.info/
category: social-networks
path:
- social-networks
bestFor: Resolving Bluesky handles ↔ DIDs (decentralized identifiers) so you can track an account across handle changes and inspect its AT Protocol identity.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free, open-source lookup tool; no account required.
opsec: passive
opsecNote: Resolving a handle/DID queries public AT Protocol / PLC directory data, not the account itself — the target gets no signal. The lookup runs through internect.info's server, which could log queries; use a puppet IP for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source tool by mozzius (a Bluesky app developer); it reads public AT Protocol identity data, so results are as authoritative as the protocol's PLC directory.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- internect
- Bluesky DID lookup
- AT Protocol search
tags:
- bluesky
- bsky
- atproto
- social-networks
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# internect.info

> A Bluesky / AT Protocol identity resolver: turn a handle into its permanent DID (and back), so a handle change can't shake your tracking.

## When to use
You have a Bluesky handle (`username`) or a DID and need the stable identity behind it. On Bluesky the human-readable handle can change, but the DID (`did:plc:...`) is permanent — so resolving handle→DID lets you keep following an account even after it rebrands, and resolving DID→handle recovers the current name of an account you logged earlier. Essential when a subject renames their Bluesky account to evade tracking.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://internect.info/.
2. Enter a Bluesky handle (e.g. `alice.bsky.social`), a DID (`did:plc:...`), or an AT URI.
3. Read the resolved identity: the account's DID, current handle, and associated AT Protocol data (PDS host, identity history where shown).
4. Record the **DID** as the durable identifier — store it, not the handle, so future handle changes don't break your reference.
5. Pivot: DID → view the account on bsky.app and archive its posts; PDS host → infer self-hosting; handle-history → prior names to search elsewhere.

## Inputs → Outputs
- **In:** `username` (Bluesky handle), DID, or AT URI
- **Out:** `social-profile` (the permanent DID + AT identity), `name` (current handle)
- **Empty/negative result looks like:** "not found" / resolution error — the handle may be deleted, mistyped, or never have existed; a DID with no current handle means the account was deleted or renamed.

## Gotchas & OpSec
- The DID is the anchor, not the handle — a subject can change their handle freely, so always capture the DID.
- Feature set is still growing ("more stuff soon"); for deep history you may need a dedicated AT Protocol explorer or PLC directory query.
- OpSec: **passive** — reads public protocol data; no target notification.

## Overlaps ("do both")
- Pairs with bsky.app profile viewing and AT Protocol firehose/archive tools — internect resolves the identity; those pull the content and posting history.
- Feed prior handles into cross-platform username search.

## Trust & verifiability
`trust: community` — a solo open-source tool, but it surfaces authoritative AT Protocol identity data (the DID mapping is protocol-level, not the author's opinion). Cross-check by resolving the same DID in the public PLC directory.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | internect-info |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
