---
id: dns-leak-tests
name: DNS Leak Tests
description: Use when you want to verify your VPN/anonymized setup isn't leaking DNS — returns the DNS resolvers actually answering for you (IPs, provider, country) so you can confirm your real ISP isn't exposed before investigating.
url: https://dnsleak.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Confirming your VPN routes DNS correctly and doesn't leak your real ISP's resolvers.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free browser-based test; no account or install needed.
opsec: active
opsecNote: The test itself issues DNS/HTTP probes that the test infrastructure (and any resolver in your path) logs — that's the mechanism. Run it on YOUR OWN connection as a pre-operation self-check, never against a target. Confirm results before you touch any investigative resource.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: One of several interchangeable DNS-leak checkers; it measures your own configuration and shows raw resolver data, easy to sanity-check against another tester.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- dnsleak.com
- DNS leak test
tags:
- opsec
- vpn
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# DNS Leak Tests

> A pre-operation self-check: confirm that the DNS queries from your machine are going through your VPN/anonymized path and not out via your real ISP's resolvers.

## When to use
Before you begin investigative browsing behind a VPN, Tor, or proxy, run this to make sure your DNS isn't leaking. A "DNS leak" is when your OS resolves hostnames using your ISP's servers instead of the VPN's — which exposes your real location and browsing to your ISP even though your traffic looks tunneled. This tool shows which resolvers actually answered your queries, so you can catch a misconfiguration before it burns your OpSec. It is about protecting the investigator, not about any subject — hence low missing-persons relevance but high operational importance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Connect your VPN/anonymization exactly as you will for the investigation.
2. Open https://dnsleak.com/ and run the (extended/standard) test.
3. Read the resolvers reported — their IPs, providers, and countries.
4. Verify: every resolver should belong to your VPN provider / chosen exit country. If you see your real ISP's name or home country, you have a leak — fix it (enable the VPN's DNS/leak protection, set resolvers manually, kill IPv6) and re-test.
5. Only once clean, proceed to investigative work.

## Inputs → Outputs
- **In:** none to type — it reads your own connection (`ip-address` context)
- **Out:** the list of DNS resolvers answering for you — IPs, provider names, countries (`ip-address`)
- **Empty/negative result looks like:** results showing your real ISP/home country = a leak (bad); results showing only your VPN provider's resolvers = clean (good). A failed/blank test means retry or use another checker.

## Gotchas & OpSec
- A single tester can misreport; confirm a clean result on a second DNS-leak checker before trusting it.
- Also check for WebRTC and IPv6 leaks separately — DNS is only one leak vector.
- OpSec: **active** in that it emits probes, but run **only against your own setup**; it is a self-test, never pointed at a target.

## Overlaps ("do both")
- Pairs with browser-hardening (e.g. [[firefox-debloat]]) and WebRTC/IP-leak testers — DNS-leak testing is one layer of a full pre-op anonymity check.

## Trust & verifiability
`trust: community` — a standard, widely-used leak checker that reports raw resolver data about your own connection; because the output is easy to cross-verify on another tester, its findings are dependable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dns-leak-tests |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
