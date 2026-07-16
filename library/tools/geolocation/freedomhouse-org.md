---
id: freedomhouse-org
name: Freedom House (Explore the Map)
description: Use when you have a `geolocation` (country) and want its political-rights and civil-liberties context — returns freedom scores and country-level `geolocation` intelligence.
url: http://freedomhouse.org/explore-the-map
category: geolocation
path:
- geolocation
bestFor: Getting a country's political-freedom, civil-liberties and internet-freedom context (0–100 scores) to inform how an investigation operates there.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to explore the interactive map and read country reports; Freedom House is a nonprofit and its assessments are published openly.
opsec: passive
opsecNote: You look up a country, not a person; nothing about a subject is submitted and no one is alerted. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Freedom House is a long-established research nonprofit; its Freedom in the World / Freedom on the Net indices are widely cited, methodologically documented assessments.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Freedomhouse.org
- Freedom in the World
- Freedom on the Net
tags:
- Maps, Geolocation and Transport
- Politics, conflicts and crisis
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Freedom House (Explore the Map)

> An interactive world map of political-rights and civil-liberties scores — country-level context on how free (and how surveilled/censored) a place is.

## When to use
You have a `geolocation` (a country) tied to a case and want to understand its governance environment: political rights, civil liberties, and internet freedom, each scored 0–100 with a narrative report. This shapes operational assumptions — press freedom, surveillance risk, how much online activity is censored or monitored — rather than identifying an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://freedomhouse.org/explore-the-map .
2. Click a country (or switch between the Freedom in the World and Freedom on the Net views).
3. Read its status (Free / Partly Free / Not Free) and its component scores.
4. Read the output: the country's freedom scores and the linked full report explaining the rating (`geolocation` context).
5. Pivot: use the internet-freedom read to calibrate OpSec (surveillance/censorship risk) for research touching that country; combine with crisis/conflict maps for a fuller picture.

## Inputs → Outputs
- **In:** `geolocation` (country)
- **Out:** `geolocation` context (political-rights, civil-liberties and internet-freedom scores plus narrative report)
- **Empty/negative result looks like:** some territories/microstates aren't scored — the map simply has no entry; use regional reports instead.

## Gotchas & OpSec
- This is country-level assessment, never person-level data — it cannot find or identify anyone.
- Scores are annual and reflect Freedom House's methodology/judgement; treat them as expert assessment, not raw fact.
- OpSec: passive; you query a country, and the internet-freedom score itself is a useful input to your own OpSec planning.

## Overlaps ("do both")
- Complements crisis/conflict maps and press-freedom indices: Freedom House gives the governance and internet-freedom backdrop for a country, which you pair with situational (conflict/hazard) sources.

## Trust & verifiability
`trust: trusted` — a well-established research nonprofit with a documented, widely-cited methodology. Authoritative as expert country assessment; the scores are judgements, not measurements.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | freedomhouse-org |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
