---
id: cisco-umbrella-popularity-list
name: Cisco Umbrella Popularity List
description: Use when you have a `domain` and want to gauge how popular/common it is in global DNS traffic — returns a top-1-million ranking (present-and-ranked, or absent) as context.
url: https://s3-us-west-1.amazonaws.com/umbrella-static/index.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- analytics
bestFor: Quickly judging whether a domain is a mainstream high-traffic site or an obscure one, from DNS-based popularity ranking.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free downloadable CSV (top-1m.csv.zip); no account or key required.
opsec: passive
opsecNote: Fully passive — you download a static, aggregated ranking file from an S3 bucket and grep it offline. No query touches the domain in question, so there is zero exposure to any target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Cisco Umbrella (OpenDNS) from its global DNS resolver traffic; a widely-cited domain-popularity dataset in security research.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Umbrella 1 Million
- Cisco Umbrella top 1m
- OpenDNS popularity list
tags:
- domain-popularity
- dns
- dataset
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Cisco Umbrella Popularity List

> A daily-generated ranking of the top 1 million domains by DNS query volume across Cisco Umbrella's global resolvers — a quick way to tell a mainstream domain from an obscure one.

## When to use
You have a `domain` and want context on how common or trafficked it is: is it a top-tier mainstream site, a mid-popularity service, or something so obscure it doesn't rank at all? Reach for this when triaging domains — e.g. deciding whether a lookalike/phishing domain is established, or whether an unfamiliar host is broadly used. Unlike a click-based web ranking, this is DNS-based, so it captures API/CDN/background domains that web-only rankings miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://s3-us-west-1.amazonaws.com/umbrella-static/index.html and download `top-1m.csv.zip`.
2. Unzip; the CSV is simply `rank,domain` for the top 1,000,000 domains.
3. Grep for your target domain to get its rank (lower = more popular), or confirm it's absent.
4. Compare ranks across candidate domains to judge relative reach.
5. Pivot: an unranked or very-low-rank domain paired with a mainstream lookalike is a phishing/typosquat signal; a high rank corroborates that a service is legitimate/widely used.

## Inputs → Outputs
- **In:** `domain`
- **Out:** a numeric popularity rank within the top 1M (or "not present")
- **Empty/negative result looks like:** the domain isn't in the top 1M — meaning it's below the popularity floor, common for niche, new, or malicious domains; it says nothing about legitimacy on its own.

## Gotchas & OpSec
- DNS-based ranking counts *queries*, so CDN, telemetry, and ad domains rank high even without human "visits" — interpret accordingly.
- It's a static daily snapshot; a brand-new domain won't appear even if it later becomes popular.
- OpSec: passive and offline once downloaded; ideal for bulk work with no exposure.

## Overlaps ("do both")
- Complements web-traffic rankings (Tranco, historical Alexa) and WHOIS/age data — popularity plus registration age together separate established sites from freshly-spun phishing domains. Cross-check rank against a second list, since methodologies differ.

## Trust & verifiability
`trust: trusted` — an authoritative, widely-used dataset published by Cisco Umbrella from real resolver traffic; the ranking is a reliable relative-popularity signal, though its DNS-query basis should frame how you read it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cisco-umbrella-popularity-list |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
