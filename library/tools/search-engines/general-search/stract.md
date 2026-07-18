---
id: stract
name: Stract
description: Use when you have a `name`, `username` or keyword and want an independent, non-Google index with custom-rankable results — returns web pages, `social-profile` and `domain` hits filterable by "Optics".
url: https://stract.com/
category: search-engines
path:
- search-engines
- general-search
bestFor: An open-source, independent search index whose "Optics" rules let you bias results toward blogs, indieweb, academic or specific sites.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free to use; open source (StractOrg/stract) and self-hostable. No account.
opsec: passive
opsecNote: An independent non-Google engine with its own crawl, so queries aren't tied to a Google identity — useful for a lower-profile search. Still a third-party server that sees your query; use a sock-puppet/VPN for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent open-source non-profit search engine (created by Mikkel Denker); code is public and auditable, but its index is far smaller than Google's, so it's a complement, not a replacement.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Stract search
- stract.com
tags:
- search-engine
- open-source
- indieweb
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Stract

> An open-source, independent web search engine with user-programmable "Optics" — a genuinely different index that can be steered toward blogs, the indieweb, or specific sites Google buries.

## When to use
You're sweeping a `name`, `username` or keyword and want results from an index that isn't Google's or Bing's. Stract crawls its own web and lets you apply **Optics** — shareable ranking/filter rules — to emphasise independent blogs, academic sources, or particular sites, and to demote SEO spam. That makes it good for finding the personal, long-tail pages (a self-hosted blog, a niche forum, an indieweb profile) that mainstream engines rank into oblivion.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://stract.com/.
2. Search the selector — a `name` (quoted), a `username`, or keywords.
3. Apply an **Optic** from the selector (e.g. "indieweb", "discussions", academic-leaning) to reshape ranking, or write/import a custom Optic to restrict to a site set or content type.
4. Read the results for `social-profile` links and personal `domain`s the big engines missed.
5. Pivot: feed discovered handles/domains back into specialist tools; re-run the same query on Google/Bing/Yandex to compare indexes.

## Inputs → Outputs
- **In:** `name`, `username`, or keywords (optionally shaped by an Optic)
- **Out:** ranked web results → `social-profile`, personal `domain`s, page mentions
- **Empty/negative result looks like:** few or no results — Stract's index is much smaller than Google's, so thin results are expected; a blank means "not in this index," not "not online." Always cross-run mainstream engines.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** and independent — not tied to a Google account, which lowers your profile; still, the Stract server sees your queries.
- **Small index**: coverage is a fraction of Google's, so use Stract as a *complementary* angle (its strength is surfacing indie/long-tail pages), never as your only search.
- Optics are powerful but have a learning curve; start with the built-in ones before writing custom rules.

## Overlaps ("do both")
- Do both with `[[swisscows]]` and mainstream engines — each independent index finds pages the others miss, and Stract's Optics specifically dig out indie/personal sites that dominate-by-SEO engines hide.

## Trust & verifiability
`trust: community` — an auditable open-source non-profit engine; results are real crawled pages (verify each directly), with the only caveat being limited index size.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stract |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
