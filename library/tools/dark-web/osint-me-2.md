---
id: osint-me-2
name: osint.me 2
description: Use when you need vetted, working dark-web OSINT starting points — returns a curated, tested list of Tor search engines, directories and resource domains.
url: https://www.osintme.com/index.php/2022/11/10/dark-web-osint-new-working-links-and-resources/
category: dark-web
path:
- dark-web
bestFor: A curated, tested reading list of working dark-web search engines, directories and resources.
selectorsIn: []
selectorsOut:
- domain
status: live
pricing: free
costNote: Free blog article; no account or payment.
opsec: passive
opsecNote: Reading the article is passive. The .onion links it lists are not — visiting any of them requires Tor and reaches live hidden services, so use a hardened Tor Browser / isolated VM and never trust dark-web sellers (the author warns ~95% are scams).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by "Matt" at osintme.com, an established independent OSINT blog; links were tested at publication (Nov 2022) but dark-web links rot fast, so re-verify before relying on any.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osint-me-1
- osint-me-3
- osint-list-of-public-sex-offenders-registers-osintme-com
aliases:
- osintme dark web osint
- osint.me dark web links
tags:
- darkweb
- Dark Web Links
- resource-list
source: uk-osint
lastVerified: '2026-08-04'
enrichment: full
---

# osint.me 2

> A curated, hand-tested reading list of working dark-web OSINT resources — Tor search engines, directories and hosting — from the osintme.com blog.

## When to use
You are starting a dark-web investigation and need reliable entry points rather than a random link dump. This article collects Tor search engines, directory services, hosting providers and educational material that the author tested as functional, plus a blunt warning that nearly all darknet vendors are scams. It's an orientation/resource page, not a search tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the article at https://www.osintme.com/index.php/2022/11/10/dark-web-osint-new-working-links-and-resources/ on the clearnet.
2. Read the categorised sections: Tor search engines, directories, hosting, educational, and misc forums/blogs.
3. Copy the specific resource (search engine / directory `domain`) you need into a hardened **Tor Browser** running in an isolated VM.
4. Re-verify each link is still live before relying on it — the list was accurate in 2022 and onion services churn.
5. Pivot: a working Tor search engine from the list becomes your query surface; findings there feed archiving (`[[darkweb-archive]]`) and selector extraction.

## Inputs → Outputs
- **In:** none (a reading/resource page)
- **Out:** a curated set of dark-web resource `domain`s (Tor search engines, directories, hosting)
- **Empty/negative result looks like:** a listed onion link that no longer resolves — expected for older entries; move to the next resource rather than assuming the whole page is stale.

## Gotchas & OpSec
- Link rot: tested in 2022; re-check each before use.
- The links lead to live hidden services — only open them through Tor in an isolated environment, never a normal browser.
- Heed the author's scam warning: do not transact with darknet "sellers."

## Overlaps ("do both")
- Sits alongside sibling osintme guides `[[osint-me-1]]` and `[[osint-me-3]]` (other topic areas of the same blog) and feeds `[[darkweb-archive]]` once you've reached a page worth preserving.

## Trust & verifiability
`trust: community` — a respected independent OSINT blog; the curation is knowledgeable and was verified at publication, but it's a personal resource list, so treat every link as needing fresh verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-me-2 |
| category | dark-web |
| selectorsIn → selectorsOut |  → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
