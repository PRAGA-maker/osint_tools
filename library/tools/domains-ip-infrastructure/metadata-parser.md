---
id: metadata-parser
name: Metadata Parser
description: Use when you have a `domain`/URL and want to programmatically pull page metadata (title, description, author, Open Graph images) at scale — returns metadata-exif, image, name.
url: https://github.com/jvanasco/metadata_parser
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Bulk-extracting Open Graph / meta-tag data (author, images, description) from web pages in Python.
selectorsIn:
- domain
selectorsOut:
- metadata-exif
- image
- name
status: live
pricing: free
costNote: Free, open-source Python library; install with `pip install metadata_parser`.
opsec: active
opsecNote: Active — the library fetches each target URL directly from wherever you run it, exposing your IP and User-Agent to the target's web server. Route through a proxy/VPN and set a neutral User-Agent when scraping subject-controlled pages.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Mature open-source library by jvanasco, in production "for many years" and used to parse billions of documents; source is public and auditable on GitHub.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- metadata_parser
- jvanasco/metadata_parser
tags:
- Domain/IP/Links
- metadata
- python
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Metadata Parser

> A battle-tested Python library that pulls as much structured metadata out of a web page as it can — Open Graph, Dublin Core, meta tags, title, canonical, author — so you can harvest page context across many URLs in code.

## When to use
You have a list of URLs/`domain`s (a subject's blog posts, profile pages, listing pages, or a set of links harvested from another tool) and you want to **extract who/what each page declares about itself** without hand-visiting each one: the `og:title`/description, `article:author` (`name`), the Open Graph `og:image`, canonical URL, and other meta fields. It is the code-level building block for enriching a bunch of links into structured leads.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install metadata_parser` (pulls in BeautifulSoup and Requests; `lxml` recommended for speed).
2. Parse a live URL:
   ```python
   import metadata_parser
   page = metadata_parser.MetadataParser(url="https://example.com/profile")
   page.get_metadatas('title')      # og/dc/meta title candidates
   page.get_metadatas('author')     # declared author name
   page.get_metadatas('image')      # og:image / thumbnail URL
   ```
3. Or parse HTML you already have (e.g. fetched behind a proxy): `MetadataParser(html=HTML)`.
4. Loop the calls over a URL list to build a table of {url → title, author, image, description}.
5. Pivot: an extracted author `name` feeds people-search; an `og:image` feeds reverse-image search; the description/keywords feed further pivots.

## Inputs → Outputs
- **In:** `domain`/URL (or raw HTML)
- **Out:** page `metadata-exif` (title, description, keywords, canonical, OG/DC fields), `image` (og:image/thumbnail URL), author `name`
- **Empty/negative result looks like:** the metadata dict is sparse or empty — the page declared no OG/meta tags (common for bare or JS-rendered pages), which is a limitation of the page, not proof of anything.

## Gotchas & OpSec
- **Active fetching:** each `url=` call is a direct HTTP request from your host — your IP/User-Agent hit the target server. For subject-controlled pages, fetch behind a proxy (or fetch the HTML separately and pass `html=`).
- It parses only server-delivered HTML; metadata injected by client-side JavaScript won't appear (fetch a rendered snapshot first if needed).
- Metadata is self-declared by the page author and can be wrong or deliberately misleading — corroborate.

## Overlaps ("do both")
- Complements a screenshotting/thumbnail workflow: this gives you the machine-readable metadata behind a page while a capture tool gives you the visual.

## Trust & verifiability
`trust: community` — long-lived, widely-used open-source code you can read and pin; the trust question is the honesty of each *page's* declared metadata, not the library.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metadata-parser |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → metadata-exif, image, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | active |
| human-in-loop | no |
