---
id: xorbruteforcer-py
name: XORBruteForcer.py
description: Use when you have a blob obfuscated with single-byte XOR (malware config, hidden strings) and want it decoded — brute-forces all 256 keys and returns readable candidates.
url: https://github.com/jesparza/scripts/blob/master/xorBruteForcer.py
category: ai-analysis-automation
path:
- ai-analysis-automation
- xor
- python
bestFor: Recovering single-byte XOR-obfuscated content by trying every key and surfacing the readable result.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free single-file Python script (Jose Esparza); no account or install beyond Python.
opsec: passive
opsecNote: Runs entirely locally on a file you already hold — no uploads, no network calls — so it leaks nothing and is safe for sensitive/malware artefacts. Analyse in an isolated VM as good practice when the source is untrusted.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: A small, well-known analyst script from a respected malware researcher (jesparza / pdfstreamdumper author); it does exactly one deterministic thing, easy to read and verify.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- xorBruteForcer
- XOR brute forcer
tags:
- malware-analysis
- deobfuscation
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# XORBruteForcer.py

> The quick answer to "this blob is XOR-obfuscated with one byte" — it tries all 256 keys and shows you which one turns the bytes back into readable content.

## When to use
You're doing file/malware forensics and hit a chunk of data that's been hidden with a single-byte XOR: an obfuscated malware configuration, a hidden URL/IP, or strings scrambled to dodge detection. This script brute-forces every possible key and lets you eyeball the decoded candidates for the one that produces sensible output (readable strings, a URL, a PE header). A niche but genuinely handy deobfuscation step.

## How to use it (`bestInteractionPattern`: cli)
1. Grab `xorBruteForcer.py` from the repo (Python).
2. Run it against the encoded file/byte sequence: `python xorBruteForcer.py <file>`.
3. Review the 256 decoded candidates, each mapped to its key value.
4. Pick the key whose output is meaningful (visible ASCII strings, a known magic number, a URL) — this is a manual judgement step.
5. Pivot: a recovered URL/IP/domain feeds infrastructure OSINT; recovered strings feed further malware/IOC analysis.

## Inputs → Outputs
- **In:** an encoded file or byte sequence (you supply the artefact — no selector)
- **Out:** decoded candidate outputs mapped to each tested XOR key
- **Empty/negative result looks like:** no candidate reads as meaningful — the data likely isn't single-byte XOR (multi-byte/rolling key, different algorithm, or compressed/encrypted); escalate to a broader tool.

## Gotchas & OpSec
- **Single-byte only:** multi-byte or rolling-XOR keys and real encryption won't yield here — recognise when to move on.
- Requires **human review** to spot the right candidate; automate detection with an entropy/known-plaintext heuristic if scaling.
- Local and safe, but treat any decoded IOCs (URLs/IPs) as live and handle malware artefacts in a sandbox.

## Overlaps ("do both")
- Complements richer deobfuscation tooling (e.g. CyberChef's XOR-brute, `xorsearch`) — this is the fast standalone script; use CyberChef when you need multi-byte keys or chained operations.

## Trust & verifiability
`trust: community` — a small, transparent script doing a deterministic transform; you can confirm any result by re-applying the chosen key yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xorbruteforcer-py |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (manual-review) |
