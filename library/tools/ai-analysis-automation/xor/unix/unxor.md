---
id: unxor
name: unxor
description: Use when you have a file XOR-encoded against a known plaintext fragment (e.g. a malware config or obfuscated blob) and want to recover the key and decode it — returns decoded content that may itself contain selectors.
url: https://github.com/tomchop/unxor
category: ai-analysis-automation
path:
- ai-analysis-automation
- xor
- unix
bestFor: Known-plaintext XOR key recovery against malware and obfuscated artifacts.
selectorsIn: []
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free, open-source Python tool on GitHub (tomchop/unxor); no account or payment.
opsec: passive
opsecNote: Runs entirely locally on the command line, so the artifact is never uploaded to a third party — the right choice when the encoded file is sensitive/evidentiary. Analyse malware in an isolated VM.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source utility by a known malware-analysis author (tomchop); small and auditable, but unmaintained-adjacent — read the code before trusting output on important evidence.
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
- tomchop unxor
tags:
- malware-analysis
- decoding
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# unxor

> A local command-line known-plaintext XOR cracker: give it an encoded blob and a string you expect inside it, and it recovers the keystream and decodes the rest.

## When to use
You have a file or blob you believe is XOR-obfuscated (common in malware configs, packed strings, and lightly-hidden data) and you know — or can guess — a fragment of the plaintext it contains (a URL, a header, a known marker). unxor uses that fragment to recover the XOR key and reveal the full content, which may then expose selectors (URLs, emails, IPs, embedded `metadata-exif`) worth pivoting on.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/tomchop/unxor` and set up its Python deps (do this in an isolated analysis VM).
2. Run it against your encoded file, supplying the known-plaintext fragment as the crib.
3. It searches for the key that produces your crib, then applies the recovered keystream to decode the file.
4. Inspect the decoded output for anything actionable — config servers, credentials, embedded identifiers.
5. Pivot: decoded URLs/IPs feed infrastructure OSINT; decoded contact strings feed email/username tooling.

## Inputs → Outputs
- **In:** an XOR-encoded file + a known-plaintext fragment (crib)
- **Out:** recovered key/keystream and decoded content (which may contain `metadata-exif` and other embedded selectors)
- **Empty/negative result looks like:** no key found — usually means the encoding isn't simple XOR, the crib is wrong, or a rolling/multi-byte scheme is in play; try a different crib or a dedicated deobfuscator.

## Gotchas & OpSec
- Only works when you actually have a correct known-plaintext fragment; blind XOR cracking is out of scope.
- It targets classic XOR; multi-layer, rolling, or crypto-grade obfuscation won't yield.
- OpSec: fully local and passive — nothing leaves your machine, ideal for sensitive artifacts. Still, run suspected malware only inside a sandbox/VM.

## Overlaps ("do both")
- Pairs with CyberChef-style multi-tool decoders when the encoding turns out to be layered (base64-over-XOR, etc.) — unxor cracks the XOR layer, a recipe tool handles the rest.

## Trust & verifiability
`trust: community` — it is a small, readable open-source tool from a credible malware-analysis author; verify decoded output independently before treating recovered identifiers as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unxor |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
