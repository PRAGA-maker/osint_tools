---
id: covaxxy
name: CoVaxxy
description: Use when you want to study state-level COVID-19 vaccine misinformation and hashtag/news-sharing patterns on Twitter — a research dashboard/dataset, not a per-person lookup.
url: https://osome.iu.edu/tools/covaxxy
category: social-networks
path:
- social-networks
bestFor: Exploring aggregate COVID-vaccine Twitter narratives, top hashtags/domains, and their correlation with US state vaccine uptake.
selectorsIn: []
selectorsOut:
- domain
status: degraded
pricing: free
costNote: Free public dashboard from a university research group; the underlying tweet-ID dataset is on GitHub (osome-iu/CoVaxxy).
opsec: passive
opsecNote: You browse an aggregate research dashboard; no target is contacted and nothing you enter identifies a subject. Purely observational.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Indiana University's Observatory on Social Media (OSoMe) with the Polytechnic University of Milan; peer-reviewed, academically maintained.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- botometer
- botometer-by-osome
- botslayer
- network-tool
- osome-iu-edu
- trends-tool
aliases:
- CoVaxxy dashboard
- osome covaxxy
tags:
- misinformation
- covid-19
- twitter-analysis
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# CoVaxxy

> An OSoMe research dashboard mapping COVID-19 vaccine conversation and misinformation on Twitter against US state vaccine-uptake data.

## When to use
You are doing narrative/misinformation analysis rather than person-finding: you want to see which hashtags and news `domain`s dominated vaccine discourse, how "low-credibility" sources spread, and how that correlated with a state's vaccine hesitancy. It is an aggregate research artifact — it will not resolve an individual account or person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osome.iu.edu/tools/covaxxy and let the interactive dashboard load.
2. Use the maps/graphs to compare vaccine uptake across US states and inspect top shared hashtags and news domains in the vaccine conversation.
3. For reproducible work, pull the tweet-ID collection from the `osome-iu/CoVaxxy` GitHub repo and rehydrate it with an academic Twitter/X pipeline.
4. Pivot: a suspect low-credibility `domain` surfaced here feeds domain-reputation and infrastructure tooling.

## Inputs → Outputs
- **In:** none (you explore aggregates, not a selector)
- **Out:** top news `domain`s / hashtags in the vaccine conversation; state-level correlation data
- **Empty/negative result looks like:** stale or non-updating panels — the live stream depended on Twitter's streaming API, so recent data may not refresh.

## Gotchas & OpSec
- **Degraded/time-boxed:** the collection was built on Twitter's academic/streaming API, which was curtailed in 2023; treat the dashboard as a historical (largely 2021–2022) record rather than a live feed, and cite the GitHub dataset for provenance.
- Not a people-search tool — no account, name, or profile lookup. Wrong tool if you need to identify a specific poster.
- **Passive**: observational only; nothing leaves an investigative trace.

## Overlaps ("do both")
- Pairs with sibling OSoMe tools `[[botometer]]`, `[[botslayer]]`, `[[trends-tool]]`, and `[[network-tool]]` — CoVaxxy frames the narrative; those score individual accounts/bots and trend structure within it.

## Trust & verifiability
`trust: trusted` — an academic, peer-reviewed project from a reputable social-media research lab; methodology and data are openly published.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | covaxxy |
