---
id: ai-search-whisper
name: AI Search Whisper
description: Use when you have a `name` or a messy research question and want ready-made advanced-operator queries — returns clickable Google/Bing dork links tailored to the problem.
url: https://google.digitaldigging.org/index2.html
category: search-engines
path:
- search-engines
bestFor: Turning a plain-language investigative question into precise Google/Bing search-operator queries.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
costNote: Free web tool from Digital Digging (Henk van Ess); runs on a hosted LLM, no account.
opsec: passive
opsecNote: You type your research problem into a third-party LLM-backed page, so avoid pasting sensitive case specifics or PII you don't want leaving your machine. The generated searches themselves run later in your own browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Made by Henk van Ess / Digital Digging, a respected OSINT trainer; it is a query-generation aid, not a data source — always run and judge the searches yourself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- deleted-tweet-finder-digital-digging-cache
- digitaldigging-org
- digitaldigging-org-2
- visualorigins-digitaldigging-org
aliases:
- AI Search Whisperer
- Digital Digging search generator
tags:
- Search engines
- Universal search tools
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# AI Search Whisper

> An LLM-backed query generator: describe your investigative problem and it hands back precise Google/Bing dork queries (operators, quotes, site:, filetype:) as clickable links.

## When to use
You know *what* you want to find — a person, a document, a leaked file — but not the exact operator syntax to surface it. AI Search Whisper converts your plain description (including a `name` or handle) into advanced search strings you can run immediately. It is a search-strategy accelerator, not a database; its value is getting to the right query faster.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://google.digitaldigging.org/index2.html.
2. Describe the problem in plain language ("find a CV PDF for [name] at [org]", "posts by [username] on forums").
3. It returns a set of Google/Bing queries using operators (`site:`, `filetype:`, `intitle:`, exact-match quotes) as clickable links.
4. Click through, review results, and iterate — refine the description if the queries miss.
5. Pivot: feed hits into the specific tools that enrich them (a found profile → username tools; a found PDF → metadata tools).

## Inputs → Outputs
- **In:** `name` / a plain-language research question
- **Out:** none as a selector — a list of ready-to-run advanced search queries/links
- **Empty/negative result looks like:** generic or off-target queries — meaning refine your description; the tool is only as good as the problem statement you give it.

## Gotchas & OpSec
- It generates queries via a third-party LLM; don't paste sensitive PII/case detail you wouldn't want processed off-machine.
- The queries are suggestions — some operators may be outdated or return nothing; verify by running them.
- Not a data source: it finds nothing itself; the search engines do the work.

## Overlaps ("do both")
- Pairs with the other Digital Digging tools (`[[digitaldigging-org]]`, `[[visualorigins-digitaldigging-org]]`) — this crafts the query, those handle deleted-content and image-origin angles.

## Trust & verifiability
`trust: community` — from a well-regarded OSINT practitioner, but it is a query aid; every result must be verified in the actual search engine and its source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ai-search-whisper |
| category | search-engines |
| selectorsIn → selectorsOut | name →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
