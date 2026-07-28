---
id: debunking-false-stories-archives
name: FactCheck.org — Debunking False Stories Archive
description: Use when you have a viral claim, image, or story and want to check whether FactCheck.org has already debunked it — a misinformation-verification archive, no personal selectors out.
url: https://www.factcheck.org/fake-news/
category: search-engines
path:
- search-engines
bestFor: Checking whether a circulating story/claim has already been fact-checked and debunked.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to read; no account. Nonprofit-funded (Annenberg Public Policy Center).
opsec: passive
opsecNote: Reading a public fact-checking archive is fully passive — nothing about your subject is disclosed. Standard site analytics apply to you as a visitor.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: FactCheck.org is a long-established, nonpartisan project of the Annenberg Public Policy Center (University of Pennsylvania) with a transparent sourcing methodology.
missingPersonsRelevance: low
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- fact-check
- scicheck
tags:
- fact-checking
- misinformation
- news-verification
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# FactCheck.org — Debunking False Stories Archive

> FactCheck.org's running archive of debunked viral hoaxes and fabricated stories — the place to check before you treat a sensational claim, screenshot, or story as evidence.

## When to use
You've encountered a viral claim, doctored image, fake quote, or "news" story in the course of an investigation and need to know whether it's already been shown false. Search this archive to avoid building on debunked misinformation. It returns fact-check articles and context, not personal selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the "Debunking False Stories" archive at factcheck.org/fake-news/.
2. Browse recent entries or use the site search for a keyword, name, or phrase from the claim.
3. Read the fact-check: the verdict, the evidence, and the primary sources it cites.
4. Follow the cited sources to the underlying facts rather than stopping at the verdict.
5. Pivot: an image debunked here → reverse image search to trace the original; a fabricated quote → the real record.

## Inputs → Outputs
- **In:** a claim / headline / keyword (not a personal selector)
- **Out:** fact-check verdicts and sourced context (no personal selectors)
- **Empty/negative result looks like:** no matching fact-check — meaning *this* outlet hasn't covered the claim, not that the claim is true. Check other fact-checkers (Snopes, Reuters/AP fact-check, regional ones) before concluding.

## Gotchas & OpSec
- Absence of a debunk ≠ confirmation; it may simply be uncovered. Triangulate across fact-checkers.
- US-centric editorial focus; regional misinformation may be better covered by local fact-checkers.
- Fully passive.

## Overlaps ("do both")
- Pairs with `[[fact-check]]` and `[[scicheck]]` (sibling FactCheck.org channels) and with other fact-check databases — coverage differs per outlet, so check more than one.

## Trust & verifiability
`trust: trusted` — a reputable, transparent, nonpartisan academic fact-checking project. Its verdicts are well-sourced; still follow the cited primary sources for your own record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | debunking-false-stories-archives |
| category | search-engines |
| selectorsIn → selectorsOut | (claim) → (fact-check verdict) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
