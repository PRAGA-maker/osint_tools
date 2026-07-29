---
id: webroot-brightcloud-url-ip-lookup
name: Webroot BrightCloud URL/IP Lookup
description: Use when you have a `domain`, URL, or `ip-address` and want its reputation, web category, and risk score — returns domain, ip-address.
url: https://www.brightcloud.com/tools/url-ip-lookup.php
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Checking the reputation, content category, and risk level of a URL, domain, or IP.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free web lookup (CAPTCHA-gated, limited queries); the underlying BrightCloud reputation data is otherwise sold as a commercial feed/API.
opsec: passive
opsecNote: Passive — you query BrightCloud's reputation database, so the target site/IP is never contacted by you. Your query does go to Webroot/OpenText.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A reputable commercial threat-intelligence vendor (Webroot/OpenText); the category and reputation are its proprietary scoring — a strong signal, not ground truth.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- BrightCloud URL/IP Lookup
- Webroot BrightCloud
tags:
- reputation
- threat-intel
- url-classification
source: arf-seed
lastVerified: '2026-07-29'
relatedTools:
- brightcloud
enrichment: full
---

# Webroot BrightCloud URL/IP Lookup

> A free reputation checker backed by Webroot's commercial threat-intelligence engine — paste a URL, domain, or IP and get its content category, reputation score, and risk level.

## When to use
You have a `domain`, URL, or `ip-address` surfaced in an investigation and want a quick read on **what it is and whether it's malicious**: is it categorised as phishing/malware/spam, what content class does it fall in, and how risky is BrightCloud's score? Useful for triaging a link from a message, deciding whether an IP is a known bad actor, and getting a first content classification before deeper digging.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.brightcloud.com/tools/url-ip-lookup.php.
2. Enter a URL, domain, or IP and solve the CAPTCHA.
3. Read the result: content category, reputation/threat score, risk level, and associated WHOIS/network info.
4. If you disagree with a categorisation, you can request a review (BrightCloud accepts change submissions).
5. Pivot: a "malicious/phishing" verdict corroborates other red flags; the category and network info feed `[[bgpview-io]]` and reputation cross-checks on other engines.

## Inputs → Outputs
- **In:** a `domain`, URL, or `ip-address`
- **Out:** content category, reputation/risk score, and network/WHOIS context for that `domain`/`ip-address`
- **Empty/negative result looks like:** "Uncategorized" / neutral reputation — BrightCloud has no strong signal on it (new or low-traffic asset), which is not the same as "safe."

## Gotchas & OpSec
- **CAPTCHA-gated** and rate-limited on the free tool; heavy use needs the paid API.
- Categories/scores are one vendor's proprietary opinion — a clean BrightCloud verdict isn't proof of safety, and a bad one deserves corroboration.
- Passive to the target, but Webroot logs your queries.

## Overlaps ("do both")
- Pairs with other reputation engines (VirusTotal, URLhaus, other vendors) — reputation feeds disagree, so cross-check a verdict across several before acting on it.

## Trust & verifiability
`trust: community` — output is a commercial vendor's classification; treat it as a strong lead and confirm important verdicts against independent reputation sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webroot-brightcloud-url-ip-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
