---
id: firebounty
name: FireBounty
description: Use when you have an `employer-org`/`domain` and want to know its bug-bounty or vulnerability-disclosure policy and in-scope assets — returns the program scope, listing linked `domain`s and disclosure channels.
url: https://firebounty.com
category: search-engines
path:
- search-engines
bestFor: Searching a huge aggregated directory of bug-bounty / VDP programs to find an organization's policy and declared in-scope assets.
selectorsIn:
- employer-org
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free to browse and search the directory (150k+ policies); commercial bug-bounty launch services are separate/paid.
opsec: passive
opsecNote: You query FireBounty's aggregated directory, not the target organization, so no target-side exposure. FireBounty logs your searches like any site; nothing sensitive is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running aggregator of publicly-posted VDP/bug-bounty policies (operated alongside YesWeHack); a convenient index of public policy pages rather than an authoritative registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Firebounty
- firebounty.com
tags:
- Search engines
- Bugbounty/vulnerabilities search tools
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# FireBounty

> A searchable directory of 150,000+ bug-bounty and vulnerability-disclosure policies — look up an organization to find its security policy, disclosure channel and declared in-scope assets.

## When to use
You have an `employer-org` or `domain` and want to know two things fast: does this organization run a bug-bounty / VDP program, and what assets does it declare in scope? The scope statement is a gift for reconnaissance — it lists the domains, subdomains, APIs and apps the organization itself acknowledges owning, plus the official channel to report to. It's also useful for finding a legitimate `security.txt`/disclosure contact.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://firebounty.com.
2. Search by organization name or `domain`, or filter by reward type (bounty/hall-of-fame), scope type (web, API, mobile) and policy type (bug bounty, CVD, security.txt).
3. Open the program page and read the scope — in-scope `domain`s/assets, out-of-scope items, and the disclosure channel.
4. Note the declared assets and reporting contact.
5. Pivot: the in-scope `domain` list seeds subdomain/attack-surface enumeration; the disclosure channel gives a legitimate route to report findings.

## Inputs → Outputs
- **In:** `employer-org` name or `domain`
- **Out:** the org's bug-bounty/VDP policy → declared in-scope `domain`s/assets and disclosure channel
- **Empty/negative result looks like:** no listing — the org may have no public program, or FireBounty hasn't indexed it. Absence isn't proof; check the org's own `/security.txt` and `/.well-known/`.

## Gotchas & OpSec
- It aggregates public policy pages, which can lag the organization's live program — confirm scope on the org's official policy before acting on it.
- Declared scope defines what you're *authorized* to test; treat out-of-scope assets as off-limits.
- OpSec: passive — you query the directory, not the target.

## Overlaps ("do both")
- Pairs with attack-surface tools like `[[bbot]]` — FireBounty tells you which assets the org admits owning and authorizes testing on, then BBOT enumerates the actual surface within that scope.

## Trust & verifiability
`trust: community` — a well-established aggregator of publicly-posted policies; convenient and broad, but verify the authoritative scope on the organization's own disclosure page before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | firebounty |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
