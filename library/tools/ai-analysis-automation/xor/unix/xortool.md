---
id: xortool
name: xortool
description: Use when you have a file or blob you suspect is XOR-encrypted and want to recover the repeating key and plaintext — returns candidate key length(s), the likely key, and decoded output.
url: https://github.com/hellman/xortool
category: ai-analysis-automation
path:
- ai-analysis-automation
- xor
- unix
bestFor: Recovering repeating (multi-byte) XOR keys and plaintext from encoded files.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source (MIT); install via pip (`pip install xortool`).
opsec: passive
opsecNote: Runs entirely locally on data you already hold — no network calls, nothing leaves your machine. Safe for sensitive artefacts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Long-standing, widely used CTF/forensics utility by hellman; mature and stable, though a niche tool rather than an audited product.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- hellman/xortool
tags:
- crypto
- xor
- ctf
- file-analysis
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# xortool

> A command-line analyzer that guesses the length and value of a repeating XOR key and decrypts the file — the go-to for "this looks XOR-obfuscated."

## When to use
You have recovered a file, config blob, or payload (from a device dump, a scraped artefact, a piece of malware, a CTF challenge) whose bytes look scrambled and you suspect a repeating (multi-byte) XOR cipher. xortool automates the classic attack: estimate the key length by character-frequency/coincidence analysis, then recover the most probable key and produce the plaintext. In an investigation it is a decoding utility, not a person-lookup — it turns an unreadable artefact into readable content you can then mine for selectors.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install xortool` (Python 3).
2. Run against the file to estimate key length:
   ```bash
   xortool suspicious.bin
   ```
   It prints the most probable key lengths ranked by confidence.
3. Recover with a chosen length and an expected most-frequent plaintext byte (often `00` for binaries or a space `20` for text):
   ```bash
   xortool -l 8 -c 00 suspicious.bin
   ```
4. Read decrypted candidates from the `xortool_out/` directory it creates; the correct key yields readable output.
5. Pivot: scan the recovered plaintext for `email`, `username`, `ip-address`, URLs, or credentials, and feed those into the relevant lookup tools.

## Inputs → Outputs
- **In:** a XOR-encoded file or byte blob (no person-selector)
- **Out:** ranked candidate key length(s), the likely key, and decrypted output files
- **Empty/negative result looks like:** no clear key length stands out, or every decrypt is still garbage — the data is probably not simple repeating-XOR (could be single-byte, rolling/stream, or a real cipher); switch approach rather than forcing a length.

## Gotchas & OpSec
- Human-in-the-loop: none, but you often iterate — try the top 2–3 suggested key lengths and different `-c` most-frequent-byte guesses.
- OpSec: **passive** — fully local, no network; safe to run on confidential evidence.
- Only handles *repeating-key* XOR. Single-byte XOR, XOR with a moving key, or actual encryption will not yield to it.

## Overlaps ("do both")
- Pairs with a general analysis workbench like `[[cyberchef]]` — CyberChef is great for quick single-byte XOR and chained operations in a GUI, while xortool is stronger at automatically *finding* an unknown multi-byte key length on larger files.

## Trust & verifiability
`trust: community` — a mature, widely used open-source tool (hellman/xortool) common in CTF and forensics; results are deterministic and locally verifiable (you can see whether the decrypt is readable), so trust rests on your own confirmation of the output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xortool |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
