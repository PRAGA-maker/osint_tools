---
id: tweetfeed
name: TweetFeed
description: Use when you have a suspicious domain, URL, or IP and want to check whether the infosec community has flagged it as a live IOC — returns matching domains/URLs/IPs/hashes.
url: https://tweetfeed.live/
category: social-networks
path:
- social-networks
bestFor: Checking a domain/URL/IP/hash against recent community-shared Indicators of Compromise (IOCs) from Twitter/X.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free live IOC feeds via web dashboard, CSV export on GitHub, and an API; no account required.
opsec: passive
opsecNote: You browse or download an aggregated public IOC list; nothing about your subject is submitted and no target is contacted. Fully passive — pulling the CSV/API leaks nothing about your investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates IOCs shared by the #infosec community on Twitter/X; the maintainer notes confidence is not always 100%, so use for threat-hunting/watchlists, not blind blocklisting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- TweetFeed.live
- tweetfeed live IOC feed
tags:
- Social Media
- Twitter
- threat-intel
- ioc-feed
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# TweetFeed

> A free live feed of Indicators of Compromise (malicious domains, URLs, IPs, and file hashes) crowd-sourced from the infosec community on Twitter/X.

## When to use
You have a suspicious `domain`, URL, `ip-address`, or file hash tied to a case — a phishing link a subject received, a server an investigation touches, a malware sample — and want to know if the security community has recently reported it as malicious. This is a threat-intelligence resource, not a people-finder; in an OSINT investigation it helps you triage infrastructure and links (e.g. flag a scam/phishing domain in a fraud or romance-scam angle) rather than locate a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tweetfeed.live/ and use the filterable tables (URLs, Domains, IPs, SHA256, MD5).
2. Search/filter for your indicator; a match shows the IOC, the reporting tweet/source, and date.
3. For automation, pull `today.csv` from the linked GitHub, or use the API / a SIEM integration (OpenCTI, MISP, Splunk, QRadar).
4. Pivot: a confirmed malicious domain/IP feeds WHOIS and IP-infrastructure tools to map the actor's other assets.

## Inputs → Outputs
- **In:** `domain` / URL / `ip-address` / file hash to check
- **Out:** matching IOC records (`domain`, `ip-address`, URLs, hashes) with source tweet and date
- **Empty/negative result looks like:** no match — meaning the indicator hasn't been shared to TweetFeed recently, NOT that it's safe; absence is not clearance. Confidence on hits is also not guaranteed.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully passive — you consume an aggregated public list; nothing about your subject or infrastructure is disclosed.
- Community-sourced: false positives and stale entries occur; corroborate a hit before acting, and never use it as a sole blocklist source.

## Overlaps ("do both")
- Pairs with WHOIS/IP-reputation tools and `[[scamadvisor]]` — TweetFeed tells you if the community flagged an indicator; those give registration/reputation depth on it.

## Trust & verifiability
`trust: community` — crowd-sourced from infosec Twitter/X with no formal vetting; the maintainer explicitly caps confidence. Excellent for leads and watchlists; verify each hit independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tweetfeed |
| category | social-networks |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
