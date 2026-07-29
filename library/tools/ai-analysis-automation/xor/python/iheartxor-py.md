---
id: iheartxor-py
name: iheartxor.py
description: Use when you have a binary/`document-id` with XOR-obfuscated strings and want to recover them — brute-forces single-byte XOR keys within a regex pattern to reveal hidden text.
url: https://hooked-on-mnemonics.blogspot.com/p/iheartxor.html
category: ai-analysis-automation
path:
- ai-analysis-automation
- xor
- python
bestFor: Brute-forcing single-byte XOR-encoded strings out of malware/binary samples during reverse engineering.
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free; the full Python source is published on the author's blog (and mirrored on GitHub/Codepad).
opsec: passive
opsecNote: Runs entirely offline on a local file you already hold — no network activity, nothing about a target leaves your machine. Analyze suspected-malware samples in an isolated VM regardless.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: python-lib
trust: community
trustNote: Written by Alexander Hanel (Hooked on Mnemonics blog), a recognized malware-analysis author; the code is short, open, and auditable.
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
- iheartxor
- iheartxor.py
tags:
- reverse-engineering
- xor
- malware-analysis
- Code
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# iheartxor.py

> A tiny Python utility that brute-forces single-byte XOR encoding to pull hidden strings — URLs, C2 hosts, filenames — out of obfuscated binaries.

## When to use
You are examining a binary, dump, or suspicious file that appears to hide readable strings behind a simple XOR key (a classic malware/obfuscation trick). iheartxor tries every key `0x01`–`0xFF` and reports where a run of valid ASCII appears inside a regex-bounded window, so buried indicators of compromise (domains, paths, addresses) become legible.

## How to use it (`bestInteractionPattern`: python-lib)
1. Grab `iheartxor.py` from the blog post (source is inline; also on Codepad/GitHub mirrors). Requires Python.
2. Run it against your sample:
   - default mode brute-forces keys `0x1`–`0xff` and matches the default regex (data between null bytes).
   - straight mode XORs the whole file with one specified key (`0x0`–`0xff`).
   - supply a custom regex to target a specific string shape (e.g. a URL pattern).
3. Read the console output: hex offset, the key that worked, and the decoded ASCII string.
4. Triage the hits by hand — most keys yield garbage; you are looking for the one that produces coherent, relevant text.
5. Pivot: recovered `domain`s/URLs/paths feed infrastructure and content OSINT downstream.

## Inputs → Outputs
- **In:** a local binary/file (`document-id`) suspected of XOR-obfuscated content
- **Out:** decoded ASCII strings with their offset and XOR key
- **Empty/negative result looks like:** only noise/garbage across all keys — the data is not single-byte-XOR encoded (it may be multi-byte XOR, compressed, or encrypted), so escalate to a heavier tool.

## Gotchas & OpSec
- Human-in-the-loop: results demand manual review — brute force surfaces many false "decodes"; you judge which string is real.
- OpSec: fully offline and passive. Still, run malware samples in an isolated VM.
- Only handles single-byte XOR; multi-byte/rolling keys need a different approach (e.g. XORSearch, floss).
- It is a 2010-era script (v0.01) but the algorithm is timeless; adapt the regex to your target string.

## Overlaps ("do both")
- Complements broader string-deobfuscation tooling (XORSearch, FLOSS): iheartxor is the quick, scriptable single-byte pass; reach for the heavier tools when it comes up empty.

## Trust & verifiability
`trust: community` — short, open, auditable code from a respected malware-analysis author; you can read the whole script before running it and verify each decode against the raw bytes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iheartxor-py |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | yes (manual-review) |
