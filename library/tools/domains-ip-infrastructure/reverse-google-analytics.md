---
id: reverse-google-analytics
name: Reverse Google Analytics
description: Use when you have a `domain` and want the other sites run by the same operator — finds domains sharing its Google Analytics/AdSense tracking ID, returning linked `domain`s.
url: https://osint.sh/analytics/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Linking multiple websites to one owner by matching the Google Analytics / AdSense ID they embed.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free browser tool in the osint.sh suite; heavy/bulk use points toward its paid API.
opsec: passive
opsecNote: You query osint.sh's crawled dataset of tracking IDs, not the target site, so the lookup is passive toward the subject. osint.sh learns which domain you're pivoting on.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of the well-known osint.sh toolset; matches depend on the crawl's coverage and freshness, and shared IDs occasionally reflect a shared agency rather than a shared owner.
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
- reverse-ip-lookup
aliases:
- osint.sh analytics
- reverse analytics ID
tags:
- Domain/IP/Links
- tracking-id
- attribution
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Reverse Google Analytics

> One of the strongest ownership pivots on the web: find every site that embeds the same Google Analytics / AdSense ID as your target, exposing an operator's whole portfolio.

## When to use
You have a `domain` and suspect the same person/organisation runs others — a scam network, a set of sockpuppet sites, a subject's personal and business pages. Site owners reuse one Google Analytics (`UA-`/`G-`) or AdSense (`pub-`) code across their properties, so matching that ID links the sites even when WHOIS is private and hosting differs. This is a top technique for de-anonymising a cluster of related domains.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.sh/analytics/.
2. Enter the target `domain` (the tool extracts its tracking IDs) — or paste a known `UA-`/`G-`/`pub-` ID directly.
3. Read the returned list of other `domain`s carrying the same ID.
4. Judge each hit: a shared code is a strong link, but confirm it's the *same* ID (not just the same platform) and rule out a shared marketing agency/template.
5. Pivot the linked domains into WHOIS, [[reverse-ip-lookup]], and content comparison to build the ownership map.

## Inputs → Outputs
- **In:** `domain` (or a raw Analytics/AdSense ID)
- **Out:** `domain` list sharing that tracking ID
- **Empty/negative result looks like:** "no other sites found" — the target uses a unique/absent ID, the code isn't in the crawl, or the site uses a tag manager the crawler didn't parse; absence isn't proof of no siblings.

## Gotchas & OpSec
- **Confirm the ID is really shared** — view the target's page source yourself to verify the code; databases can be stale or misattributed.
- Shared IDs sometimes mean a shared **agency/developer**, not a shared owner — corroborate before asserting one person runs all the sites.
- Modern sites load Analytics via Google Tag Manager, which can hide the raw ID from simple crawlers; check GTM containers manually.
- Passive toward the target; only osint.sh sees your query.

## Overlaps ("do both")
- Pairs with [[reverse-ip-lookup]] and WHOIS — tracking-ID overlap, shared hosting, and registrant data are independent signals; a cluster confirmed by two of them is far stronger than any one alone.

## Trust & verifiability
`trust: community` — a reputable free tool surfacing a third-party crawl of tracking IDs; treat matches as strong leads to verify in the sites' own source, not as proof on their own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reverse-google-analytics |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
