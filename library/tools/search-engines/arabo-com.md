---
id: arabo-com
name: ArabO
description: Use when you have a `name`, business, or topic in the Arab world and want Arabic-language sites a Western engine misses — returns social-profile, domain, and directory leads.
url: http://arabo.com/
category: search-engines
path:
- search-engines
bestFor: Finding Arabic-language websites, businesses, and directory listings across the Arab region.
selectorsIn:
- name
- domain
selectorsOut:
- domain
- social-profile
- employer-org
status: live
pricing: free
costNote: Free to search and browse the directory; no account required.
opsec: passive
opsecNote: A directory/search query leaks only to ArabO, not to the subject. The site aggressively blocks automation and datacenter IPs (403), so query from a normal residential-style browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent Arabic web directory and search portal (operating since 2003); a curated third-party index, not an authoritative record.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ArabO
- arabo.com
- ArabO Arab Search Engine
tags:
- arabic
- web-directory
- regional-search
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# ArabO

> An Arabic-language web directory and search portal: category-organized listings of Arab-region sites and businesses that mainstream engines under-index.

## When to use
Your subject or their business is in the Arabic-speaking world and Google/Bing surface little in Arabic. ArabO is a curated, category-based directory (news, business, education, technology) plus a custom search over Arab-region sites — useful for locating an Arabic company site, a regional social/forum presence, or a topical directory entry you can then translate and pivot from.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://arabo.com/ (or the home page at /home.html) in a normal browser session.
2. Use the custom search box with an Arabic or transliterated `name`/business term, or browse the category tree (e.g. Business, Education, International).
3. Follow directory listings out to the target sites; use a translation layer if you don't read Arabic.
4. Read each linked site for a `domain`, contact details, or social handles.
5. Pivot: a discovered `domain` feeds WHOIS; an Arabic business name feeds regional corporate registries and social search.

## Inputs → Outputs
- **In:** `name` / business / topic (Arabic or transliterated), or a `domain`
- **Out:** directory listings resolving to `domain`s, `employer-org` sites, and `social-profile`/contact leads
- **Empty/negative result looks like:** a bare category page or no matches — the directory is curated and incomplete, so absence here doesn't mean the entity has no web presence.

## Gotchas & OpSec
- The site returns 403 to automation, VPNs, and datacenter IP ranges; browse manually from a clean session.
- It is a hand-curated directory, so coverage is uneven and some listings are stale.
- Arabic-language content — plan for transliteration/translation of both queries and results.
- OpSec: passive; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with general engines and Yamli/Arabic keyboard tools — ArabO's editorial directory catches regional sites that pure crawlers rank poorly, while a general engine catches the fresh long tail.

## Trust & verifiability
`trust: community` — an independent, human-curated Arabic directory running since 2003; treat listings as leads to verify at the source, not as authoritative records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arabo-com |
| category | search-engines |
| selectorsIn → selectorsOut | name, domain → domain, social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
