---
id: keyword-density
name: Keyword Density
description: Use when you have a `domain`/page (or text) and want its most frequent terms — returns word/phrase frequency and density, revealing a page's real focus and recurring identifiers.
url: https://tools.seobook.com/general/keyword-density/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- analytics
bestFor: Quickly surfacing the dominant words/phrases on a page to characterise its topic, tone, or repeated names.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free SEObook web tool; no account required.
opsec: active
opsecNote: When you give it a URL, the tool fetches that page itself (from SEObook's servers, not yours), so your IP isn't exposed to the target — but the target could see SEObook's fetch. For pasted text it stays local to the tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running SEObook utility. It counts words mechanically; the output is descriptive, not authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- SEObook keyword density
tags:
- analytics
- content-analysis
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Keyword Density

> A simple word-frequency analyser — paste a URL or text and see which terms dominate a page, which is a fast way to read what it's really about and spot repeated names or handles.

## When to use
You have a `domain`/page (a suspect blog, bio, product page, forum profile) and want its actual emphasis rather than skimming it by eye. Frequency analysis surfaces the recurring nouns — repeated personal names, brands, place names, usernames, or contact terms — that hint at ownership, topic or intent. Niche and low relevance, but handy when triaging long pages.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://tools.seobook.com/general/keyword-density/.
2. Enter the page URL (or paste raw text).
3. Run it and read the ranked one/two/three-word terms with counts and density percentages.
4. Interpret: unexpectedly frequent names/places/handles are leads; boilerplate (nav, cookie text) is noise to ignore.
5. Pivot: a repeated proper noun or handle becomes a `name`/`username` to search elsewhere.

## Inputs → Outputs
- **In:** `domain`/URL or pasted text
- **Out:** ranked keyword/phrase frequencies and density (a content characterisation; no data selectors)
- **Empty/negative result looks like:** only generic/stopword terms surface — the page is boilerplate-heavy or JS-rendered (the fetcher sees little). Paste the visible text manually if the URL fetch returns thin content.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **active** in that SEObook fetches the URL server-side; your IP isn't exposed, but the fetch is. Pasting text keeps it fully passive.
- It counts raw HTML text, so navigation/footer terms can dominate — mentally discount site chrome.

## Overlaps ("do both")
- Pairs with a tech-stack fingerprinter — density tells you what a page *says*, a fingerprinter (`[[whatruns]]`) tells you what it's *built on*; together they characterise a site.

## Trust & verifiability
`trust: unverified` — a mechanical counting utility; results are exactly reproducible but purely descriptive, so treat surfaced terms as leads to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | keyword-density |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → — |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
