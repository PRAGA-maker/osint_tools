---
id: dorksearch-netlify-app
name: dorksearch.netlify.app
description: Use when you have a `name`, `email`, `username`, or `domain` and want help composing Google dork queries to surface hidden pages — returns a ready-to-run dork URL yielding `social-profile`, `document-id`, `domain`.
url: https://dorksearch.netlify.app/
category: search-engines
path:
- search-engines
- search-tools
bestFor: Quickly assembling Google advanced-operator (dork) queries around a selector without memorizing the syntax.
selectorsIn:
- name
- email
- username
- domain
selectorsOut:
- social-profile
- document-id
- domain
status: live
pricing: free
costNote: Free, no account; a lightweight client-side query builder.
opsec: passive
opsecNote: The builder itself just assembles a query string; the actual search runs on Google under your session. Run the resulting dork from a sock-puppet browser — Google logs the query and the target sites see nothing until you click through.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A community-built, Netlify-hosted dork helper (not the only tool by this name) — it only formats standard Google operators, so there is no data-quality risk, just verify it points at real google.com searches.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- api-guesser
- deaditarchive-netlify-app
- reddit-timer
- search-it
aliases:
- dorksearch
tags:
- google-dorks
- search-operators
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# dorksearch.netlify.app

> A point-and-click builder for Google dork queries — pick operators, drop in a selector, and it hands you a ready-to-run advanced search that surfaces pages plain keywords miss.

## When to use
You have a `name`, `email`, `username`, or `domain` and want to squeeze more out of Google with advanced operators (`site:`, `filetype:`, `intitle:`, `inurl:`, quoted exact phrases) but don't want to hand-write the syntax. It turns your inputs into a valid dork URL — useful for finding exposed documents, directory listings, profile pages, and mentions across a specific site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dorksearch.netlify.app/.
2. Choose operators and enter your selector — e.g. constrain to a `domain` with `site:`, hunt documents with `filetype:pdf`, or pin an exact `"First Last"`.
3. It generates the composed Google query/URL; run it (ideally in a sock-puppet browser).
4. Read Google's results and pivot: an exposed `document-id`/PDF feeds metadata analysis; a profile URL feeds `social-profile` tools; a new `domain` feeds infrastructure OSINT.

## Inputs → Outputs
- **In:** `name` / `email` / `username` / `domain` + chosen operators
- **Out:** a ready-to-run Google dork → results yielding `social-profile`, `document-id` (exposed files), `domain`
- **Empty/negative result looks like:** a valid dork that Google returns zero results for — usually means the operator combination was too narrow; loosen it, since the tool only builds the query and cannot itself "find nothing."

## Gotchas & OpSec
- It does not search — it only builds the query; the search and its logging happen on Google under your identity, so use sock-puppet hygiene.
- Overly specific dorks return nothing; iterate from broad to narrow.
- Google may throw a CAPTCHA on aggressive dorking — that is Google's rate limit, not a tool failure.

## Overlaps ("do both")
- Pairs with `[[search-it]]` and other dork/query helpers — different builders expose different operator presets, so try more than one when a search runs dry.

## Trust & verifiability
`trust: unverified` — a small community-hosted helper; it merely formats standard Google operators, so results are exactly as trustworthy as Google itself, but confirm it links to genuine `google.com` searches.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dorksearch-netlify-app |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, username, domain → social-profile, document-id, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
