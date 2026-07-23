---
id: ip2whois
name: IP2WHOIS
description: Use when you have a `domain` and want its WHOIS registration — returns registrant `name`/`email`/`address` (when not redacted), registrar and registration dates.
url: https://www.ip2whois.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: Free WHOIS lookups for a domain — registrant contact, registrar and registration/expiry dates.
selectorsIn:
- domain
selectorsOut:
- name
- email
- address
status: live
pricing: free
costNote: Free web lookup from IP2Location; a free API key (with a monthly query quota) is available for programmatic use.
opsec: passive
opsecNote: Queries public WHOIS data via IP2Location, not the target domain, so the registrant sees nothing. IP2Location logs your lookups; use a clean session for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by IP2Location, an established IP/geolocation data vendor; the WHOIS data is sourced from registries and is a convenient free front-end rather than an authoritative registry itself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- IP2WHOIS
- ip2whois.com
tags:
- whois-records
- domain-and-ip-research
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# IP2WHOIS

> IP2Location's free WHOIS lookup: enter a `domain` and get its registration record — registrant contact (where public), registrar, nameservers and key dates.

## When to use
You have a `domain` and want the classic WHOIS pivot: who registered it, through which registrar, and when. Registration dates alone are valuable (a domain created days before a scam launched is a red flag), and where the registrant's details aren't redacted you get a `name`, `email` and `address` to run further. It's a quick, no-account front-end for WHOIS.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ip2whois.com and enter the `domain`.
2. Read the record: registrant/admin/tech contact (if not privacy-protected), registrar, creation/updated/expiry dates, nameservers.
3. For bulk/automation, register a free API key and query the endpoint within the monthly quota.
4. Note redaction — if contacts show a privacy service, that itself is a data point.
5. Pivot: a registrant `email`/`name` feeds account and breach tooling; nameservers/registrar cluster related domains; creation date anchors a timeline.

## Inputs → Outputs
- **In:** `domain`
- **Out:** registrant `name`/`email`/`address` (when public), registrar, nameservers, creation/expiry dates
- **Empty/negative result looks like:** contacts replaced by a privacy/proxy service (very common post-GDPR), or "no match" for an unregistered/ccTLD domain the source doesn't cover. Redaction ≠ no owner; it's just hidden here.

## Gotchas & OpSec
- Most modern WHOIS records are privacy-protected or GDPR-redacted, so expect registrar + dates more often than a real name; historical WHOIS tools may still hold the pre-redaction owner.
- It's a third-party front-end — cross-check anything critical against the registry/registrar directly.
- OpSec: passive — the domain owner isn't contacted.

## Overlaps ("do both")
- Pairs with historical-WHOIS services and registry Whois like `[[whois-arin-online]]` — IP2WHOIS gives the current record fast, while historical WHOIS can recover the registrant from before privacy protection was applied.

## Trust & verifiability
`trust: community` — a reputable vendor's convenient WHOIS front-end; the underlying data comes from registries, so verify decision-critical details at the authoritative registrar/registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip2whois |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → name, email, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
