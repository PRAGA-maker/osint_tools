---
id: newsbrief
name: EMM NewsBrief
description: Use when you have a `name` or `employer-org` and want breaking multilingual news mentions — returns clustered articles across ~70 languages with named-entity links.
url: https://emm.newsbrief.eu/NewsBrief/clusteredition/en/latest.html
category: search-engines
path:
- search-engines
- news-search
bestFor: Monitoring a person, organization or place across thousands of news sources in dozens of languages, clustered in near-real time.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
status: live
pricing: free
costNote: Free public service run by the European Commission's Joint Research Centre (Europe Media Monitor); no account or payment. (The service is being consolidated under media-monitor.europa.eu.)
opsec: passive
opsecNote: Reading a public news-aggregation site — no login, nothing written, the subject is not notified. Ordinary web-reading hygiene applies; the value is that queries touch the aggregator, not the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the EU's Joint Research Centre (Europe Media Monitor / EMM); the clustering and entity-tagging are automated over third-party news, so verify the underlying articles at their source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- NewsBrief
- Europe Media Monitor
- EMM
tags:
- news-aggregator
- multilingual
- named-entity
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# EMM NewsBrief

> The EU Joint Research Centre's Europe Media Monitor — near-real-time multilingual news clustering across thousands of sources, with automatic people/organization tagging.

## When to use
You want to know whether a `name`, `employer-org`, or place is being reported on right now, and across languages you might not search directly. EMM NewsBrief crawls thousands of news outlets in ~70 languages, groups related articles into clusters, and tags named entities — so a single query can surface foreign-language coverage, co-mentioned people (`associate` leads), and the organizations tied to a subject. It is strongest for entities with a public/news footprint and for breaking, multilingual situations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the clustered edition at https://emm.newsbrief.eu/NewsBrief/clusteredition/en/latest.html (or the consolidated portal at media-monitor.europa.eu).
2. Search a name/organization, or browse the topic and country clusters.
3. Open a cluster to see all articles on that story across sources/languages, and the entities EMM has tagged in it.
4. Note co-mentioned people and organizations as leads, then open the original articles to verify.
5. Pivot: tagged `associate`s and `employer-org`s feed people-search and corporate-registry lookups; foreign-language hits feed translation and local-source follow-up.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or a place/topic
- **Out:** clustered multilingual news articles + tagged named entities (`associate`, `employer-org`)
- **Empty/negative result looks like:** no clusters/mentions — meaning the subject isn't currently in EMM's monitored news stream, common for private individuals with no news footprint.

## Gotchas & OpSec
- Human-in-the-loop: none; entity tagging is automated and can mis-tag — confirm each entity against the source article.
- It monitors *news media*, not social media or records — absence here doesn't mean absence elsewhere.
- The EMM services are being consolidated under media-monitor.europa.eu; if the clustered-edition URL moves, use that portal.

## Overlaps ("do both")
- Pairs with a general news search and a broad web search — this adds real-time multilingual clustering and entity extraction those don't provide.

## Trust & verifiability
`trust: trusted` — an official EU-JRC service; the platform is authoritative but its clustering/tagging is automated over third-party reporting, so verify specific claims at the original outlet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | newsbrief |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
