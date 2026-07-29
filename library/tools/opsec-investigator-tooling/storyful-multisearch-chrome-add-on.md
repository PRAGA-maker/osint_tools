---
id: storyful-multisearch-chrome-add-on
name: Storyful Multisearch
description: Use when you have a keyword, `username`, or `name` and want to search many social platforms at once — opens the same query across Twitter/Instagram/Tumblr/Spokeo etc. in parallel tabs.
url: https://chrome.google.com/webstore/detail/storyful-multisearch/hkglibabhninbjmaccpajiakojeacnaf?hl=en
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: One-click parallel search of a term across multiple social networks and search engines.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source (MIT) Chrome extension by Storyful; source on GitHub. No account.
opsec: passive
opsecNote: It just opens normal search-result pages on each platform in separate tabs — the same queries you'd run by hand, so it's passive and doesn't contact any subject. Be aware you're hitting each platform from your own IP/browser session; run it in a sock-puppet browser profile if you don't want the searches tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Built and open-sourced by Storyful (a reputable journalism/verification agency); the code is public (MIT) and simply automates opening search URLs.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- whatsmyname
aliases:
- Storyful Multisearch
- multisearch
tags:
- social-media
- socmint
- search
- browser-extension
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Storyful Multisearch

> A Chrome extension that fires one search term across many social platforms at once — Twitter (posts/videos/images), Tumblr, Instagram, Spokeo, and more — each opening in its own tab.

## When to use
You have a keyword, `username`, `name`, or hashtag and want to sweep it across several platforms fast instead of typing the same query into each site. Storyful Multisearch (built for breaking-news journalists) opens the term simultaneously in separate tabs per platform, so an early-stage social sweep that would take many manual searches becomes one click. Great for the first broad pass on a subject or event.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Storyful Multisearch extension in Chrome (from the Web Store or build the MIT-licensed source).
2. Click the toolbar icon; tick which platforms to include (Twitter, Twitter images/videos, Tumblr, Instagram, Spokeo, Storyful feeds, etc.).
3. Type the term (`name`/`username`/hashtag) and search — each selected platform opens in its own tab (up to ~8).
4. Work through the tabs, capturing `social-profile` hits and media.
5. Note the gap (no native Facebook) and cover it separately.

## Inputs → Outputs
- **In:** keyword / `username` / `name` / hashtag
- **Out:** parallel search-result pages per platform → `social-profile` matches
- **Empty/negative result looks like:** thin or no results across tabs — the term may be too unique/misspelled, or the platforms restrict logged-out search; try variants and log into a sock-puppet where needed.

## Gotchas & OpSec
- **Automates opening searches, not deep enumeration** — it surfaces result pages; you still verify each profile is really your subject.
- No Facebook; some platforms limit results to logged-in users — pair with dedicated tools.
- OpSec: **passive**, but searches run from your session/IP — use a sock-puppet browser profile.

## Overlaps ("do both")
- Pairs with `[[whatsmyname]]` — Multisearch does broad *content/keyword* search across platforms; WhatsMyName does systematic *username enumeration* across hundreds of sites. Run Multisearch for the quick sweep, then WhatsMyName to nail down where a specific handle exists.

## Trust & verifiability
`trust: community` — open-source (MIT) and from a reputable verification agency; it only opens standard search URLs, so there's nothing opaque about what it does.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | storyful-multisearch-chrome-add-on |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
