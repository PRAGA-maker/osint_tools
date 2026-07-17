---
id: what-browser-am-i-using-co
name: What browser am I using.co
description: Use when you want a quick check of what your browser reveals — returns the browser name, version, OS, and user-agent a website sees, so you can confirm your investigation browser presents as intended.
url: https://www.whatbrowseramiusing.co/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- browser-tests
bestFor: Confirming the browser/OS/user-agent your setup presents to sites during anonymization checks.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free instant web check; no account or input needed.
opsec: active
opsecNote: The page reads and displays what your browser already exposes to every site (user-agent, version, OS). Run it on YOUR OWN setup as a self-check; it reveals nothing new to the wider world, but do it in the same profile/VPN you'll investigate from so the result reflects your real posture.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple, single-purpose detection page; it reports standard, easily-cross-checked browser data, so its output is trivially verifiable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- dns-leak-tests
aliases:
- whatbrowseramiusing.co
- what browser am I using
tags:
- opsec
- browser-test
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# What browser am I using.co

> A one-glance page that echoes back the browser name, version, OS, and user-agent a website sees from you — a quick sanity check on what your investigation browser is broadcasting.

## When to use
During anonymization setup, when you want to confirm your research browser presents the identity you intend — the expected user-agent, browser version, and OS — rather than leaking your real daily-driver signature. It's a fast self-check to verify a spoofed user-agent took effect, or simply to see the baseline string sites receive. It protects the investigator, not a subject (low missing-persons relevance), and is a first, shallow layer — not a full fingerprint audit.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the exact browser profile / VPN session you'll investigate from, open https://www.whatbrowseramiusing.co/.
2. Read the reported browser name, version, operating system, and full user-agent string.
3. Compare against what you intend to present — e.g. confirm a spoofed UA or a hardened profile shows the expected values, not your personal setup.
4. If it reveals something identifying or unexpected, adjust (UA override, correct profile) and re-check.
5. Follow up with deeper leak/fingerprint tests before relying on the setup.

## Inputs → Outputs
- **In:** none — it reads your current browser automatically
- **Out:** your browser name, version, OS, and user-agent as seen by websites
- **Empty/negative result looks like:** N/A — it always reports something; the "bad" outcome is it showing an identity you didn't intend (your real browser/OS when you meant to mask it).

## Gotchas & OpSec
- **Shallow check:** user-agent is only one signal. A matching UA does NOT mean you're unfingerprintable — canvas, fonts, WebGL, screen size, and IP all still identify you.
- A spoofed UA that's inconsistent with other signals can itself be a red flag; harden holistically, don't just change the string.
- OpSec: run it in the real investigation profile; it exposes nothing new externally but only tells the truth about the session you run it in.

## Overlaps ("do both")
- Pairs with [[dns-leak-tests]] and a full fingerprinting audit (e.g. Cover Your Tracks / AmIUnique) — this checks the UA/browser string, those check IP/DNS leakage and the overall fingerprint.

## Trust & verifiability
`trust: community` — a trivial single-purpose page reporting standard browser data you can cross-check in any other UA tester or dev-tools; its output is easy to verify and hard to get wrong.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | what-browser-am-i-using-co |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
