---
id: ddecode-php-decoder
name: DDecode - PHP Decoder
description: Use when you have obfuscated PHP (a webshell, malware snippet, or eval/base64 blob) and want readable source — returns deobfuscated PHP text plus any embedded URLs/IPs.
url: https://ddecode.com/phpdecoder/
category: ai-analysis-automation
path:
- ai-analysis-automation
- php
bestFor: Peeling layered eval/base64/gzinflate obfuscation off PHP webshells to reveal what the code actually does.
selectorsIn: []
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free web tool; no account or payment required.
opsec: active
opsecNote: You paste the sample into a third-party server, so the operator sees your submission. Never paste code containing your own secrets, and assume anything you submit could be logged. For untrusted-attacker code this is fine; for sensitive incident material prefer a local deobfuscator instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing free PHP-decoder site used by malware analysts; it mechanically unwraps encodings rather than making judgement calls, so its output is verifiable by re-running.
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
- DDecode
- ddecode.com
tags:
- malware-analysis
- deobfuscation
- php
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# DDecode - PHP Decoder

> A free web decoder that recursively unwraps `eval`/`base64_decode`/`gzinflate`/`str_rot13` layers in obfuscated PHP until it reaches readable source.

## When to use
You have a chunk of obfuscated PHP — a webshell dropped on a compromised site, a malicious plugin, a suspicious snippet from an incident — and want to see what it actually does: what URLs it calls back to, what commands it runs, what it exfiltrates. Attribution-relevant artifacts (C2 `domain`s, `ip-address`es, hardcoded credentials) often surface once the layers are peeled.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the decoder page.
2. Paste the encoded/obfuscated PHP into the input box.
3. Submit; the tool decodes one layer and shows the result.
4. Repeat on the output — it can descend many layers (webshells routinely stack 10–20) until it hits a layer it cannot mechanically unwrap.
5. Read the final cleartext for callback URLs, IPs, filenames, and behavior; extract those as pivots.

## Inputs → Outputs
- **In:** obfuscated/encoded PHP source (pasted text)
- **Out:** decoded PHP source; embedded `url`s, `domain`s, `ip-address`es, and credentials become readable
- **Empty/negative result looks like:** the tool returns the input unchanged or errors — the encoding uses a scheme it doesn't support (custom XOR, runtime-only tricks), meaning you need a sandbox or manual analysis, not that the code is benign.

## Gotchas & OpSec
- Active third-party submission: the operator sees whatever you paste. Only submit attacker/untrusted code; keep your own secrets and sensitive incident data out of it.
- It unwraps encodings; it does not *execute* code, so runtime-generated payloads (built at eval-time from external input) won't fully resolve here.
- Always re-derive any load-bearing indicator (a callback IP) yourself before acting on it.

## Overlaps ("do both")
- Pairs with a live PHP sandbox / local deobfuscator for the layers DDecode can't crack, and with WHOIS/IP tools to run down any callback `domain`/`ip-address` it reveals.

## Trust & verifiability
`trust: community` — an unofficial but widely used analyst tool; because it performs deterministic decoding, you can independently verify any result by decoding the same layer elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ddecode-php-decoder |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | (none) → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
