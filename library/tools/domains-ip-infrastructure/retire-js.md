---
id: retire-js
name: Retire.js
description: Use when you have a `domain`/web app and want to fingerprint the JavaScript libraries it loads and flag known-vulnerable versions — returns metadata-exif (tech stack) and domain leads.
url: https://chrome.google.com/webstore/detail/retirejs/moibopkbhjceeedibkbkbchbjnkadmom/related
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Detecting which JavaScript libraries (and vulnerable versions) a website uses, via a browser extension or CLI.
selectorsIn:
- domain
selectorsOut:
- metadata-exif
- domain
status: live
pricing: free
costNote: Free and open source. Available as a Chrome/Firefox extension, an npm CLI, a Burp/ZAP plugin, and a Grunt task.
opsec: passive
opsecNote: The extension inspects JavaScript your browser already loaded from normally visiting the site — no extra probing of the target, so it's as passive as an ordinary visit. Still, that visit reaches the target's server from your IP; use a sock-puppet browser/VPN if the visit itself must not be attributed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Well-established open-source project (RetireJS) maintained against a public vulnerability database; widely used in appsec.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Retire.js
- RetireJS
tags:
- Domain/IP/Links
- Source Code Analyzes
- tech-fingerprint
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Retire.js

> A vulnerability scanner for front-end JavaScript — as you browse a site it tells you which JS libraries and versions load, and flags those with known CVEs.

## When to use
You're profiling a `domain`/web application tied to a subject or organization and want to fingerprint its technology: which JavaScript libraries and exact versions it ships, and whether any are known-vulnerable. The library set is a tech-stack signature useful for correlating sites (same unusual stack → possibly same builder) and for understanding what a target runs. It's a web-recon/appsec tool; the OSINT value is the fingerprint, not exploiting the flaws.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Retire.js extension (Chrome/Firefox) — or use the CLI (`npm i -g retire`) for scripted scans.
2. Browse to the target site in a sock-puppet browser; the extension icon flags detected vulnerable libraries.
3. Open the extension to list each detected library, its version, and any known vulnerabilities.
4. For batch/offline use, run `retire --js --outputpath report.json` against downloaded assets or via the CLI on a URL.
5. Pivot: an unusual library/version combo → compare against other suspected sites (shared stack); the fingerprint → tech-profiling of the org.

## Inputs → Outputs
- **In:** a `domain`/web app you visit (or downloaded JS for the CLI)
- **Out:** list of JS libraries + versions loaded and known-vulnerable ones (`metadata-exif`-style tech fingerprint), plus the asset URLs (`domain`)
- **Empty/negative result looks like:** no libraries flagged — the site uses only current/untracked libraries or heavily bundled/minified code the scanner can't fingerprint; empty ≠ proof the stack is unknown or safe.

## Gotchas & OpSec
- Only sees client-side JS it can identify — bundled/obfuscated code and server-side tech are invisible.
- It reports *known* vulnerabilities from its database; absence isn't proof of security.
- OpSec: passive beyond a normal site visit — but that visit still touches the target; sock-puppet it.

## Overlaps ("do both")
- Pairs with Wappalyzer/BuiltWith (broader tech fingerprint) and `[[secretfinder]]` (secrets/endpoints in JS) — Retire.js focuses on library versions/vulns; the others round out the stack picture.

## Trust & verifiability
`trust: trusted` — mature, widely-used open-source appsec tool backed by a public vulnerability database; findings are reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | retire-js |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → metadata-exif, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
