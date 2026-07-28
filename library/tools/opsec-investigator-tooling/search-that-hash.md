---
id: search-that-hash
name: Search-That-Hash
description: Use when you have a `password` hash and want it identified and cracked — returns the hash type and, where crackable, the plaintext `password` via online lookup or Hashcat.
url: https://github.com/HashPals/Search-That-Hash
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Auto-identifying a hash type and attempting recovery across online cracking sites, falling back to local Hashcat.
selectorsIn:
- password
selectorsOut:
- password
status: live
pricing: free
costNote: Free and open-source Python tool; local Hashcat fallback is also free (needs your own hardware).
opsec: active
opsecNote: Online mode submits your hash(es) to third-party cracking sites, so those services see the hashes you're investigating — never submit hashes that are sensitive to the case. Run in offline/Hashcat mode to keep hashes local.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community project by HashPals (1.4k+ stars); it orchestrates Name-That-Hash plus public cracking APIs and Hashcat. Identification is heuristic; a plaintext result is verifiable by re-hashing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- sth
tags:
- Passwords
- hash-cracking
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Search-That-Hash

> A hash identifier + auto-cracker — feed it a hash and it names the algorithm, tries popular online cracking services, and falls back to Hashcat when they come up empty.

## When to use
You've recovered a `password` hash from a breach dump, config file, or database export and want to know what it is and whether it's already cracked. Useful when triaging leaked credentials tied to a subject — a recovered plaintext (often reused) can unlock other accounts. Peripheral to missing-persons work; relevant when working leaked-credential leads.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install search-that-hash` (or `pipx`).
2. Single hash: `sth -t <hash>`; a file of hashes: `sth -f hashes.txt`.
3. It first identifies the type (via Name-That-Hash), then queries online crackers; add options to pipe misses into local Hashcat with a wordlist.
4. Use `--json` for machine-readable output.
5. Pivot: a cracked `password` → test for reuse on the subject's other accounts (never against live services without authorisation).

## Inputs → Outputs
- **In:** `password` hash(es) — single string or file
- **Out:** identified hash type + cracked plaintext `password` where available
- **Empty/negative result looks like:** "not found / not cracked" — the hash is strong, salted, or simply not in any online database. That's expected for good hashing; move to targeted offline cracking or drop the lead.

## Gotchas & OpSec
- Human-in-the-loop: none, though large lists take time and online sources rate-limit.
- OpSec: **active** in online mode — hashes leave your machine for third-party services. Use offline/Hashcat mode for anything sensitive.
- Only ever crack hashes you are authorised to work; verify a plaintext by re-hashing it before trusting it.

## Overlaps ("do both")
- Wraps Name-That-Hash for identification and Hashcat for offline cracking — use those directly when you want fine control; Search-That-Hash is the one-shot convenience layer.

## Trust & verifiability
`trust: community` — an open-source orchestrator; identification is heuristic, but any returned plaintext is trivially verifiable by re-hashing, making positive results self-proving.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-that-hash |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | password → password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
