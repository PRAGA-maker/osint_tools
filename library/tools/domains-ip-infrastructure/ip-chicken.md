---
id: ip-chicken
name: IP Chicken
description: Use when you need to confirm your own exit `ip-address` — returns the public IP and hostname your traffic currently presents.
url: https://www.ipchicken.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A quick "what is my public IP" self-check to verify your VPN/proxy exit before an operation.
selectorsIn: []
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free, no account.
opsec: passive
opsecNote: This is an OpSec self-check, not a lookup on any target — it reports YOUR current public IP/hostname. Use it to confirm your VPN/proxy/Tor exit is what you expect before doing attributable work; the site sees your IP (that's the point).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing simple "what's my IP" page; it accurately reports the requesting IP, which is trivially verifiable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ipchicken.com
- what is my IP
tags:
- toddington
- curated-directory
- opsec
- ip-check
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# IP Chicken

> A dead-simple "what is my public IP" page — used on the investigator's side to confirm the exit IP/hostname your traffic is presenting before you do anything attributable.

## When to use
Not a target lookup — an **OpSec self-check**. Before running active tools or logging into sock-puppet accounts, load IP Chicken to confirm your VPN/proxy/Tor circuit is actually routing you through the exit you intend (and not leaking your real IP). A fast sanity check that your attribution surface is what you think it is.

## How to use it (`bestInteractionPattern`: web-manual)
1. Connect your VPN/proxy/Tor as intended.
2. Open https://www.ipchicken.com.
3. Read the reported public `ip-address` and reverse-DNS hostname.
4. Confirm it matches your intended exit (country/provider) — if it shows your real ISP, your tunnel isn't working; stop and fix it.
5. Pivot: once verified, proceed with the attributable task; re-check after any network change.

## Inputs → Outputs
- **In:** none (it reads your connection)
- **Out:** your current public `ip-address` and hostname
- **Empty/negative result looks like:** it always returns *an* IP — the failure mode is it showing the *wrong* one (your real ISP instead of the tunnel), which means a leak to fix, not an empty result.

## Gotchas & OpSec
- It only reports your **IPv4 web-request IP** — it won't catch DNS/WebRTC/IPv6 leaks; use a dedicated leak-test suite for a thorough pre-op check.
- Confirms the exit IP, not full anonymity — browser fingerprinting and logins can still deanonymise you.
- OpSec: this IS an OpSec tool; the site necessarily sees your IP.

## Overlaps ("do both")
- Pairs with a full anonymity/leak-test suite (DNS/WebRTC/IPv6 checks) and [[the-hitchhiker-s-guide-to-online-anonymity]] — IP Chicken is the 5-second exit-IP glance; the leak suite and guide cover the rest of your OpSec.

## Trust & verifiability
`trust: community` — a trivial, long-standing utility; it reports the requesting IP, which you can cross-verify against any other "what's my IP" service instantly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip-chicken |
