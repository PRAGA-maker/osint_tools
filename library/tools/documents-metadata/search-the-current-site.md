---
id: search-the-current-site
name: Search the current site
description: Use when you're on a site and have a `name`/`username`/keyword to find across all its pages — returns matching pages via a one-click `site:` search.
url: https://chromewebstore.google.com/detail/search-the-current-site/jliolpcnkmolaaecncdfeofombdekjcp
category: documents-metadata
path:
- documents-metadata
bestFor: One-click Google `site:` search of every page of the website you're currently viewing.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Chrome extension; no account or payment.
opsec: passive
opsecNote: It just runs a Google `site:` query — a normal search, invisible to the site owner. Your Google session sees the query; use a sock-puppet browser profile if you don't want it tied to your identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A simple third-party utility that automates a Google `site:` search; the results come from Google, not the extension, so trust rests on Google's index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- google-universal-dork-builder
- dork-dump
aliases:
- Search the Current Site with Google Site Search
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- site-search
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Search the current site

> A toolbar button that runs a Google `site:thispage.com` search — the fast way to sweep an entire forum, directory, or archive for a name or handle without leaving the page.

## When to use
You're on a site that has weak or no internal search — a forum, a membership directory, a local-news archive, a niche community — and you want to know everywhere your `name`/`username`/keyword appears on it. The extension fires a `site:`-scoped Google query for the current domain in one click, turning any site into something searchable across all its indexed pages.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Search the current site" from the Chrome Web Store in your investigation profile.
2. Browse to the site you want to search.
3. Click the toolbar button, type your term (a `name`, `username`, phone fragment, etc.), and run it — it opens Google results limited to that domain.
4. Optionally right-click → Options to switch the engine to Bing/Yahoo/Yandex (each has a different index) or enable a right-click "search this domain" context action.
5. Pivot: profile/thread hits become `social-profile` leads and new selectors (other handles, emails, locations) to chase.

## Inputs → Outputs
- **In:** `name` / `username` / keyword (against the current domain)
- **Out:** matching pages on that site → `social-profile`, threads, mentions
- **Empty/negative result looks like:** no results — either the term isn't on the site, or Google hasn't indexed those pages (common for login-walled or `robots.txt`-blocked areas). Retry with Bing/Yandex, or use the site's own search if it has one.

## Gotchas & OpSec
- You're limited to what the chosen engine has indexed; deep, paginated, or auth-walled content won't appear.
- Switching engines (Bing/Yandex) can surface pages Google missed — worth doing on a thin site.
- OpSec: passive; it's a search query, not a site interaction.

## Overlaps ("do both")
- Complements manual dorking via `[[google-universal-dork-builder]]` and `[[dork-dump]]` — this is the quick single-site version; the dork builders let you add filters (filetype, intitle, date) the button doesn't expose.

## Trust & verifiability
`trust: unverified` — the extension only wraps a search-engine query, so reliability is the engine's index; confirm each hit on the live page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-the-current-site |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
