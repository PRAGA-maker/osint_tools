---
id: jayde-b2b-business-search
name: Jayde B2B Business Search
description: Use when you have a company `name` and want a legacy web-directory listing that may carry an older business URL or contact — returns `employer-org`, `domain`.
url: http://www.jayde.com
category: search-engines
path:
- search-engines
bestFor: Checking a legacy B2B directory for an older business listing, URL, or category placement.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- domain
status: degraded
pricing: free
costNote: Free to browse/search; ad-supported legacy directory, no account.
opsec: passive
opsecNote: Browsing the directory is passive and anonymous; the listed business is not notified you looked it up.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A legacy 1990s-2000s web directory (iEntry, Inc.), largely superseded by modern search; listings are self-submitted, dated, and unvetted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Jayde
tags:
- toddington
- curated-directory
- business-directory
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Jayde B2B Business Search

> A legacy web-era B2B directory — mostly of historical value, but occasionally holds an old business listing, URL, or category tag that modern search has dropped.

## When to use
You're researching a company and want to check whether it left a listing in an old-school web directory — sometimes preserving a defunct business URL, an old category placement, or a contact that current sources no longer show. Jayde is a legacy categorized directory (1990s-2000s model), largely eclipsed by Google and modern B2B platforms, so treat it as a low-yield supplementary check for older or obscure businesses, not a primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.jayde.com.
2. Search the company `name`, or browse the relevant industry category.
3. Open any listing: note the business name, category, and any linked URL/contact.
4. Read the output: a directory entry pointing to a business `domain` (possibly an older/defunct one worth checking in the Wayback Machine).
5. Pivot: an old domain feeds whois/archive tools; a category/description corroborates a business's line of work. Prefer modern registries for authoritative data.

## Inputs → Outputs
- **In:** `name` / `employer-org`
- **Out:** `employer-org` (directory listing), `domain` (linked business URL)
- **Empty/negative result looks like:** no listing for the company — likely never submitted or long removed; this directory's coverage is thin and dated, so absence means little.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive.
- Status degraded: it's a legacy directory with stale, self-submitted listings — verify anything it shows against current sources, and expect many dead links.

## Overlaps ("do both")
- Redundant with modern business registries and search — use Jayde only as a historical supplement; an archived old URL it surfaces is best chased via the Wayback Machine.

## Trust & verifiability
`trust: unverified` — a legacy self-submission directory of dwindling relevance; treat any listing as a dated, unvetted lead to confirm elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jayde-b2b-business-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
