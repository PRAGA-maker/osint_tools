---
id: my-ip-address
name: MyIPAddress.com
description: Use when checking what public IP your own connection exposes (sock-puppet/VPN verification) — returns your current ip-address and coarse geolocation.
url: http://www.myipaddress.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Instantly showing the public IP (and rough geolocation) that YOUR current connection presents to websites.
selectorsIn: []
selectorsOut:
- ip-address
- geolocation
status: live
pricing: free
costNote: Free; no account required.
opsec: passive
opsecNote: This reports YOUR own egress IP, not a target's — an OPSEC self-check. Load it through the exact VPN/proxy you plan to use and confirm it shows the cover exit, not your real IP, before doing any collection.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple "what is my IP" reflector; it just echoes your connection's public IP, so the value is objective (subject to your VPN state).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmybrowser-org
aliases:
- myipaddress.com
- what is my IP
tags:
- ip-check
- opsec
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# MyIPAddress.com

> A one-line "what is my public IP" reflector — mainly an OPSEC self-check that your sock-puppet connection presents the cover IP you intend, not your real one.

## When to use
Before active collection from a sock-puppet, confirm your egress: load this from the operational VPN/proxy and check that the reported `ip-address` (and its coarse `geolocation`) matches your cover exit, not your home network. It's the fastest sanity check that your anonymity routing is actually engaged. It reports **your** IP — it is not a way to look up someone else's.

## How to use it (`bestInteractionPattern`: web-manual)
1. Turn on your operational VPN/proxy and open the sock-puppet browser.
2. Go to http://www.myipaddress.com — it immediately shows the public IP your connection is using.
3. Verify the IP and its rough location are the cover exit, not your real ISP/city.
4. Cross-check for leaks (WebRTC/DNS) with a dedicated leak/fingerprint tester (`[[whatsmybrowser-org]]`).
5. Pivot: a mismatch (real IP showing) → fix the VPN before proceeding; a correct cover IP → safe to continue collection.

## Inputs → Outputs
- **In:** (none — it inspects your own connection)
- **Out:** your current public `ip-address` and its coarse `geolocation`
- **Empty/negative result looks like:** it shows your **real** IP/location — a red flag that your VPN/proxy is off or leaking; remediate before any active work.

## Gotchas & OpSec
- Only shows the headline IP — it does not detect WebRTC/DNS leaks; pair it with a leak/fingerprint tester.
- Self-check only; it tells you nothing about a target.
- OpSec: passive, but the point is to protect your own attribution — always run it through the operational stack.

## Overlaps ("do both")
- Pairs with `[[whatsmybrowser-org]]` and dedicated leak testers — this confirms the exit IP; those confirm the browser fingerprint and catch WebRTC/DNS leaks the IP check misses.

## Trust & verifiability
`trust: community` — a trivial reflector that echoes your connection's public IP; the readout is objective, reflecting exactly what sites see from you.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | my-ip-address |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | (none) → ip-address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
