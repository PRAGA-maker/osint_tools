---
id: office-mal-scanner
name: OfficeMalScanner
description: Use when you have a legacy Office document and want to find embedded malware/shellcode — returns detected macros, shellcode, PE files, and OLE structure.
url: https://www.reconstructer.org/
category: documents-metadata
path:
- documents-metadata
- office-files
bestFor: Statically scanning legacy MS Office (OLE .doc/.xls/.ppt) documents for macros, shellcode, and embedded executables — locally, offline.
selectorsIn:
- metadata-exif
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free tool by Frank Boldewin (reconstructer.org). Windows binary, run locally.
opsec: passive
opsecNote: Runs entirely on your own machine against a file you already have — no upload, no network. Analyze inside an isolated VM, since you're handling live malicious documents.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Long-established, respected malware-analysis utility by Frank Boldewin; a classic in document-forensics training, though focused on the legacy OLE format.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- OfficeMalScanner
- reconstructer.org
tags:
- document-malware
- ole
- static-analysis
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# OfficeMalScanner

> A classic offline scanner for weaponised legacy Office documents: it hunts through the OLE structure for macros, shellcode, and embedded executables.

## When to use
You have a legacy-format Office document (OLE-based `.doc/.xls/.ppt`) suspected of being malicious and want to analyze it *locally* without uploading it anywhere. OfficeMalScanner statically inspects the file for VBA macros, shellcode patterns (via heuristic brute-force disassembly), embedded PE/OLE objects, and can dump/decompress the OLE streams. It's document-malware forensics; missing-persons relevance is low (dissecting a lure sent to a victim and extracting embedded IOCs), and it keeps sensitive documents off third-party servers.

## How to use it (`bestInteractionPattern`: cli)
1. Download OfficeMalScanner from https://www.reconstructer.org/ and run it in an **isolated analysis VM** (it's a Windows CLI binary; you're handling live malware).
2. Scan the document:
   ```
   OfficeMalScanner suspect.doc scan brute
   OfficeMalScanner suspect.doc info      # dump VBA macro code / OLE structure
   ```
   `scan brute` looks for shellcode/embedded content; `info` extracts macros and structure.
3. Read the output: detected macros (dumped as source), shellcode hits, embedded PE files, and a risk indication.
4. Pivot: extracted macro code / URLs / payload hashes feed sandboxes (`[[hybrid-analysis]]`), VirusTotal, and IOC extraction (`[[iocextract]]`).

## Inputs → Outputs
- **In:** a legacy OLE Office document (its embedded content + `metadata-exif`)
- **Out:** detected macros (source), shellcode/embedded-PE findings, OLE structure, `metadata-exif`
- **Empty/negative result looks like:** no macros/shellcode detected — the document may be benign, OR it's a modern OOXML (`.docx/.xlsm`) that this OLE-focused tool doesn't fully parse; for OOXML use oletools/oledump instead.

## Gotchas & OpSec
- **Legacy focus:** built for the old OLE compound-file format; modern `.docx/.xlsm` are better handled by oletools (olevba/oledump). Use the right tool for the format.
- Windows binary — run in a disposable VM; you're executing analysis on real malware.
- Static/heuristic detection can miss novel obfuscation (false negatives).
- OpSec: fully local/passive — nothing is uploaded.

## Overlaps ("do both")
- Complements oletools (olevba, oledump) for modern Office formats and hosted analyzers like `[[tylabs-quicksand-framework]]` / `[[hybrid-analysis]]` — OfficeMalScanner's niche is offline dissection of *legacy* OLE documents; use the others for OOXML or behavioural detonation.

## Trust & verifiability
`trust: community` — a respected, long-standing analyst tool from Frank Boldewin; its findings are concrete artifacts you can inspect, with the caveat that it targets legacy OLE and heuristic detection has blind spots.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | office-mal-scanner |
| category | documents-metadata |
| selectorsIn → selectorsOut | metadata-exif → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
