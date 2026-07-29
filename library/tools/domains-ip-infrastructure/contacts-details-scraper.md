---
id: contacts-details-scraper
name: Contacts Details Scraper
description: Use when you have a `domain`/website and want to harvest its published contact points — returns emails, phone numbers and linked social profiles.
url: https://github.com/vdrmota/Social-Media-and-Contact-Info-Extractor
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Crawling a website to extract emails, phone numbers and social-media profile links.
selectorsIn:
- domain
selectorsOut:
- email
- phone
- social-profile
status: live
pricing: freemium
costNote: Open-source; runs free as an Apify actor (Apify's free tier covers light use) or from source. Heavier Apify usage consumes platform credits.
opsec: active
opsecNote: Active — it crawls the target website, so requests hit the subject's server and appear in their logs. When run via Apify the crawl originates from Apify's infrastructure, not your IP; running from source uses your own IP, so use a research egress.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community open-source Apify actor (~122 stars) by vdrmota; extraction is regex/HTML-parsing based, so expect noise and false positives.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
relatedTools:
- webosint
- jsleak
aliases:
- Social Media and Contact Info Extractor
tags:
- Domain/IP/Links
- Searchers, scrapers, extractors, parsers
- contact-scraper
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Contacts Details Scraper

> An Apify actor that crawls a website and pulls out its published emails, phone numbers and social-media profile links.

## When to use
You have a `domain`/website (a subject's site, a business, an organisation) and want its published contact surface in one pass — emails, phone numbers, and linked Facebook/Twitter/LinkedIn/Instagram profiles — rather than clicking through pages manually. Good for turning a website into pivot points (contacts and social handles).

## How to use it (`bestInteractionPattern`: web-manual)
1. Easiest: run it as an Apify actor from the linked page (needs a free Apify account — the human-in-the-loop gate). Alternatively clone the repo and run the source (Node) locally.
2. Provide starting URL(s) and set crawl depth/limits.
3. Let it follow in-domain links and extract contact details via HTML parsing/regex.
4. Export results as JSON/CSV/Excel and de-duplicate/triage (expect some false positives).
5. Pivot: extracted `email`/`phone` feed contact-OSINT; `social-profile` links feed username/social tools.

## Inputs → Outputs
- **In:** `domain`/website URL(s)
- **Out:** `email`, `phone`, `social-profile` links harvested from the site
- **Empty/negative result looks like:** few/no contacts (a site that hides contact info or renders it as images/JS) — absence isn't proof none exist.

## Gotchas & OpSec
- Human-in-the-loop: the Apify path needs a free account (`account-login`); the source path avoids that but uses your IP.
- OpSec: **active** — crawling touches the target's server. Prefer the Apify-hosted run (its IP, not yours) or a research egress; respect robots/scope and local law.
- Regex/HTML extraction is noisy — verify emails/phones before acting; social links may be generic (share buttons), not the subject's.

## Overlaps ("do both")
- Pairs with `[[webosint]]` (WHOIS/DNS/subdomain context for the domain) and `[[jsleak]]` (mine the site's JavaScript for endpoints/emails the crawler misses).

## Trust & verifiability
`trust: unverified` — a small community scraper; every extracted contact is a parser guess, so confirm emails/phones/profiles independently before treating them as the subject's.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | contacts-details-scraper |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → email, phone, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
