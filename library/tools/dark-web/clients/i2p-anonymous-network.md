---
id: i2p-anonymous-network
name: I2P (Invisible Internet Project)
description: Use when an investigation points into the I2P darknet — install the router to reach I2P-only "eepsites" and services that Tor and the clearnet can't access.
url: https://i2p.net/
category: dark-web
path:
- dark-web
- clients
bestFor: Accessing I2P-only sites and services (eepsites) to investigate content hosted inside the I2P network.
selectorsIn: []
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source; you run your own I2P router locally, no account or payment.
opsec: passive
opsecNote: I2P's garlic routing anonymizes your connection to in-network services, so you reach eepsites without exposing your IP. Run the router in a hardened/VM environment, never mix it with attributable browsing, and treat any content you reach as potentially hostile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: A long-running, open-source anonymity network (like Tor for in-network services); the software is trusted, though content hosted on I2P is unvetted.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- i2p-invisible-internet-project
aliases:
- I2P
- Invisible Internet Project
- i2p.net
tags:
- dark-web
- anonymity
- i2p
- darknet
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# I2P (Invisible Internet Project)

> An anonymity network optimized for hidden in-network services — the "other darknet" alongside Tor, hosting eepsites and services you can only reach by running an I2P router.

## When to use
Your investigation surfaces an I2P address (a `.i2p` "eepsite" or a base32 destination) — in a forum post, a leak, a ransom note, or a marketplace reference — and you need to actually reach it. Tor and the clearnet can't open I2P destinations; you must run the I2P router locally. It's infrastructure/access, not a search tool: use it to view I2P-hosted content, then analyse what you find with other tools. Low direct person-finding value, but essential when a case leads into I2P.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install the I2P router from https://i2p.net/ (or use I2P+/i2pd) in an isolated/VM environment.
2. Let the router integrate into the network (build tunnels), then configure your browser to use I2P's HTTP proxy (127.0.0.1:4444).
3. Open the `.i2p` eepsite or destination you're investigating; use the router console/address book to resolve names.
4. Pivot: capture content, onion/eepsite links (`domain`), usernames, and wallet addresses found, and feed those into the appropriate selector-specific tools.

## Inputs → Outputs
- **In:** an I2P destination (`.i2p` eepsite or base32 address) you already have
- **Out:** access to the in-network service and any `domain`s/links/content it exposes
- **Empty/negative result looks like:** the eepsite won't resolve or load — I2P sites are frequently offline/ephemeral, or your tunnels haven't built yet; retry after the router warms up rather than assuming the address is fake.

## Gotchas & OpSec
- Human-in-the-loop: none, but there's a real setup step and a warm-up delay before tunnels are usable.
- I2P is separate from Tor — Tor tools and onion addresses don't work here, and vice versa; you need the I2P router specifically.
- Content is unvetted and potentially illegal/malicious; operate in a hardened VM, follow your engagement's legal rules, and never deanonymise yourself by mixing personal browsing.

## Overlaps ("do both")
- Pairs with `[[i2p-invisible-internet-project]]` (same network) and Tor tooling like `[[ahmia]]` — a thorough darknet investigation checks both Tor and I2P, since services choose one network or the other.

## Trust & verifiability
`trust: trusted` — the I2P software is a mature open-source project; the network is authoritative for reaching I2P services, but anything you find hosted there is unverified and must be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | i2p-anonymous-network |
| category | dark-web |
| selectorsIn → selectorsOut |  → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
