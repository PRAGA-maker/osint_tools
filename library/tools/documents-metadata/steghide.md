---
id: steghide
name: steghide
description: Use when you have an image or audio file from a subject and suspect embedded data — returns hidden files/text extracted from the carrier, plus a presence signal.
url: https://github.com/StefanoDeVuono/steghide
category: documents-metadata
path:
- documents-metadata
bestFor: Recovering data steganographically hidden inside a subject's JPEG/BMP/WAV/AU files (often CTF-style).
selectorsIn:
- image
selectorsOut:
- metadata-exif
- document-id
status: live
pricing: free
costNote: Free and open-source; `apt install steghide` on Debian/Kali/Trace Labs VM, or build from the repo.
opsec: passive
opsecNote: Fully local and offline — you run it against a file you already hold, so nothing leaves your machine and the subject is never contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Classic, widely packaged steganography utility; this GitHub mirror tracks the long-standing steghide codebase shipped in Kali and the Trace Labs VM.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- steghide extract
tags:
- steganography
- forensics
- ctf
source: tracelabs-repos
lastVerified: '2026-07-23'
enrichment: full
---

# steghide

> A command-line steganography tool that embeds and extracts data hidden inside JPEG, BMP, WAV, and AU files — used defensively to pull whatever a subject concealed in shared media.

## When to use
You have an `image` (or audio file) shared by a subject and have reason to think data is hidden inside it — an odd file size, a CTF prompt, a suspiciously "innocent" attachment, or a known steghide workflow. steghide can test for and extract an embedded payload if you can supply (or crack) the passphrase. This is niche forensics, not a routine person-finding step.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `apt install steghide` (or build from the repo URL). It is pre-installed in the Trace Labs VM and Kali.
2. Check what a carrier holds: `steghide info suspect.jpg` — reports whether embedded data is present and prompts for the passphrase.
3. Extract: `steghide extract -sf suspect.jpg` and enter the passphrase; the hidden file is written out.
4. If the passphrase is unknown, try likely words, or run a wordlist wrapper (e.g. `stegcracker`/`stegseek` against the same file).
5. Pivot: an extracted `document-id`, note, or `metadata-exif` blob feeds normal document/metadata analysis.

## Inputs → Outputs
- **In:** a carrier `image`/audio file (JPEG, BMP, WAV, AU) and a passphrase.
- **Out:** the embedded file/text if present (which may itself contain a `document-id`, `metadata-exif`, or coordinates), and a presence/absence signal from `steghide info`.
- **Empty/negative result looks like:** `steghide info` reports no embedded data, or `extract` fails with "could not extract any data with that passphrase!" — meaning either nothing is hidden, a different tool/algorithm was used, or the passphrase is wrong.

## Gotchas & OpSec
- steghide only handles its own format; PNG/GIF and other tools' payloads won't be found here — try `zsteg`, `binwalk`, or `foremost` instead.
- Extraction almost always needs the correct passphrase; a wrong one is indistinguishable from "nothing hidden."
- Re-compressing or resizing a carrier destroys the payload, so work from the original file.

## Overlaps ("do both")
- Complements general metadata/forensics tooling (EXIF readers, `binwalk`): those read what's declared or appended, while steghide recovers what was deliberately hidden in the pixel/sample data.

## Trust & verifiability
`trust: trusted` — mature open-source utility packaged in mainstream forensic distributions; output is your own local extraction, fully reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steghide |
