---
id: truth-or-fiction-search
name: Truth Or Fiction Search
description: Use when you have a claim, viral message, or `name` and want to check whether it is a known scam, hoax, or debunked story — returns fact-check articles with sourcing and verdicts.
url: http://www.truthorfiction.com
category: documents-metadata
path:
- documents-metadata
bestFor: Verifying viral claims, chain messages, scams, and misinformation against an existing fact-check archive.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to read and search; a "Support Us" subscription is optional and does not gate the fact-checks.
opsec: passive
opsecNote: You're reading a public fact-check archive, not querying anything about a subject, so nothing is exposed to a target. Searches go to the site's own server; use a sock-puppet browser if you don't want the site associating queries with you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running independent fact-checking outlet with bylined, sourced articles; a secondary source — corroborate its verdicts against primary evidence and other fact-checkers.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- TruthOrFiction
- Truth or Fiction?
tags:
- fact-check
- misinformation
- scams
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# Truth Or Fiction Search

> An independent fact-checking archive — search a viral claim, chain email, or rumour and see whether it's been investigated and what the verdict was.

## When to use
You have a claim, a suspicious viral message or image, a scam pitch, or a `name`/topic attached to a rumour, and you want to know if it's already been debunked or confirmed. In OSINT this is a fast sanity check on secondary sources: before you build on a "fact" circulating online, see whether Truth or Fiction (or its peers) has already run it down. It won't find a person; it evaluates the *claims* around them or an event.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.truthorfiction.com and use the site Search (also at `/search/`).
2. Enter distinctive words from the claim — a phrase from a chain message, the subject `name`, or the scam's hook.
3. Open matching fact-check articles; read the verdict (true / fiction / misattributed / unproven) and, crucially, the cited sources.
4. Follow those primary sources to verify independently — the article is a lead, the sourcing is the evidence.
5. Pivot: sourced `document-id`s/links become primary references for your report; a "no result" means run the claim through other fact-checkers.

## Inputs → Outputs
- **In:** a claim/keyword, or a `name` tied to a rumour
- **Out:** fact-check articles (`document-id`), verdicts, and cited sources
- **Empty/negative result looks like:** no matching article — the claim hasn't been fact-checked here; not evidence the claim is true or false, just uncovered. Check Snopes/PolitiFact/Reuters Fact Check too.

## Gotchas & OpSec
- Secondary source: use it to find the *primary* evidence, not as the final word.
- Coverage skews to English-language, US-centric viral content; niche or non-English rumours may be absent.
- OpSec: passive reading; no login needed.

## Overlaps ("do both")
- Pair with other fact-checkers (Snopes, PolitiFact, Reuters/AP Fact Check) and reverse-image tools — Truth or Fiction may cover a claim they don't and vice versa; triangulate verdicts and always trace to primary sources.

## Trust & verifiability
`trust: community` — an established independent fact-checking outlet with bylined, sourced work, but still a secondary source; its verdicts are only as good as the primary evidence it cites, which you should confirm yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | truth-or-fiction-search |
| category | documents-metadata |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
