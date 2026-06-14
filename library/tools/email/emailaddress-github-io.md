---
id: emailaddress-github-io
name: emailaddress.github.io
description: Use when you want a curated directory of email-OSINT tools and techniques to plan an address investigation — returns links/resources, not data.
url: https://emailaddress.github.io/
category: email
path:
- email
bestFor: A curated hub/index of email-OSINT tools and techniques.
selectorsIn:
- email
selectorsOut:
- metadata
status: unknown
pricing: free
costNote: Free static GitHub Pages resource list.
opsec: passive
opsecNote: A static link directory; browsing it leaks nothing about your target. The third-party tools it links each have their own OpSec profile.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained GitHub Pages collection; quality depends on the unnamed maintainer and update cadence.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- resource-list
- Email Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# emailaddress.github.io

> A community-curated GitHub Pages directory of email-OSINT tools, services, and techniques — a planning resource, not a lookup engine.

## When to use
You are starting an email-address investigation and want a map of available reverse-lookup, verification, breach, and account-enumeration tools rather than a single answer. Use it to pick the right downstream tool for an `email` you hold.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the page and skim the categorized list of email tools/techniques.
2. Identify the category you need (verification, reverse lookup, breach, account enumeration).
3. Follow the relevant link and run your `email` there.
4. Pivot: each linked tool is the actual data source; this page only routes you to them.

## Inputs → Outputs
- **In:** `email` (conceptually — you bring the address to the tools it links)
- **Out:** `metadata` (a list of tools/resources to use next)
- **Empty/negative result looks like:** the page is just a directory; "empty" means a link is dead or the section is sparse.

## Gotchas & OpSec
- Human-in-the-loop: it is a reading/triage resource; it does no lookups itself.
- Link rot is common in curated GitHub lists — verify a linked tool is still live before relying on it.
- OpSec: passive; browsing leaks nothing about your subject.

## Overlaps ("do both")
- Complements `[[email-search-tool-by-inteltechniques]]`, which actively dispatches an address across services rather than just listing them.

## Trust & verifiability
`trust: community` — an open, community-maintained GitHub Pages collection; treat as a curated index whose individual links each need their own verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | emailaddress-github-io |
| category | email |
| selectorsIn → selectorsOut | email → metadata |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
