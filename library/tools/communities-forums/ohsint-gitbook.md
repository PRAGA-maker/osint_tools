---
id: ohsint-gitbook
name: OhSINT GitBook
description: Use when you need OSINT/OPSEC methodology or a curated tool pointer for a particular investigative problem — returns tradecraft articles and category-organized tool/resource links (reference reading, no selector output).
url: https://github.com/OhShINT/ohshint.gitbook.io
category: communities-forums
path:
- communities-forums
bestFor: Methodology reading and curated, category-organized OSINT/OPSEC tool references when you're deciding how to approach an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open knowledge base (GitHub source + GitBook reader). No account.
opsec: passive
opsecNote: Passive — reading public documentation. Note the site itself heavily covers OPSEC/counter-surveillance, which is useful guidance for keeping your own investigation clean.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community knowledge base (OhShINT, ~900+ stars) curated by an individual researcher; a reference/reading resource, not a data source, so weigh advice and verify linked tools yourself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ohshint.gitbook.io
tags:
- gitbook
- knowledge-base
source: gh-topic-osint-resources
lastVerified: '2026-07-21'
enrichment: full
---

# OhSINT GitBook

> A curated OSINT/OPSEC knowledge base — articles on tradecraft, surveillance and counter-surveillance, plus category lists of tools — best used to decide *how* to run an investigation, not to look up a person.

## When to use
You're stuck on approach — which technique or class of tool fits the problem (a username, an image, a network, staying anonymous while you dig) — and want vetted methodology and a shortlist of tools to try. It's reference reading and a link hub, so reach for it at the planning/technique stage, then execute in the actual tools it points to.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the polished version at **ohshint.gitbook.io** (the GitHub repo is the source/mirror).
2. Browse the articles, "protips," and resource lists by discipline: OSINT investigations, OPSEC/privacy, surveillance/counter-surveillance, tradecraft, CTF writeups.
3. Pick the technique and candidate tools for your case; open those tools directly.
4. Apply the OPSEC guidance to your own setup (sock puppets, egress) before touching a target.
5. Pivot: from methodology here to the concrete lookup tools elsewhere in this library.

## Inputs → Outputs
- **In:** an investigative question / technique need (not a selector)
- **Out:** methodology articles + curated tool/resource links (guidance, not data)
- **Empty/negative result looks like:** the topic isn't covered or a linked tool has rotted — updates are sporadic (the author admits an irregular schedule), so cross-check tool status.

## Gotchas & OpSec
- It's a **reference/reading** resource — it never returns data about a person.
- Updated irregularly; some linked tools may be stale — verify before relying.
- OpSec: passive; and its OPSEC sections are worth reading to protect your own operation.

## Overlaps ("do both")
- Pairs with `[[non-typical-osint-guide]]` and other OSINT guides — read across a couple of methodology sources, then converge on the concrete tools they recommend.

## Trust & verifiability
`trust: community` — a respected individual-run knowledge base; treat it as informed guidance, confirm any linked tool's current state, and cite primary sources for the actual findings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ohsint-gitbook |
| category | communities-forums |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
