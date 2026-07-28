---
id: text-and-file-hash-calculator
name: Text and File Hash Calculator (defuse.ca)
description: Use when you need to compute or verify MD5/SHA hashes of text or a file — to confirm integrity, match a known/blocklisted hash, or fingerprint evidence — returns checksums.
url: https://defuse.ca/checksums.htm
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Quickly computing MD5/SHA-1/SHA-256 checksums of a string or file to verify integrity or match a known hash.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free single-page web tool; no account.
opsec: passive
opsecNote: For sensitive files, prefer hashing locally (sha256sum/certutil/PowerShell Get-FileHash) rather than uploading to any website — a hash of a private file, and the file itself, shouldn't leave your machine. Use this web tool for non-sensitive strings/files or when local tooling isn't handy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple hashing utility on a known security author's site (defuse.ca); the algorithms are standard, so output is verifiable against any local hasher.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- defuse
- big-number-calculator
- html-sanitizer-tool
- x86-and-x64-intel-assembler
aliases:
- defuse checksums
- hash calculator
tags:
- hashing
- integrity
- forensics
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Text and File Hash Calculator (defuse.ca)

> A quick checksum tool: compute MD5/SHA-1/SHA-256 of a string or file — for verifying integrity, matching a known hash, or fingerprinting a piece of evidence.

## When to use
You need a hash: to confirm a downloaded file matches a published checksum, to fingerprint evidence so you can prove it hasn't changed, to check a file/string against a known-hash list (malware, or a known image/document), or to compare two files by digest rather than byte-by-byte. It computes standard hashes; interpreting them (matching against a corpus, a blocklist, or a chain-of-custody record) is the OSINT/forensic use.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://defuse.ca/checksums.htm.
2. Paste text, or select a file, and compute the MD5/SHA-1/SHA-256 digest.
3. Compare the result to the reference hash (published checksum, evidence log, known-hash list).
4. For sensitive material, compute the hash **locally** instead (`sha256sum`, `Get-FileHash`, `certutil -hashfile`) and compare.
5. Pivot: a matching known-hash tells you a file is a specific known artefact; record hashes in your case log (e.g. `[[obsidian]]`) for integrity.

## Inputs → Outputs
- **In:** a text string or a file (no person selector)
- **Out:** MD5/SHA-1/SHA-256 checksums to compare or record (no person-level `selectorsOut`)
- **Empty/negative result looks like:** two hashes that don't match — the file differs from the reference (tampered, wrong version, or corrupted); a match confirms identity to the strength of the algorithm.

## Gotchas & OpSec
- OpSec: don't hash sensitive/private files via a website — hash locally so neither the file nor its digest leaves your control.
- MD5/SHA-1 are fine for integrity/known-file matching but are cryptographically broken — don't rely on them where collision-resistance matters; prefer SHA-256.
- A hash proves sameness/difference, not content — you still need the file to know what it is.

## Overlaps ("do both")
- Pairs with `[[agent-ransack]]` and case notes (`[[obsidian]]`) — hash files you collect to fingerprint and dedupe them, and log the digests for chain-of-custody.

## Trust & verifiability
`trust: community` — a simple utility running standard algorithms; any output is independently verifiable with a local hasher, which is also the safer option for sensitive files.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | text-and-file-hash-calculator |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
