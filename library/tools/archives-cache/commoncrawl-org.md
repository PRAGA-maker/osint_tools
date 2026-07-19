---
id: commoncrawl-org
name: Common Crawl
description: Use when you have a `domain`/URL or a broad pattern and want to mine a massive open archive of the web at scale — returns historical page captures and an index (document-id) you can query for URLs, snapshots, and extracted text.
url: https://commoncrawl.org/overview
category: archives-cache
path:
- archives-cache
bestFor: Bulk/at-scale web-corpus mining — querying billions of archived pages and URL indexes by domain or pattern.
selectorsIn:
- domain
selectorsOut:
- document-id
- domain
status: live
pricing: free
costNote: Free open dataset (hosted on AWS S3); the data is free, but processing it at scale can incur your own compute/egress costs.
opsec: passive
opsecNote: You query a pre-collected open archive, not the target's live site, so nothing reaches the subject. Fully passive; ideal when you must avoid touching a subject-controlled server.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by the Common Crawl Foundation, a well-known non-profit whose corpus underpins major web-scale research; captures are authentic but partial (a sample of the web per crawl), not exhaustive.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- commoncrawl
- Common Crawl corpus
tags:
- archives
- web-corpus
- big-data
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- common-crawl
- index-commoncrawl-org
---

# Common Crawl

> A free, petabyte-scale open archive of the web, refreshed monthly — use its URL index and captures to find pages, domains, and text at a scale no single-URL archive can match, entirely without touching the target.

## When to use
You need breadth or scale that a point lookup can't give: enumerate every archived URL under a `domain`, find historical pages a subject's site once hosted, search for a selector across a huge slice of the web, or extract text/links in bulk for analysis. It's the tool for "what did the web look like around this domain/pattern," and for fully passive collection when you can't risk hitting the live site.

## How to use it (`bestInteractionPattern`: cli)
1. Read the overview at https://commoncrawl.org/overview and note the latest crawl's paths.
2. For URL discovery, query the **CDX/columnar index** for a `domain` (e.g. via the `cc-index` or the Athena/columnar index) to list captured URLs and their WARC locations.
3. Fetch the specific WARC/WAT/WET records you need from the public S3 buckets (WARC = raw response, WET = extracted text, WAT = metadata/links).
4. Process locally or with cloud compute; expect to write a little code — this is a dataset, not a search box.
5. Pivot: discovered URLs feed the Wayback Machine for point history, and extracted text/links feed selector searches and link-graph analysis.

## Inputs → Outputs
- **In:** `domain` or URL pattern (index query)
- **Out:** `document-id` (WARC/WET/WAT captures) and the set of captured `domain`/URLs
- **Empty/negative result looks like:** a domain/URL absent from a given crawl — Common Crawl samples the web, so many pages simply aren't captured in any one crawl; check multiple monthly crawls before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: not a login, but effective use needs tooling/code and often AWS access — treat the **api-key/compute setup** as the barrier; it's not a casual web lookup.
- OpSec: fully **passive** — everything comes from the pre-built archive, never the target's server.
- Coverage is broad but incomplete and time-sliced; it favours popular/link-reachable pages. It is a research corpus, not a comprehensive or real-time mirror.

## Overlaps ("do both")
- Pairs with the Wayback Machine / [[archive-org]] and with `waybackurls`-style tools — Common Crawl is best for *scale and bulk discovery*, the Wayback Machine for *the full snapshot history of one URL*; use CC to enumerate, then Wayback to read specific captures.

## Trust & verifiability
`trust: trusted` — the Common Crawl Foundation is a reputable non-profit and its WARC captures are authentic raw web responses you can inspect directly; the only caveat is completeness (a sample per crawl), which you mitigate by querying several crawls.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | commoncrawl-org |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
