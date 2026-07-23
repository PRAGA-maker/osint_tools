---
id: ioc-parser
name: IOC Parser
description: Use when you have a `domain`/threat report (PDF/HTML/text) and want the indicators pulled out — returns structured IOCs (domains, IPs, hashes, URLs).
url: https://github.com/armbues/ioc_parser
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ioc-tools
bestFor: Bulk-extracting indicators of compromise from PDF/HTML/text security reports into CSV/JSON/YARA.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open source (MIT). Installed via pip; runs locally.
opsec: passive
opsecNote: Parses documents locally with no network calls (unless you enable the optional link-fetch), so nothing about your source material leaves your machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Long-standing, widely-forked open-source parser (armbues/ioc_parser); auditable MIT source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- iocp
- ioc_parser
tags:
- ioc-extraction
- threat-intel
- cli
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# IOC Parser

> Feed it a messy threat report; get back a clean, deduplicated list of every domain, IP, hash, and URL it mentions.

## When to use
You have a security report, threat advisory, or any document (`PDF`, `HTML`, or text) and want to machine-extract its indicators of compromise instead of copying them by hand. IOC Parser regexes out `domain`s, `ip-address`es, file hashes, URLs, CVEs, and emails, deduplicates them, and writes CSV/JSON/YARA. It's an extraction/tooling helper feeding infrastructure analysis; missing-persons relevance is low (it accelerates working through documents tied to a case).

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install ioc_parser` (add extras for PDF/HTML support — PyPDF2/pdfminer, BeautifulSoup).
2. Run against a file:
   ```
   iocp -i pdf report.pdf
   iocp -i html page.html -o json
   ```
   `-i` sets input type (pdf/html/txt), `-o` the output format (csv/json/yara), and it deduplicates by default.
3. Read the structured output — each IOC with its type.
4. Pivot: feed extracted `domain`s/`ip-address`es straight into passive DNS, reputation feeds (`[[alienvault-otx]]`, GreyNoise), or WHOIS for enrichment.

## Inputs → Outputs
- **In:** a `PDF`/`HTML`/text document (the `domain`s etc. are inside it)
- **Out:** structured `domain`, `ip-address`, hash, URL, CVE, email indicators (CSV/JSON/YARA)
- **Empty/negative result looks like:** no IOCs extracted — either the document genuinely has none, or (for image-only/scanned PDFs) the text layer is missing; OCR first, then re-parse.

## Gotchas & OpSec
- Scanned/image PDFs have no extractable text — you'll get nothing until you OCR them.
- Regex extraction can defang or mangle intentionally-obfuscated IOCs (`hxxp`, `[.]`); check the pattern file handles the report's defanging style.
- OpSec: passive/local; only the optional "download referenced links" mode touches the network.

## Overlaps ("do both")
- Feeds enrichment tools (`[[alienvault-otx]]`, GreyNoise, passive DNS, WHOIS) — IOC Parser *extracts*, those *enrich*. Comparable to other IOC extractors (e.g. Cacador, iocextract); use whichever handles your input format best.

## Trust & verifiability
`trust: community` — mature, auditable MIT-licensed code; because extraction is regex-based, spot-check a few IOCs against the source document for defanging/false extractions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ioc-parser |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
