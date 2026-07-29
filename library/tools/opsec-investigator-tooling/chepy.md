---
id: chepy
name: Chepy
description: Use when you have encoded/encrypted/obfuscated data (a token, a blob, an encoded string) and want to transform it from the command line — a Python/CLI CyberChef equivalent; returns decoded/transformed data.
url: https://github.com/securisec/chepy
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Scriptable, chainable data decoding/encoding/parsing from the terminal or Python — CyberChef without the browser.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (pip install chepy); no account.
opsec: passive
opsecNote: Runs locally on your own machine and transforms data offline — nothing is uploaded, nothing touches any subject. Ideal for handling sensitive artefacts you don't want to paste into a web tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Actively developed open-source project (securisec/chepy, 1k+ stars); inspectable and installable from PyPI, community-maintained.
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
- chepy
tags:
- NOOSINT tools
- data-transformation
- cyberchef
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Chepy

> A local, scriptable CyberChef: decode/encode/parse data by chaining operations in the terminal or a Python script — no browser, no upload.

## When to use
You hit encoded or transformed data during an investigation — a base64/hex/URL-encoded string, a JWT, a magic-header blob, an obfuscated parameter — and want to decode or manipulate it offline and repeatably. Chepy is the CLI/library workhorse for that: it does not find people, it makes recovered artefacts readable so you can extract selectors (emails, URLs, IDs) from them.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install chepy`.
2. Chain operations CyberChef-style, e.g. `chepy "SGVsbG8=" --from_base64 -o` to decode base64.
3. Stack transforms (base64 → gunzip → parse) in one pipeline, on the CLI or via the Python API for automation.
4. Parse file formats (PE/ELF) or apply hashing/crypto operations as needed.
5. Pivot: feed any recovered `email`/URL/`domain`/ID from the decoded output into the matching OSINT tool.

## Inputs → Outputs
- **In:** encoded/encrypted/obfuscated data (not an OSINT selector)
- **Out:** decoded/transformed data (from which you manually extract selectors)
- **Empty/negative result looks like:** an error or unchanged/garbled output — the wrong operation for the data, or the input wasn't actually encoded the way you assumed.

## Gotchas & OpSec
- Local and offline — the right choice for sensitive data you must not upload to a web tool.
- It's a transformation toolkit, not an analyst: you still have to know which operations to chain.
- Being a broad crypto/encoding library, results are only as correct as the recipe you build.

## Overlaps ("do both")
- Fills the automation gap left by browser CyberChef — use CyberChef to prototype a recipe interactively, then reproduce it in Chepy for scripting/bulk.

## Trust & verifiability
`trust: unverified` — open-source and installable from PyPI, so it's inspectable and its transforms are deterministic; community-maintained rather than formally audited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chepy |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
