---
id: diceware-generator
name: Diceware Generator
description: Use when you need a strong, memorable passphrase for a sock-puppet account or an encryption key — an OpSec utility that generates EFF/Diceware passphrases client-side; returns a passphrase.
url: https://www.rempe.us/diceware/#eff
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Generating high-entropy Diceware/EFF passphrases in the browser for investigator account hygiene.
selectorsIn: []
selectorsOut:
- password
status: live
pricing: free
costNote: Free and open-source; runs entirely in the browser.
opsec: passive
opsecNote: Generation is client-side using the browser's cryptographic RNG, so the passphrase never leaves your machine. Still, treat any generated secret as sensitive — for maximum assurance run it offline or use the physical dice method for your highest-value keys.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project by Glenn Rempe implementing the EFF/Diceware wordlists; auditable code, but as with any web crypto tool, verify it runs locally (offline) for critical secrets.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- EFF Diceware passphrase generator
- rempe diceware
tags: []
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Diceware Generator

> A client-side EFF/Diceware passphrase generator — an investigator OpSec utility, not a lookup tool. It produces strong, human-memorable passphrases for your own accounts and keys.

## When to use
This is an **operational-security helper**, not an investigative source. Reach for it when you need a strong, unique passphrase for a new sock-puppet account, an encrypted container, or a PGP key. Diceware strings (several random words from a fixed list) are far easier to remember than random characters while offering high entropy. It returns nothing about a subject and has no missing-persons value directly — it just keeps your investigation accounts secure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.rempe.us/diceware/#eff (loads the EFF long wordlist by default; the app may redirect to its current host).
2. Choose the number of words (6+ recommended for account passwords, more for encryption keys).
3. Click generate; copy the passphrase it produces from your browser's secure RNG.
4. For your highest-value secrets, load the page then go offline (or use physical dice + the printed wordlist) so the value is generated with the network disconnected.
5. Store the passphrase in a password manager — never reuse it across sock puppets.

## Inputs → Outputs
- **In:** none (you only choose word count/wordlist)
- **Out:** `password` (a multi-word passphrase)
- **Empty/negative result looks like:** N/A — it always produces a passphrase; a "weak" outcome only happens if you pick too few words, so use 6+.

## Gotchas & OpSec
- Entropy scales with word count — a 4-word passphrase is weak for account use; prefer 6+.
- It's a web page: for critical keys, confirm generation happens client-side (disconnect the network) or use offline dice.
- Purely a security utility; it yields no intelligence on any subject.

## Overlaps ("do both")
- Complements a password manager and any account-creation workflow for building compartmentalized sock-puppet identities; pair with 2FA on those accounts.

## Trust & verifiability
`trust: community` — open-source and auditable, implementing the well-regarded EFF Diceware method; for maximum assurance on high-value secrets, run it offline rather than trusting any live web page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | diceware-generator |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  → password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
