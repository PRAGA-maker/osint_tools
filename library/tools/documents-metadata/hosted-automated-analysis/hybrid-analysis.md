---
id: hybrid-analysis
name: Hybrid Analysis
description: Use when you have a suspicious file/URL or a file hash and want a behavioural malware report — returns sandbox verdict, IOCs, and related samples.
url: https://hybrid-analysis.com/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
bestFor: Detonating a suspicious document/executable/URL in a free sandbox, or searching an existing hash for its behavioural report and IOCs.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free to search existing reports and submit files (free tier caps uploads, ~limited submissions/month, 30 MB files). A free CrowdStrike/HA account and API key unlock more. Heavy/commercial use is paid.
opsec: active
opsecNote: Submitting a file or URL is ACTIVE and consequential — the sample (and any secrets or victim data inside it) is uploaded to third-party infrastructure and often becomes searchable by other analysts. If a target could be watching, detonating their URL can tip them off. Prefer *searching by hash* first; only upload when you accept the exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by CrowdStrike (Falcon Sandbox); a mainstream, reputable malware-analysis service widely used by SOCs and researchers.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Falcon Sandbox
- HA
- hybrid-analysis.com
tags:
- malware-sandbox
- ioc-extraction
- threat-intel
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Hybrid Analysis

> A free malware sandbox (CrowdStrike Falcon Sandbox): submit or look up a file/URL and get a behavioural report — what it does, who it talks to, and the indicators to pivot on.

## When to use
You have a suspicious document, executable, APK, or `domain`/URL connected to a case (a phishing lure, a link sent to a victim, an attachment) and want to understand what it does and what infrastructure it contacts — without running it yourself. Hybrid Analysis detonates the sample and reports network callbacks (`domain`s, `ip-address`es), dropped files, registry/behavioural indicators, and a malicious/benign verdict. It's malware/document triage; direct missing-persons value is low (its use is mapping infrastructure behind a scam/extortion/grooming campaign).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://hybrid-analysis.com/.
2. **Search first:** paste a file hash (MD5/SHA-256), `domain`, or URL — if the sample was analysed before, you get the report with zero exposure.
3. **Submit (only if needed):** upload a file or enter a URL to detonate. Choose the sandbox environment; wait for the report.
4. Read the report: threat verdict/score, contacted `domain`s/`ip-address`es, dropped files, MITRE ATT&CK behaviours, and extracted IOCs.
5. Pivot: feed contacted `domain`s/`ip-address`es into passive DNS, `[[alienvault-otx]]`, and GreyNoise; feed related hashes back into this search.

## Inputs → Outputs
- **In:** a file / URL / `domain` / file hash
- **Out:** verdict + behavioural report, contacted `domain`s and `ip-address`es, dropped-file hashes, related samples
- **Empty/negative result looks like:** "no reports found" on a hash search means it hasn't been analysed here (try VirusTotal or submit) — not that it's clean; a benign verdict is only as good as the sandbox's detonation.

## Gotchas & OpSec
- **Uploads are public-ish and irreversible** — sensitive documents (containing PII/victim data) uploaded here may be retrievable by others; never upload confidential material.
- Detonating a target's URL is an active touch that can alert them and burns operational stealth.
- Sandbox evasion exists — sophisticated malware may behave benignly in the sandbox.
- Free tier is rate-limited; an API key raises limits.

## Overlaps ("do both")
- Pairs with VirusTotal (multi-engine + its own sandbox) and `[[alienvault-otx]]` — search the same hash/URL across all, since each has samples and reports the others lack. Feeds IOC-enrichment tools with the extracted network indicators.

## Trust & verifiability
`trust: trusted` — a reputable CrowdStrike-run service; the behavioural evidence is solid, but a verdict is a sandbox observation (evadable) rather than proof, so corroborate across engines.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hybrid-analysis |
| category | documents-metadata |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
