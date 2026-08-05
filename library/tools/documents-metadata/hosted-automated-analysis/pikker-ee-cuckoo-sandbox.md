---
id: pikker-ee-cuckoo-sandbox
name: Pikker.ee Cuckoo Sandbox
description: Use when you have a suspicious file or URL and want free automated dynamic (behavioral) malware analysis — returns a behavior report with contacted domains/IPs and dropped-file metadata.
url: https://sandbox.pikker.ee/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
bestFor: Free automated dynamic malware analysis with detailed behavioral reports.
selectorsIn:
- domain
- document-id
selectorsOut:
- domain
- ip-address
- metadata-exif
status: live
pricing: free
costNote: Free public Cuckoo Sandbox instance; you can submit URLs/files/hashes without payment (an account may be needed for full history).
opsec: active
opsecNote: Submissions can become visible to other researchers and are detonated on infrastructure you don't control — never submit files/URLs containing sensitive, private, or case-identifying data, as that would leak it. The detonation also makes real network requests to the sample's C2, which may tip off the operator. Treat submission as public.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community/CERT-hosted Cuckoo Sandbox; the analysis engine is the well-known open-source Cuckoo, but this specific public instance's uptime and retention aren't guaranteed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- pikker sandbox
- sandbox.pikker.ee
tags:
- malware-analysis
- sandbox
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Pikker.ee Cuckoo Sandbox

> A free public Cuckoo Sandbox — detonate a suspicious file or URL and get an automated behavioral report of what it does.

## When to use
Malware/artifact triage in an investigation. You have a suspicious `document-id` (a file/attachment) or a `domain`/URL and want to know what it *does* — what hosts it contacts, what it drops, what it changes — without running it on your own machine. Pikker's hosted Cuckoo detonates it in an instrumented VM and reports the behaviour, surfacing C2 `domain`s/`ip-address`es and dropped-file `metadata-exif` to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sandbox.pikker.ee/ and use the submit interface for a URL, file, or hash.
2. Wait for the automated analysis to complete, then open the report.
3. Read the behavioral sections: network contacts (domains/IPs), dropped files and hashes, registry/process activity.
4. Extract IOCs — contacted infrastructure and file hashes.
5. Pivot: contacted `domain`/`ip-address` → infrastructure OSINT (WHOIS/passive DNS); file hashes → VirusTotal/other sandboxes.

## Inputs → Outputs
- **In:** a suspicious file/`document-id`, URL, or hash (a `domain` for URL submissions)
- **Out:** behavioral report with contacted `domain`s/`ip-address`es and dropped-file `metadata-exif`/hashes
- **Empty/negative result looks like:** a benign or inert report (no meaningful network/file activity) — the sample may be benign, environment-aware (sandbox-evading), or need a specific trigger.

## Gotchas & OpSec
- **Submissions are effectively public** and shared with researchers — never submit anything with private/case-sensitive content.
- Detonation makes **real** callbacks to the sample's infrastructure, which can alert the operator that their sample was analysed.
- Public instances go offline or purge data; don't rely on it for long-term retention, and cross-check with another sandbox.
- Sandbox-aware malware may behave benignly to hide.

## Overlaps ("do both")
- Cross-submit to other sandboxes (Any.Run, Hybrid Analysis, Joe Sandbox) and to VirusTotal — each detonation environment triggers different behaviour and coverage.

## Trust & verifiability
`trust: community` — the Cuckoo engine is a respected open-source analyzer, but this is an unofficial public instance; corroborate its IOCs against at least one other sandbox before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pikker-ee-cuckoo-sandbox |
| category | documents-metadata |
| selectorsIn → selectorsOut | domain, document-id → domain, ip-address, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
