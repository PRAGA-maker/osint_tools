---
id: firefox-debloat
name: Firefox-debloat
description: Use when you want to harden Firefox for investigative browsing — a curated user.js/policies config that strips telemetry and reduces fingerprinting so your research browser leaks less about you.
url: https://github.com/amq/firefox-debloat
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
bestFor: Hardening a Firefox profile to cut telemetry and reduce fingerprinting for OSINT work.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source configuration files on GitHub; no purchase or account.
opsec: passive
opsecNote: Purely local configuration — nothing is transmitted by applying it. It reduces (never fully eliminates) telemetry and fingerprinting. Apply it to a dedicated investigation profile, not your personal browser, and test the result with a fingerprinting/leak checker.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: An open-source config repo whose changes are human-readable prefs you can audit line by line; it is a personal project, so review it before applying and pin to a known commit.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- dns-leak-tests
aliases:
- firefox-debloat
- amq firefox-debloat
tags:
- opsec
- browser-hardening
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Firefox-debloat

> A curated Firefox hardening config (user.js / policies.json) that turns off telemetry and tightens privacy prefs — a starting point for a lower-fingerprint investigation browser.

## When to use
When you're setting up a dedicated browser profile for OSINT and want to reduce what Firefox reveals about you: disabling Mozilla telemetry, cutting tracking/prefetch, and tightening privacy-relevant preferences. It protects the *investigator*, not a subject, so missing-persons relevance is low but operational value is real — a hardened, consistent research browser leaks less and behaves more predictably. Apply it to a throwaway/investigation profile, not your daily browser.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Open https://github.com/amq/firefox-debloat and read the README and the config contents (know what each pref changes before applying).
2. Create a **separate Firefox profile** for investigations (`firefox -P`), so hardening doesn't disrupt personal browsing.
3. Apply the config: drop the provided `user.js` into that profile's directory, and/or deploy `policies.json` via the distribution/policies mechanism.
4. Restart Firefox and verify prefs took effect (`about:config`, `about:telemetry`).
5. Validate the result with a fingerprinting test and a leak checker (see overlaps) before relying on it.

## Inputs → Outputs
- **In:** none (a configuration you apply to a Firefox profile)
- **Out:** a hardened Firefox instance with reduced telemetry and fingerprinting surface
- **Empty/negative result looks like:** prefs not applied (wrong profile directory, or `user.js` overridden) — confirm via `about:config`. Note that hardening only *reduces* fingerprinting; a test may still show a fairly unique fingerprint.

## Gotchas & OpSec
- Not anonymity by itself: it lowers telemetry/fingerprinting but does not hide your IP — pair with a VPN/Tor and leak testing.
- Aggressive prefs can break sites (logins, media); expect to tune. Consider that a heavily-customized config can itself become a distinctive fingerprint.
- It's a third-party personal repo — audit the prefs and pin to a reviewed commit rather than blindly pulling latest.
- OpSec: **passive** — local config only, nothing transmitted by applying it.

## Overlaps ("do both")
- Pairs with [[dns-leak-tests]] and WebRTC/IP-leak checkers — harden the browser, then verify it actually isn't leaking. For a stronger anti-fingerprinting baseline, compare against a hardened Firefox fork or the Tor Browser.

## Trust & verifiability
`trust: community` — an open-source config of human-readable Firefox preferences you can audit directly; because every change is a visible pref, you can verify exactly what it does before applying.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | firefox-debloat |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
