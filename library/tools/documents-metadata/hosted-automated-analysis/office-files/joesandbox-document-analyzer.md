---
id: joesandbox-document-analyzer
name: Joe Sandbox Document Analyzer
description: Use when you have a suspicious file or URL (`document-id`) and want deep behavioural malware analysis — returns a detonation report with threat score and extracted IOCs.
url: https://www.joesandbox.com/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
- office-files
bestFor: Deep automated sandbox detonation of documents/executables/URLs with behavioural reporting.
selectorsIn:
- document-id
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Joe Sandbox Cloud Basic offers free community analysis (public submissions); private/commercial tiers add confidentiality and more depth.
opsec: passive
opsecNote: Submitting to the free/community tier makes your sample and report PUBLIC — never upload case-sensitive files there (it can tip off an attacker or leak evidence). Searching existing reports is passive; detonating your own file is a disclosure decision.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Joe Security's sandbox is a well-established, respected automated malware-analysis platform used across the DFIR industry.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Joe Sandbox
- Joe Security sandbox
tags:
- documents-metadata
- malware
- sandbox
- dfir
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Joe Sandbox Document Analyzer

> A deep automated malware sandbox — detonate a document, executable, or URL and get a full behavioural report with a threat score and extracted network IOCs.

## When to use
You have a suspicious file (malicious Office doc, PDF, executable) or URL and need to know what it *does*: dropped files, registry/process activity, and the `domain`s/`ip-address`es it contacts. Joe Sandbox runs it in an instrumented VM and produces a detailed report — far more than a static hash lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.joesandbox.com/ (Joe Sandbox Cloud); register for the free Basic tier or search existing public reports by hash first.
2. Submit the file/URL (mind the public-disclosure OpSec note) and select the target environment.
3. Read the report: threat score, behaviour graph, dropped files, and network IOCs (contacted `domain`s/`ip-address`es).
4. Pivot: extracted C2 `domain`s/`ip-address`es feed reputation tools (`[[alienvault-open-threat-exchange]]`, `[[malwareurl]]`); the verdict classifies the file.

## Inputs → Outputs
- **In:** a file or URL (referenced by hash/`document-id`)
- **Out:** behavioural report, threat score, and network IOCs (`domain`, `ip-address`)
- **Empty/negative result looks like:** a benign verdict/low score, or a sample that didn't detonate (evasive malware detecting the sandbox, or needing specific triggers/args).

## Gotchas & OpSec
- Free-tier submissions are PUBLIC — never upload sensitive/attributable samples there; search by hash first, and use a private tier for confidential work.
- Sandbox-evasive malware may behave benignly; a clean report isn't proof of safety.
- Account required for submission.

## Overlaps ("do both")
- Complements `[[virusshare-com]]` (sample corpus), `[[koodous]]` (Android), and multi-engine scanners — Joe Sandbox gives dynamic behaviour; cross-check the verdict and IOCs with other engines.

## Trust & verifiability
`trust: trusted` — an industry-standard automated analysis platform; its behavioural findings are strong, but corroborate a critical verdict with a second sandbox/scanner.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | joesandbox-document-analyzer |
| category | documents-metadata |
| selectorsIn → selectorsOut | document-id → domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
