---
id: webmapper
name: Webmapper
description: Use when you want to visualize your OWN browsing history as a zoomable map — a Chrome extension for reviewing where a session went, not for looking up a subject.
url: https://chrome.google.com/webstore/detail/webmapper/foachceonkmkeiigdbkjcihnaabppicf/related
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Reviewing and searching your own recent browser history as a clustered visual map to retrace an investigation session.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome extension; no account or payment. Works on Chromium-based browsers via the Chrome Web Store.
opsec: passive
opsecNote: Webmapper reads YOUR local browser history, not any target's — nothing is sent to a target. But it operationally exposes your own trail: the map reveals every site your session touched, so run it only in the compartmentalized profile you use for a case, and be aware an extension with history access is a data-exfil risk if the profile is compromised. The developer states data isn't sold, but treat any history-reading extension with care.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Single-developer Chrome extension (Ryan Hamerly), ~1,000+ users, ~4.5 stars, last updated 2022; a small niche utility, functional but not actively developed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Webmapper extension
tags:
- Browser analyze
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Webmapper

> A Chrome extension that turns *your own* browser history into a zoomable, searchable cluster map. A self-review/OpSec aid — it inspects your trail, not a subject's.

## When to use
Use it to retrace and review your **own** investigation session: which sites you visited over the last 10–100 days, clustered by domain and sized by visit frequency. Handy for reconstructing "where did I find that?" after a long research spree, or for OpSec self-audit — seeing at a glance everything your investigative profile touched. It does not gather any data about a subject; it visualizes local history only.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Webmapper from the Chrome Web Store into the browser **profile you use for investigations** (not a personal one).
2. Open the extension; it renders your history as an interactive map — points are pages, sized by visit frequency, clustered by similarity.
3. Choose a time range (10/20/50/100 days) and a color palette.
4. Click a node to revisit a page, zoom into a domain, or search to locate a specific site you visited.
5. Use it to reconstruct your research path or audit your session footprint; remove it when done if you don't want a history-reading extension resident.

## Inputs → Outputs
- **In:** none (reads your local browser history, not a selector)
- **Out:** a visual map of your own visited domains/pages — no subject `selectorsOut`
- **Empty/negative result looks like:** a sparse/empty map if the profile has little history or history is cleared.

## Gotchas & OpSec
- It reads **your** history, so keep it in a compartmentalized case profile; a map of every site you touched is itself sensitive.
- Any extension with history permissions is a potential exfil vector if the browser is compromised — install deliberately and remove when finished.
- Unmaintained since 2022 and single-developer; fine but don't depend on updates.

## Overlaps ("do both")
- Complements OpSec browser-profile hygiene tools — Webmapper reviews the trail those compartmentalize; it does not overlap with any subject-facing lookup.

## Trust & verifiability
`trust: community` — a small, functional single-developer extension with a modest user base and no recent updates; trust it for casual self-review, not as a maintained security tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webmapper |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
