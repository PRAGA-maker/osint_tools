---
id: speedtest-com
name: Speedtest.net (Ookla)
description: Use to check your own connection's public `ip-address` and speed from Ookla's global servers — primarily a bandwidth test with an incidental IP/ISP readout; minimal target-lookup value.
url: https://www.speedtest.net
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Measuring your own connection's speed and seeing the public IP/ISP your egress presents (an opsec self-check).
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free web speed test by Ookla; optional account to save history.
opsec: passive
opsecNote: The test exposes YOUR public IP, ISP, and rough location to Ookla and the chosen server — it profiles your own egress, not a target. Use it to confirm what your research connection/VPN leaks; never treat it as a way to look up someone else's IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Ookla Speedtest is the industry-standard bandwidth test; authoritative for speed/your-own-IP, but not an intelligence source about other people.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ookla-speedtest
aliases:
- Speedtest.net
- Ookla Speedtest
tags:
- toddington
- speed-test
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Speedtest.net (Ookla)

> Ookla's ubiquitous bandwidth test — mainly for your own connection; its only OSINT-adjacent use is confirming the public IP/ISP your egress presents.

## When to use
Rarely for target work. Reach for it to (a) verify the public `ip-address`, ISP, and approximate location your own research connection or VPN exposes before doing sensitive work, or (b) benchmark a link's speed. It measures *your* connection — it cannot look up a target's IP or infrastructure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.speedtest.net from the connection you want to check.
2. For an opsec check, read the detected IP/ISP/server-location panel before running.
3. Optionally click "Go" to run the download/upload/latency test.
4. Pivot: if the shown IP/location isn't what you expect (a VPN/proxy leak), fix your setup before continuing elsewhere.

## Inputs → Outputs
- **In:** your own connection (auto-detected public `ip-address`)
- **Out:** your public `ip-address`, ISP, approximate geolocation, and speed metrics
- **Empty/negative result looks like:** N/A — it always reports the current connection; a failure is a network/server issue, not a data result.

## Gotchas & OpSec
- **Not a target-lookup tool** — for a subject's IP/domain intel use a WHOIS/IP-geolocation service.
- Running it discloses your own egress to Ookla; treat it as self-diagnostic.
- Human-in-the-loop: none. OpSec: passive toward others; it profiles you.

## Overlaps ("do both")
- For an IP self-check it overlaps with any "what's my IP" service; for real infrastructure OSINT use dedicated WHOIS/IP tools — this is not that.

## Trust & verifiability
`trust: trusted` — authoritative for bandwidth and your own connection details; contributes no evidentiary value about another person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | speedtest-com |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
