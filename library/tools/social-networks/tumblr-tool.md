---
id: tumblr-tool
name: Tumblr Tool (Digital Methods)
description: Use when you have a Tumblr tag/term and want to harvest posts tagged with it plus their co-tag network — returns a tabular post dump and a Gephi-ready co-tag graph for network analysis.
url: http://labs.polsys.net/tools/tumblr/
category: social-networks
path:
- social-networks
bestFor: Bulk-collecting Tumblr posts for a tag and mapping co-tag communities around a subject or topic.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- username
- associate
status: degraded
pricing: freemium
costNote: Free web tool; no payment. Depends on Tumblr's API, which has tightened over time, so functionality can be intermittent.
opsec: passive
opsecNote: The tool queries Tumblr's public tag API server-side; you are not logging in or interacting with the target. Passive, but note your query runs through the third-party tool host.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A research tool from the Digital Methods Initiative / polsys lab; academically credible but community-maintained and dependent on Tumblr's API remaining open.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- TumblrTool
- polsys Tumblr tool
tags:
- Social Media
- Tumblr
- network-analysis
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- flickr-photopool-contact-network
---

# Tumblr Tool (Digital Methods)

> A research harvester that pulls posts for a Tumblr tag and builds a co-tag network graph — turning a topic or community into analysable data.

## When to use
Your subject or topic lives on Tumblr and you want more than one-off browsing: collect all posts under a tag, or map how tags co-occur to reveal the communities and accounts clustered around a term. Exports feed spreadsheets (.tab) and Gephi (.GDF), so this is for structured/network analysis of a Tumblr footprint — surfacing associated accounts and adjacent interests rather than resolving a single identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://labs.polsys.net/tools/tumblr/.
2. Enter the tag/term of interest and set options (method, date range, HTML output).
3. Run it and download the tabular post file (.tab, opens in Excel) and the co-tag file (.GDF).
4. Open the .GDF in Gephi to visualise co-tag clusters; scan the .tab for posting accounts.
5. Pivot: accounts and adjacent tags become new `social-profile`/`username` leads and `associate` candidates to run through Tumblr and cross-platform tools.

## Inputs → Outputs
- **In:** a Tumblr tag/term (tied to a `username`/`social-profile` of interest)
- **Out:** tabular post dump, co-tag network graph → posting accounts (`social-profile`, `username`), community links (`associate`)
- **Empty/negative result looks like:** an empty/failed export — often means the tag is sparse OR Tumblr's API has throttled/changed and the backend can't fetch (see status: degraded).

## Gotchas & OpSec
- API-dependent and degraded: Tumblr has repeatedly restricted its tagged API; the tool's backend may fail or return partial data — treat empty results as possibly a tooling issue, and verify by browsing Tumblr directly.
- Tag-centric, not identity-centric: it maps topics/communities; resolving a specific person still needs cross-referencing.
- OpSec: passive, but queries route through the third-party lab host.

## Overlaps ("do both")
- Pairs with photo/contact-network tools ([[flickr-photopool-contact-network]]) and general social-profile search — this maps Tumblr co-tag communities, while those extend the network to other platforms.

## Trust & verifiability
`trust: community` — a credible academic (Digital Methods Initiative) tool, but community-maintained and reliant on Tumblr's API; confirm any harvested finding against live Tumblr before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tumblr-tool |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile, username, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
