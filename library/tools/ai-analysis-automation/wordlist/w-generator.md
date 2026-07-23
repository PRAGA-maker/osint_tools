---
id: w-generator
name: W Generator
description: Use when you have personal facts about a subject (`name`, `dob`, `username`) and want a targeted password wordlist for authorised credential testing — returns candidate `password` lists.
url: https://app.wgen.io/
category: ai-analysis-automation
path:
- ai-analysis-automation
- wordlist
bestFor: Building custom, pattern-driven password wordlists from a target's known personal details across 60+ languages.
selectorsIn:
- name
- dob
- username
selectorsOut:
- password
status: live
pricing: free
costNote: Free browser-based generator; a free offline version also exists on GitHub. No account required.
opsec: passive
opsecNote: The pattern builder runs in-browser and does not touch any target system — generation itself is passive. Using the resulting wordlist against a live account is active and must be authorised (pentest/red-team engagement or your own account); brute-forcing someone else's login is intrusive and often illegal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent security utility (wgen.io) with public docs and an open-source offline build; not a vetted enterprise tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WGEN
- wgen.io
tags:
- ai-analysis-automation
- wordlist
- password-cracking
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# W Generator

> A browser-based, pattern-driven wordlist builder: turn a subject's known personal facts into a targeted dictionary for authorised password attacks.

## When to use
You are doing authorised credential testing (a pentest, red-team engagement, or recovering your own account) and have publicly-known facts about the subject — `name` variants, `dob`, `username`, pet/place names, dates. W Generator expands those into a focused wordlist far smaller and more likely-to-hit than generic rockyou-style lists.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://app.wgen.io/ (docs at https://docs.wgen.io/docs).
2. In the pattern/UI builder, add fields for the subject's details — names, shortened name variations, advanced date permutations, etc.
3. Tune the language profile (60+ languages; define vowels for better string-shortening) and use groups/permutations to control the arrangements produced.
4. Generate and export the wordlist; optionally export/import your pattern to reuse or share. Feed the list into your cracking tool (hashcat/john) against the authorised target.

## Inputs → Outputs
- **In:** `name`, `dob`, `username` and other known personal facts
- **Out:** a candidate `password` wordlist (potentially millions of entries)
- **Empty/negative result looks like:** an over-broad list if you feed too little targeting info, or zero hits when the subject's real password isn't derived from the facts you supplied — a wordlist is only as good as the intel behind it.

## Gotchas & OpSec
- Generation is passive; *using* the wordlist against a live login is active, intrusive, and must be legally authorised.
- Overly permissive permutation settings explode list size and slow cracking — constrain patterns to plausible ones.
- Prefer the offline build for sensitive engagements so target-specific inputs never leave your machine.

## Overlaps ("do both")
- Pairs with any personal-details OSINT (names, dates, associates) — those feed the pattern fields here. Compare with other wordlist generators (e.g. CUPP-style tools) which do the same job from a CLI.

## Trust & verifiability
`trust: unverified` — an independent utility with public documentation and an open-source offline variant, but not audited; verify the offline code before trusting it with sensitive inputs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | w-generator |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, dob, username → password |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
