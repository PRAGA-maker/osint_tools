---
id: kahu-revelo
name: Kahu Revelo
description: Use when you have obfuscated JavaScript (from a suspect page/link tied to a subject) and want to read what it really does — returns deobfuscated code and any decoded redirect `domain`s/URLs.
url: https://www.kahusecurity.com/tools.html
category: ai-analysis-automation
path:
- ai-analysis-automation
- javascript
bestFor: Manually deobfuscating malicious/obfuscated JavaScript to reveal hidden redirects and payloads.
selectorsIn: []
selectorsOut:
- domain
status: live
pricing: free
costNote: Free download from Kahu Security; no account or payment.
opsec: active
opsecNote: Revelo can execute and hook the script it is analysing, so run it only inside a disposable Windows VM with no network path to your real environment. If you let it follow live redirects, you touch attacker infrastructure — do that only from an isolated, attributable-to-nobody host.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-standing free malware-analysis utility from Kahu Security; Windows-only GUI tool, widely referenced in JS-deobfuscation tutorials. Tangential to person-finding — a payload-analysis aid.
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
- kahu-converter-utilities
aliases:
- Revelo
- Kahu Security Revelo
tags:
- javascript
- deobfuscation
- malware-analysis
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Kahu Revelo

> A free Windows GUI for unpacking obfuscated JavaScript — beautifier, DOM walker, and built-in firewall/proxy/sniffer — used to reveal where a malicious script actually points.

## When to use
You have obfuscated JavaScript pulled from a suspicious page, phishing link, or malspam sample connected to your subject, and you need to see the hidden behaviour — most importantly the `domain`s/URLs it redirects to. This is a malware-analysis aid; its OSINT value is indirect (turning an opaque script into infrastructure leads), so it sits well outside the core people-finding toolkit.

## How to use it (`bestInteractionPattern`: desktop-app)
1. On a disposable Windows VM (isolated, no route to your real network), download Revelo from https://www.kahusecurity.com/tools.html and run the executable.
2. Paste or load the obfuscated JavaScript into the input pane.
3. Use the built-in beautifier and the deobfuscation methods (eval override, DOM walker, decoders) to progressively unpack the code.
4. Read the decoded output for hidden redirect URLs, dropped-file names, and C2/redirect `domain`s.
5. Pivot: feed extracted domains/IPs into infrastructure-recon tools (WHOIS, passive DNS, threat-intel) to map the operator.

## Inputs → Outputs
- **In:** obfuscated JavaScript source (a code artifact, not a person selector)
- **Out:** `domain` (decoded redirect/C2 hosts) plus readable deobfuscated code and dropped-file indicators
- **Empty/negative result looks like:** code that stays opaque or throws — heavily packed/anti-analysis samples may resist Revelo; that means "needs deeper tooling," not "benign."

## Gotchas & OpSec
- **Windows-only** GUI; no CLI/API despite the automation category.
- **Active/dangerous:** the tool can execute script paths and follow redirects — always sandbox in a throwaway VM and disable live network unless you deliberately want to reach the payload host from an isolated IP.
- Older tool; extremely modern obfuscation may need a current dynamic sandbox in addition.

## Overlaps ("do both")
- Pairs with `[[kahu-converter-utilities]]` — Revelo unpacks the script while the Converter utilities decode the individual encoded strings/blobs you extract.

## Trust & verifiability
`trust: community` — an established free utility from Kahu Security; because it can run untrusted code, treat it as a lab tool and verify any extracted indicator against independent infrastructure sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kahu-revelo |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
