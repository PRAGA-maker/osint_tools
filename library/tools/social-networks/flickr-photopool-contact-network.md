---
id: flickr-photopool-contact-network
name: Flickr Photopool Contact Network
description: Use when you have a Flickr group (photopool) ID and want its member list for network analysis — returns participant usernames as a graph file for Gephi.
url: http://labs.polsys.net/tools/flickr/photopool/
category: social-networks
path:
- social-networks
bestFor: Extracting the member/participant list of a Flickr group as a .gdf graph for social-network analysis in Gephi.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: degraded
pricing: free
costNote: Free web tool from an academic lab (labs.polsys.net). Depends on the Flickr API — may be rate-limited or broken if Flickr's API changes.
opsec: passive
opsecNote: It pulls public Flickr group membership via the API; group members are not notified. Passive. Your IP hits the lab's server and Flickr; use browser hygiene, but there's no target-side exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small academic lab utility; functional as of listing but reliant on Flickr's API, so it may degrade without notice — verify output before trusting completeness.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- tumblr-tool
aliases:
- Flickr Photopool network tool
tags:
- Social Media
- Flickr
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Flickr Photopool Contact Network

> A niche utility that turns a Flickr group's photopool into a member list exported as a Gephi graph — for mapping who participates in a photo community around your subject.

## When to use
Your subject is active in a Flickr group (a "photopool") and you want to map the community around it — every participant's username, ready for network/graph analysis. Useful when a shared-interest group (a location, a hobby, an event) might connect your subject to associates, or when you want to find other accounts in the same niche. Specialist and low general relevance; only when Flickr groups are in play.

## How to use it (`bestInteractionPattern`: web-manual)
1. Find the target Flickr group's photopool ID (e.g. `16135094@N00`).
2. Open the tool, paste the photopool ID, and run it (it queries the Flickr API — allow time).
3. Copy the result and save it as a `.gdf` file.
4. Import the `.gdf` into Gephi for graph/community analysis (centrality, clusters).
5. Pivot: prominent members (`username`s) become new subjects; shared membership suggests `associate` links to your subject.

## Inputs → Outputs
- **In:** a Flickr group photopool ID (community your `username` belongs to)
- **Out:** a member list of `username`s / `social-profile`s as a Gephi-ready graph
- **Empty/negative result looks like:** an error or empty output — the group ID is wrong, the group is private, or the Flickr API is rate-limited/changed (this tool can silently degrade); confirm the group exists and retry.

## Gotchas & OpSec
- API-dependent and unmaintained-prone — it may be broken or truncated at any time; sanity-check the member count against the group page.
- Only public group membership is visible.
- Requires Gephi (separate install) to actually analyze the output.
- OpSec: passive; members aren't alerted.

## Overlaps ("do both")
- Pairs with Flickr's own group pages and general username-search — this bulk-extracts the network for graphing; manual review confirms which members matter and resolves them across platforms.

## Trust & verifiability
`trust: community` — an academic lab tool over Flickr's public API; output is authentic member data when it works, but verify completeness since the tool can degrade silently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flickr-photopool-contact-network |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
