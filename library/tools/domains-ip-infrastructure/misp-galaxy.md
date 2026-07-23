---
id: misp-galaxy
name: MISP Galaxy
description: Use when you have a threat-actor `name`/alias or malware label and want its canonical cluster, synonyms and attribution — returns associate/alias links and context.
url: https://www.misp-galaxy.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Resolving threat-actor aliases and mapping APT groups to their known synonyms, tools and targets.
selectorsIn:
- name
- username
selectorsOut:
- associate
- name
status: live
pricing: free
costNote: Fully free and open. Data published under CC0 / 2-clause BSD; browsable on the web and downloadable as JSON from GitHub.
opsec: passive
opsecNote: A static reference dataset — you read public taxonomies. No query touches any actor or target; nothing to leak beyond your own visit to the site/repo.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the MISP Project and a large open community; widely used across CTI teams. Clusters aggregate vendor reporting, so attribution reflects those sources' confidence, not ground truth.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- MISP galaxy clusters
- misp-galaxy.org
tags:
- threat-actor-search
- threat-intel
- attribution
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# MISP Galaxy

> The open, community-curated catalogue of threat-actor, malware and technique clusters — the standard place to resolve an APT alias into its canonical group and synonyms.

## When to use
You have a threat-actor `name` or handle (e.g. "APT28", "Fancy Bear", a vendor codename) and need to know who else calls them what, which tools/malware and target sectors are attributed to them, and their documented history. Use it to normalise noisy, vendor-specific naming into one cluster before pivoting into infrastructure or campaign analysis.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.misp-galaxy.org/ and pick the relevant galaxy (e.g. Threat Actor, or a vendor cluster like the 360net APT catalogue) — or clone the JSON from the MISP `misp-galaxy` GitHub repo for programmatic use.
2. Search the actor `name` or alias. Each cluster entry lists synonyms, suspected country of origin, targeted sectors/regions, associated malware, and source references.
3. Note the full synonym set — these are your alternate search terms for every other tool.
4. For automation, load the galaxy JSON directly (it's the same data that ships inside MISP instances).
5. Pivot: feed the synonyms and associated tooling into infrastructure/domain hunting and campaign reporting; the references point to the primary vendor write-ups.

## Inputs → Outputs
- **In:** threat-actor `name`, codename, or `username`/handle
- **Out:** canonical cluster with `associate`/`alias` synonyms, attributed malware & sectors, source citations
- **Empty/negative result looks like:** no cluster matches the term — meaning it's an unindexed or very new label, not that the actor is unknown; check the primary vendor report instead.

## Gotchas & OpSec
- Attribution is aggregated from public vendor reporting; confidence varies and overlapping clusters can conflict. Read the cited sources, don't treat a cluster as fact.
- Focused on cyber threat actors — not a people-finder; missing-persons relevance is low and indirect.
- OpSec: **passive** — a static reference; nothing is queried against any target.

## Overlaps ("do both")
- Complements primary CTI write-ups and MITRE ATT&CK group pages — MISP Galaxy unifies the *names*, those give the *behaviour*. Cross-reference both when attributing.

## Trust & verifiability
`trust: trusted` — an established, openly licensed, community-maintained standard used across the CTI industry. Reliable as an alias/synonym index; attribution claims inherit the certainty (and disputes) of the underlying sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | misp-galaxy |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name, username → associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
