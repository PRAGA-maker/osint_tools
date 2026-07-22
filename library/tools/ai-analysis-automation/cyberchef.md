---
id: cyberchef
name: CyberChef
description: Use when you have encoded, encrypted, or obfuscated data (Base64, hex, timestamps, ciphers) and want to decode/transform it — returns the decoded plaintext or restructured data.
url: https://gchq.github.io/CyberChef/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building and replaying multi-step decode/transform "recipes" on any text or binary blob you pull out of an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (Apache-2.0); runs entirely client-side and can be self-hosted or run offline.
opsec: passive
opsecNote: All processing happens in your own browser — data is not sent to a server. For sensitive material, download the standalone build and run it offline/air-gapped rather than the public GitHub Pages copy, so nothing leaves your machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and open-sourced by GCHQ; the code is public and processing is local, so output is deterministic and independently verifiable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Cyber Chef
- "the Cyber Swiss Army Knife"
tags:
- decoding
- data-transform
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# CyberChef

> The "Cyber Swiss Army Knife" — a browser-based workbench that chains decode, decrypt, parse and transform operations into repeatable recipes, all client-side.

## When to use
Any time an artifact you've collected is not human-readable: a Base64 or URL-encoded string in a link, a hex blob from a capture, a Unix/Windows timestamp, a ROT/XOR-obfuscated value, an EXIF field, or a JWT. Drop it into CyberChef and stack operations until it becomes intelligible — then save the recipe so you can replay it on similar data later.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gchq.github.io/CyberChef/ (or a local/offline build for sensitive data).
2. Paste the data into the **Input** pane.
3. Search operations (e.g. "From Base64", "Magic", "From Hex", "URL Decode", "JWT Decode") and drag them into the **Recipe** pane in order.
4. Read the transformed **Output**; use the **Magic** operation to auto-detect likely encodings when you're unsure.
5. Save/share the recipe (it encodes into the URL) so the same transform is reproducible; pivot the decoded result (a URL, coordinates, an email) into the relevant selector search.

## Inputs → Outputs
- **In:** any text/binary/hex/Base64 string or file
- **Out:** the decoded/transformed result of the recipe
- **Empty/negative result looks like:** garbage output means the wrong operation order or encoding guess — try **Magic**, or reorder the recipe; CyberChef never "fails," it just faithfully applies whatever you gave it.

## Gotchas & OpSec
- No login, no server round-trip — everything runs locally in the browser.
- For confidential case data, use the downloadable standalone build offline so nothing is even loaded from GitHub Pages.
- It transforms data; it does not fetch or interpret meaning — you still verify what the decoded value represents.

## Overlaps ("do both")
- Complements metadata/EXIF viewers and forensic carving tools — those extract raw fields, CyberChef decodes and reshapes the fields they surface.

## Trust & verifiability
`trust: trusted` — open-sourced by GCHQ with fully local, deterministic processing; anyone can audit the code and reproduce any recipe's output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cyberchef |
