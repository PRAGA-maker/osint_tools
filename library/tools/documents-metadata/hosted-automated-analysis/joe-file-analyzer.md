---
id: joe-file-analyzer
name: Joe Sandbox File Analyzer
description: Use when you have a suspicious file (`document-id`/hash) and want dynamic malware analysis — returns behaviour, IOCs, and system-interaction reports.
url: https://www.file-analyzer.net/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
bestFor: Detonating a Windows/PE file in a sandbox to observe behaviour and extract indicators of compromise.
selectorsIn:
- document-id
selectorsOut:
- domain
- ip-address
- metadata-exif
status: live
pricing: freemium
costNote: file-analyzer.net now redirects to Joe Sandbox (joesandbox.com), which offers a free Community/Cloud Basic tier (public reports) alongside paid private analysis. Free tier requires the file be submitted publicly.
opsec: active
opsecNote: You UPLOAD the file to Joe Sandbox and, on the free tier, the report is PUBLIC and shared with the community — never submit sensitive/private documents. Detonation causes the sandbox to execute the sample and reach out to its C2/network resources, which can alert an attacker's infrastructure that the sample was analysed. Use hash search first when you only need existing results.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Joe Security's Joe Sandbox is a well-established commercial malware-analysis platform used across the industry. Reports are detailed and reproducible; verdicts are analyst aids, not absolute.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- joesandbox-document-analyzer
- joe-apk-analyzer
- joe-sandbox-url-analyzer
- virustotal
- hybrid-analysis
aliases:
- file-analyzer.net
- Joe Sandbox File Analyzer
tags:
- malware-analysis
- sandbox
- dynamic-analysis
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Joe Sandbox File Analyzer

> The file/PE entry point to Joe Sandbox — submit a suspicious executable or document and get a deep dynamic-analysis report: behaviour, dropped files, network IOCs, and a maliciousness verdict.

## When to use
You have a suspicious file (an attachment, a downloaded binary, a hash) connected to your investigation and need to know what it does and what infrastructure it talks to. Joe Sandbox detonates it in an instrumented environment and reports API calls, dropped artefacts, and — most useful for OSINT pivoting — the `domain`s and `ip-address`es it contacts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.file-analyzer.net/ (redirects to Joe Sandbox) and sign in / create a free Cloud Basic account.
2. First, **search the hash** — if the sample was analysed before, read the existing report without re-detonating (quieter and instant).
3. To analyse a new file, upload it (accept that the free-tier report is public) and start the run.
4. Read the report: verdict/score, behaviour graph, dropped files, and the **network** section (contacted `domain`s/`ip-address`es) plus file `metadata-exif`.
5. Pivot: extracted `domain`s/`ip-address`es feed `[[virustotal]]` and infrastructure tools to map the wider campaign.

## Inputs → Outputs
- **In:** a file or its hash (`document-id`)
- **Out:** behavioural report, IOCs — contacted `domain`s/`ip-address`es, dropped files, `metadata-exif`, maliciousness verdict
- **Empty/negative result looks like:** a benign/low score, or a sample that doesn't execute (wrong environment, anti-analysis evasion, needs args) — low signal isn't proof of safety; try another sandbox or an evasion-aware config.

## Gotchas & OpSec
- **Public disclosure:** free-tier submissions and reports are public and shared — don't upload private/sensitive files. Use hash search to avoid re-uploading.
- **Detonation is active:** the sandbox contacts the sample's C2, which can tip off an attacker. Consider whether that matters before running.
- Free tier is rate-limited and uses a standard environment; sophisticated malware may detect the sandbox and stay dormant.

## Overlaps ("do both")
- Part of the Joe Sandbox suite — pair with `[[joesandbox-document-analyzer]]` (Office docs), `[[joe-apk-analyzer]]` (Android), and `[[joe-sandbox-url-analyzer]]` (URLs) for the matching file type. Cross-check verdicts with `[[virustotal]]` and `[[hybrid-analysis]]`.

## Trust & verifiability
`trust: trusted` — an established, industry-standard sandbox. Reports are detailed and reproducible; treat the automated verdict as a strong aid and confirm key IOCs independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | joe-file-analyzer |
