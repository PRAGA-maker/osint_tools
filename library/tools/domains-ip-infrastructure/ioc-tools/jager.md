---
id: jager
name: Jager
description: Use when you have documents/pages and want to pull out indicators — extracts and aggregates IOCs (`domain`, `ip-address`, hashes, `email`) into a standardized set.
url: https://github.com/sroberts/jager
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ioc-tools
bestFor: Extracting and aggregating indicators of compromise (domains, IPs, emails, hashes, URLs) from reports, PDFs and text into a structured format.
selectorsIn:
- domain
- ip-address
- email
selectorsOut:
- domain
- ip-address
- email
status: live
pricing: free
costNote: Free and open-source (Python) on GitHub; run locally. No account.
opsec: passive
opsecNote: Runs locally over documents you already hold — it does not contact the indicators it extracts. Passive. (Any later enrichment/resolution of those IOCs is a separate, potentially active step.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: An open-source utility by sroberts (a known threat-intel author); auditable, but a personal project — validate extracted IOCs before acting on them.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- cacador
aliases:
- jager IOC extractor
tags:
- ioc-tools
- threat-intelligence
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Jager

> A local IOC extractor — pulls domains, IPs, emails, hashes and URLs out of documents and normalises them into a structured set.

## When to use
You have a threat report, PDF, or blob of text (e.g. a phishing analysis, an incident writeup) and want to mechanically pull out every indicator — `domain`s, `ip-address`es, `email`s, file hashes, URLs — into a clean list for triage or enrichment, rather than copy-pasting by hand.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/sroberts/jager (Python; `pip install`/clone).
2. Point it at a document, URL, or text; it parses out and deduplicates IOCs.
3. Take the standardized output (JSON) and feed it into enrichment tools (WHOIS, passive DNS, reputation).
4. The enrichment/resolution step is where active exposure happens — do that from a controlled environment.

## Inputs → Outputs
- **In:** documents/text/URLs containing indicators
- **Out:** structured IOCs — `domain`, `ip-address`, `email`, hashes, URLs
- **Empty/negative result looks like:** few/no IOCs because the source had none in recognisable form, or defanged indicators it did not un-defang — check the input and Jager's parsing options.

## Gotchas & OpSec
- Human-in-the-loop: none, but you need Python tooling.
- OpSec: extraction is passive (local); resolving/enriching the IOCs afterwards can be active — mind that separately.
- It matches patterns — expect some false positives (version strings that look like IPs, etc.); validate before acting.

## Overlaps ("do both")
- Overlaps with `[[cacador]]` and other IOC extractors: they do the same job with different parsing strengths — pick one, or run both and reconcile for completeness on a messy source.

## Trust & verifiability
`trust: unverified` — a respected author's open-source utility; auditable and handy, but validate extracted indicators before you act on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jager |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address, email → domain, ip-address, email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
