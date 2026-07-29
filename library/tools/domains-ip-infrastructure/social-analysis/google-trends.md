---
id: google-trends
name: Google Trends
description: Use when you have a `name`, `username`, brand or keyword and want to see search-interest over time and by region — returns geolocation (where interest concentrates) and timing context.
url: https://trends.google.com/trends/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- social-analysis
bestFor: Measuring search interest in a term/name over time and mapping where (region/city) that interest concentrates.
selectorsIn:
- name
- username
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free; no account required. Signing in adds saved searches but is unnecessary for lookups.
opsec: passive
opsecNote: Passive against the subject, but Google logs your queries and may tie them to your account/IP. Query from a sock-puppet or logged-out session; don't run sensitive terms while signed into a personal Google account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google product; the interest data is authoritative for what it measures (relative, normalized search volume) but is a proxy signal, not a headcount.
missingPersonsRelevance: low
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
- trends.google.com
tags:
- search-analytics
- social-analysis
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Google Trends

> Google's own view of relative search interest — how much a term is searched over time and, crucially, which regions and cities search it most.

## When to use
You have a `name`, `username`, brand, event, or keyword and want context on public attention: when interest spiked (correlate with an event or disappearance date), whether it's rising or fading, and — most usefully for OSINT — the geographic breakdown of where searches concentrate (country → region → city). The regional map can hint at where a name is locally significant. Treat it as a contextual/pattern signal, not a source of hard identifiers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://trends.google.com/trends/ in a logged-out/sock-puppet session.
2. Enter the term (a name, handle, or keyword). Set the time window (past hour → past 5 years → custom) and geography.
3. Read **Interest over time** (spikes/trends) and **Interest by region/city** (the geographic map — drill down to metro level).
4. Add up to five comparison terms to benchmark relative attention (e.g. two spellings of a name).
5. Pivot: a spike date → search news/social for that window; a concentrated region → focus local records/tools there; "related queries" → surface associated terms/handles.

## Inputs → Outputs
- **In:** `name`, `username`, brand, or keyword
- **Out:** normalized interest-over-time curve, `geolocation` breakdown (region/city where interest concentrates), related/rising queries
- **Empty/negative result looks like:** "not enough search volume" for a rare/private name — Trends only reports terms with meaningful volume, so an obscure individual usually returns nothing. Absence means low search volume, not nonexistence.

## Gotchas & OpSec
- Values are relative and normalized (0–100), not absolute counts — you can't read population from them.
- Low-volume/private names return no data; it's biased toward public figures and popular topics.
- OpSec: passive on the target, but Google logs you — stay logged out and consider a proxy for sensitive terms.

## Overlaps ("do both")
- Complements news and social-monitoring tools — Trends tells you *when* and *where* attention peaked; those tell you *what* was being said.

## Trust & verifiability
`trust: trusted` — first-party Google data, authoritative for normalized relative search interest, but it's a proxy signal; don't over-interpret small movements.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-trends |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name, username → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
