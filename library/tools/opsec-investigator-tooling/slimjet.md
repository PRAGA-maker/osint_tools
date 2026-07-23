---
id: slimjet
name: Slimjet
description: Use when you want a Chromium-based browser with built-in ad/tracker blocking for OSINT browsing — an alternative sock-puppet environment (no subject selectors in or out).
url: http://www.slimjet.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A privacy-leaning Chromium fork for investigative browsing, with ad/tracker blocking and anti-fingerprinting options built in.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free download (FlashPeak Slimjet) for Windows/macOS/Linux; no account.
opsec: active
opsecNote: Like any browser it is your leak surface. Slimjet's built-in ad/tracker blocking and anti-fingerprinting reduce passive tracking, but it does NOT anonymise your IP — pair it with a VPN/proxy and a compartmentalised profile per case, and don't sign into personal accounts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: A long-running Chromium fork by FlashPeak; reliable as a browser, but a smaller vendor than mainstream browsers — weigh that in your trust model and keep it updated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- chrome
aliases:
- FlashPeak Slimjet
tags:
- browsers
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Slimjet

> A Chromium browser with privacy features baked in — an alternative base for sock-puppet OSINT browsing when you want ad/tracker blocking without bolting on extensions.

## When to use
Not a lookup source — it's an *environment*, like [[chrome]]. Reach for Slimjet when you want a Chromium-compatible browser (runs Chrome extensions) that ships with ad blocking, tracker/fingerprint resistance, and download tools already on, to use as a compartmentalised research browser. Useful as a second, separate browser identity distinct from your everyday one.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Slimjet from http://www.slimjet.com and install; it accepts Chrome Web Store extensions.
2. Create a **dedicated per-case profile** and do not sign it into any personal account.
3. Enable/verify its privacy features (ad block, anti-fingerprint) and add OSINT extensions as needed.
4. Route it through a VPN/proxy — the browser's tracker blocking does not hide your IP.
5. Tear down or reset the profile between cases to avoid cross-contamination.

## Inputs → Outputs
- **In:** none (browsing environment)
- **Out:** none as selectors — provides the compartmentalised browser other tools run in
- **Empty/negative result looks like:** N/A; the failure mode is an identity/IP leak from misconfiguration, not an empty query.

## Gotchas & OpSec
- Blocking trackers ≠ anonymity — you still need a VPN/proxy for IP separation.
- Smaller vendor than Chrome/Firefox; keep it patched and weigh supply-chain trust.
- Being Chromium-based, it inherits Chrome-extension compatibility (a plus) and some Chromium fingerprint traits (a minus).

## Overlaps ("do both")
- An alternative to [[chrome]] for the same job — pick one as your research browser; the value of Slimjet is the built-in privacy defaults, but the compartmentalisation discipline is identical either way.

## Trust & verifiability
`trust: community` — a mature third-party Chromium fork; dependable as software, though its investigative value is purely as a controllable browsing environment, not a data source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slimjet |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
