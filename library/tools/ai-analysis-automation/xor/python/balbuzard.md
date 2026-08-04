---
id: balbuzard
name: Balbuzard
description: Use when you have a suspicious file and want to pull hidden indicators — returns extracted URLs/`domain`s, IPs, and decoded XOR/obfuscated strings from binaries and documents.
url: https://github.com/decalage2/balbuzard
category: ai-analysis-automation
path:
- ai-analysis-automation
- xor
- python
bestFor: Extracting IoCs and brute-forcing simple obfuscation (XOR/ROL) from malware and suspicious files.
selectorsIn: []
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open source (BSD); a local Python toolkit.
opsec: passive
opsecNote: Runs locally on files you already hold — it does not upload samples to any service, so nothing about your investigation leaves your machine. Still analyse malware inside an isolated VM.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: By Philippe Lagadec (decalage2), the author of oletools; well known in malware analysis. Older Python 2-era tooling, so expect setup friction on modern systems.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- oletools
aliases:
- decalage2/balbuzard
tags:
- malware-analysis
- ioc-extraction
- deobfuscation
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Balbuzard

> A local Python toolkit that scans suspicious files for embedded patterns (URLs, IPs, keywords) and brute-forces simple XOR/ROL obfuscation to reveal what a sample is hiding.

## When to use
You are holding a suspicious file connected to a subject — a malware sample, a booby-trapped document, an encoded artifact — and want to extract its indicators of compromise (the `domain`s/`ip-address`es it contacts) and unmask lightly obfuscated strings. It is a malware-analysis tool; its OSINT value is turning an opaque file into infrastructure leads you can then attribute.

## How to use it (`bestInteractionPattern`: cli)
1. In an isolated analysis VM, install it: `pip install balbuzard` (or clone `https://github.com/decalage2/balbuzard`). Note it is older Python 2-era code — a Python 2 environment or minor fixes may be needed.
2. Run `balbuzard <file>` to scan for embedded URLs, IPs, emails, and known patterns.
3. Run `bbcrack <file>` to brute-force XOR/ROL/ADD transforms and surface strings hidden behind simple obfuscation.
4. Read the extracted IoCs and decoded strings.
5. Pivot: feed extracted `domain`s/`ip-address`es into infrastructure recon (WHOIS, passive DNS, threat intel) to map the operator.

## Inputs → Outputs
- **In:** a suspicious file (binary/document — a code artifact, not a person selector)
- **Out:** `domain`, `ip-address` (extracted IoCs) plus decoded/deobfuscated strings and pattern hits
- **Empty/negative result looks like:** no patterns found and no productive transform — meaning the sample is clean, packed, or uses stronger encryption than bbcrack handles (escalate to a dynamic sandbox).

## Gotchas & OpSec
- Dated (Python 2 heritage): expect environment setup effort; for modern packed malware, pair with a current sandbox/unpacker.
- Local-only and passive by design — no sample leaves your machine — but always detonate/inspect malware in an isolated VM.
- bbcrack only defeats *simple* transforms (XOR/ROL/ADD); real crypto won't yield.

## Overlaps ("do both")
- Pairs with `[[oletools]]` (same author) — oletools dissects Office/OLE document structure and macros while Balbuzard extracts and de-obfuscates the embedded indicators.

## Trust & verifiability
`trust: community` — from a reputable malware-analysis author; extracted IoCs are directly checkable, so verify each `domain`/`ip-address` against independent infrastructure sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | balbuzard |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
