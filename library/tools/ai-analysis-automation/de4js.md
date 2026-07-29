---
id: de4js
name: De4js
description: Use when you have obfuscated/packed JavaScript (from a suspect site, a phishing kit, a scam page) and want to read it — an in-browser deobfuscator that returns human-readable source.
url: https://lelinhtinh.github.io/de4js/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Unpacking and beautifying obfuscated JavaScript so you can read what a page's script actually does.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source, runs entirely client-side in your browser; no account.
opsec: passive
opsecNote: De4js runs in your own browser — the code you paste is not sent to a server, so pasting hostile script is safe from an exfiltration standpoint. It only transforms text; it does NOT execute the script, which is exactly why it's safe for malware analysis.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Open-source community project (lelinhtinh/de4js); inspectable and client-side, but community-maintained with no formal audit.
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
- de4js
tags:
- Code
- javascript-deobfuscation
- malware-analysis
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# De4js

> A safe, client-side JavaScript deobfuscator: paste packed/obfuscated script and get readable source back, without ever running it.

## When to use
You've pulled obfuscated JavaScript from a page tied to your subject — a phishing site, a scam landing page, a suspicious profile widget — and need to understand what it does: where it exfiltrates to, what endpoints/`domain`s it calls, what it hides. De4js unpacks common obfuscators (eval-packing, JSFuck, Obfuscator.io-style, array-string encoding) into human-readable code so you can extract those artefacts. It analyses code, not people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://lelinhtinh.github.io/de4js/ (it may redirect to the maintainer's current mirror — that's the same tool).
2. Paste the obfuscated JavaScript into the input pane.
3. Choose the un-pack method (auto/eval/array/JSFuck/etc.) and run; it beautifies and decodes in-browser.
4. Read the output for embedded URLs, endpoints, keys, or logic; copy artefacts out.
5. Pivot: feed any recovered `domain`/URL/endpoint into infrastructure and reputation tooling.

## Inputs → Outputs
- **In:** obfuscated JavaScript source (not an OSINT selector)
- **Out:** deobfuscated, beautified JavaScript (readable code; extract URLs/domains/strings manually)
- **Empty/negative result looks like:** output nearly identical to input, or garbled — the obfuscation type isn't supported, or the "code" was already plain/minified; try a different method or a dedicated sandbox.

## Gotchas & OpSec
- It **transforms, never executes** — safe for hostile scripts; do not paste it into a live console instead.
- Runs client-side, so pasted code isn't uploaded anywhere — good for sensitive samples.
- Heavily-layered or VM-based obfuscation may only partially unpack; treat de4js as a first pass, not a full reverse-engineering suite.

## Overlaps ("do both")
- Complements a sandbox/network-capture (which shows runtime behaviour) — de4js reveals static intent, a sandbox reveals what it actually calls; do both for a suspect script.

## Trust & verifiability
`trust: unverified` — open-source and fully client-side (you can read the tool's own code), but community-maintained; verify recovered indicators independently before acting on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | de4js |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
