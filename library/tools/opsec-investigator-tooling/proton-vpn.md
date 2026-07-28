---
id: proton-vpn
name: Proton VPN
description: Use when you need to mask your real IP and location during recon — provides encrypted VPN tunneling with a genuine free tier (investigator OpSec, not a per-subject lookup).
url: https://protonvpn.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A privacy-focused, audited VPN (Swiss, no-logs) with a real free tier for masking investigator IP/location.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Genuine free tier (limited server countries, no ads, no data cap on the free plan's terms); paid plans add servers, speed, Secure Core, and Tor-over-VPN.
opsec: passive
opsecNote: A VPN hides your IP/location from the sites you visit, decoupling recon from your real network. It is NOT anonymity — the provider can technically see your traffic (Proton's audited no-logs policy and Swiss jurisdiction mitigate this), and logging into a personal account still deanonymizes you. For strong anonymity, layer Tor ([[whonix]]).
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Operated by Proton (Switzerland); open-source clients, independent security audits, and a strong no-logs reputation.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
aliases:
- ProtonVPN
tags:
- vpn
- opsec
- privacy
- anonymity
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# Proton VPN

> A reputable, audited VPN with a real free tier — the baseline layer for keeping your investigation traffic off your real IP.

## When to use
You're doing any active-ish recon (visiting a target's site, running lookups that log your IP, operating sock-puppet accounts) and want your real network identity out of the picture. Proton VPN routes your traffic through its servers so destinations see the VPN's IP/location, not yours. It's investigator-side infrastructure, not a lookup tool.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Create a Proton account and install the app (Windows/macOS/Linux/iOS/Android) from https://protonvpn.com.
2. Connect to a server — pick a country/city appropriate to your cover; the free tier limits which countries are available.
3. Verify your apparent IP/location changed (an IP-geolocation check) before starting sensitive work.
4. For higher assurance, use Secure Core (multi-hop) or Tor-over-VPN on paid plans, or combine with [[whonix]].
5. Pivot: Proton VPN is the transport layer — your actual tools run over it.

## Inputs → Outputs
- **In:** N/A — it's a VPN client/service
- **Out:** a masked IP/location for your outbound traffic
- **Empty/negative result looks like:** N/A — validate it's working by confirming your public IP changed and there are no DNS/WebRTC leaks.

## Gotchas & OpSec
- A VPN ≠ anonymity: your account, browser fingerprint, and any logins still identify you. Treat it as IP masking, not a cloak.
- Some sites block or challenge known VPN IP ranges (CAPTCHAs, geoblocks); rotate servers if needed.
- The free tier's country choices are limited — for a specific apparent origin you may need a paid plan.

## Overlaps ("do both")
- Pair with [[whonix]]/Tor when the threat model demands anonymity, not just IP masking — VPN hides you from the destination, Tor hides you from the VPN too.

## Trust & verifiability
`trust: trusted` — an audited, open-source-client, Swiss no-logs provider; among the more credible VPNs, though "no-logs" ultimately rests on the provider's word plus its audits and jurisdiction.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | proton-vpn |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (account-login) |
