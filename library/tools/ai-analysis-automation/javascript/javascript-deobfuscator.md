---
id: javascript-deobfuscator
name: JavaScript Deobfuscator
description: Use when a page (`domain`) runs obfuscated/minified JavaScript you need to read — this Firefox extension logs the actual code the page executes, exposing hidden URLs, trackers and logic.
url: https://addons.mozilla.org/en-US/firefox/addon/javascript-deobfuscator/
category: ai-analysis-automation
path:
- ai-analysis-automation
- javascript
bestFor: Seeing the real JavaScript a page runs — deobfuscated/unpacked — to expose hidden endpoints, trackers and behavior.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free Firefox extension; no account.
opsec: active
opsecNote: To capture executing code you load the target page in your browser, which runs its scripts (and any trackers/callbacks) against your session — a real, attributable visit. Use a sandboxed/sock-puppet browser and VPN for hostile pages.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Long-standing Firefox extension (by a reputable developer) that logs code passed to eval/Function; auditable and widely used for web analysis.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- view-rendered-source
aliases:
- JavaScript Deobfuscator Firefox addon
tags:
- javascript
- code-analysis
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# JavaScript Deobfuscator

> A Firefox extension that captures the JavaScript a page *actually executes* — including code passed to `eval`/`Function` — so obfuscated, packed or dynamically-generated scripts become readable.

## When to use
You're analyzing a suspicious page on a `domain` whose behavior is buried in obfuscated or minified JavaScript — a phishing kit, a malicious redirect, a skimmer, a tracker you want to understand. Static source view shows the packed blob; this extension logs the deobfuscated code as it runs, revealing the real URLs it calls, the data it exfiltrates, and the logic it hides.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "JavaScript Deobfuscator" from Mozilla Add-ons (Firefox).
2. Open its panel, then load the target page (ideally in a sandboxed/sock-puppet Firefox profile).
3. Let the page run — the extension logs the scripts and dynamically-evaluated code it executes.
4. Read the captured, deobfuscated code for exfil endpoints, hidden `domain`s/URLs, and behavior.
5. Pivot: extracted callback/exfil `domain`s feed infra tooling and a link graph; understood logic informs how the page/kit works.

## Inputs → Outputs
- **In:** a page on a `domain` running obfuscated JS
- **Out:** the deobfuscated/executed JavaScript → hidden `domain`s/URLs, endpoints, and page logic
- **Empty/negative result looks like:** little logged — the page's JS isn't obfuscated/eval-based, or the malicious behavior is gated (only triggers on certain referrers/geos/interaction), so it didn't fire in your session.

## Gotchas & OpSec
- Running a hostile page executes its code against your browser — always use a disposable/sandboxed profile and a VPN; never analyze a live phishing/malware page from your real session.
- Behavior can be conditional (cloaking) and simply not run for you; combine with a sandbox that spoofs referrer/geo.
- OpSec: active — this is a real visit that runs the target's scripts.

## Overlaps ("do both")
- Pairs with `[[view-rendered-source]]` and a network-tab/proxy capture — the rendered-source view shows injected markup, this shows executed code, and a proxy log confirms the outbound calls, together giving the full picture of what the page does.

## Trust & verifiability
`trust: community` — a reputable, auditable Firefox extension; it reports the actual code your browser ran, so the output is trustworthy, with the caveat that you must run it safely (sandboxed).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | javascript-deobfuscator |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
