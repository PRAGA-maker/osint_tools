---
id: network-analyzer-investigation-tool-app-mobile-ios
name: Network Analyzer Investigation Tool App (Mobile – iOS)
description: Use when you have a `domain` or `ip-address` and only a phone to hand — runs ping, traceroute, whois, DNS, and port scans from iOS, returning resolved IPs, hosting, and open-port intel.
url: https://itunes.apple.com/ca/app/network-analyzer-ping-traceroute/id557405467?mt=8
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: On-the-go network reconnaissance from an iPhone — resolving a domain, tracing its route, WHOIS, DNS records, and scanning ports without a laptop.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
status: live
pricing: freemium
costNote: Free version does ping/traceroute/basic lookups with ads; a paid Pro upgrade unlocks port scanning, Wi-Fi device discovery, and removes ads.
opsec: active
opsecNote: Ping, traceroute, and especially port scanning send packets directly to the target host — these appear in the target's logs and originate from your device's IP. Route the scans through a VPN/sock-puppet connection, and never port-scan infrastructure you aren't authorized to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: community
trustNote: Popular, long-standing iOS network utility (Techet's "Network Analyzer"); the diagnostics are standard TCP/IP tools, so results are as trustworthy as the underlying protocols.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Network Analyzer
- Network Analyzer Pro
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- network-recon
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Network Analyzer Investigation Tool App (Mobile – iOS)

> A pocket network-recon kit for iOS — ping, traceroute, WHOIS, DNS, and port scanning against a domain or IP, when all you have is your phone.

## When to use
You're away from a workstation but need to profile a network target: resolve a `domain` to its `ip-address`, see the hops between you and it, pull WHOIS/DNS records, or check which ports are open on a host. Useful for quick field triage of a suspicious server, or auditing the Wi-Fi network you're on. It duplicates desktop CLI tools (`dig`, `traceroute`, `nmap`) in a touch UI.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install "Network Analyzer" from the iOS App Store (the linked iTunes URL now resolves to the App Store listing).
2. Enter the target `domain` or `ip-address` in the lookup/tools tab.
3. Run the relevant tool:
   - **DNS/WHOIS** → registrar, name servers, record types, resolved IPs (`ip-address`).
   - **Ping / traceroute** → reachability and the network path/hops to the host.
   - **Port scan** (Pro) → open TCP ports and detected services on the target.
   - **Wi-Fi / LAN scan** → devices, IPs, and vendors on your current network.
4. Pivot resolved IPs and hosting details into WHOIS/passive-DNS and IP-geolocation tools for attribution.

## Inputs → Outputs
- **In:** `domain` or `ip-address` (or the local network you're joined to)
- **Out:** resolved `ip-address`, `domain`/DNS records, route hops, open ports, WHOIS
- **Empty/negative result looks like:** "host unreachable" / no DNS record / all ports filtered — the host may be down, firewalled, or blocking ICMP; a filtered scan is not proof nothing is running.

## Gotchas & OpSec
- Ping/traceroute/**port scans are active** and log your device IP on the target — scan only what you're authorized to, and tunnel through a VPN/sock-puppet connection.
- Port scanning is a Pro (paid) feature; basic lookups are free-with-ads.
- Mobile-carrier NAT and firewalls can distort traceroute hops and block ICMP, producing incomplete paths.
- App-Store links and app names drift over time; confirm you've installed the genuine Techet "Network Analyzer" before trusting output.

## Overlaps ("do both")
- Mirrors desktop network tools — use this in the field for a first look, then re-run the same domain/IP through fuller desktop WHOIS/DNS/passive-DNS tooling for depth and logging you can archive.

## Trust & verifiability
`trust: community` — a well-regarded consumer utility wrapping standard protocols; results are reliable, but interpret filtered/blocked responses carefully rather than as definitive absence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | network-analyzer-investigation-tool-app-mobile-ios |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | no |
