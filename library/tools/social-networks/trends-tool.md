---
id: trends-tool
name: OSoMe Trends Tool
description: Use when you have a hashtag, keyword, or URL and want to chart how its volume on Twitter/X rose and fell over time — returns a time-series of tweet activity (no subject PII).
url: https://osome.iu.edu/tools/trends/
category: social-networks
path:
- social-networks
bestFor: Charting the historical tweet-volume timeline of a hashtag, keyword, or URL to spot when a topic spiked.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free academic tool from Indiana University's Observatory on Social Media; no account required.
opsec: passive
opsecNote: You query OSoMe's own indexed dataset, not Twitter/X or any subject — nothing you do reaches a target. Your queries are seen only by OSoMe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by Indiana University's OSoMe research group on a ~10% sample of public tweets; a reputable academic source, bounded by what its sample and collection window captured.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- botometer
- botometer-by-osome
- botslayer
- covaxxy
- network-tool
- osome-iu-edu
aliases:
- OSoMe Trends
tags:
- twitter
- trends
- social-media-analysis
- academic
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# OSoMe Trends Tool

> Indiana University's Observatory on Social Media plots how much a hashtag, keyword, or URL was tweeted over time — drawn from a ~10% sample of public tweets indexed and retained for years — so you can see when a topic trended.

## When to use
An investigation touches a topic, campaign, hashtag, or a shared URL, and you need to know *when* it was active on Twitter/X and how sharply it spiked — for corroborating a timeline, spotting coordinated bursts, or contextualising a claim's virality. It returns aggregate activity over time, not individual accounts or PII, so it is a context/timeline tool rather than a people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osome.iu.edu/tools/trends/ (no login).
2. Enter a hashtag, keyword, or URL.
3. Read the time-series: tweet volume over the covered period, highlighting spikes and quiet stretches. Compare multiple terms to contrast trajectories.
4. Pivot: a spike's date narrows where to look; feed the timeframe into other OSoMe tools ([[network-tool]] for spread, [[botometer]]/[[botslayer]] for bot involvement) or into targeted archive searches.

## Inputs → Outputs
- **In:** a hashtag, keyword, or URL (no subject PII)
- **Out:** a time-series of tweet volume for that term
- **Empty/negative result looks like:** flat/near-zero volume — either the term genuinely saw little activity or it falls outside the sample's coverage window; low volume is not proof of silence given the 10% sample.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — you query an academic dataset, never Twitter/X or a subject.
- It reflects a ~10% sample within OSoMe's collection window, so treat volumes as relative/indicative, not exhaustive counts, and be aware coverage is bounded by when the data was collected.

## Overlaps ("do both")
- Pairs with the sibling OSoMe tools — [[network-tool]] shows *who* spread a topic, [[botometer]] and [[botslayer]] flag automation, while Trends shows the *when-and-how-much*; run them together for a full picture of a topic's life.

## Trust & verifiability
`trust: trusted` — a peer-reviewed academic project from Indiana University with a documented methodology. Its numbers are sampled, so cite it as an indicative timeline and corroborate specific claims against primary posts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trends-tool |
| category | social-networks |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
