---
id: i2p-invisible-internet-project
name: I2P - Invisible Internet Project
description: Use when an investigation touches I2P "eepsites"/services and you need to access or understand this anonymity network — the client software for reaching I2P-hosted content.
url: https://i2p.net/en/
category: dark-web
path:
- dark-web
bestFor: Accessing and understanding I2P-hosted anonymous services (eepsites, messaging) as an investigator.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source, volunteer-run anonymity network; you install the router software locally.
opsec: active
opsecNote: Running an I2P router participates in the network and routes others' traffic; joining is observable at the network level (your ISP can see I2P activity). Use on a dedicated/isolated machine, ideally over a VPN, and never mix I2P persona activity with attributable accounts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Mature (20+ years), open-source, volunteer-maintained anonymity project; the software is reputable, though content reached through it is not.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- I2P
- Invisible Internet Project
tags:
- dark-web
- anonymity
- overlay-network
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- i2p-anonymous-network
---

# I2P - Invisible Internet Project

> An anonymous overlay network (like Tor's hidden services, different design) — the client you install to reach I2P "eepsites" and services during dark-web investigations.

## When to use
Your investigation references I2P — an eepsite address (`.i2p`), an I2P-hosted forum/market, or a subject known to use it — and you need to access that content or understand the network. I2P routes traffic through layered encryption across volunteer routers, hiding user IPs and hosting locations. It's investigator plumbing for reaching I2P-only content, not a search tool itself.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install the I2P router from https://i2p.net/ (or use i2pd) on a dedicated/isolated machine.
2. Configure your browser to use I2P's proxy; wait for the router to integrate into the network.
3. Navigate to `.i2p` eepsite addresses you've obtained from other intelligence.
4. Pivot: content, handles, and `crypto-wallet`/contact details found on I2P feed the rest of your workflow — archive carefully and never deanonymise via careless clearnet leaks.

## Inputs → Outputs
- **In:** an I2P eepsite address / service you already know about (no selector input)
- **Out:** access to that I2P-hosted content (no automated selector output)
- **Empty/negative result looks like:** an eepsite that won't resolve/load — the service is offline, the address is stale, or your router hasn't finished integrating.

## Gotchas & OpSec
- Running a router participates in routing and is visible as I2P traffic to your ISP — isolate the machine and consider a VPN.
- I2P is a separate network from Tor; `.onion` addresses won't work here and vice versa.
- Discovery is hard — I2P has no central index; you need addresses from prior intelligence.

## Overlaps ("do both")
- Complements Tor and dark-web indexes — different network, different content; investigate both when a subject's footprint could span them.

## Trust & verifiability
`trust: trusted` — the I2P software is a long-standing, open-source, reputable project; that trust is in the tool, not in any content you reach through it, which must be verified independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | i2p-invisible-internet-project |
| category | dark-web |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
