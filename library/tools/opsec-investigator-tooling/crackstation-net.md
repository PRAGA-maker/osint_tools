---
id: crackstation-net
name: CrackStation.net
description: Use when you have an unsalted `password` hash and want the plaintext — returns the original password via massive precomputed lookup tables.
url: https://crackstation.net/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Instantly reversing common unsalted password hashes (MD5, SHA1, NTLM, etc.) to plaintext.
selectorsIn:
- password
selectorsOut:
- password
status: live
pricing: free
costNote: Free web lookup; up to 20 hashes per submission. No account.
opsec: passive
opsecNote: The lookup runs against CrackStation's own tables — you submit a hash, not the target's live account, so it's passive. But you are sending the hash to a third party; don't submit hashes you must keep confidential, and only work with hashes you're authorised to handle.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-standing, well-regarded free service by Defuse Security; results are deterministic table lookups, so a hit is a correct plaintext.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CrackStation
tags:
- opsec-investigator-tooling
- password-cracking
- hashes
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# CrackStation.net

> A free hash-lookup service — paste an unsalted hash and, if it's in the tables, get the plaintext password back in a fraction of a second.

## When to use
You have one or more unsalted `password` hashes (from an authorised assessment, a recovered credential, or a leak you're analysing) and want the plaintext. CrackStation reverses common algorithms (LM, NTLM, MD5, SHA1, SHA-2 family) against 15B+ precomputed entries — a fast first attempt before you spin up a real cracker.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://crackstation.net/.
2. Paste up to 20 hashes, one per line, and solve the CAPTCHA if prompted.
3. Read the results: each hash resolves to its plaintext, or is marked not-found.
4. Pivot: a recovered `password` may reveal a reuse pattern for the subject (feed a wordlist generator like `[[w-generator]]`); a not-found hash is likely salted or uncommon — move to a GPU cracker.

## Inputs → Outputs
- **In:** unsalted `password` hash(es)
- **Out:** the plaintext `password` for any hash in the tables
- **Empty/negative result looks like:** "not found" — the hash is salted, uses an unsupported algorithm, or the password isn't in the lookup tables; it doesn't mean uncrackable, just not by table lookup.

## Gotchas & OpSec
- Only works on UNSALTED hashes — salted hashes will never match.
- You send hashes to a third party; never submit anything confidential or unauthorised.
- Absence of a hit says nothing about password strength beyond "not in these tables".

## Overlaps ("do both")
- Complements offline crackers (hashcat/john) and `[[w-generator]]` — CrackStation is the instant table lookup; escalate to a real cracker for salted/uncommon hashes.

## Trust & verifiability
`trust: trusted` — a reputable, long-lived service; a returned plaintext is verifiable (re-hash it to confirm), so hits are reliable by construction.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crackstation-net |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | password → password |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
