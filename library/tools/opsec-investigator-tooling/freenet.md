---
id: freenet
name: Freenet (Hyphanet)
description: Use when an investigation touches the Freenet/Hyphanet darknet — a peer-to-peer anonymous publishing/file-sharing network — and you need to understand or access it; it's an anonymity network, not a selector lookup.
url: https://freenetproject.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Accessing/understanding the Freenet (Hyphanet) anonymous P2P publishing and filesharing darknet.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (now branded Hyphanet); you run a node yourself on your own hardware.
opsec: active
opsecNote: Running a Freenet/Hyphanet node connects you into a P2P darknet and stores encrypted fragments of others' content on your disk — a meaningful legal/operational exposure. Run it only on an isolated, disposable machine you control, understand your jurisdiction's stance, and never mix it with your real identity. "Opennet" mode reveals your node to strangers; "darknet" mode connects only to trusted peers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: A long-established open-source anonymity project (Freenet, now Hyphanet); the software is genuine, though content on the network is unindexed and unvetted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Hyphanet
- Freenet Project
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Freenet (Hyphanet)

> A peer-to-peer anonymous publishing and filesharing darknet — investigatively, a network you may need to access or understand, not a lookup tool.

## When to use
When a case references content hosted on Freenet/Hyphanet ("freesites", keyindexes, FMS/Sone posts) or a subject is known to use it, and you need to reach or understand that space. Freenet is a distributed, censorship-resistant store where content is addressed by key rather than by server — so it behaves nothing like the clearnet or even Tor onion sites. It produces no selectors itself; it's the environment.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the node software from https://freenetproject.org/ and install it on an **isolated, disposable** machine.
2. Choose a connection mode: "opennet" (auto-connects to strangers, easier but exposes your node) or "darknet" (only trusted friend nodes).
3. Access freesites/indexes through the local node's web interface using known keys (Freenet has no central search; you follow keyindexes).
4. Keep the node walled off from your real identity and mind the legal implications of relaying/storing encrypted fragments.
5. Pivot: content/keys found on Freenet feed your case analysis; identities there are pseudonymous by design.

## Inputs → Outputs
- **In:** none (an anonymity network you join) — content is fetched by key
- **Out:** none as selectors — access to Freenet-hosted content, which is pseudonymous
- **Empty/negative result looks like:** dead keys / unreachable content — Freenet content expires if not re-inserted, so old keys frequently return nothing.

## Gotchas & OpSec
- **Real exposure:** your node stores encrypted fragments of others' data and connects into a darknet — isolate it and understand the legal risk in your jurisdiction.
- **Opennet vs darknet** modes have very different exposure; choose deliberately.
- No search: you need keys/indexes to find anything, and content decays over time.

## Overlaps ("do both")
- A distinct network from Tor/I2P; if a lead spans anonymity networks, cover each separately — content on one is not reachable from the others.

## Trust & verifiability
`trust: trusted` — the software is a genuine, long-standing open-source project; but the network's content is unindexed, pseudonymous, and unvetted, so treat anything found there as an unverified lead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | freenet |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
