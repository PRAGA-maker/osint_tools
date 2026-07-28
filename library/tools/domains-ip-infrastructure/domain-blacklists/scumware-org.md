---
id: scumware-org
name: scumware.org
description: Use when you have a `domain`, `ip-address` or file hash and want to check it against a malware/phishing threat database — returns associated malicious URLs, IPs and classifications.
url: https://www.scumware.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- domain-blacklists
bestFor: Checking whether a domain/IP/hash is catalogued as malicious and pivoting to the URLs/IPs linked to a threat.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free for security/malware researchers; some detailed views require credits earned by solving CAPTCHAs.
opsec: passive
opsecNote: You query scumware.org's own crawl database, not the malicious host, so nothing touches the target infrastructure. Your query is logged by scumware.org.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run threat database populated by automated crawling and user submissions; useful for corroboration, not an authoritative verdict.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- soc-multi-tool
aliases: []
tags:
- malware
- domain-blacklist
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# scumware.org

> A free malware/phishing URL database — check a domain, IP or file hash against catalogued threats and follow the linked indicators.

## When to use
You have a `domain`, `ip-address`, hostname fragment or MD5 hash surfaced in an investigation (a link from a suspect message, a server in a log, an attachment) and want to know whether it's flagged as malicious and what else is tied to it. Relevant for vetting infrastructure and expanding from one bad indicator to related ones — tangential to missing-persons work but useful for infrastructure attribution.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.scumware.org/.
2. Search by MD5 hash, IP address, hostname or URL fragment.
3. Read the threat entries: each shows the malicious URL, associated IP(s), geolocation, and malware classification (e.g. JS.Spy, Trojan.InstallCore).
4. Solve a CAPTCHA to earn credits if a detailed report is gated.
5. Pivot: an associated IP → other hostnames on it; a shared classification/campaign → related URLs.

## Inputs → Outputs
- **In:** `domain` / hostname / `ip-address` / MD5 hash
- **Out:** associated malicious URLs, IPs, geolocation, malware classification
- **Empty/negative result looks like:** "no results" — the indicator isn't in scumware's crawl. That is not clearance; cross-check with a broader engine before concluding it's clean.

## Gotchas & OpSec
- Human-in-the-loop: CAPTCHA-gated credits for some views; automated scraping is prohibited.
- OpSec: **passive** — queries are against scumware's database, not the malicious host. Use a burner session anyway.
- Coverage is partial and community-driven; absence of an entry means little.

## Overlaps ("do both")
- Pairs with `[[soc-multi-tool]]` — SOC Multi-tool checks the same indicator against VirusTotal/AbuseIPDB, so running both gives a multi-source reputation picture instead of one database's view.

## Trust & verifiability
`trust: community` — a volunteer/automated research database; good for leads and corroboration, but classifications and coverage are not authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scumware-org |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
