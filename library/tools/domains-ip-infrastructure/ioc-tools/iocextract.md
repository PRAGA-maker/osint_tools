---
id: iocextract
name: iocextract
description: Use when you have text with defanged/obfuscated indicators and want them extracted and refanged — returns clean IOCs (domains, IPs, URLs, hashes, emails).
url: https://github.com/InQuest/iocextract
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ioc-tools
bestFor: Pulling IOCs out of messy text, including defanged ones (hxxp, 1.1.1[.]1), and normalising them back to usable form.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open source (InQuest, GPL). pip-installable Python library and CLI.
opsec: passive
opsecNote: Runs locally over text you provide with no network calls, so nothing about your source material leaves your machine. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by InQuest, a reputable threat-intelligence vendor; widely used, auditable open-source library.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- omnibus
- threatingestor
aliases:
- iocextract
tags:
- ioc-extraction
- deobfuscation
- python-lib
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# iocextract

> An IOC extractor that understands *defanging*: it finds indicators even when they're written `hxxps://bad[.]com` or `8.8.8[.]8`, and can refang them back to usable form.

## When to use
You have raw text — a threat report, an email, a chat log, a paste — that mentions indicators, and you want them extracted programmatically. iocextract's distinguishing feature is handling the deliberately "defanged" IOCs analysts write to avoid accidental clicks, and optionally refanging them so you can act on them. It's an extraction/normalisation helper feeding infrastructure work; missing-persons relevance is low and indirect.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install iocextract`.
2. Run over a file or stdin:
   ```
   iocextract < report.txt
   cat report.txt | iocextract --refang
   ```
   Or in Python: `iocextract.extract_iocs(text, refang=True)`, plus type-specific `extract_urls`, `extract_ips`, `extract_hashes`, `extract_emails`.
3. Read the extracted, optionally refanged IOCs.
4. Pivot: feed refanged `domain`s/`ip-address`es/URLs into passive DNS, `[[alienvault-otx]]`, GreyNoise, or a sandbox for enrichment.

## Inputs → Outputs
- **In:** free text containing (possibly defanged) indicators
- **Out:** extracted `domain`s, `ip-address`es, URLs, hashes, emails — refanged on request
- **Empty/negative result looks like:** nothing extracted — the text has no recognisable indicators, or they're obfuscated in a scheme iocextract doesn't model; try a different extractor or manual review.

## Gotchas & OpSec
- Extraction is regex-based — verify a sample against the source, especially refanged values you intend to visit.
- Handles common defang styles; exotic/one-off obfuscation may still slip through.
- **Refanged IOCs are live** — a refanged URL is clickable/reachable; don't accidentally visit a malicious host without proxying.
- OpSec: passive/local.

## Overlaps ("do both")
- Directly comparable to `[[ioc-parser]]` (both extract IOCs; iocextract's edge is deobfuscation/refang) and feeds pipeline tools `[[threatingestor]]` / `[[omnibus]]`. Run alongside ioc-parser when a report mixes clean and defanged indicators.

## Trust & verifiability
`trust: trusted` — a reputable InQuest open-source library; because it's regex extraction, spot-check refanged indicators before acting, and never visit a refanged malicious URL unproxied.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iocextract |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
