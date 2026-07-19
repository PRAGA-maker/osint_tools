---
id: testmy-net-internet-speed-test
name: TestMy.Net Internet Speed Test
description: Use to test your own connection's speed and see the public `ip-address` your egress presents — an independent speed test; minimal target-lookup value.
url: https://testmy.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Benchmarking your own connection and confirming the public IP/ISP your research egress exposes (an opsec self-check).
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free browser-based speed test; optional account to log results over time.
opsec: passive
opsecNote: The test discloses YOUR public IP, ISP, and rough location to TestMy's servers — it profiles your own egress, not a target. Use it to confirm what your VPN/research connection leaks; it cannot look up someone else's IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running independent speed-test service; dependable for bandwidth/your-own-IP, but not an intelligence source about other people.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- speedtest-com
- ozspeedtest-australia
aliases:
- TestMy.net
tags:
- toddington
- speed-test
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# TestMy.Net Internet Speed Test

> An independent browser speed test — mainly for your own connection; its only OSINT-adjacent use is confirming the public IP/ISP your egress presents.

## When to use
Rarely for target work. Use it to (a) verify the public `ip-address`, ISP, and approximate location your research connection/VPN exposes before sensitive work, or (b) benchmark a link's throughput. It measures *your* connection — it cannot look up a target's IP or infrastructure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://testmy.net/ from the connection you want to check.
2. For an opsec check, note the detected IP/ISP/location it reports.
3. Optionally run the download/upload test.
4. Pivot: if the shown IP/location isn't what you expect (a VPN leak), fix it before continuing elsewhere.

## Inputs → Outputs
- **In:** your own connection (auto-detected public `ip-address`)
- **Out:** your public `ip-address`, ISP, approximate location, and speed metrics
- **Empty/negative result looks like:** N/A — it always reports the current connection; a failure is a network issue, not a data result.

## Gotchas & OpSec
- **Not a target-lookup tool** — for a subject's IP/domain intel use a WHOIS/IP-geolocation service.
- Running it discloses your own egress to a third party; treat it as self-diagnostic.
- Human-in-the-loop: none. OpSec: passive toward others; it profiles you.

## Overlaps ("do both")
- Overlaps with `[[speedtest-com]]` and `[[ozspeedtest-australia]]` — all are speed tests with an incidental "your IP" readout; pick one for an egress self-check.

## Trust & verifiability
`trust: community` — reliable for bandwidth/your-own-IP; contributes no evidentiary value about another person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | testmy-net-internet-speed-test |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
