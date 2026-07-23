---
id: threatpinch-lookup
name: ThreatPinch Lookup
description: Use when you're reading a page full of IOCs (`ip-address`, `domain`, hashes, `email`) and want hover-to-enrich tooltips pulling threat-intel from many sources at once — returns inline reputation/enrichment without leaving the page.
url: https://github.com/cloudtracer/ThreatPinchLookup
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ioc-tools
bestFor: In-browser hover enrichment of IOCs (IP, domain, hash, email, CVE) across many threat-intel sources at once.
selectorsIn:
- ip-address
- domain
- email
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open source; installs as a Chrome/Firefox extension. Some data sources need your own free API keys entered in the settings.
opsec: passive
opsecNote: Enrichment queries go to third-party threat-intel APIs, not the target — but every IOC you hover is sent to those services, so assume your lookups are visible to each configured provider. Add only keys/sources you're comfortable exposing your indicators to.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source browser extension with a public GitHub repo; auditable, though it aggregates many third-party APIs whose availability and quality vary.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- ThreatPinchLookup
- cloudtracer/ThreatPinchLookup
tags:
- ioc-tools
- threat-intel
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# ThreatPinch Lookup

> A browser extension that turns any IOC on a page into a hover tooltip of enrichment — highlight or mouse over an IP, domain, hash, email or CVE and it pulls reputation/intel from dozens of configured sources inline.

## When to use
You're triaging a report, a paste, an email header or a log full of indicators and don't want to copy each one into a dozen lookup sites. ThreatPinch enriches IOCs where you read them: hover an `ip-address`, `domain`, hash or `email` and get a consolidated tooltip (WHOIS, reputation, passive DNS, VirusTotal-style verdicts) from whichever sources you've enabled.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the ThreatPinch Lookup extension (Chrome/Firefox) from the repo/store.
2. Open its settings and enable the lookup sources you want; paste your own free API keys where a source requires one.
3. Browse to any page containing indicators.
4. Hover (or select) an IOC — a tooltip pops with enrichment from each configured source.
5. Pivot: a flagged domain/IP feeds deeper infra tooling; a linked `domain`/`ip-address` in the results becomes your next lookup.

## Inputs → Outputs
- **In:** IOCs on any web page — `ip-address`, `domain`, `email`, hashes, CVEs
- **Out:** inline enrichment tooltips → reputation verdicts, related `domain`s/`ip-address`es, WHOIS/passive-DNS snippets
- **Empty/negative result looks like:** a tooltip with empty/"no data" sections — usually a source without an API key configured, a rate-limited provider, or a genuinely unknown indicator. Enable more sources before concluding an IOC is clean.

## Gotchas & OpSec
- It's only as good as the sources you enable and the API keys you add; out of the box, coverage is limited.
- Every hovered IOC is transmitted to each enabled provider — don't enrich sensitive/internal indicators against services you don't trust.
- OpSec: passive toward the target, but exposes your indicators to third-party intel providers.

## Overlaps ("do both")
- Pairs with standalone lookups (WHOIS, passive-DNS like `[[mnemonic]]`, VirusTotal) — ThreatPinch is the fast in-context triage layer, while the standalone tools give you the full, unabridged record for anything that looks important.

## Trust & verifiability
`trust: community` — auditable open-source extension; the enrichment quality depends entirely on the third-party sources and keys you configure, so verify critical verdicts at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | threatpinch-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain, email → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
