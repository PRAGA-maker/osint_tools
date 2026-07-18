---
id: google-finance
name: Google Finance
description: Use when you have a company name or ticker (`employer-org`) and want a quick financial and news overview — returns stock data, company summary, and related-company links.
url: https://www.google.com/finance/
category: public-records
path:
- public-records
- general-info-and-news
bestFor: Fast public-company snapshot — price, summary, recent news, and peer/related companies — for context on a subject's employer or a company of interest.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free; no account required for the public finance pages (a Google login only adds a personal watchlist).
opsec: passive
opsecNote: Queries go to Google, never to the company itself. If you sign in to save a watchlist, that activity is tied to your Google account — browse signed-out or with a research profile for clean tradecraft.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Google, aggregating market data and licensed news feeds; reliable for headline financial facts, though it is a convenience aggregator, not a primary filing source (use SEC/EDGAR for authoritative filings).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Google Finance
tags:
- finance
- company
- news
- arf-seed
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Google Finance

> Google's free financial dashboard: type a company or ticker and get price, a business summary, recent news, and a list of related companies — fast context, not deep records.

## When to use
You have a subject's `employer-org` (or a company tied to your investigation) and want a quick, no-friction read on it: is it public, what does it do, what's the recent news, and which peer companies sit near it. It's a triage step — confirm a company exists and is real, get the ticker and sector, and pull recent headlines that might name executives or events relevant to your subject. For serious corporate structure or officer detail, move to a registry tool instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.google.com/finance/ (no login needed).
2. Search the company name or stock ticker in the box.
3. Read the panel:
   - Price/market data and a short business summary (what the company does, HQ, size).
   - A **news** feed of recent articles mentioning the company — scan these for names, events, and links.
   - **Related companies** / "you may be interested in" — competitors and peers, useful for mapping a sector.
4. For anything authoritative (filings, officers, ownership), follow the news/summary to primary sources (company site, SEC EDGAR, a corporate registry).
5. Pivot: news articles → executive/employee `name`s and events; related companies → the broader corporate landscape around your subject's employer.

## Inputs → Outputs
- **In:** company name or ticker (`employer-org`)
- **Out:** stock/financial data, company summary, recent news, related `employer-org`s, `name`s surfaced in coverage
- **Empty/negative result looks like:** no matching listing or only tangential news — the company is likely private or too small to be indexed here; use a corporate registry instead.

## Gotchas & OpSec
- Covers publicly traded / well-covered companies well; private firms and small businesses are thin or absent.
- It aggregates rather than originates data — treat it as a pointer to primary sources, not the source itself.
- Fully passive; sign out (or use a research Google profile) to avoid tying watchlists to your identity.

## Overlaps ("do both")
- Complements `[[opencorporates]]`: Google Finance gives the fast public snapshot and news, OpenCorporates gives the official registry record, officers, and addresses.

## Trust & verifiability
`trust: trusted` — Google-operated with licensed market/news data, reliable for headline facts; because it is an aggregator, verify anything actionable against the primary filing or registry it points to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-finance |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
