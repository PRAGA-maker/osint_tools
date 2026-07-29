---
id: siftrss-com
name: Siftrss.com
description: Use when you have an RSS/Atom feed `url` and want a filtered version that only emits items matching your terms — returns a new feed `url` for monitoring a target.
url: https://siftrss.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Turning a noisy RSS/Atom feed into a filtered feed that alerts only on items mentioning a subject's name, handle, or keyword.
selectorsIn:
- domain
- name
selectorsOut:
- domain
status: live
pricing: free
costNote: Free to use with no account or login required; you paste a feed URL and get a filtered feed URL back.
opsec: passive
opsecNote: SiftRSS fetches the source feed server-side on its own infrastructure, so the target site sees SiftRSS's servers, not you — this is good passive tradecraft for monitoring. Note that your filter terms (which may reveal who/what you are watching) are stored in the generated feed URL on a third-party service; keep the terms generic if that matters and consume the feed through a reader you control.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small independent free utility; it is a pass-through filter proxy rather than a data source, so trust concerns are about uptime and privacy of your filter terms, not data accuracy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SiftRSS
- RSS feed filter
tags:
- Files
- monitoring
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Siftrss.com

> A free RSS/Atom filter proxy: paste a noisy feed, get back a feed that only fires on items matching your keywords — a lightweight monitoring primitive.

## When to use
You have a source that publishes an RSS/Atom feed — a news site, a forum, a blog, a court-record or notice feed — and you only care about items mentioning a specific `name`, handle, place, or keyword. SiftRSS returns a new feed URL pre-filtered to those terms, so your reader alerts you only on relevant hits instead of the whole firehose. Ideal for standing surveillance of a subject or topic across many sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Find the source feed URL (many sites expose `/feed`, `/rss`, or a feed `<link>` in the page head).
2. Go to https://siftrss.com/ and paste the feed URL.
3. Add filter rules — match on title, description, link, or a PCRE **regex** (with flags like case-insensitivity) — and choose include (only matching) or exclude (drop matching).
4. Copy the generated SiftRSS feed URL and subscribe to it in your RSS reader.
5. New items matching your terms now arrive automatically; pivot each hit into the underlying source for full context.

## Inputs → Outputs
- **In:** a source feed `url` + filter terms (`name`/keyword)
- **Out:** a filtered feed `url` you subscribe to
- **Empty/negative result looks like:** the filtered feed stays empty — either nothing has matched yet (keep watching) or your regex is too strict; loosen it and confirm the source feed itself is valid.

## Gotchas & OpSec
- No login, so nothing to leak on your side — but the filter terms live inside the generated URL on SiftRSS's servers; keep them generic if the watch-list itself is sensitive.
- SiftRSS polls the source on its own schedule; near-real-time alerting isn't guaranteed.
- It only works on sources that actually publish RSS/Atom; for HTML-only pages, pair with a page-to-feed generator first.

## Overlaps ("do both")
- Pairs with page-to-RSS generators (turn an HTML page into a feed, then filter it here) and with any RSS reader/alerting tool that consumes the filtered feed.

## Trust & verifiability
`trust: community` — it is a small independent pass-through utility, not a data source, so there's no data-accuracy risk; the caveats are uptime and the privacy of your stored filter terms.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | siftrss-com |
| category | documents-metadata |
| selectorsIn → selectorsOut | domain, name → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
