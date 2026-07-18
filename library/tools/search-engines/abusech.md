---
id: abusech
name: abuse.ch
description: Use when you have a `domain`, `ip-address`, URL, or file hash and want to know if it is linked to malware, botnets, or phishing — returns `domain`, `ip-address`, `associate` (threat infrastructure).
url: https://hunting.abuse.ch
category: search-engines
path:
- search-engines
bestFor: Checking whether a domain/IP/URL/hash is tied to known malware, C2, or phishing infrastructure.
selectorsIn:
- domain
- ip-address
- document-id
selectorsOut:
- domain
- ip-address
- associate
status: live
pricing: free
costNote: Free threat-intelligence platform (community project, now under the Institute for Cybersecurity and Engineering); a free account/Auth-Key is needed for the API and some bulk features, but web lookups are free.
opsec: passive
opsecNote: You query abuse.ch's databases, not the malicious host itself, so you don't touch the adversary's infrastructure. Signing up for an API key ties activity to that account — use an appropriate one.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: trusted
trustNote: A widely-trusted, long-running threat-intel project (MalwareBazaar, URLhaus, ThreatFox, Feodo Tracker) used across the security industry; data is community-contributed but curated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- malwarebazaar
- urlhaus
- yaraif
- zeus-c2-tracker
- zeus-tracker
tags:
- speciality-search-engines
- threat-intelligence
- malware
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# abuse.ch

> A cluster of free threat-intelligence databases (URLhaus, MalwareBazaar, ThreatFox, Feodo Tracker) — check a `domain`, `ip-address`, URL, or file hash for links to malware, botnet C2, and phishing.

## When to use
You have a technical indicator — a `domain`, `ip-address`, URL, or malware hash — surfaced during an investigation and you need to know whether it's part of known malicious infrastructure. abuse.ch tells you if a domain hosts malware payloads (URLhaus), if a hash is known malware (MalwareBazaar), if an IP/domain is a known C2 (ThreatFox, Feodo Tracker). In a missing-persons or fraud context it's a supporting tool: it flags whether infrastructure tied to a scam, sextortion, or phishing lure is part of a wider tracked campaign, and surfaces related indicators to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the relevant abuse.ch portal (start at https://hunting.abuse.ch, or go direct: urlhaus.abuse.ch, bazaar.abuse.ch, threatfox.abuse.ch).
2. Search your indicator — paste the `domain`, `ip-address`, URL, or file hash.
3. Read the result: whether it's a known bad indicator, the malware family/campaign, first/last seen dates, and linked indicators.
4. For automation/bulk, register for a free Auth-Key and use the API.
5. Pivot: linked domains/IPs/hashes are `associate` infrastructure leads; a named malware family or campaign feeds wider threat-intel searches.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, URL, or file hash (`document-id`)
- **Out:** `domain` / `ip-address` (related indicators), `associate` (shared campaign/C2 infrastructure), malware-family/campaign labels
- **Empty/negative result looks like:** "no results" for the indicator — it isn't in abuse.ch's tracked datasets; that means "not known-bad here," not "safe." Cross-check other threat feeds.

## Gotchas & OpSec
- Human-in-the-loop: web lookups are free and open; the API and some bulk features require a free registered Auth-Key.
- OpSec: passive — you query abuse.ch, never the malicious host. Keep any API key on an appropriate account.
- Scope: this is malware/threat infrastructure, not person data — low direct missing-persons value; use it to validate and expand technical indicators.

## Overlaps ("do both")
- Pairs with `[[urlhaus]]` and `[[malwarebazaar]]` (its own sub-services) and general domain/IP tools — abuse.ch confirms malicious reputation, while whois/passive-DNS tools give ownership/hosting context. Do both on a suspect indicator.

## Trust & verifiability
`trust: trusted` — a long-established, industry-relied-upon threat-intel project; data is community-contributed but curated, so a positive hit is high-signal (confirm campaign attribution against a second feed).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | abusech |
| category | search-engines |
| selectorsIn → selectorsOut | domain, ip-address, document-id → domain, ip-address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (api-key) |
