---
id: one-charliebrassington
name: one (charliebrassington)
description: Use when you have an `email`, `username`, `name` or UK postcode and want a Python CLI that scrapes multiple people-search and account sources at once — returns addresses, phones, associates and linked accounts.
url: https://github.com/charliebrassington/one
category: people-search
path:
- people-search
bestFor: Running several people-search / account-discovery scrapers (US + UK, Discord, Minecraft, account-recovery) from one command line.
selectorsIn:
- email
- username
- name
- address
- phone
selectorsOut:
- address
- phone
- associate
- name
- social-profile
status: unknown
pricing: free
costNote: Open-source (MIT-style) on GitHub, free to clone and run; some individual scrapers may hit paywalled or rate-limited upstream sites.
opsec: active
opsecNote: Each scraper queries a live third-party site (people-search DBs, Discord, Virgin Media postcode lookup) directly from your IP, so this is active — those sites log the request and may rate-limit or block. Run from a sock-puppet IP/VPN, and expect that scraping people-search sites can violate their ToS.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: python-lib
trust: community
trustNote: Small community project (~34 GitHub stars) by an individual developer; code is inspectable but unmaintained-scale and dependent on brittle upstream scrapers that break when target sites change.
missingPersonsRelevance: high
coverage:
- us
- gb
auth: none
api: false
localInstall: true
registration: false
aliases:
- one osint tool
- charliebrassington/one
tags:
- people-search
- scraper
- cyberbackgroundchecks
- us
- uk
- python
source: gh-topic-osint-framework
lastVerified: '2026-07-15'
enrichment: full
---

# one (charliebrassington)

> A Python command-line aggregator that fires several OSINT scrapers at a target and cross-validates what they return — "finds more information with the information it finds."

## When to use
You have a seed selector — `email`, `username`, `name`, `phone`, `address`, or a UK postcode+surname — and want to fan out across multiple sources in one shot rather than querying each by hand. It bundles email-to-accounts, Discord profile, Minecraft username, US **and** UK people-search, account-recovery info, and a Virgin Media device lookup (postcode + surname). Good as an early wide-net pass to see which sources have anything, then verify manually.

## How to use it (`bestInteractionPattern`: python-lib)
1. Clone: `git clone https://github.com/charliebrassington/one && cd one`.
2. Install deps: `pip install -r requirements.txt` (Python 3).
3. Run against your seed, e.g. `python3 main.py --search-depth 5 --email target@example.com --minecraft-username someHandle`. `--search-depth` controls how aggressively it re-queries on newly found data.
4. Read the consolidated console output: matched accounts, addresses/phones from people-search modules, relatives, and validation notes.
5. Pivot: feed discovered addresses/phones/relatives into dedicated public-records tools; feed found usernames into cross-platform checks.

## Inputs → Outputs
- **In:** `email`, `username`, `name`, `phone`, `address` / UK postcode
- **Out:** `address`, `phone`, `associate` (relatives), `name`, `social-profile` (Discord/Minecraft/other accounts)
- **Empty/negative result looks like:** modules returning "no results" or throwing scrape errors (HTTP 403/CAPTCHA/layout change). A blank result usually means the upstream site blocked the scrape, not that no data exists — retry manually on that source.

## Gotchas & OpSec
- **Brittle scrapers:** it depends on the current HTML of third-party sites (cyberbackgroundchecks and similar); when those change or add anti-bot defenses, modules silently break. Verify anything critical directly.
- **Active & ToS-sensitive:** you are hitting people-search and provider sites directly; use a VPN/sock-puppet IP and be aware scraping may breach their terms.
- **rate-limit** human-in-loop: expect CAPTCHAs / throttling on the heavier US people-search modules; you may need to slow `--search-depth` or run modules individually.
- Data can be stale — people-search records lag reality by months to years.

## Overlaps ("do both")
- Pairs with authoritative single-source tools ([[account-live-com]] for Microsoft-account existence, dedicated UK/US public-records lookups) — `one` casts the wide net cheaply; those confirm and enrich the specific hits it surfaces.

## Trust & verifiability
`trust: community` — a small, individually-maintained GitHub project. The code is open to inspection, but results are only as good (and current) as the brittle upstream scrapers it wraps; treat every hit as a lead to verify, not a fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | one-charliebrassington |
| category | people-search |
| selectorsIn → selectorsOut | email, username, name, address, phone → address, phone, associate, name, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | active |
| human-in-loop | yes (rate-limit) |
