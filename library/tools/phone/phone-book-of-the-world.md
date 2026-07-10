---
id: phone-book-of-the-world
name: Phone Book of the World
description: Use when you have a `name`/`phone` in a specific country and want its national directory — returns links to that country's white/yellow pages and reverse-lookup services.
url: http://www.phonebookoftheworld.com/
category: phone
path:
- phone
bestFor: A country-by-country directory of national phone books and reverse-lookup services worldwide.
selectorsIn:
- name
- phone
selectorsOut:
- phone
- name
- address
status: degraded
pricing: free
costNote: Free directory of links to national phone books; the destination directories vary (many free, some paid). No account needed.
opsec: passive
opsecNote: This is a link directory — the OpSec that matters is each destination country's phone book. Browsing the index is passive; the actual lookups happen on third-party national sites, so use a sock-puppet browser throughout. No contact reaches the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing curated index of international phone directories; value depends entirely on the destination national directories, whose coverage, freshness and availability vary widely (and some links may be stale).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Phone Book of the World
- phonebookoftheworld.com
tags:
- toddington
- curated-directory
- telephone-numbers
- international
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Phone Book of the World

> A gateway to the world's national phone books — pick a country and it points you to that country's white/yellow pages and reverse-lookup services.

## When to use
Your subject or number is tied to a specific country and you need that country's local directory rather than a US-centric broker. Phone Book of the World is a launchpad: it collects links to national white/yellow-page and reverse-lookup services across the globe, so you can find the right in-country tool to attribute a `phone` or find a listed `name`/`address`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.phonebookoftheworld.com/ (may be intermittently down; retry).
2. Select the relevant country.
3. Follow the links to that country's phone directories / reverse-lookup services.
4. Run your `name` or `phone` search **on the destination national directory** — this site is the index, not the data.
5. Pivot: a listed address feeds local property/people research; a name feeds in-country people-search; combine with international carrier lookups (`[[phone-validator-us]]`, `[[textmagic-free-carrier-lookup]]`).

## Inputs → Outputs
- **In:** `name` or `phone` (used at the destination directory)
- **Out:** via the linked national directory — listed `phone`, `name`, `address` where the country's directory exposes them
- **Empty/negative result looks like:** dead links or a destination with no results — link rot is common in link directories, and many countries have thin/no public phone data. Treat a broken link as tool-side and search the country's directory directly.

## Gotchas & OpSec
- **It's an index, not a database** — cite the destination directory, and expect some links to be stale/dead.
- Coverage and data-protection rules vary hugely by country; many EU countries expose little due to privacy law.
- OpSec: **passive**; keep a sock puppet across the destination lookups.

## Overlaps ("do both")
- Pairs with `[[numberway]]`/thisnumber (another international directory gateway) and country-specific white pages — international directory gateways overlap imperfectly, so try both to find a working in-country directory.

## Trust & verifiability
`trust: community` — a curated index whose reliability rests on the linked national directories. Assess each result at its actual source, and prefer official/established national directories.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phone-book-of-the-world |
| category | phone |
| selectorsIn → selectorsOut | name, phone → phone, name, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
