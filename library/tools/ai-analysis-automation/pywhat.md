---
id: pywhat
name: pywhat
description: Use when you have an unknown string or file and want to identify what the artifacts in it are — returns typed identifications (emails, hashes, `crypto-wallet` addresses, IPs, API keys, and more).
url: https://pypi.org/project/pywhat/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Instantly recognising and classifying unknown strings/files — "what is this?" for OSINT artifacts.
selectorsIn: []
selectorsOut:
- email
- crypto-wallet
- ip-address
- phone
status: live
pricing: free
costNote: Free and open-source (MIT); install via pip or Homebrew. Runs locally, no account or API key.
opsec: passive
opsecNote: Runs entirely offline on your own machine against text/files you provide — nothing is sent anywhere, so it is fully passive with no signal to any target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known open-source utility (from the "Bee-San"/Ciphey ecosystem) with a large user base; identifications are regex/heuristic and may need confirmation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- pywhat
- what
tags:
- ai-analysis-automation
- identifier
- cli
- triage
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# pywhat

> "What is this?" for unknown data — point pywhat at a string or file and it tells you which artifacts are inside: emails, hashes, crypto addresses, IPs, phone numbers, API keys, and hundreds more.

## When to use
You have a blob of text, a config dump, a pastebin, a filename, or a file and you don't yet know what the interesting artifacts are. pywhat recursively scans it and labels every recognised item by type — a fast triage step to find the emails, `crypto-wallet` addresses, `ip-address`es, `phone` numbers and secrets worth pivoting on.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install pywhat` (or `brew install pywhat`).
2. Run against a string: `pywhat "0x52908400098527886E0F7030069857D2E4169EE7"`, or a file/directory: `pywhat ./dump.txt`.
3. Read the tagged output — each match shows its identified type (and often a note, e.g. which coin an address is). Filter by tag, sort, or export JSON (`--json`).
4. Pivot: each identified artifact routes to its specialist tool — emails → email OSINT, `crypto-wallet` → a block explorer, `ip-address` → geolocation/reputation.

## Inputs → Outputs
- **In:** an arbitrary string, file, or directory (no fixed selector)
- **Out:** typed identifications — `email`, `crypto-wallet`, `ip-address`, `phone`, hashes, API keys, etc.
- **Empty/negative result looks like:** no recognised patterns — the input contains nothing matching pywhat's signatures (or the artifacts are obfuscated/encoded).

## Gotchas & OpSec
- Identification is pattern/heuristic-based — it can flag false positives (a random hex string ≠ a real key); confirm before acting.
- It classifies, it does not resolve — pywhat tells you *what* an artifact is, not *who* it belongs to.
- Large inputs produce lots of noise; use tag filters to focus.

## Overlaps ("do both")
- Complements CyberChef-style tools — pywhat spots and classifies artifacts; CyberChef decodes/transforms them. Run pywhat first to know what you're looking at.

## Trust & verifiability
`trust: community` — a mature, widely-used open-source utility; reliable as a triage classifier, but treat each identification as a lead to verify, not a fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pywhat |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  → email, crypto-wallet, ip-address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
