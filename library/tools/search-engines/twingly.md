---
id: twingly
name: Twingly
description: Use when you have a `name`, `username`, or keyword and want broad blog/news/forum (and dark-web) monitoring across many languages — returns matching posts and `social-profile`/`domain` leads.
url: https://www.twingly.com
category: search-engines
path:
- search-engines
bestFor: API-driven monitoring of news, blogs, and forums worldwide for mentions of a subject or term.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: freemium
costNote: Freemium — free API trial/keys with volume limits; sustained/commercial use is paid.
opsec: passive
opsecNote: You query Twingly's aggregated index, not the source sites, so monitoring is passive and the subject isn't alerted. API use requires registering for a key (tie it to a sock-puppet identity, not your real one).
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: Established Swedish content-aggregation company; its index is broad and reputable, but coverage per source varies and its data is a firehose to filter, not a curated answer.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- twingly.com
- Twingly Blog Search
tags:
- Search engines
- Universal search tools
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Twingly

> A content-aggregation platform "turning headlines into data" — millions of daily news articles, blog posts, and forum threads (plus dark-web content) searchable via API across 100+ countries.

## When to use
You need broad, multilingual monitoring of the open web's *conversational* layer — blogs, news, and forums — for mentions of a `name`, `username`, org, or keyword, especially outside English. Good for building an ongoing watch (alerts as new posts appear) rather than a one-time lookup, and for reaching smaller sources that mainstream search deprioritizes.

## How to use it (`bestInteractionPattern`: api)
1. Sign up at https://www.twingly.com for a free API key (blog/news/forum search endpoints).
2. Query the relevant API with your search term and language/date filters; parse the JSON/XML results (title, URL, source, published date).
3. For ongoing monitoring, poll on a schedule and diff for new posts.
4. Review hits manually — it's a firehose, so filter aggressively for genuine matches.
5. Pivot: a post's author/handle is a `social-profile` lead; the hosting site is a `domain` to profile.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword (with language/date filters)
- **Out:** `social-profile` (post authors/blogs), `domain` (source sites) — matching posts with metadata
- **Empty/negative result looks like:** zero results for a term means it hasn't appeared in Twingly's indexed sources in your window — narrow-language or very local mentions may simply be outside coverage.

## Gotchas & OpSec
- Human-in-the-loop: requires an **API key** (register with a sock-puppet), and free tiers cap volume.
- It's a **firehose**, not a ranked answer — expect noise and filter hard.
- Coverage varies by source type and language; absence isn't proof.

## Overlaps ("do both")
- Pairs with Google News/blog dorks and social-platform searches — do both, since Twingly reaches long-tail blogs/forums that general search buries, while general search catches what Twingly hasn't indexed.

## Trust & verifiability
`trust: community` — a reputable aggregator, but it delivers raw matches from third-party sites; verify each hit at its source and treat coverage gaps as index limits, not confirmed absence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twingly |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
