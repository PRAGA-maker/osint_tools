---
id: webrtc-leak-test
name: WebRTC Leak Test (Perfect Privacy)
description: Use when you want to confirm your VPN isn't leaking your real IP via WebRTC — returns the IP addresses WebRTC exposes to any website, so you can verify your OpSec.
url: https://www.perfect-privacy.com/en/tests/webrtc-leaktest
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: A focused check that WebRTC doesn't bypass your VPN and reveal your true IP address.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free public test page from VPN provider Perfect Privacy; no account needed.
opsec: active
opsecNote: Tests YOUR browser, not a target. Run it from the sock-puppet/VPN profile you investigate from. A leak here means any site you visit — including a target's server — could log your real IP; fix before doing active recon.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Provided by an established VPN vendor as a free diagnostic; the result is your browser's actual WebRTC behaviour, directly verifiable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- browser-leaks
- perfect-privacy
- dnsleaktest
aliases:
- Perfect Privacy WebRTC leak test
tags:
- opsec
- webrtc
- vpn
- privacy
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# WebRTC Leak Test (Perfect Privacy)

> A single-purpose diagnostic that shows which IP addresses your browser's WebRTC stack exposes — the classic way a real IP leaks straight past an otherwise-working VPN.

## When to use
WebRTC can reveal your true local and public IP to any website even when your VPN is connected and every other check looks clean — a notorious blind spot. Before any **active** OSINT from a sock-puppet setup, run this to confirm WebRTC only shows your VPN IP (or nothing), so a target's server can't quietly log your real address. It's an investigator self-check, not a lookup on anyone else.

## How to use it (`bestInteractionPattern`: web-manual)
1. Connect your VPN and open your investigative browser profile.
2. Go to https://www.perfect-privacy.com/en/tests/webrtc-leaktest.
3. Read the IP addresses WebRTC reports. If your real public IP (or your ISP's) appears alongside/instead of the VPN IP, WebRTC is leaking.
4. If leaking: disable WebRTC (browser flag or an extension like uBlock Origin's "Prevent WebRTC from leaking local IP"), reconnect, and re-test until only the VPN IP shows.
5. Re-run after any VPN/browser/extension change.

## Inputs → Outputs
- **In:** `ip-address` (your own browser under test)
- **Out:** the `ip-address`(es) WebRTC exposes to websites
- **Empty/negative result looks like:** only your VPN IP (or no public IP) shown — that is the pass state; seeing your real ISP IP is the failure you must fix.

## Gotchas & OpSec
- A green result on other leak tests does NOT imply WebRTC is safe — this vector is separate; test it explicitly.
- Some browsers reintroduce WebRTC leaks after updates or new extensions; treat it as a recurring check.
- Returns nothing about a target — this is purely investigator OpSec.

## Overlaps ("do both")
- Pairs with `[[browser-leaks]]` (full fingerprint + multi-vector suite) and `[[dnsleaktest]]` — confirm the same "no real-IP leak" conclusion across more than one tester before trusting your setup.

## Trust & verifiability
`trust: trusted` — a free diagnostic from an established VPN provider; the output is your own browser's real WebRTC behaviour, instantly reproducible after a fix.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webrtc-leak-test |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
