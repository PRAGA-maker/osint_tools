---
id: xorsearch-and-xorstrings
name: XORSearch & XORStrings
description: Use when you have a binary blob or obfuscated file and want to find strings (URLs, IPs, keys, IOCs) hidden behind XOR/ROT/ROL encoding — returns decoded candidate strings and the key.
url: https://blog.didierstevens.com/programs/xorsearch/
category: ai-analysis-automation
path:
- ai-analysis-automation
- xor
- unix
bestFor: Brute-forcing XOR/ROL/ROT/SHIFT encodings in a binary to surface hidden strings and indicators.
selectorsIn: []
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free, open command-line tools by Didier Stevens; download and run locally.
opsec: passive
opsecNote: Runs entirely offline on your own machine — the sample never leaves your host. Ideal for analysing untrusted binaries in an isolated VM; passive toward any third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Authored by Didier Stevens, a well-known SANS ISC handler; these tools are standard, widely-cited malware-analysis utilities.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- pdf-tools
- exiftool
aliases:
- XORSearch
- XORStrings
- Didier Stevens XORSearch
tags:
- malware-analysis
- forensics
- cli
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# XORSearch & XORStrings

> Didier Stevens' offline brute-forcers for XOR/ROL/ROT-encoded content — pull the hidden URL, IP, or key out of a binary that a plain `strings` run misses.

## When to use
You have a suspicious binary, a document with an embedded payload, or any file where meaningful strings appear to be obfuscated (malware routinely XOR-encodes its C2 domains, IPs, and config). XORSearch brute-forces single-byte XOR/ROL/ROT/SHIFT keys hunting for a string you supply; XORStrings surfaces all strings that appear under some XOR/ROL transformation. Together they extract the indicators — `domain`s, `ip-address`es, keys — hidden behind simple encoding.

## How to use it (`bestInteractionPattern`: cli)
1. Download `XORSearch` / `XORStrings` from https://blog.didierstevens.com/programs/xorsearch/ and compile/run them in an isolated analysis VM.
2. To find a known marker: `xorsearch -i sample.bin http` — it tries every XOR/ROL/ROT key and reports which key reveals `http` (a hidden URL) and at what offset.
3. To enumerate hidden strings blindly: `XORStrings sample.bin` — lists strings that emerge under XOR/ROL transformations, with their keys.
4. Note the winning key and offset, then dump the surrounding bytes with that key to read the full decoded string.
5. Pivot: recovered `domain`s/`ip-address`es feed infrastructure lookups (WHOIS, passive DNS, Shodan) and threat-intel enrichment.

## Inputs → Outputs
- **In:** a binary / obfuscated file (not an OSINT selector)
- **Out:** decoded candidate strings and the key/offset that reveals them — often `domain`s and `ip-address`es (C2/IOCs)
- **Empty/negative result looks like:** no key reveals the marker, or XORStrings surfaces only noise — the content isn't single-key XOR-encoded (try a multi-byte key or a different tool).

## Gotchas & OpSec
- Only handles simple single-byte XOR/ROL/ROT/SHIFT; multi-byte keys, RC4, or real crypto need other tools.
- Always run untrusted samples in an isolated/offline VM — these tools read the file but you may be handling live malware.
- OpSec: fully local; nothing is uploaded, which is exactly why it's safe for sensitive samples.

## Overlaps ("do both")
- Pairs with `[[pdf-tools]]` (Stevens' companion suite for malicious PDFs) and `[[exiftool]]` — use pdf-tools/ExifTool to locate the embedded object, then XORSearch to decode obfuscated strings inside it.

## Trust & verifiability
`trust: trusted` — written and maintained by Didier Stevens, a SANS Internet Storm Center handler; the tools are open, standard, and widely cited in malware-analysis literature.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xorsearch-and-xorstrings |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
