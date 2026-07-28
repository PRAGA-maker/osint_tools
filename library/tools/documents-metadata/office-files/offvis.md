---
id: offvis
name: OffVis
description: Use when you have a legacy Office binary file (.doc/.xls/.ppt) and want to inspect its internal record structure and spot exploit shellcode — returns structure/`metadata-exif` analysis.
url: https://download.microsoft.com/download/1/2/7/127ba59a-4fe1-4acd-ba47-513ceef85a85/OffVis.zip
category: documents-metadata
path:
- documents-metadata
- office-files
bestFor: Visualizing the internal structure of legacy Office binary files (OLE/CFB) and detecting known malformed-record exploits.
selectorsIn: []
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free first-party Microsoft tool; Windows GUI requiring .NET Framework 2.0. Runs fully offline.
opsec: passive
opsecNote: Runs entirely on your local machine — no file upload, nothing leaves the host. Safe for analyzing suspicious/malicious samples inside an isolated VM.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: First-party Microsoft (MSRC) tool for the legacy Office binary format; authoritative but old — last updated ~2009/2010, and it does NOT parse modern .docx/.xlsx (OOXML) files.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Microsoft Office Visualization Tool
- OffVis 1.1
tags:
- office-forensics
- file-analysis
- malware-analysis
- metadata
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# OffVis

> Microsoft's own Office binary visualizer: open a legacy `.doc/.xls/.ppt` and see its record tree, hex, and any known-exploit red flags — all locally.

## When to use
You have a legacy Office binary document (the pre-2007 OLE/Compound-File formats: `.doc`, `.xls`, `.ppt`, `.pps`, `.pot`) and want to look inside it — to read its structure, extract embedded objects/metadata, or check whether it's a weaponized sample exploiting a known Office CVE. Useful in document forensics when a file arrived from or relates to a subject and you need to understand or safely triage it.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and unzip OffVis.zip (from Microsoft's Download Center); ensure **.NET Framework 2.0** is installed on a Windows host — ideally an isolated analysis VM.
2. Launch `OffVis.exe` and open the target Office binary file.
3. Explore the panes: a **structure/object tree** of the file's records, a synchronized **hex dump** (hover a record to highlight its bytes), and a **parser** that flags malformed records matching known exploit signatures.
4. Read embedded metadata/objects and note anything anomalous (shellcode-like blobs, exploit indicators).
5. Pivot: extracted authorship/metadata feeds identity work; a confirmed exploit sample feeds malware analysis / IOC extraction.

## Inputs → Outputs
- **In:** a legacy Office binary file (`.doc/.xls/.ppt/.pps/.pot`)
- **Out:** internal record/structure visualization, hex, embedded objects and `metadata-exif`, plus known-exploit detection
- **Empty/negative result looks like:** the parser reports no known-exploit match and a clean structure — the file parses as an ordinary document (not proof it's benign, just no known signature hit).

## Gotchas & OpSec
- **Legacy formats only** — it will not open modern OOXML `.docx/.xlsx/.pptx`; use a ZIP/XML inspector or `oletools` for those.
- Windows + .NET 2.0 dependency; the tool hasn't been updated in years, so its exploit signatures cover older CVEs only.
- OpSec: passive and offline — nothing uploads, so it's safe for malware samples in a sandbox.

## Overlaps ("do both")
- Pair with `oletools`/OLE inspectors and a metadata extractor — OffVis gives the visual record structure and known-exploit flagging, those give scripted macro/metadata extraction and OOXML coverage.

## Trust & verifiability
`trust: trusted` — a genuine Microsoft MSRC forensic tool, authoritative for the binary format it targets; the only caveat is age, so treat its exploit detection as "known older signatures", not comprehensive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | offvis |
| category | documents-metadata |
| selectorsIn → selectorsOut |  → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
