---
id: tagsexplorer
name: TAGSExplorer
description: Use when you have a TAGS-collected Twitter/X dataset and want to map the conversation network — returns an interactive graph of who replied to/mentioned whom (`associate`/`social-profile` links).
url: https://tags.hawksey.info/tagsexplorer/
category: social-networks
path:
- social-networks
- twitter
- analytics
- hashtag
bestFor: Visualising reply/mention networks from a hashtag or search archive already collected with TAGS.
selectorsIn:
- social-profile
- username
selectorsOut:
- associate
- social-profile
status: degraded
pricing: free
costNote: Free tool by Martin Hawksey; the visualiser is free, but you must already have a TAGS Google Sheet archive, and TAGS collection now depends on paid X API access.
opsec: passive
opsecNote: Operates entirely on data you already collected into a Google Sheet — no live contact with target accounts during analysis. The collection step (TAGS) touches the X API under your own key; the mapping step here is offline analysis.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by Martin Hawksey, a well-known ed-tech developer; the tool is transparent (reads a Google Sheet via the Visualization API + d3.js), but it is a hobby project dependent on TAGS-collected data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- TAGS Explorer
- Hawksey TAGSExplorer
tags:
- twitter
- network-analysis
- conversation-mapping
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# TAGSExplorer

> Turns a TAGS Twitter/X archive into an interactive conversation network — who replies to and mentions whom around a hashtag or search term.

## When to use
You have already collected a Twitter/X dataset with TAGS (Twitter Archiving Google Sheet) around a hashtag, event, or account, and you want to see the social structure: which accounts are central, who talks to whom, and the clusters of interaction. In an investigation this exposes a subject's most-engaged contacts (`associate`) and the accounts (`social-profile`) orbiting a person or event — leads that a flat tweet list hides.

## How to use it (`bestInteractionPattern`: web-manual)
1. First collect data with TAGS into a Google Sheet (this now requires X API access, which is paid/limited — the main friction).
2. Open https://tags.hawksey.info/tagsexplorer/ and point it at your published TAGS spreadsheet.
3. Read the graph: nodes are accounts (sized by reply/mention frequency), solid lines are replies (conversations), dotted lines are mentions.
4. Identify central accounts and tight clusters — the subject's frequent interlocutors.
5. Pivot: a central `associate` handle feeds cross-network username search and profile enrichment.

## Inputs → Outputs
- **In:** a TAGS Google Sheet archive (accounts + tweets); conceptually `username`/`social-profile` set
- **Out:** interactive network graph → `associate` (frequent interlocutors), `social-profile` links, centrality/cluster structure
- **Empty/negative result looks like:** a sparse or empty graph — usually the underlying TAGS sheet is thin or collection failed (X API limits). Not a signal about the subject.

## Gotchas & OpSec
- **The bottleneck is data collection**, not the visualiser: since X restricted its free API (2023+), building a fresh TAGS archive is hard/paid — hence `status: degraded`. It shines on archives you already hold.
- Analysis is retrospective; it won't show interactions outside your collected window.
- OpSec: **passive** — offline analysis of your own dataset.

## Overlaps ("do both")
- Complements live-search tools that gather the tweets in the first place; TAGSExplorer is the analysis layer on top of whatever archive you've assembled.

## Trust & verifiability
`trust: community` — a transparent, well-regarded hobby tool; the graph is only as good and complete as the TAGS archive feeding it, so state your collection window when citing results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tagsexplorer |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
