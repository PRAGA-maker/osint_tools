---
id: perfect-privacy
name: Perfect Privacy Check-IP
description: Use when you are about to run an operation and want to confirm your own connection isn't leaking — returns your visible `ip-address`, DNS servers, WebRTC status and a fingerprint summary.
url: https://www.perfect-privacy.com/check-ip/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Pre-operation self-check that your VPN/proxy hides your real IP and isn't leaking via DNS or WebRTC.
selectorsIn: []
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free leak-check page provided by the Perfect Privacy VPN service; no account needed to run the test.
opsec: active
opsecNote: This is a self-directed check — you point it at your OWN connection, not a target. It necessarily sends your current IP/DNS/browser data to a third-party VPN provider's server, so run it only as an anonymization test and be aware Perfect Privacy sees that request. Never run it while logged into anything attributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Hosted by Perfect Privacy, a commercial VPN vendor; the leak-check itself is a standard, verifiable browser test, though it's a vendor page (cross-check with an independent leak tester).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- webrtc-leak-test
aliases:
- Perfect Privacy IP check
- perfect-privacy check-ip
tags:
- opsec
- vpn-test
- leak-check
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# Perfect Privacy Check-IP

> An investigator self-check: does my VPN actually hide me, and am I leaking via DNS or WebRTC — run this before touching a target.

## When to use
Before any active step in an investigation (visiting a target's site, logging into a sock puppet, probing infrastructure), you verify your own anonymization is intact. This page shows what a remote server sees about you — visible IP, DNS resolvers, WebRTC-exposed addresses, and browser fingerprint — so you catch a leak before it deanonymizes you, not after. It's opsec hygiene, not a target-lookup tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Connect through your operational VPN/proxy and open a clean browser profile.
2. Go to https://www.perfect-privacy.com/check-ip/.
3. Read the results: does the visible `ip-address` match your VPN exit (not your real ISP)? Are DNS servers your VPN's? Is WebRTC exposing a local/real IP?
4. If anything shows your real IP/ISP/location, stop — fix the leak (disable WebRTC, force VPN DNS) and re-test.
5. Only proceed to the operation once the check is clean; re-run after any network change.

## Inputs → Outputs
- **In:** none — it inspects your own live connection
- **Out:** your visible `ip-address`, DNS servers, WebRTC status, fingerprint summary
- **Empty/negative result looks like:** if it shows your real ISP IP or home geolocation, your anonymization is FAILING — that "result" is the warning to act on.

## Gotchas & OpSec
- Self-directed only: this is about protecting the investigator; it returns nothing about a subject.
- Vendor page: it's a VPN company's own tester — cross-check with an independent leak-test tool so you're not trusting one source.
- WebRTC and DNS leaks are the usual culprits even behind a VPN — this is exactly what to watch.
- Run it through the same browser/profile you'll operate from, or the result doesn't reflect your real footprint.

## Overlaps ("do both")
- Pairs with [[webrtc-leak-test]] and other IP/DNS leak checkers — run at least two independent testers before an operation so a single tool's blind spot doesn't give false confidence.

## Trust & verifiability
`trust: unverified` — the underlying browser checks are standard and self-verifiable, but it's a commercial VPN vendor's page; corroborate the result with an independent leak tester before trusting your anonymity to it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | perfect-privacy |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → ip-address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
