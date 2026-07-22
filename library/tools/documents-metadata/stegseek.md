---
id: stegseek
name: stegseek
description: Use when you have an `image`/file suspected of hiding steghide-embedded data and want to crack it — brute-forces the passphrase and extracts the hidden payload (`metadata-exif`).
url: https://github.com/RickdeJager/stegseek
category: documents-metadata
path:
- documents-metadata
bestFor: Cracking steghide-protected files fast (wordlist brute-force) to recover hidden data when the passphrase is unknown.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open source (MIT); a single fast CLI binary.
opsec: passive
opsecNote: Cracking runs entirely offline against a file you already hold — nothing is sent anywhere and no subject is contacted. Work on a copy and hash the original for chain-of-custody.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Open source and bundled in the Trace Labs OSINT VM; results are deterministic and reproducible against the same file/wordlist.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- stegseek
tags:
- steganography
- cracking
- ctf
source: tracelabs-repos
lastVerified: '2026-07-22'
enrichment: full
---

# stegseek

> A blazing-fast steghide cracker — brute-forces the passphrase of a steghide-embedded file against a wordlist and dumps the hidden payload, in seconds rather than hours.

## When to use
You have an `image` (or audio) file you suspect conceals data via steghide — a common CTF and forensic scenario, occasionally seen in real investigations where someone hides information in an innocuous picture. If the passphrase is unknown, stegseek tries a wordlist (e.g. rockyou) at high speed to recover it and extract the embedded content.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/RickdeJager/stegseek (deb package or build; already present in the Trace Labs VM).
2. Run against a copy of the file with a wordlist: `stegseek suspicious.jpg wordlist.txt`.
3. If it cracks, it writes the passphrase and extracts the hidden file automatically.
4. Use `--seed` / the "confirm steghide is present" check if you only want to detect embedding.
5. Pivot: examine the extracted payload (`metadata-exif`/hidden file) and feed any selectors it contains into the appropriate searches.

## Inputs → Outputs
- **In:** an `image`/file suspected of steghide embedding (+ a wordlist)
- **Out:** the cracked passphrase and the extracted hidden data (`metadata-exif`/embedded file)
- **Empty/negative result looks like:** "Could not find a valid passphrase" — either there's no steghide payload, or the passphrase isn't in your wordlist; absence isn't proof the file is clean.

## Gotchas & OpSec
- Only cracks **steghide** specifically — other stego tools (LSB, OpenStego, etc.) need different tools; a negative here doesn't rule out all steganography.
- Success depends entirely on the wordlist; a strong/random passphrase won't crack.
- OpSec: fully offline and passive; still work on a copy and hash the original for evidence integrity.

## Overlaps ("do both")
- Complements EXIF/metadata viewers and other stego detectors — metadata tools read visible fields, stegseek attacks steghide-hidden payloads those never surface.

## Trust & verifiability
`trust: trusted` — open source, widely used in CTF/forensics and shipped in Trace Labs' VM; any extraction is reproducible from the same file and wordlist.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stegseek |
