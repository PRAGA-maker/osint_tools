---
id: ransomware-darknet-websites
name: Ransomware Darknet websites
description: Use when you're tracking ransomware activity and need a starting index of gang leak-site `.onion` addresses — a clearnet blog list pointing to darknet extortion/leak portals.
url: https://sizeof.cat/post/ransomware-darknet-websites/
category: dark-web
path:
- dark-web
bestFor: A clearnet-readable, curated list of ransomware group darknet leak/extortion sites as an entry point for tracking victims and gang activity.
selectorsIn: []
selectorsOut:
- domain
status: live
pricing: free
costNote: Free clearnet blog post; no account to read.
opsec: active
opsecNote: Reading the clearnet list is passive, but its purpose is to send you to ransomware leak portals on Tor — a hostile, monitored environment. Visit any onion link only from a hardened Tor Browser on an isolated VM under a sock-puppet identity, and never log in or download from these sites casually.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A personal security blog's curated list; useful as a snapshot, but ransomware onion addresses rotate constantly as sites are seized or move, so treat entries as time-stamped leads to re-verify.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- onions-darknetlive
aliases:
- ransomware leak sites list
tags:
- dark-web
- ransomware
- onion-directory
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Ransomware Darknet websites

> A clearnet blog post that indexes ransomware gangs' darknet leak/extortion portals — a readable starting point before you enter Tor to track a group's victims.

## When to use
You're investigating ransomware — a breach, an extortion claim, a victim organisation, or a specific gang — and need current `.onion` entry points to the groups' **leak sites** (where they name victims and dump stolen data). This list collects them in one clearnet page so you can orient before switching to Tor. Relevant for cyber-incident and threat-intel work; leak sites occasionally expose stolen personal data pertinent to wider investigations.

## How to use it (`bestInteractionPattern`: web-manual)
1. From the clearnet, read https://sizeof.cat/post/ransomware-darknet-websites/ to get the list of gangs and their leak-site `.onion` addresses.
2. Note the group you care about and its onion address; **cross-check the address** against a second darknet index before trusting it (phishing clones are common).
3. To visit, switch to a **hardened Tor Browser on an isolated VM** under a sock-puppet identity and paste the verified address.
4. Treat the leak portal as hostile and monitored: capture what you need (victim names, post dates, sample data claims) and leave; don't log in or download recklessly.
5. Corroborate any victim/data claim with independent reporting before relying on it.

## Inputs → Outputs
- **In:** a ransomware group/incident you're researching
- **Out:** leak-site `.onion` `domain` links (entry points), and downstream, victim names/leak metadata inside the sites
- **Empty/negative result looks like:** the gang isn't listed, or its address is stale/dead — the group is defunct, rebranded, or moved; find a current address from an actively maintained tracker.

## Gotchas & OpSec
- **It's a snapshot** — ransomware onion addresses change fast; verify each against a live, maintained source before connecting.
- **Phishing risk:** clones of leak sites exist; confirm addresses across multiple indexes.
- Visiting is active and legally/operationally sensitive; do it only with proper Tor isolation and authorization.
- Assume every leak portal is monitored by law enforcement and the gang alike.

## Overlaps ("do both")
- Pairs with [[onions-darknetlive]] and dedicated ransomware trackers (e.g. ransomwatch-style feeds) — cross-referencing multiple sources is the standard defence against stale/phished addresses and gives fresher coverage than any single blog snapshot.

## Trust & verifiability
`trust: community` — a curated personal-blog list; valuable as an orientation snapshot, but always re-verify onion addresses against actively maintained trackers before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ransomware-darknet-websites |
| category | dark-web |
| selectorsIn → selectorsOut |  → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (manual-review) |
