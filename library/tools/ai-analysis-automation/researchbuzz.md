---
id: researchbuzz
name: ResearchBuzz (SearchGizmos)
description: Use when you have a `name` or keyword and want purpose-built search constructors — free tools that build Google/News/social/archive queries and timeline navigations.
url: https://searchgizmos.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building targeted search queries (Google, News, social, Internet Archive) with small free web tools by Tara Calishain.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free tools by ResearchBuzz's Tara Calishain; the ResearchBuzz tools moved to SearchGizmos.com. No account required.
opsec: passive
opsecNote: The gizmos only *construct* queries and hand you a URL — the actual searching happens on Google/Archive/etc. under whatever browser session you run it in. Use a research browser/VPN for the follow-through searches; the constructor itself touches no subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by Tara Calishain (ResearchBuzz), a long-respected search/research author; the tools are simple query builders, so results come from the underlying engines, not from her.
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
- ResearchBuzz
- SearchGizmos
- Tara Calishain
tags:
- tools-collections-toolkits
- search
- query-builder
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# ResearchBuzz (SearchGizmos)

> A collection of small, free search-constructor tools by ResearchBuzz's Tara Calishain (now hosted at SearchGizmos.com) that build precise Google, News, social, and Internet Archive queries for you.

## When to use
You have a `name`, handle, or topic and want to search *systematically* rather than typing ad-hoc queries. The gizmos assemble structured queries — date-bounded Google searches, news-source constructors, Internet Archive / Wayback timeline navigation for a Twitter account or blog — that you'd otherwise craft by hand. Good for building repeatable, well-scoped searches around a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the site (ResearchBuzz's tools now live at SearchGizmos.com).
2. Pick the gizmo that fits: Google date/site query builder, news-search constructor, Internet Archive timeline navigator, etc.
3. Enter your `name`/keyword and parameters (dates, sources, sites).
4. The tool outputs a ready-made search URL — click through to run it on the real engine.
5. Pivot: results surface pages, social profiles, and co-mentioned `associate`s to chase further.

## Inputs → Outputs
- **In:** `name`/keyword (+ dates, sources)
- **Out:** constructed search URLs → whatever the underlying engine returns (pages, `social-profile`s, `associate`s)
- **Empty/negative result looks like:** the constructor always builds a query; a "null" result is the *engine* returning nothing — narrow or widen your parameters and re-run.

## Gotchas & OpSec
- These are query builders, not a search index — the coverage and freshness come from Google/Archive/etc., not from the tool.
- The ResearchBuzz → SearchGizmos move means old `researchbuzz.github.io` links now redirect; use the current SearchGizmos site.
- Individual gizmos come and go as engines change their query syntax; expect some to break over time.

## Overlaps ("do both")
- Pairs with general search engines and Wayback/archive tools — the gizmos make you *better* at driving those, they don't replace them.

## Trust & verifiability
`trust: community` — from a credible, long-standing search-research author; because output is just a query URL, you verify by inspecting the search you're about to run.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | researchbuzz |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
