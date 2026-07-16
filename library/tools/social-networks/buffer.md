---
id: buffer
name: Buffer
description: Use when you have a `username`/handle and want to check for a public Buffer Start Page link-in-bio — returns linked social-profiles; otherwise low OSINT value.
url: https://buffer.com
category: social-networks
path:
- social-networks
bestFor: Checking whether a handle has a public Buffer "Start Page" link-in-bio that aggregates the person's other social profiles.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free-forever tier (no card needed) for the publishing product and Start Page; paid plans add channels/analytics. None of it is needed to *view* a public Start Page.
opsec: passive
opsecNote: Viewing someone's public Start Page is an anonymous pageview. Buffer is primarily a publishing/scheduling tool, not a lookup service — you cannot search Buffer for a person, so there's little to leak.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established, reputable social-media management company; included here for its public link-in-bio surface, not as an investigative database.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- buffer.com
- Buffer Start Page
tags:
- real-time-search-social-media-search-and-general-social-media-tools
- link-in-bio
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Buffer

> Mainly a social-media publishing/scheduling platform. Its only real OSINT surface is the public **Start Page** link-in-bio, which can aggregate a person's other profiles.

## When to use
Reach for this only in a narrow case: you have a `username` and are checking every link-in-bio provider for a public landing page. Buffer's **Start Page** (a Linktree-style bio page) can list a person's other `social-profile`s, contact links, and current projects in one place. Buffer is not searchable by person and has no people database — so if you're not chasing a specific Start Page, this tool has little to offer and you should prefer real social-search tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. If you have a candidate Start Page URL or handle, open it directly in a browser (Start Pages are public, no login).
2. Alternatively, a subject's Instagram/TikTok/Twitter bio "link" may resolve to a Buffer Start Page — follow it.
3. Read the page: it aggregates outbound links to the person's other profiles, shop, or contact.
4. Harvest each linked `social-profile` and pivot into it individually.
5. If no Start Page exists for the handle, stop — Buffer's core app requires the account owner's login and is not investigable from outside.

## Inputs → Outputs
- **In:** `username` / `name` (as a Start Page guess or a resolved bio link)
- **Out:** aggregated `social-profile` links from a public Start Page
- **Empty/negative result looks like:** no Start Page for the handle (404), or the subject uses a different link-in-bio provider. This is the common case — treat Buffer as a quick negative check, not a primary source.

## Gotchas & OpSec
- Buffer is a publishing tool: you cannot query it for a person, only view a Start Page you can already point to. Set expectations low.
- Links on a Start Page are self-curated marketing — present, not exhaustive; absence of a profile there doesn't mean it doesn't exist.
- OpSec: passive, anonymous pageview.

## Overlaps ("do both")
- Pairs with other link-in-bio checks (Linktree, Beacons, Carrd) — the same person may use any of them, so a handle that's blank on Buffer may resolve elsewhere. Run the whole set when chasing a bio link.

## Trust & verifiability
`trust: community` — a reputable vendor; the Start Page content is authoritative *as the person's own self-published links*, but it's promotional and self-selected, so corroborate each linked profile independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | buffer |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
