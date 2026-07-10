---
id: impersonal-me
name: impersonal.me
description: Use when you have a `name`, `username`, or keyword and want to see Google results as they appear in another country/language — returns localized `social-profile`s and pages hidden by your own geo/language defaults.
url: https://impersonal.me/
category: search-engines
path:
- search-engines
bestFor: Viewing localized Google search results from 50+ countries and 30+ languages without changing your own location.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: passive
opsecNote: You search Google via impersonal.me rather than the target — passive toward the subject. The service states it doesn't store/track queries, but you are still routing searches through a third party; use a clean/sock-puppet browser for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A localized-Google front-end aimed at SEO/researchers; it surfaces Google's own results, so quality is Google's — the tool just changes the geo/language lens.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- impersonal.me
- localized Google search
tags:
- searchengines
- Search Engines
- localized-search
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# impersonal.me

> A localized-Google lens — run a search as if you were in another country/language, surfacing results your home geo/language would bury.

## When to use
You have a `name`, `username`, or keyword and suspect the most relevant results are region-specific — e.g. a subject active in another country, whose local news, directory listings, or social profiles rank in that country's Google but not yours. impersonal.me lets you see Google exactly as a user in 50+ countries / 30+ languages would, without a VPN or changing your settings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://impersonal.me/.
2. Enter your search terms (`name`, `username`, distinctive phrase).
3. Select the target country and language, and toggle desktop/mobile view.
4. Read the localized results — compare against your home-region results to spot country-specific pages.
5. Pivot: open localized `social-profile`s / directory hits; repeat across several relevant countries if the subject's location is uncertain.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword + a target country/language
- **Out:** localized Google results — `social-profile`s, news, and pages ranked in that region
- **Empty/negative result looks like:** same or empty results as your home search — meaning nothing region-specific surfaced (or your terms are too generic). Try other countries/languages and exact-phrase queries.

## Gotchas & OpSec
- It's a lens on Google, not a separate index — it can't find what Google doesn't have.
- Best value when you already suspect a specific country/language; blind sweeping across all 50 is noisy.
- Passive; still route sensitive searches through a sock-puppet browser.

## Overlaps ("do both")
- Pairs with direct Google country/language operators (`gl=`/`hl=`) and other search engines (Yandex for Russia, Baidu for China) — impersonal.me is the quick way to fake geo, native engines cover what Google under-indexes locally.

## Trust & verifiability
`trust: community` — a convenience front-end over Google. Reliable as a geo/language switch; the results are Google's and should be verified at their source.
