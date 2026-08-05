---
id: opswat-meta-defender
name: OPSWAT Meta Defender
description: Use when you have a file, hash, URL, IP, or domain and want a multi-engine malware/reputation verdict — returns detections, IOCs, and metadata across many AV engines.
url: https://metadefender.opswat.com/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
bestFor: Checking a file/hash/URL/IP against many antivirus engines and reputation sources at once.
selectorsIn:
- document-id
- domain
- ip-address
selectorsOut:
- metadata-exif
- domain
- ip-address
status: live
pricing: freemium
costNote: Free in-browser scanning of files, hashes, URLs, IPs, and domains. Heavier/API use and larger files need an account and hit free-tier limits; enterprise features are paid.
opsec: active
opsecNote: Uploading a FILE sends its contents to OPSWAT and, potentially, onward to AV vendors — never upload a sensitive or evidentiary original; hash it locally and search the hash instead. Hash/URL/IP/domain lookups are lighter but still logged, and submitting a target's URL/IP is a query about that target — use a sock-puppet account for sensitive work.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: OPSWAT is a established security vendor; MetaDefender Cloud aggregates 20+ commercial AV engines and reputation feeds, so verdicts are authoritative multi-engine signals (a mainstream VirusTotal alternative).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- metadefender
aliases:
- MetaDefender Cloud
- metadefender.opswat.com
tags:
- malware-analysis
- multi-engine-scanner
- file-reputation
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# OPSWAT Meta Defender

> A multi-engine malware and reputation scanner (a VirusTotal-style service): drop in a file, hash, URL, IP, or domain and get verdicts from many AV engines plus metadata and IOCs.

## When to use
You have an artefact from an investigation — a suspicious file or attachment (`document-id`), a file hash, a `domain`, or an `ip-address` — and you want to know whether it is known-malicious and what metadata/IOCs are associated. Useful for triaging a link or file sent to/by a subject, or corroborating that infrastructure is flagged.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://metadefender.opswat.com/.
2. Choose the input type and submit: upload a file, paste a **hash** (prefer this for anything sensitive — no content leaves your machine), or enter a URL, IP, or domain.
3. Read the report: per-engine detection verdicts, an overall malicious/clean signal, extracted file metadata (`metadata-exif`), and associated IOCs (domains, IPs, hashes).
4. For a `domain`/`ip-address`, read the reputation and related-indicator view.
5. Pivot: flagged IOCs feed infrastructure mapping; file metadata (author, tool, timestamps) can feed document-attribution work.

## Inputs → Outputs
- **In:** a file or its hash (`document-id`), `domain`, or `ip-address`
- **Out:** multi-engine detection verdicts, extracted file `metadata-exif`, and related `domain`/`ip-address` IOCs
- **Empty/negative result looks like:** "no detections" across engines (likely clean, or too new/unknown to be flagged — absence of detection is not proof of safety), or "hash not found" meaning nobody has submitted that artefact before.

## Gotchas & OpSec
- Multi-engine ≠ infallible: novel/targeted malware may pass clean; a single-engine hit can be a false positive. Weigh the consensus.
- Uploading a file shares it — a serious OpSec/evidentiary risk. Hash locally and search the hash whenever the file is sensitive.
- Free tier has size and rate limits; large or frequent scans need an account.
- OpSec: active — submissions are logged and file uploads propagate; use a dedicated account and never upload originals you must preserve.

## Overlaps ("do both")
- Cross-check verdicts and metadata against VirusTotal and a dedicated `[[metadefender]]` workflow — engine line-ups differ, so one service may flag what another misses, and agreeing verdicts raise confidence.

## Trust & verifiability
`trust: trusted` — a mainstream security vendor aggregating many commercial engines; verdicts are strong multi-source signals, with the standard caveat that "clean" only means "not yet detected."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opswat-meta-defender |
