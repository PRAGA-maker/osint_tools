---
id: i2p
name: I2P
description: Use when you need to reach or research I2P hidden services anonymously — returns access to the I2P overlay network (an anonymity layer, not subject data).
url: https://geti2p.net
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Anonymously accessing I2P "eepsite" hidden services and darknet content outside Tor.
selectorsIn: []
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source; no account.
opsec: active
opsecNote: Investigator-side anonymity. I2P routes your traffic through a peer-to-peer garlic-routed overlay, hiding your real `ip-address` from the hidden service you visit. But by design you also relay other users' traffic, and misconfiguration (or leaving I2P for the clearnet) can deanonymise you — keep it in an isolated VM and never log into attributable accounts over it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Long-running open-source anonymity project (The Invisible Internet Project); the software is auditable and widely studied.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Invisible Internet Project
- geti2p
- eepsite
tags:
- privacy-and-encryption-tools
- anonymity
- darknet
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# I2P

> The Invisible Internet Project — a peer-to-peer anonymity network and darknet, an alternative to Tor for reaching hidden ".i2p" services.

## When to use
An investigation touches content hosted on I2P "eepsites" (`.i2p` addresses) rather than Tor `.onion` sites — some marketplaces, forums, and file shares live only on I2P. You need I2P installed and running to reach and research those services while hiding your real `ip-address`.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the router from https://geti2p.net (Java I2P or the C++ i2pd) and install it, ideally inside an isolated VM.
2. Start the I2P router; give it time to integrate into the network (peer discovery takes a few minutes).
3. Configure your browser to use the I2P HTTP proxy (127.0.0.1:4444) — or use a dedicated profile.
4. Browse `.i2p` eepsites; use the router console's address book / jump services to resolve names.
5. Pivot: `.i2p` service names (`domain`) and content found there feed your case notes; correlate personas across I2P and clearnet cautiously.

## Inputs → Outputs
- **In:** none (a network client) — you supply `.i2p` addresses to visit
- **Out:** access to I2P hidden services (`.i2p` `domain`s and their content)
- **Empty/negative result looks like:** an eepsite that won't resolve or load — I2P services are often intermittent, and an address may be offline rather than blocked.

## Gotchas & OpSec
- Slower and less populated than Tor; expect intermittent, flaky hidden services.
- Running a router means relaying others' traffic — understand the exposure and jurisdiction before participating.
- Do not cross the streams: logging into clearnet accounts or leaking DNS/WebRTC defeats the anonymity — isolate in a VM.
- Different network from Tor — `.onion` sites are not reachable over I2P and vice versa.

## Overlaps ("do both")
- Pairs with Tor/[[tails-live-os]] — cover both darknets: use Tor for `.onion` and I2P for `.i2p`; a target present on one is sometimes present on the other under linked personas.

## Trust & verifiability
`trust: trusted` — a mature, peer-reviewed open-source anonymity network; the client is auditable, though the anonymity guarantee depends entirely on correct configuration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | i2p |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
