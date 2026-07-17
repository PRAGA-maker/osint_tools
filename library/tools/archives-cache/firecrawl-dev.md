---
id: firecrawl-dev
name: firecrawl.dev
description: Use when you have a `domain`/URL and want its content as clean structured data — crawls and converts pages to markdown/JSON for archiving or bulk extraction.
url: https://www.firecrawl.dev/
category: archives-cache
path:
- archives-cache
bestFor: Programmatically scraping/crawling a site into clean markdown or JSON (JS-rendered pages included) for capture and analysis.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: freemium
costNote: Free tier of ~1,000 pages/month; paid Hobby/Standard/Growth plans for higher volume. Open-source self-host option available.
opsec: active
opsecNote: Firecrawl fetches the target site's live pages (its servers, or yours if self-hosted, hit the target) — so the site's logs see that traffic, not you directly if using the cloud API. Treat as active toward the target; throttle, respect robots where appropriate, and avoid hammering a small site.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: trusted
trustNote: Widely-adopted open-source scraping platform (150k+ GitHub stars, used by many companies); it's tooling, so output fidelity depends on the target site.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- httrack
- waybackpy
- scrapy
aliases:
- Firecrawl
- firecrawl.dev
tags:
- archive
- Archive & Cached Related Sites
- scraping
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# firecrawl.dev

> A scraping/crawling API that turns websites into clean markdown or JSON — for capturing and bulk-extracting content from a site, JavaScript and all.

## When to use
You need to grab a site's content as structured data — snapshot a subject's whole blog/forum/profile section before it changes, or extract fields across many pages — and want it clean (markdown/JSON) rather than raw HTML. Firecrawl handles JS rendering and pagination, which plain scrapers choke on. It's infrastructure/tooling (low direct MP relevance) but useful for preserving and processing web evidence at scale.

## How to use it (`bestInteractionPattern`: api)
1. Sign up at https://www.firecrawl.dev/ for an API key (free tier ~1,000 pages/month), or self-host the open-source version.
2. Call **scrape** for a single URL → clean markdown/JSON/screenshot; or **crawl** for a whole site/section.
3. Use the **search** endpoint to find pages, or the interact features to reach content behind clicks/logins (with care and authorization).
4. Store the returned markdown/JSON as your captured record.
5. Pivot: extracted contacts/usernames/links → the rest of the investigation; for a permanent public archive of a single URL instead, use `[[waybackpy]]`/the Wayback Machine.

## Inputs → Outputs
- **In:** a `domain`/URL (single page or a crawl scope)
- **Out:** clean markdown/JSON/screenshots of the page(s) — a captured document (`document-id`)
- **Empty/negative result looks like:** empty content or an error — the site blocked the crawler, requires auth Firecrawl can't pass, or the URL is dead; check status and consider a self-hosted run.

## Gotchas & OpSec
- **Active toward the target:** it fetches live pages; don't overwhelm small sites, and respect legal/robots limits.
- Free tier is capped (~1,000 pages/month) — plan crawl scope accordingly.
- It captures live content, not history — for past versions of a page use an archive tool, not Firecrawl.
- "Interact behind logins" must only be used where you're authorized.

## Overlaps ("do both")
- Pairs with `[[waybackpy]]`/the Wayback Machine — Firecrawl captures the *current* site cleanly; the Wayback Machine gives *historical* captures and a permanent public record. Use both for now-and-then.
- Pairs with `[[httrack]]` for a full offline mirror when you want files rather than structured text.

## Trust & verifiability
`trust: trusted` — a mature, widely-used, open-source platform. The captured content is a faithful copy of what the target served at capture time; verify anything decisive against the live page or an independent archive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | firecrawl-dev |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | api |
| opsec | active |
| human-in-loop | yes (api-key) |
