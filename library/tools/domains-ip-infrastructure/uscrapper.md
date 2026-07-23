---
id: uscrapper
name: USCRAPPER
description: Use when you have a `domain`/URL and want contact details harvested from it — returns `email`s, `phone`s, `social-profile` links, and other extracted identifiers.
url: https://github.com/z0m31en7/Uscrapper
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Automated one-shot extraction of emails, phones, and social links from a target web page.
selectorsIn:
- domain
selectorsOut:
- email
- phone
- social-profile
status: live
pricing: free
costNote: Free and open-source; run locally with Python.
opsec: active
opsecNote: "USCRAPPER fetches the target page(s) directly from your machine, so the site's logs see your IP and user-agent — this is active reconnaissance against the target's server. Run it through a VPN/proxy and a sock-puppet user-agent, and respect that hammering a small personal site is noisy and potentially attributable."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source community tool (z0m31en7/Uscrapper); it is a straightforward regex/scraper, so review the code before running and treat extracted data as unverified leads.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- what-mail
aliases:
- Uscrapper
- z0m31en7/Uscrapper
tags:
- Domain/IP/Links
- Searchers, scrapers, extractors, parsers
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# USCRAPPER

> A small Python scraper that pulls contact details — emails, phone numbers, social links — out of a web page in one command.

## When to use
You have a `domain`/URL (a personal site, a small-business page, a portfolio) and want to quickly harvest the contact identifiers it exposes rather than eyeballing the source. It turns a page into a de-duplicated list of `email`s, `phone`s, and `social-profile` links you can then pivot on. It only reads what a page publishes, so it is a convenience/extraction tool with low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/z0m31en7/Uscrapper && cd Uscrapper` then install its Python requirements.
2. Run against a target: `python Uscrapper.py -u https://example.com` (add flags for crawl depth/threads as documented).
3. Read the output: extracted emails, phone numbers, social-media links, and other identifiers it recognizes.
4. Route it through a proxy/VPN first (it hits the site directly).
5. Pivot: feed a harvested `email` into an email-verification/breach tool, or a social link into profile enrichment.

## Inputs → Outputs
- **In:** `domain`/URL
- **Out:** `email`, `phone`, `social-profile` links extracted from the page
- **Empty/negative result looks like:** no matches — the page simply doesn't expose contact data in a scrapable form (images, contact forms, JS-rendered content defeat it); absence ≠ the person has no email.

## Gotchas & OpSec
- **Active:** it fetches the target directly, so your IP hits the site's logs — proxy it and don't hammer small sites.
- Regex-based extraction misses obfuscated (`name [at] domain`), image-embedded, or JS-rendered contacts, and can produce false positives.
- It's community code — read it before running and treat every extracted value as an unverified lead.

## Overlaps ("do both")
- Pairs with [[what-mail]] and email-verification tools — USCRAPPER harvests candidate `email`s from a site, those tools then validate and enrich them.

## Trust & verifiability
`trust: community` — an open, auditable scraper with no central service; reliability is only as good as the target page's markup, so confirm every harvested identifier independently.
