---
id: duckduckgo-url-scraper
name: DuckDuckGo URL Scraper (its0x08)
description: Use when you have a search query/`domain` and want a scriptable list of DuckDuckGo result URLs for a pipeline — returns a list of domains/URLs.
url: https://github.com/its0x08/duckduckgo
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Pulling DuckDuckGo search-result URLs from the command line to feed other recon tools.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open-source (Python 3) on GitHub; run it locally, no account or key.
opsec: active
opsecNote: Scraping DuckDuckGo sends automated queries from your IP — that's active and can trip rate limits or blocks. Route through a proxy/VPN, keep the built-in rate limiting on, and don't hammer it; heavy automated scraping may breach the engine's terms.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: A small community CLI (self-described v0.0.1-beta "demonstration"); read the code before running, and expect breakage when DuckDuckGo changes its markup.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- ddg url scraper
- its0x08 duckduckgo
tags:
- search
- cli
- automation
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# DuckDuckGo URL Scraper (its0x08)

> A small Python CLI that runs a DuckDuckGo query and prints the result URLs — glue for feeding search hits into an automated recon pipeline.

## When to use
You want the URLs that a DuckDuckGo query returns as machine-readable output — to pipe into other tools (dorking, screenshotting, subdomain/asset enumeration) rather than click through a browser. Reach for it when scripting: e.g. dork a `domain`, collect every result URL, and hand them to the next stage. It gathers links, not people; it's plumbing for automation.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/its0x08/duckduckgo` and ensure Python 3 is installed.
2. Run `python ddg.py "<query>"` with flags: `-n` result count, `-t` timing, `-o` output file.
3. Capture the printed URLs (or the output file) and pipe them into your next tool.
4. Keep the built-in rate limiting; add a proxy/VPN so the automated queries aren't tied to your IP.
5. Pivot: feed the URL list into screenshotters, `[[pdfmyurl]]`-style capture, or domain/asset recon.

## Inputs → Outputs
- **In:** a search query (often a `domain` or dork)
- **Out:** a list of result URLs/`domain`s, printable or written to file
- **Empty/negative result looks like:** zero results or an error/CAPTCHA page scraped instead — DuckDuckGo may have rate-limited or changed markup; back off, add delay, or update the scraper.

## Gotchas & OpSec
- OpSec: **active** automated querying — rate-limit, proxy, and don't abuse the engine (heavy scraping can breach its terms and get you blocked).
- It's a v0.0.1-beta "demonstration" tool: read the code first, and expect it to break when DuckDuckGo changes its HTML.
- For low volume, a manual browser search is simpler; use this only when you genuinely need scripted output.

## Overlaps ("do both")
- Feeds capture/recon tools like `[[pdfmyurl]]` — this produces the URL list, those preserve or fingerprint each URL. Chain them for a scripted collect-then-capture flow.

## Trust & verifiability
`trust: community` — a small open-source CLI; verifiable because you can read the code, but unmaintained scrapers rot quickly, so confirm it still parses current results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | duckduckgo-url-scraper |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (rate-limit) |
