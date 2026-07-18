---
id: social-media-fingerprint
name: Social Media Fingerprint
description: Use when you want to verify your own OpSec — checks in-browser which social networks you are logged into, so you can confirm an investigation profile is isolated — returns `social-profile` (your own session exposure).
url: https://robinlinus.github.io/socialmedia-leak/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- privacy-clean-up
bestFor: Confirming an OSINT browser profile leaks no logged-in personal social sessions before you use it.
selectorsIn: []
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free open-source demo page hosted on GitHub Pages; nothing to install.
opsec: active
opsecNote: This is a self-check, not a tool to point at a subject. It uses login-detection (cross-site redirect timing) to reveal which networks THIS browser is logged into — run it in the profile you plan to investigate from, to confirm it is not carrying your personal sessions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known proof-of-concept by Robin Linus demonstrating the social-media login-leak technique; open-source and static, but detection accuracy drifts as platforms patch the trick.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- socialmedia-leak
- Robin Linus social media leak
tags:
- opsec
- browser-fingerprint
- self-check
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Social Media Fingerprint

> A one-click self-audit: it detects which social networks the current browser is silently logged into — use it to prove your investigation profile is clean before you touch a target.

## When to use
This is an OpSec hygiene check for the investigator, not a lookup on a subject. Before working a case from a "sock puppet" or dedicated OSINT browser profile, load this page in that profile: it tells you whether that browser is still carrying live sessions to Facebook, Twitter/X, Google, etc. A leak means the profile is not properly compartmentalised and could attribute your activity to your real identity. Run it whenever you set up or reset an investigation browser.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the exact browser profile you plan to investigate from, open https://robinlinus.github.io/socialmedia-leak/.
2. Let it run — no input needed; it probes login state via cross-site redirect/timing behaviour.
3. Read the list of platforms flagged as "logged in."
4. If any personal network shows as logged in, that profile is contaminated: log out / clear it / use a fresh container before doing OSINT.
5. Re-run after clearing to confirm the profile is clean.

## Inputs → Outputs
- **In:** none (it inspects the current browser's own session state)
- **Out:** `social-profile` exposure — the set of networks this browser is logged into (about *you*, not a target)
- **Empty/negative result looks like:** nothing detected as logged in — good, the profile appears isolated (though absence can also mean a platform patched the detection, so don't treat "clean" as absolute proof).

## Gotchas & OpSec
- Human-in-the-loop: none.
- This does NOT fingerprint a subject — pointing it at a target does nothing; it only reads the browser running it.
- Detection is a moving target: platforms periodically break the login-leak technique, so a "clean" result is reassurance, not a guarantee — still use separate profiles/VMs.

## Overlaps ("do both")
- Pairs with browser-compartmentalisation practice (containers, dedicated VMs, sock-puppet accounts) — this verifies that hygiene held; the practice is what actually keeps you isolated.

## Trust & verifiability
`trust: community` — a respected open-source proof-of-concept; the code is inspectable and static, but treat its results as an indicator whose accuracy erodes as platforms patch, not a certified audit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-media-fingerprint |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
