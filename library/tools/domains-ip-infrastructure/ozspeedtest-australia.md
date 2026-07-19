---
id: ozspeedtest-australia
name: OzSpeedTest (Australia)
description: Use when you want your own connection's `ip-address` and a broadband speed test from Australian servers — primarily a speed test with a basic "what's my IP" tool; limited OSINT value.
url: http://www.ozspeedtest.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Testing your own internet connection speed against AU/NZ/UK/US servers; a bundled tool also shows your current public IP.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free speed test and IP tool; optional account for saving results.
opsec: passive
opsecNote: The speed test reveals YOUR connection's public IP and location to the test servers — it does not query a target. If you run it, it profiles your own egress, so use it only from research infrastructure you're happy to expose, never as a target lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running Australian broadband speed-test and news site; reliable for its stated purpose but not a person/infrastructure intelligence source.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Oz Broadband Speed Test
tags:
- toddington
- speed-test
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# OzSpeedTest (Australia)

> An Australian broadband speed-test site — mostly for checking your own connection; its only OSINT-adjacent feature is a basic "what is my IP" readout.

## When to use
Rarely, in OSINT terms. Reach for it only to (a) confirm the public `ip-address` and rough location your own research connection presents (an opsec self-check), or (b) test throughput from a research box against AU/NZ/UK/US servers. It does **not** look up a target's IP, domain, or infrastructure — it measures *your* connection.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.ozspeedtest.com from the connection you want to check.
2. For opsec: read the detected IP/location panel to see what your egress exposes.
3. To test speed: run the test against a chosen server; results show download/upload/latency.
4. Pivot: if the displayed IP isn't the one you expect (VPN leak), fix your setup before doing sensitive work elsewhere.

## Inputs → Outputs
- **In:** your own connection (no target selector; optionally your public `ip-address` is auto-detected)
- **Out:** your public `ip-address`, approximate geolocation, and speed metrics
- **Empty/negative result looks like:** N/A — it always reports on the current connection; a failed test means a network/server issue, not a data result.

## Gotchas & OpSec
- **Not a target-lookup tool.** For a target's IP/domain intel, use a WHOIS/IP-geolocation service instead.
- Running it exposes your own egress IP/location to a third party — treat it as a self-diagnostic only.
- Human-in-the-loop: none. OpSec: passive toward others, but it profiles you.

## Overlaps ("do both")
- For an opsec IP self-check it overlaps with any "what's my IP" service; for actual target infrastructure OSINT use a dedicated WHOIS/IP tool — this is not that.

## Trust & verifiability
`trust: community` — dependable for speed testing; not an authority on anyone's identity or infrastructure, so it contributes essentially no evidentiary value to a case.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ozspeedtest-australia |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
