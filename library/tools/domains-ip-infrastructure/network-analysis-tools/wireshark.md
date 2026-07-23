---
id: wireshark
name: Wireshark
description: Use when you have a network-traffic capture (.pcap/.pcapng) and want to extract endpoints, hostnames, and app metadata — returns ip-address, domain, device-id and any cleartext account artifacts.
url: https://www.wireshark.org/download.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- network-analysis-tools
bestFor: Dissecting a captured .pcap to see who talked to whom and what identifiers leaked in cleartext.
selectorsIn:
- ip-address
- device-id
selectorsOut:
- ip-address
- domain
- device-id
- email
status: live
pricing: free
costNote: Free and open-source (GPLv2); no account, no paid tier.
opsec: passive
opsecNote: Reading an existing capture is fully offline and passive. Live-capturing on a network you do not own or are not authorized to monitor can be unlawful interception — only capture traffic you are entitled to see.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Long-standing (since 1998) open-source project maintained by the Wireshark Foundation and audited by vendors and the community.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Ethereal
- tshark
tags:
- pcap
- network-analysis
- forensics
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Wireshark

> The reference packet analyzer: open a capture file and see every host, protocol, and cleartext identifier that crossed the wire.

## When to use
You have a packet capture (`.pcap`/`.pcapng`) — from a seized device, a router, a phone backup, or a malware sandbox — and want to reconstruct which `ip-address`/`domain` a device contacted, pull a `device-id` fingerprint (User-Agent, DHCP hostname, MAC), or recover an `email`/credentials sent in cleartext (HTTP, FTP, POP3, unauthenticated SMTP). This is post-collection forensic analysis of traffic you already lawfully hold — not a way to find a person from a name.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Wireshark from the URL (Windows/macOS/Linux), or use the bundled `tshark` CLI for headless/scripted work.
2. **File → Open** your capture. Do not start a live capture unless you are authorized to sniff that network.
3. **Statistics → Conversations** lists every IP pair and top talkers; **Statistics → Endpoints** gives a host inventory.
4. Apply display filters to isolate identifiers: `http.request` (URLs/hosts), `dns` (queried `domain`s), `dhcp` (device hostnames), `http.user_agent` (`device-id`), `frame contains "password"`.
5. Right-click a packet → **Follow → TCP/HTTP Stream** to read a whole conversation in cleartext.
6. Pivot: a harvested `ip-address` → an IP-geolocation/WHOIS tool; a leaked `domain` → DNS tooling.

## Inputs → Outputs
- **In:** a capture file (`.pcap`/`.pcapng`), optionally an `ip-address`/`device-id` you already know to filter on.
- **Out:** `ip-address`, `domain`, `device-id` (hostnames/User-Agent/MAC) and any cleartext `email`/credentials.
- **Empty/negative result looks like:** an all-TLS capture where payloads are encrypted — you still get endpoint IPs and SNI hostnames but no readable bodies. A truncated capture may show no application-layer data at all.

## Gotchas & OpSec
- Modern traffic is mostly TLS-encrypted: you get metadata (endpoints, SNI, timing) but not message contents without keys.
- Live capture on a network you do not own can be unlawful interception — treat this as an offline analyzer of lawfully obtained captures.
- Large captures are slow; pre-filter with a capture/display filter or split with `editcap`/`tshark`.

## Overlaps ("do both")
- Complements DNS/WHOIS infrastructure tooling: Wireshark surfaces the `domain`s and `ip-address`es actually contacted, which those tools then attribute and enrich.

## Trust & verifiability
`trust: trusted` — first-party open-source software; results are your own deterministic reading of the raw bytes, not a third-party claim.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wireshark |
