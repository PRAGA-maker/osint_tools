---
id: new-york-public-library-search
name: New York Public Library — Articles & Databases
description: Use when you have a `name` or `employer-org` and want to search premium newspaper, genealogy and business databases free via a public library — returns archival records, articles and directory data.
url: http://www.nypl.org/collections/articles-databases
category: public-records
path:
- public-records
bestFor: Free gateway to paywalled newspaper archives, genealogy and business databases for research on a person or organization.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free to browse the database catalog; many databases are usable in-branch by anyone, and remotely with a free NYPL library card (some are cardholder-only).
opsec: passive
opsecNote: Searching library databases is passive and reveals nothing to the subject. Remote access ties queries to your library-card account, so use appropriate account hygiene if that matters.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the New York Public Library, a major public institution licensing authoritative commercial databases (newspapers, genealogy, business directories).
missingPersonsRelevance: medium
coverage:
- us
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- NYPL Articles & Databases
- New York Public Library databases
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
- genealogy
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# New York Public Library — Articles & Databases

> A free public-library gateway into premium newspaper archives, genealogy, and business databases — paywalled research power without the subscription.

## When to use
You have a `name` or `employer-org` and need the kind of deep archival research that normally sits behind expensive paywalls — historical newspaper runs, genealogy records (census, vital records), and business/company databases. A free NYPL card unlocks these remotely, making the library a force-multiplier for biographical background, address history, relatives, and corporate ties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.nypl.org/collections/articles-databases and browse the catalog by subject (news, genealogy, business, biography).
2. For remote access, sign in with a free NYPL library card (eligibility permitting) — some databases are in-branch only.
3. Choose a database fit to your selector (e.g. a newspaper archive for a `name`, a business directory for an `employer-org`).
4. Search within that database and read the records — articles, listings, genealogical entries.
5. Pivot: an obituary/genealogy hit yields relatives (`associate`) and an `address` history; a business record yields officers and an org `address`.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** archival articles, genealogy records, business listings → `address`, `associate`s, `employer-org` detail
- **Empty/negative result looks like:** a database returns no records — try a different database in the catalog; coverage varies wildly by source and era, so one miss isn't conclusive.

## Gotchas & OpSec
- Human-in-the-loop: many databases require a library-card login; some are strictly in-branch — expect an access gate.
- Card eligibility: full remote access generally expects a New York State connection, though many resources are open to anyone in-branch.
- Coverage is per-database: this is a gateway to many licensed products, each with its own scope and date range.
- OpSec: passive; remote queries are tied to your card account.

## Overlaps ("do both")
- Pairs with dedicated newspaper-archive and genealogy tools — the library bundles licensed versions of several such databases, so use it to reach premium sources you'd otherwise pay for, then corroborate in a specialised tool.

## Trust & verifiability
`trust: trusted` — the NYPL is a major public institution licensing authoritative commercial databases; the underlying records are high quality, bounded by each database's coverage and your access level.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-york-public-library-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
