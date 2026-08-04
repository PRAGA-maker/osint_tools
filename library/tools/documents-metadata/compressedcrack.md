---
id: compressedcrack
name: CompressedCrack
description: Use when you have a password-protected ZIP/RAR/7z archive (from a leak, seizure, or evidence set) and want to brute-force the password — a local cracking tool, returns the `password`.
url: https://github.com/mnismt/CompressedCrack
category: documents-metadata
path:
- documents-metadata
bestFor: Brute-forcing the password of a protected ZIP/RAR/7z archive locally to open its contents.
selectorsIn:
- document-id
selectorsOut:
- password
status: live
pricing: free
costNote: Free and open-source (MIT); Python 3.6+ CLI installed via pip, runs entirely locally.
opsec: passive
opsecNote: Runs fully offline against a file you already hold — nothing leaves your machine, so it is passive. Only crack archives you are legally authorized to open; brute-forcing others' protected files may be unlawful regardless of OpSec.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: A popular open-source utility (~300 stars, MIT); the code is short and auditable, but it is a community tool — inspect before running on evidentiary files.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- mnismt/CompressedCrack
tags:
- documents-metadata
- password-recovery
- forensics
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# CompressedCrack

> A small local CLI that brute-forces the password on a protected ZIP/RAR/7z archive so you can open its contents.

## When to use
An investigation turns up a password-protected archive — from a breach dump, a seized device, or a file a subject shared — and you need what's inside. CompressedCrack tries password combinations (with length bounds) against the archive locally until it finds one. It returns the recovered `password`; the payoff is the archive's contents (documents, images, credentials) that then become new leads. Only run it on files you are authorized to access.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install` the tool from https://github.com/mnismt/CompressedCrack (review the code first).
2. Run against the archive: `compressedcrack [options] path/to/file.zip`.
3. Constrain the search with `--min-length` / `--max-length` (and `--verbose` for progress) — a tight length range makes brute force feasible; a wide one may be intractable.
4. Read the output: on success it prints the discovered `password`, the attempt count, and elapsed time.
5. Pivot: open the archive with the recovered password and process its contents; a found password is itself worth testing for credential reuse elsewhere.

## Inputs → Outputs
- **In:** a password-protected archive (a `document-id` — ZIP/RAR/7z)
- **Out:** the recovered `password` (and thus access to the archive contents)
- **Empty/negative result looks like:** exhaustion without a hit within your length/charset bounds. That means the password is longer/more complex than the search space — widen carefully, switch to a wordlist/rules approach (hashcat/John), or accept it as computationally infeasible.

## Gotchas & OpSec
- Human-in-the-loop: yes — you must set sensible length/charset bounds and judge when brute force is hopeless; it's a script, not a service.
- OpSec: **passive** and fully offline. The legal, not technical, risk dominates — only crack archives you have authority to open.
- Pure brute force scales badly. For anything beyond short passwords, a wordlist/rule-based cracker (hashcat, John the Ripper) with the archive hash is far more effective.

## Overlaps ("do both")
- Complements hashcat/John the Ripper (extract the archive hash and run dictionary+rules there for hard passwords) — CompressedCrack is the quick, simple option for short/simple passwords.

## Trust & verifiability
`trust: community` — a popular MIT-licensed open-source script you can read before running. Success is self-evident (the archive opens with the recovered password), so correctness verifies itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | compressedcrack |
| category | documents-metadata |
| selectorsIn → selectorsOut | document-id → password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (manual-review) |
