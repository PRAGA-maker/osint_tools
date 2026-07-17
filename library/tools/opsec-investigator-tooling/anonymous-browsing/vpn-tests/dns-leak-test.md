---
id: dns-leak-test
name: DNS Leak Test
description: Use when you are behind a VPN/proxy and want to confirm your DNS isn't leaking your real ISP — returns the `ip-address`es and operators of the DNS servers handling your lookups.
url: https://www.dnsleaktest.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Checking that DNS queries route through your VPN and not your real ISP before doing sensitive OSINT.
selectorsIn: []
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free, no account; runs a standard and an extended test in the browser.
opsec: active
opsecNote: This is a self-diagnostic you run on YOUR own connection to verify anonymity — it reveals which DNS servers see your lookups. Run it before investigative work; a leak here means your real ISP/location could be exposed to the sites you visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-standing, widely-referenced VPN self-test; results reflect your own connection and are directly reproducible.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- dnsleaktest.com
- DNS leak check
tags:
- opsec
- vpn-test
- anonymity
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# DNS Leak Test

> A one-click self-check for your own anonymity: it shows which DNS servers are resolving your queries, so you can confirm your VPN is carrying DNS too — and isn't silently leaking to your real ISP.

## When to use
Before (and periodically during) sensitive OSINT, you route through a VPN so target sites see the VPN's exit, not you. But DNS can leak: if your OS still uses your ISP's resolver, the sites and services you look up can be tied back to your real location even with the VPN up. Run this to verify your DNS egress matches your VPN, so your sock-puppet stays clean. This is an investigator **self-protection** tool, not something you point at a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Connect your VPN/proxy as you would for the investigation.
2. Go to https://www.dnsleaktest.com/ and run the **Extended test**.
3. Read the results: each DNS server's `ip-address`, the operator (ISP/hosting), and country.
4. Confirm every listed server belongs to your VPN provider and country — **not** your real ISP or home country. If your ISP appears, you have a leak.
5. Remediate: enable the VPN's DNS/leak protection, set the OS to the VPN's resolvers, disable IPv6 if it bypasses the tunnel, then re-test until clean.

## Inputs → Outputs
- **In:** none (it reads your live connection)
- **Out:** `ip-address`es and operator/country of the DNS servers handling your lookups
- **Empty/negative result (good result) looks like:** only your VPN provider's DNS servers/country appear — no leak. A **bad** result is your real ISP or home country showing up in the list.

## Gotchas & OpSec
- OpSec: **active** self-diagnostic — the point is to expose leaks to *you* before a target could exploit them.
- A pass is point-in-time; re-test after reconnecting, switching networks, or OS updates.
- DNS is only one leak vector — also check WebRTC/IP leaks and IPv6, which this test doesn't cover.

## Overlaps ("do both")
- Pairs with WebRTC/IP-leak and browser-fingerprint checks — together they confirm your whole browsing setup is anonymous, not just DNS.

## Trust & verifiability
`trust: trusted` — a mature, transparent self-test; because it reports your own connection's resolvers, the result is immediately verifiable and reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dns-leak-test |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
