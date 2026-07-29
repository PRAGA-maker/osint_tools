---
id: multifind
name: MultiFind
description: Use when you have a web page (or many tabs) and want to highlight multiple search terms — names, handles, keywords — across it at once; a browser extension for scanning long pages.
url: https://chromewebstore.google.com/detail/multifind/amegoafkcikfmdbfeldmchinkjfdgoog
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Highlighting several selectors (names/handles/keywords) simultaneously across a page or set of tabs.
selectorsIn:
- name
- username
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome extension; no account.
opsec: passive
opsecNote: Runs locally in your browser against pages you already loaded — it highlights text, it does not query any target. Standard extension caution applies: it can read page content, so install it in your investigation browser profile only and review its permissions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Built by Jake Creps, a well-known OSINT practitioner; a small, older (2020) but still-listed extension with a handful of users — reputable author, low install base.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MultiFind extension
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- browser-extension
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# MultiFind

> A multi-term highlighter for the browser — like Ctrl-F but for a whole list of names/handles/keywords at once, across a long page or many tabs.

## When to use
You're scanning a long document, forum thread, leak dump, or set of tabs and want to spot every occurrence of several selectors simultaneously — a list of a subject's known aliases, associates' names, addresses, or keywords. Native Ctrl-F only finds one term at a time; MultiFind highlights your whole watchlist together (text, links, and images), so nothing gets missed on a dense page.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install MultiFind from the Chrome Web Store into your investigation browser profile.
2. Open the target page(s) and launch the extension.
3. Enter (or bulk-import) your list of terms — aliases, associate names, keywords.
4. It highlights every match across the page/tabs; scan the highlights to find where selectors co-occur.
5. Pivot: a page where several of your terms cluster is a strong lead — extract the surrounding context for the next tool.

## Inputs → Outputs
- **In:** a list of terms built from `name`/`username`/keywords, plus loaded page(s)
- **Out:** in-page highlights of every match (a reading aid, not a data selector)
- **Empty/negative result looks like:** no highlights — none of your terms appear on the loaded page(s); it does not search the web, only what's already open.

## Gotchas & OpSec
- It highlights only content **already loaded** in the browser — it's a reading aid, not a search engine; pair it with an actual search to find the pages first.
- Older extension (2020) with few users; verify it still installs and review its page-read permission before trusting it on sensitive tabs.
- **Passive**: local highlighting only, no queries leave your browser.

## Overlaps ("do both")
- Pairs with `[[googler]]`/site search to *find* candidate pages, then MultiFind to rapidly scan each for your watchlist of selectors.

## Trust & verifiability
`trust: community` — from a respected OSINT author but small and unmaintained since 2020; functionally simple (highlighting), so low risk, but confirm current availability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | multifind |
