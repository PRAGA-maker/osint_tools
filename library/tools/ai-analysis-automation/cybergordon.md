---
id: cybergordon
name: CyberGordon
description: Use when you have an `ip-address`, `domain`, `email`, or file hash and want a one-query reputation/threat check across dozens of sources — returns aggregated risk verdicts and enrichment.
url: https://cybergordon.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Fanning a single indicator (IP, domain, URL, email, hash) out across many threat-intel and reputation engines in one lookup.
selectorsIn:
- ip-address
- domain
- email
selectorsOut:
- ip-address
- domain
status: live
pricing: freemium
costNote: Free web interface for interactive lookups; heavier/automated use and some engines may require an account or paid plan.
opsec: passive
opsecNote: CyberGordon queries third-party reputation databases about the indicator, not the indicator's owner — so it is passive with respect to your target. Note that submitting an indicator shares it with CyberGordon and downstream engines; don't submit sensitive case data you need to keep confidential.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-regarded community IOC aggregator; results are only as good as the underlying engines it queries, and it adds no independent verification of its own.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Cyber Gordon
tags:
- threat-intelligence
- ioc-enrichment
- reputation
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# CyberGordon

> A one-box IOC enrichment service — paste an IP, domain, URL, email, or hash and it queries dozens of reputation/threat-intel engines, returning consolidated verdicts.

## When to use
You have an indicator — an `ip-address`, `domain`, `email`, URL, or file hash — and want a fast, broad reputation and threat check without visiting each engine (VirusTotal, AbuseIPDB, urlscan, etc.) individually. Ideal for triaging a suspicious IP/domain in an investigation and deciding whether it warrants a deeper look.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cybergordon.com.
2. Paste one or more indicators (it auto-detects type) into the query box and run.
3. Read the aggregated results table: each source's verdict/score and any enrichment (geo, ASN, categorisation).
4. Click through to individual engines for the raw detail behind a flag.
5. Pivot: a malicious/dirty verdict feeds deeper infrastructure OSINT (WHOIS, passive DNS, hosting); a clean-but-interesting result feeds content/registrant analysis.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, `email`, URL, or hash
- **Out:** aggregated reputation verdicts and enrichment across multiple engines (`ip-address`/`domain` context)
- **Empty/negative result looks like:** all engines return "unknown/clean" — the indicator isn't in their datasets, which is weak evidence of safety, not proof.

## Gotchas & OpSec
- **Aggregator, not an authority**: it relays other engines' verdicts and adds no independent check — always confirm a critical flag at the source engine.
- Submitting an indicator shares it downstream; avoid pasting confidential case identifiers.
- Free-tier engine coverage/rate limits may vary; a missing engine can change the picture.

## Overlaps ("do both")
- Pair with the individual engines it fronts (VirusTotal, AbuseIPDB, urlscan) and with `[[honeydb]]`-style feeds — CyberGordon is the fast wide pass; the source engines give the authoritative, detailed verdict.

## Trust & verifiability
`trust: community` — a respected community aggregator, but its value is convenience, not authority; every verdict must be traced back to the engine that produced it for verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cybergordon |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | ip-address, domain, email → ip-address, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
