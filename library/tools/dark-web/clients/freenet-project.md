---
id: freenet-project
name: Freenet / Hyphanet
description: Use when an investigation points to content hosted on the Freenet/Hyphanet darknet — returns access to censorship-resistant sites, forums, and files inside the network.
url: https://www.hyphanet.org/
category: dark-web
path:
- dark-web
- clients
bestFor: Accessing and monitoring content published on the Freenet/Hyphanet anonymous peer-to-peer network.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (GPL). No account or payment; you only supply disk and bandwidth to run a node.
opsec: active
opsecNote: Running a Freenet/Hyphanet node makes your machine part of the network — you route and cache other users' (encrypted) data, and your node advertises to peers. Use a dedicated/VM install, never your main machine, and understand you are participating in, not just reading, the network. Opennet mode exposes you to arbitrary strangers; darknet (friend-to-friend) mode is more discreet.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Long-standing open-source project (since 1999, now Hyphanet); the client is legitimate, but content published inside the network is anonymous and unvetted.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Freenet
- Hyphanet
- hyphanet.org
tags:
- darknet
- p2p
- anonymous-network
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Freenet / Hyphanet

> A censorship-resistant peer-to-peer darknet you install as a client — the way to reach content, forums, and "freesites" that exist only inside the Freenet/Hyphanet overlay.

## When to use
A lead (a paste, a forum reference, a `username`, or a freesite key) points to material hosted on Freenet/Hyphanet rather than Tor or the clearnet. Unlike Tor onion services, Freenet content lives distributed across nodes, so you cannot reach it from a normal browser — you must run the client. Use it to read freesites, follow in-network microblogging/forums (e.g. Sone, FMS), and retrieve files that surfaced in your investigation.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the installer for Windows/Linux/macOS/Android from https://www.hyphanet.org/ and install it — preferably in a disposable VM, not your primary system.
2. Launch the node; it opens a local web interface (typically `http://localhost:8888/`).
3. Choose a connection mode: Opennet (connects to strangers automatically) or darknet/friend-to-friend (only trusted peers) — the latter is safer for OpSec.
4. Enter a freesite key (a `USK@`/`SSK@`/`CHK@` URI) to open in-network content, or install plugins (Sone for social, FMS for forums) to browse discussions and handles.
5. Pivot: an in-network `username`/handle or a linked clearnet reference becomes a selector for cross-site username and social-profile checks.

## Inputs → Outputs
- **In:** a freesite key / `username` / in-network reference
- **Out:** access to the referenced `social-profile`, freesite, forum thread, or file
- **Empty/negative result looks like:** a key that never resolves (content not currently held by reachable nodes — Freenet data can expire if unrequested) or a freshly started node that must build peers before it can fetch anything. Neither means the content never existed.

## Gotchas & OpSec
- This is **active**: your node participates in routing and caching encrypted blocks for others. Isolate it (VM/dedicated box) and understand the legal/ethical implications in your jurisdiction.
- Content availability is probabilistic — unpopular data can drop out of the network, so retrieve and preserve anything relevant immediately.
- A new node is slow until it establishes peers; give it time before concluding a key is dead.

## Overlaps ("do both")
- Pairs with Tor/onion tooling and darknet index/search tools — those cover the Tor side of the dark web; Freenet/Hyphanet is a separate overlay they cannot see, so run both when chasing anonymized content.

## Trust & verifiability
`trust: trusted` — the client is a mature, open-source privacy project; the trust rating covers the software, not the anonymous, unverified content it lets you reach, which must be corroborated independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | freenet-project |
| category | dark-web |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | yes (manual-review) |
