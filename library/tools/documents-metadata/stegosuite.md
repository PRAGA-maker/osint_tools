---
id: stegosuite
name: Stegosuite
description: Use when you suspect an `image` hides embedded data and you want to extract it (or embed your own) — returns hidden text/files concealed via steganography.
url: https://github.com/osde8info/stegosuite
category: documents-metadata
path:
- documents-metadata
bestFor: GUI embedding/extraction of hidden (optionally AES-encrypted) data in BMP/GIF/JPG/PNG images.
selectorsIn:
- image
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open-source (GPL-3.0) Java GUI app; run locally (`java -jar stegosuite-*.jar`). No account.
opsec: passive
opsecNote: Runs entirely offline on your machine against files you hold — passive, nothing leaves your host. Handle suspect images in an isolated environment as you would any untrusted file.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Established open-source steganography tool; it works with data hidden by its own scheme, so it's not a universal stego detector — a negative doesn't rule out other methods.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- StegOSuite
tags:
- documents-metadata
- steganography
- image
- forensics
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Stegosuite

> A Java GUI steganography tool — hide data inside images, or try to extract data hidden with its scheme, with optional AES encryption.

## When to use
You have an `image` you suspect carries concealed data (a message or file hidden via steganography), or you need to embed data into an image yourself (for a controlled test/persona). Stegosuite supports BMP, GIF, JPG, and PNG and can AES-encrypt the payload, embedding while avoiding homogeneous areas.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and build/run from https://github.com/osde8info/stegosuite (`java -jar target/stegosuite-*.jar`).
2. To extract: open the suspect `image`, supply the key/password if known, and attempt extraction.
3. To embed: open a carrier image, add your text/file and a passphrase, and save the stego image.
4. Pivot: an extracted message/file (`document-id`) becomes new evidence to analyse (identify with `[[pywhat]]`, scan, or read); combine with other stego/forensic tools when extraction fails.

## Inputs → Outputs
- **In:** an `image` (BMP/GIF/JPG/PNG), plus a key if the payload is encrypted
- **Out:** extracted hidden data/file (`document-id`), or a new stego image you created
- **Empty/negative result looks like:** no data extracted — the image has no Stegosuite-embedded payload, uses a different stego method, or you lack the correct key; this does NOT prove the image is clean.

## Gotchas & OpSec
- It extracts data hidden with *its* algorithm — it's not a universal detector; other tools (zsteg, steghide, StegExpose) are needed for other schemes.
- A negative result never rules out steganography generally.
- Java GUI app — requires a JRE; treat untrusted images carefully.

## Overlaps ("do both")
- Complements other stego tools (steghide/zsteg/StegExpose) and `[[pywhat]]` — try multiple stego tools since each targets different embedding methods, then identify whatever you extract.

## Trust & verifiability
`trust: community` — a solid open-source tool for its specific scheme; because coverage is method-specific, corroborate a "nothing hidden" conclusion with other stego analysers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stegosuite |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
