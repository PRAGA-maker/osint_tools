---
id: whatismybrowser-com
name: WhatIsMyBrowser.com
description: Use when you need to verify what your own investigation browser leaks — returns your visible user-agent, headers, IP and fingerprint so you can confirm your sock-puppet setup is clean.
url: https://www.whatismybrowser.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- spoof-user-agent
bestFor: Confirming your investigation browser's user-agent, IP and fingerprint before touching a target.
selectorsIn: []
selectorsOut:
- ip-address
- device-id
status: live
pricing: freemium
costNote: Free browser-fingerprint/user-agent self-check; also offers a paid user-agent-parsing API/database for developers (not needed for OpSec self-checks).
opsec: passive
opsecNote: This is an OpSec self-test — you point it at YOUR OWN session, never a target. It shows exactly what a site sees from you (UA, headers, IP, language, fingerprint bits); use it to confirm your sock-puppet browser/VPN isn't leaking a real UA, WebRTC IP or timezone that would attribute you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-established, reputable browser-capabilities reference site; the self-check reflects your actual request, so it is directly verifiable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- What Is My Browser
- whatismybrowser.com
tags:
- opsec
- fingerprint
- user-agent
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- user-agent-parser
---

# WhatIsMyBrowser.com

> An OpSec mirror: it tells you exactly what your investigation browser reveals — user-agent, headers, IP, language, timezone and fingerprint — so you can catch leaks before they attribute you to a target.

## When to use
Before (and periodically during) an operation, to sanity-check your sock-puppet environment. When you're spoofing a user-agent, routing through a VPN/proxy, or using a hardened browser, this confirms the disguise actually holds: does the site see your intended UA or your real one? Does it see the VPN IP or a leaked WebRTC/real IP? Does your timezone/language betray your real location? It's a self-diagnostic, not a target lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. From the exact browser/profile/VPN combination you'll use for the investigation, open https://www.whatismybrowser.com/.
2. Read the headline user-agent and the detailed sections: IP address, headers, language, timezone, and fingerprinting/detection details.
3. Compare against your intended cover: the UA should match your spoof, the IP should be the VPN/proxy exit, timezone/language should fit the persona — fix any mismatch before proceeding.
4. Re-check after changing extensions, VPN nodes or spoof settings. Pivot: once clean, proceed to active tools; if it leaks, remediate (disable WebRTC, align timezone, fix UA) first.

## Inputs → Outputs
- **In:** nothing about a target — it reads your own live session
- **Out:** your visible `ip-address`, user-agent, headers, and `device-id`-style fingerprint signals
- **Empty/negative result looks like:** N/A — it always reports your current session; a "leak" looks like a real UA/IP/timezone showing through your intended disguise.

## Gotchas & OpSec
- Strictly a self-check — never a way to profile someone else.
- Fingerprint coverage is indicative, not exhaustive; pair with dedicated WebRTC-leak and DNS-leak tests for full assurance.
- The paid UA-parsing API is a developer feature, unrelated to OpSec self-checks.

## Overlaps ("do both")
- Pairs with WebRTC/DNS leak testers and IP-geolocation checks — this shows the UA/headers/fingerprint; those catch the specific network-level leaks it may not surface.

## Trust & verifiability
`trust: trusted` — a reputable, long-running reference; the result is literally your own request reflected back, so it's directly verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatismybrowser-com |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → ip-address, device-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
