---
id: jondonym
name: JonDonym IP-Check
description: Use when you want to audit your investigative connection's anonymity — returns your exposed IP, headers, cookies, and fingerprint with an anonymity assessment.
url: https://ip-check.info/?lang=en
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: A thorough anonymity/privacy audit of your current browser and connection (IP, headers, DNS, cookies, JS fingerprint).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free anonymity-test service (from the JonDonym project) at ip-check.info; the test tool lives at tools.ip-check.info. No account.
opsec: active
opsecNote: This is a self-test of YOUR connection, not a lookup on a target — but it deliberately exposes and reports your real network/browser data to their server during the check. Run it only on the VPN/Tor/sock-puppet setup you want to verify, before touching a target; never run it on your real identity's browser and assume privacy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-standing, detailed anonymity-test tool from the JonDonym (JonDos) privacy project; widely used to verify anonymization, though the JonDonym mix service itself has wound down.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ipcheck
- panopticlick
aliases:
- ip-check.info
- JonDos IP Check
tags:
- opsec
- anonymity-test
- vpn-test
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# JonDonym IP-Check

> A deep anonymity-audit page — point your investigative browser at it to see exactly what your connection leaks (IP, headers, DNS, cookies, fingerprint) and how anonymous you really are.

## When to use
Defensive OpSec tooling. Before running an investigation through a VPN, Tor, or a sock-puppet setup, use IP-Check to verify the anonymization actually holds — that your real IP, DNS, or a distinctive fingerprint isn't leaking. It's more detailed than a simple "what's my IP" page, covering browser headers, cookies, JavaScript, and more. Run it whenever you set up or change an anonymized browsing profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the check in the exact browser/connection you'll operate from (test page: tools.ip-check.info).
2. Let it run — no input needed; it probes your connection and browser automatically.
3. Read the report: exposed IP and geolocation, DNS, browser headers, cookie/JS status, and fingerprint elements, with an anonymity assessment.
4. Fix leaks (e.g. DNS leak, WebRTC, unique fingerprint) and re-test until clean.
5. Pivot: a verified-anonymous profile is the safe base from which to run every other tool in your workflow.

## Inputs → Outputs
- **In:** none (audits the connection/browser you visit with)
- **Out:** your exposed IP/geo, headers, DNS, cookies, and fingerprint, plus an anonymity assessment
- **Empty/negative result looks like:** N/A — it always returns a report; a "bad" outcome is a leak (real IP/DNS exposed, unique fingerprint) that means you must harden before operating.

## Gotchas & OpSec
- It tests the browser/connection you use — test the real op profile, not your daily setup.
- The JonDonym mix service has largely wound down, but this test page remains a useful audit tool.
- One clean test isn't permanent — extensions/updates/network changes can reintroduce leaks; re-test.

## Overlaps ("do both")
- Pairs with `[[panopticlick]]` (Cover Your Tracks) — IP-Check focuses on network/connection leaks; Cover Your Tracks focuses on fingerprint uniqueness; run both for full coverage.

## Trust & verifiability
`trust: trusted` — a reputable, detailed anonymity-test tool from a privacy project; the diagnostics are authoritative for auditing your own exposure.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jondonym |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
