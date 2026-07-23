---
id: lemmeknow
name: LemmeKnow
description: Use when you have an unknown string (a `crypto-wallet`, hash, token, ID) and want to identify what it is — returns candidate types with regex-matched descriptions.
url: https://github.com/swanandx/lemmeknow
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Instantly classifying mystery strings — wallet addresses, API keys, hashes, IDs — pulled from documents, dumps, or messages.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
- ip-address
- document-id
status: live
pricing: free
costNote: Free and open source (MIT). Prebuilt binaries, cargo, Nix, or build-from-source; also runs in-browser via WebAssembly.
opsec: passive
opsecNote: Runs entirely locally against text you supply — no network calls, nothing leaves your machine. Safe to run on sensitive strings offline.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source project by swanandx, a faster Rust reimplementation of the well-known PyWhat identifier; auditable source, active community.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- lemmeknow
- pywhat alternative
tags:
- string-identification
- forensics
- cli
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# LemmeKnow

> "What is this string?" answered in milliseconds: point it at mystery text and it tells you whether it's a Bitcoin address, an API key, a hash, a YouTube channel ID, and more.

## When to use
You've pulled an unidentified string out of a document, a data dump, a chat log, or EXIF/metadata and need to know what it is before you can pivot. LemmeKnow runs a large regex library over the input and returns the likely identity — `crypto-wallet` addresses, hashes, credit-card numbers, IPs, tokens, phone/ID formats, etc. It's a forensic triage/identification helper; direct missing-persons value is low, but classifying an unknown identifier (e.g. spotting a wallet address in a ransom note) can open a new investigative thread.

## How to use it (`bestInteractionPattern`: cli)
1. Install: grab a prebuilt binary from the releases page, or `cargo install lemmeknow` (also available via Nix / WASM for browser use).
2. Run against a string or file:
   ```
   lemmeknow "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
   lemmeknow suspicious_dump.txt
   ```
3. Read the output: each match lists the identified type, a description, and rarity. Use `--json` for machine-readable output to feed a pipeline.
4. Pivot: an identified `crypto-wallet` goes to a blockchain explorer; an identified hash type goes to a hash-lookup/cracking workflow; an identified ID goes to the relevant platform lookup.

## Inputs → Outputs
- **In:** any string or file of strings (`crypto-wallet`, hash, token, ID, `ip-address`, …)
- **Out:** candidate type labels with descriptions — e.g. `crypto-wallet`, `ip-address`, `document-id`
- **Empty/negative result looks like:** no matches returned — the string doesn't fit any known pattern; try `--boundaryless` mode or treat it as free-form/proprietary data.

## Gotchas & OpSec
- It's a *pattern* matcher: a string matching the Bitcoin-address regex isn't guaranteed to be a real, funded wallet — verify downstream.
- Short/common strings can match many patterns (false positives); use the rarity field and context to rank.
- OpSec: fully local and passive — nothing is transmitted, so it's safe on confidential material.

## Overlaps ("do both")
- Directly comparable to PyWhat (LemmeKnow is the faster Rust port) — either identifies strings; run whichever is installed. Feeds downstream lookups (blockchain explorers, hash databases, platform ID resolvers).

## Trust & verifiability
`trust: community` — auditable MIT-licensed source with an active maintainer; because it only classifies by regex, always confirm the identified value with the authoritative service for that type.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lemmeknow |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet, ip-address, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
