---
id: wikiwho
name: WikiWho (AILEF)
description: Use when you have an `employer-org` and want anonymous Wikipedia edits made from its IP ranges — returns the org's edit history and the pages it touched.
url: http://wikiwho.ailef.tech/
category: social-networks
path:
- social-networks
bestFor: Surfacing Wikipedia edits made anonymously from a specific organization/government/company's IP ranges, and which articles they altered.
selectorsIn:
- employer-org
selectorsOut:
- ip-address
- employer-org
status: degraded
pricing: free
costNote: Free web app; the code is open-source on GitHub (aileftech/wikiwho) and self-hostable if the hosted instance is offline.
opsec: passive
opsecNote: Queries a third-party database of already-public Wikipedia edit logs; no interaction with any subject or with Wikipedia's live infrastructure. No target footprint.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: An independent research project (AILEF) that maps anonymous-editor IP ranges to known organizations; the IP→org mapping is heuristic, so attributions are strong leads, not proof of who at an org made an edit.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Wikiwho
- aileftech wikiwho
- Wikipedia organization edits
tags:
- wikipedia
- edit-attribution
- osint
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# WikiWho (AILEF)

> A tool that ties anonymous Wikipedia edits to the organizations behind them: when someone edits while logged out, Wikipedia logs their IP — WikiWho maps those IPs to known org ranges (governments, militaries, corporations) so you can see what an institution has been quietly changing.

## When to use
You have an `employer-org` (a company, agency, or institution) and want to know whether people on its network have anonymously edited Wikipedia and what they touched — a classic signal of reputation management, insider interest, or PR activity. You can also start from an article to see which organizations edited it. This is an institutional-behavior lens, not a person locator, but leaked edits can point at motive and internal interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://wikiwho.ailef.tech/ (an intermittently-hosted side project — if it 503s/offline, self-host from github.com/aileftech/wikiwho).
2. Look up an organization (e.g. a government body or company), an article, or search for added/removed words.
3. Read the results: edits attributed to the org's `ip-address` ranges, the pages affected, and the diffs.
4. Pivot: a suspicious edit anchors a timeline and motive; the article + timing can corroborate an org's interest in a subject; combine with Wikipedia's own page history.

## Inputs → Outputs
- **In:** `employer-org` (or an article/keyword)
- **Out:** anonymous edits from the org's `ip-address` ranges, affected pages, diffs
- **Empty/negative result looks like:** no edits attributed — the org's editors may log in (hiding IP), edit from other networks, or simply not edit; absence isn't proof. Attribution is by IP range, so it shows the network, not the individual.

## Gotchas & OpSec
- IP→organization mapping is heuristic and covers a curated set of ranges; it attributes to a *network*, never to a named person.
- The hosted instance is a side project and goes up and down (hence `status: degraded`); the open-source code is the durable fallback.
- OpSec: passive; only public edit logs are read.

## Overlaps ("do both")
- Complements Wikipedia's native page-history and other anon-edit trackers (e.g. congress-edits-style bots) — cross-check attributions and diffs.

## Trust & verifiability
`trust: community` — an independent project on public data; the edits are real and verifiable in Wikipedia history, but the org attribution is IP-range inference to be treated as a lead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikiwho |
| category | social-networks |
| selectorsIn → selectorsOut | employer-org → ip-address, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
