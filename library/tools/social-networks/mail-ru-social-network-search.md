---
id: mail-ru-social-network-search
name: Mail.Ru Social Network Search
description: Use when you have a `name` or `username` for a RU/CIS subject and want to surface Russian-language social and web results — returns social-profile and name leads.
url: https://go.mail.ru/search_social
category: social-networks
path:
- social-networks
bestFor: Russian-language name/username search that indexes VK, Odnoklassniki and other RU/CIS web content Google under-covers.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free Russian search portal; no account needed. The old dedicated `search_social` endpoint now 301-redirects to Mail.Ru's general web search, so it is no longer a purpose-built social-only filter.
opsec: passive
opsecNote: Mail.Ru is a Russian (VK Group) service; every query is logged under Russian jurisdiction and may be tied to your IP. Use a sock-puppet browser + VPN, and never search from an attributable session. Nothing is sent to the target.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by VK Group (Mail.Ru). Authoritative reach into RU/CIS content, but a commercial engine with opaque ranking and heavy ad content — treat results as leads.
missingPersonsRelevance: high
coverage:
- ru
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- yandex-people-search
aliases:
- go.mail.ru social search
- Mail.ru search
tags:
- real-time-search-social-media-search-and-general-social-media-tools
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Mail.Ru Social Network Search

> Russia's Mail.Ru search portal used as an OSINT lens on RU/CIS subjects — strong on VK/Odnoklassniki and Cyrillic content that Western engines miss.

## When to use
Your subject is Russian, Ukrainian, Belarusian or otherwise CIS-linked, and Google/Bing return little. Enter a `name` (in Cyrillic if you can) or `username` to pull Russian-language social and web results — useful for locating VK/OK profiles, forum posts, and news mentions tied to a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://go.mail.ru/search_social in a sock-puppet browser (it redirects to Mail.Ru's main search — that's expected).
2. Enter the subject's name or username. Cyrillic spelling dramatically improves recall; transliterate if needed (e.g. "Ivan Petrov" → "Иван Петров").
3. Scan results for VK (`vk.com`), Odnoklassniki (`ok.ru`), and RU news/forum hits.
4. Solve any CAPTCHA the portal throws (common from non-RU IPs).
5. Pivot: a VK/OK profile ID feeds VK-specific enumeration tools and reverse-friend analysis.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (VK/OK/RU sites), `name` corroboration
- **Empty/negative result looks like:** generic ad-heavy results with no person match — often means you searched Latin script; retry in Cyrillic before concluding nothing exists.

## Gotchas & OpSec
- Human-in-the-loop: CAPTCHAs appear frequently for foreign IPs and rapid queries — solve manually and slow down.
- Degraded: the dedicated social-search filter is gone; you now get general web search, so add `site:vk.com` / `site:ok.ru` to focus it.
- OpSec: passive but **Russian-jurisdiction logging** — never query from an attributable browser/IP.

## Overlaps ("do both")
- Pairs with Yandex people search — both index RU content but rank and cache differently, so each surfaces profiles the other buries.
- Follow with a dedicated VK profile tool once you have a `vk.com` ID.

## Trust & verifiability
`trust: community` — a first-party major search engine with authoritative RU reach, but ranking is opaque and ad-laden; verify each hit against the actual social profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mail-ru-social-network-search |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
