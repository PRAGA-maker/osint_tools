---
id: online-tools
name: Online Tools (emn178)
description: Use when you have an encoded/hashed string from collected data and want to decode, hash, encrypt or reformat it in the browser — returns the transformed value locally.
url: https://emn178.github.io/online-tools/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Client-side decode/encode/hash/format bench (Base64, hex, JWT, MD5/SHA, JSON) for analysing artefacts.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free static web app hosted on GitHub Pages; no account, no ads.
opsec: passive
opsecNote: Passive and self-contained — the page states operations run client-side (locally in your browser), so pasted data is not transmitted. Still confirm you're on the emn178.github.io origin, and prefer offline copies for the most sensitive material.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running open-source utility collection by emn178 (author of widely-used JS hashing libraries); computations are client-side and inspectable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- emn178 online tools
tags:
- encoding
- hashing
- decoder
- utilities
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Online Tools (emn178)

> A client-side toolbox for decoding, encoding, hashing, encrypting and reformatting strings — Base64, hex, JWT, MD5/SHA, JSON and more, all in the browser.

## When to use
During analysis you hit an opaque value — a Base64 blob in a URL, a JWT from a captured request, an MD5/SHA hash, a hex dump, a URL-encoded parameter, or messy JSON/XML — and want to transform or inspect it quickly without installing anything. It's a support/analysis utility: it processes strings you already have and produces no OSINT selectors of its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://emn178.github.io/online-tools/ and pick the operation (Base64/Base32/Base58, Hex, URL/HTML, JWT, hash algorithms, AES/DES/RC4, GZIP/Brotli, JSON/XML format).
2. Paste your input; the result computes locally as you type.
3. For JWTs, decode the header/payload to read claims (issuer, subject, timestamps) — useful context on a captured token.
4. For hashes, compute a digest to compare against a known value, or reformat/validate JSON to make a payload readable.
5. Pivot: a decoded value (a URL, an email, an ID inside a JWT/Base64 blob) becomes a fresh selector to run through the rest of the library.

## Inputs → Outputs
- **In:** a string/blob you already hold (no OSINT selector)
- **Out:** the decoded/encoded/hashed/formatted value — an analysis aid, not selectors
- **Empty/negative result looks like:** garbled output when you chose the wrong codec/algorithm, or a JWT that won't decode because it isn't actually a JWT — try a different operation.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive/local — operations run client-side, so data isn't uploaded; verify the origin and use an offline copy for top-sensitivity work.
- It transforms, it doesn't crack: hashing is one-way and encryption needs the key — this is not a password/hash-cracking tool.

## Overlaps ("do both")
- Complements local analysis via `[[ollama]]` — use these deterministic codecs for exact transforms, and an LLM for interpreting the decoded content.

## Trust & verifiability
`trust: community` — an established open-source utility whose logic runs in your browser and can be inspected; the transforms are deterministic, so outputs are self-verifying (re-encode to check).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | online-tools |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
