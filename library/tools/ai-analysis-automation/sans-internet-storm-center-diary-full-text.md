---
id: sans-internet-storm-center-diary-full-text
name: SANS Internet Storm Center Diary (Full Text)
description: Use when you want an authoritative, monitorable feed of emerging threats and attack patterns — the full-text RSS of SANS ISC handler diaries, for tracking IOCs and campaigns (no subject selectors).
url: https://isc.sans.edu/rssfeed_full.xml
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Subscribing to SANS Internet Storm Center handler diaries in full text to monitor new threats, scanning trends, and indicators of compromise.
selectorsIn: []
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free public RSS feed; no account or key.
opsec: passive
opsecNote: You're pulling a public RSS feed from SANS — entirely passive, revealing nothing about a subject. Any IOCs (IPs/domains) you then investigate are separate actions with their own footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: SANS Internet Storm Center is a long-standing, authoritative volunteer-analyst security operation; its handler diaries are well-sourced and reliable threat reporting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- dshield-api
aliases:
- SANS ISC Diary
- Internet Storm Center RSS
tags:
- osint-rss-feeds
- threat-intel
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# SANS Internet Storm Center Diary (Full Text)

> The full-text RSS of SANS ISC handler diaries — authoritative daily analysis of emerging threats, scanning activity, and IOCs you can pull straight into a reader or pipeline.

## When to use
You want to **stay ahead of and contextualise** current threats rather than look up a specific person. Subscribe to this feed to track new attack campaigns, exploited CVEs, malware, and the IP/domain indicators SANS handlers publish. In an investigation it helps you recognise whether an IP/domain you're seeing matches a known ongoing campaign, and it feeds threat-intel automation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Add `https://isc.sans.edu/rssfeed_full.xml` to an RSS reader, or fetch it in a script/SIEM pipeline (it's XML, easy to parse).
2. Read the full diary entries (full-text feed, so no click-through needed) for analysis and any published indicators.
3. Extract IOCs — `ip-address`/`domain` values, hashes — mentioned in a diary relevant to your case.
4. Correlate those indicators against your own findings; pivot IPs/domains into WHOIS, passive DNS, and reputation tools.
5. Pair with the SANS/DShield data APIs for structured indicator queries.

## Inputs → Outputs
- **In:** none (a subscription feed — you consume it)
- **Out:** threat analysis plus published `ip-address`/`domain` indicators of compromise
- **Empty/negative result looks like:** N/A for a feed; the limitation is relevance — most entries won't touch your specific case, so scan for the ones that do.

## Gotchas & OpSec
- It's **threat-intel context**, not a people-finder — its OSINT value is recognising and enriching infrastructure indicators, not locating individuals.
- Full-text feed can be high-volume; filter/keyword it in your reader to surface what matters.
- Fully passive; SANS just sees a feed request.

## Overlaps ("do both")
- Pairs with [[dshield-api]] — the diary gives the human analysis and narrative, DShield gives the structured attack/IP data behind it; use the feed to spot a campaign and the API to query indicators programmatically.

## Trust & verifiability
`trust: trusted` — SANS ISC is an authoritative, long-running security-analysis source; its diaries are well-sourced, though you should still validate any single indicator before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sans-internet-storm-center-diary-full-text |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  → ip-address, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
