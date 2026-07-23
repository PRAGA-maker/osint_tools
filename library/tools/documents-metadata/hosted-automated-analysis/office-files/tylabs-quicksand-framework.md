---
id: tylabs-quicksand-framework
name: TYLabs QuickSand Framework
description: Use when you have a suspicious Office document/PDF and want exploit/malware detection — returns YARA matches, embedded-exploit findings, and extracted payloads.
url: https://scan.tylabs.com/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
- office-files
bestFor: Static analysis of malicious documents (Office, PDF, email) to detect exploits, obfuscation, and embedded active content.
selectorsIn:
- metadata-exif
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: The QuickSand engine is free and open source (quicksand.io) and runs offline locally; the hosted scan.tylabs.com service is free to use but involves uploading files.
opsec: active
opsecNote: The hosted scanner requires uploading the document to third-party infrastructure — do NOT upload confidential/PII-laden documents there. For sensitive material, run the open-source QuickSand library locally, which is passive and offline.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source document-forensics tool by tylabs (QuickSand); auditable and used in malware-analysis workflows, though a smaller project than mainstream sandboxes.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- QuickSand
- quicksand.io
- scan.tylabs.com
tags:
- document-malware
- exploit-detection
- yara
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# TYLabs QuickSand Framework

> A document forensics engine: statically pulls apart Office files, PDFs, and emails to find embedded exploits, obfuscated content, and hidden payloads — without detonating them.

## When to use
You have a suspicious document (a `.doc/.xls/.ppt`, PDF, or email attachment) tied to a phishing or malware lure in a case, and you want to know whether it's weaponised and how — which exploit/CVE, what obfuscation, what payload it hides. Unlike a detonation sandbox, QuickSand does *static* analysis: YARA-signature matching and structural decoding to surface active content and embedded objects. It's document-malware triage; direct missing-persons value is low (understanding a lure sent to a victim and extracting IOCs from it).

## How to use it (`bestInteractionPattern`: web-manual)
1. **Local (preferred for sensitive files):** install the open-source engine — `pip install quicksand` — and run it on the file to get a JSON report of signatures and extracted objects. No upload, fully offline.
2. **Hosted:** go to https://scan.tylabs.com/ and upload the document for a web report (only for non-confidential samples — see OpSec).
3. Read the report: YARA matches, detected exploits/CVEs, risk scoring, decoded streams, and extracted embedded content.
4. Pivot: extracted URLs/`domain`s and payload hashes feed `[[hybrid-analysis]]`, VirusTotal, and passive-DNS enrichment; document `metadata-exif` (author/producer) can attribute the lure.

## Inputs → Outputs
- **In:** an Office document / PDF / email (its structure and embedded `metadata-exif`)
- **Out:** YARA signature hits, exploit/CVE detection, risk score, decoded/embedded objects, document `metadata-exif`
- **Empty/negative result looks like:** no signatures/exploits found — the document may be benign, or use a technique QuickSand's signatures don't cover; a clean static result doesn't guarantee safety (pair with a sandbox).

## Gotchas & OpSec
- **Static analysis only** — it detects known exploit patterns and structure, not runtime behaviour; combine with a behavioural sandbox for full coverage.
- **Uploads to scan.tylabs.com are exposure** — never send confidential documents; use the local library instead.
- Detection is signature-driven, so novel obfuscation can slip through (false negatives).

## Overlaps ("do both")
- Pairs with behavioural sandboxes like `[[hybrid-analysis]]` and VirusTotal (static structure vs. runtime behaviour) and with document-metadata tools — run QuickSand to see *how* a document is built and weaponised, the sandbox to see *what it does*.

## Trust & verifiability
`trust: community` — an auditable open-source forensics tool; its static findings are concrete (you can inspect the matched objects), but treat a clean result as inconclusive and corroborate with dynamic analysis.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tylabs-quicksand-framework |
| category | documents-metadata |
| selectorsIn → selectorsOut | metadata-exif → metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
