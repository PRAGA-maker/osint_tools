---
id: common-crawl
name: Common Crawl
description: Use when you have a `domain`/URL and want to mine web content at scale across billions of pages — a free petabyte-scale web corpus queryable by URL/domain via its index, returning archived page content and links.
url: https://commoncrawl.org/
category: archives-cache
path:
- archives-cache
- web
bestFor: Bulk historical web-content mining — pulling every crawled page/URL for a domain, or searching the corpus for a selector.
selectorsIn:
- domain
selectorsOut:
- domain
- email
- social-profile
status: live
pricing: free
costNote: Free and open. Data lives on AWS S3 (public bucket); you pay only if you run large compute against it. The URL index is free to query.
opsec: passive
opsecNote: You read a published dataset — you never touch the target's servers, so it's fully passive and the subject cannot see your queries. Ideal for researching a live site without hitting it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: Common Crawl is a well-known non-profit that has published open web crawls since 2008; widely used in research and by search/AI projects.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- commoncrawl-org
- index-commoncrawl-org
- wayback-machine
aliases:
- CommonCrawl
- CC
tags:
- web-archive
- corpus
- dataset
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Common Crawl

> A free, petabyte-scale open archive of the web — query its URL index to recover every page it crawled for a domain, or scan the corpus for a name/email at scale.

## When to use
You want web content in bulk rather than one snapshot: all the URLs Common Crawl has seen under a `domain`, the archived HTML of pages that may now be changed or gone, or a large-scale search for where a selector (email, handle, phrase) appears across the web. It complements the Wayback Machine — different crawl coverage and, crucially, a queryable **index** plus downloadable raw content (WARC) you can process yourself. Best when you need breadth/automation, not a single citeable snapshot.

## How to use it (`bestInteractionPattern`: api)
1. Pick a crawl (they're released roughly monthly) from https://commoncrawl.org/ / the index list.
2. Query the URL index for a domain, e.g. `https://index.commoncrawl.org/CC-MAIN-<crawl>-index?url=example.com/*&output=json` — returns every captured URL with the WARC file + byte offset.
3. Fetch the specific record (ranged GET against the public S3 WARC) to get the archived page content.
4. For corpus-wide selector search, run the columnar index (Athena/Parquet on AWS) rather than downloading everything.
5. Extract selectors from retrieved pages with `[[datasurgeon]]`.
6. Pivot: recovered URLs/emails/handles feed domain, email and username workflows.

## Inputs → Outputs
- **In:** a `domain`/URL pattern (or a selector to search the corpus)
- **Out:** list of captured URLs, archived page content (WARC), and any `email`/`social-profile`/links inside those pages
- **Empty/negative result looks like:** the index returns nothing for the domain — Common Crawl samples the web (it doesn't capture everything), so absence means "not in this crawl," not "never existed." Check other crawl months and the Wayback Machine.

## Gotchas & OpSec
- Not a point-and-click tool — it rewards a bit of scripting (index API + ranged S3 reads). The hosted index is the low-friction entry point.
- Coverage is a sample, released per crawl; check multiple crawls and combine with `[[wayback-machine]]` for completeness.
- Large-scale processing on AWS can incur compute cost even though the data is free; the URL index alone is free and light.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` — Common Crawl gives bulk/queryable coverage and raw content for analysis; Wayback gives deeper per-URL history and citeable snapshots. `[[index-commoncrawl-org]]` is the front-end to the URL index.

## Trust & verifiability
`trust: trusted` — Common Crawl is a long-running, reputable non-profit whose datasets underpin major research and search/AI projects. The archived content is authentic captures; as with any crawl, a page's *content* reflects what was live at crawl time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | common-crawl |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain, email, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
