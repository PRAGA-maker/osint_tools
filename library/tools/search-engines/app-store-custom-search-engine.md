---
id: app-store-custom-search-engine
name: App Store Custom Search Engine
description: Use when you have an app name, developer, or `username` and want to search Apple/Google app-store listings — returns developer org, linked sites, and social profiles.
url: https://cse.google.com/cse/publicurl?cx=006205189065513216365:aqogom-kfne
category: search-engines
path:
- search-engines
bestFor: Scoping a Google search to app-store listing pages to find who publishes an app and their linked contact details.
selectorsIn:
- username
- name
selectorsOut:
- employer-org
- social-profile
- domain
status: degraded
pricing: freemium
costNote: Free to use (Google Programmable Search); no account needed. Results depend on a third-party CSE configuration that can rot over time.
opsec: passive
opsecNote: Runs as an ordinary Google query, so it leaks only to Google — not to any app developer. No account or login required; a clean browser session is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built Google Programmable Search Engine (CSE); it only re-scopes Google's index, so result quality is Google's but the site whitelist is whoever configured the cx.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- App Store CSE
- Google Programmable Search app stores
tags:
- custom-search-engine
- app-store
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# App Store Custom Search Engine

> A pre-built Google Programmable Search that restricts results to app-store listing pages, so you can find the developer and contact trail behind an app.

## When to use
You have an app name, a developer handle, or a `username`/`name` you suspect publishes mobile apps, and you want to reach the listing pages (Apple App Store, Google Play, and similar) without wading through the open web. App-store listings expose the publishing `employer-org`/developer, a support `domain` and email, and often links to the developer's `social-profile`s — a useful pivot when a subject or a business is tied to an app.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL and type the app name, developer, or username into its search box.
2. Read the returned listing pages for: developer/publisher name, support website and email, privacy-policy domain, and linked social accounts.
3. If the CSE returns nothing useful, fall back to plain Google with explicit scoping: `site:apps.apple.com` or `site:play.google.com "<term>"`.
4. Pivot: the developer name feeds people/company search; the support domain feeds WHOIS; a privacy-policy email feeds email-OSINT.

## Inputs → Outputs
- **In:** `username` / `name` / app name
- **Out:** `employer-org` (developer/publisher), `domain` (support/privacy site), `social-profile` links
- **Empty/negative result looks like:** no listings, or the CSE page fails to load — the underlying `cx` config may have been deleted. Treat an empty CSE as "use the `site:` fallback," not as "no app exists."

## Gotchas & OpSec
- This is a third-party CSE: its whitelist and continued existence are outside your control, so verify with a raw `site:` query when precision matters (status is flagged `degraded` for that reason).
- It only narrows Google's index — it cannot see anything Google has not crawled, and store pages are sometimes thin.

## Overlaps ("do both")
- Pairs with direct `site:apps.apple.com` / `site:play.google.com` searches and with WHOIS on the support domain — the CSE is a convenience wrapper; the raw scoped search is the durable method.

## Trust & verifiability
`trust: community` — the search results are Google's, but the app-store scoping is defined by an unknown third party's CSE config, which can silently break; confirm important hits directly on the store.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | app-store-custom-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | username, name → employer-org, social-profile, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
