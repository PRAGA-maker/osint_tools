---
id: youfilter-youtube-advanced-search-filter
name: YouFilter – YouTube Advanced Search Filter
description: Use when you have a YouTube search or channel and want structured results — returns social-profile and username leads (channel owners, contacts, stats) exportable to CSV.
url: https://chrome.google.com/webstore/detail/youfilter-–-youtube-advan/lnlanlnejphdbhplbgokklmgfbjphigi
category: social-networks
path:
- social-networks
bestFor: Turning YouTube search results into a sortable table of videos, channels, stats, and owner-contact links, exportable to CSV.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free Chrome extension; install from the Chrome Web Store, no payment required.
opsec: passive
opsecNote: The extension reformats YouTube search results you're already viewing — it doesn't message creators, so it's passive toward targets. It runs in your browser with access to page data, so install into a dedicated research browser profile and vet the extension's permissions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A third-party Chrome extension (source cyb-detective); useful but not officially vetted — review its permissions before installing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- YouFilter
- YT YouFilter
tags:
- Social Media
- YouTube
- browser-extension
source: cyb-detective
lastVerified: '2026-07-20'
enrichment: full
---

# YouFilter – YouTube Advanced Search Filter

> A Chrome extension that rebuilds YouTube search results as a sortable, exportable table — surfacing per-video stats and quick links to channel owners' contacts.

## When to use
You're working a YouTube angle — enumerating a subject's channels, mapping who covers a topic, or pulling a creator's contact/social links — and the native YouTube UI is too shallow to compare or export. YouFilter tabulates results (views, likes, subscriber counts, publish dates, keywords) and links to channel-owner contacts, then exports to CSV for offline analysis, making YouTube search results into structured data you can pivot on.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store (link above) into a research browser profile.
2. Run a normal YouTube search (by `name`, `username`/handle, or topic).
3. YouFilter overlays a table of results; sort/filter by channel, subscribers, date, or keywords.
4. Read the channel column for owner/contact links (`social-profile`) and note handles (`username`).
5. Export to CSV, then pivot: channel handles feed cross-platform username searches; contact emails feed email-OSINT.

## Inputs → Outputs
- **In:** a YouTube search — a `name`, `username`/handle, or topic
- **Out:** `social-profile` (channels + owner-contact links), `username` (handles), plus per-video stats, as CSV
- **Empty/negative result looks like:** a search with no relevant channels, or an extension that fails to inject on a changed YouTube layout — refresh or re-check the extension is enabled.

## Gotchas & OpSec
- Browser-extension trust: it can read page content; install only into a locked-down research profile and review permissions.
- YouTube UI changes can break overlay extensions — verify the table still populates.
- OpSec: passive toward targets (no outreach), but the extension itself is a local supply-chain consideration.

## Overlaps ("do both")
- Pair with dedicated username-enumeration and YouTube metadata tools: YouFilter structures and exports the search surface, those deep-dive an individual channel/handle.

## Trust & verifiability
`trust: unverified` — a third-party extension not officially audited; its stats mirror YouTube, but treat owner-contact links as leads and vet the extension before installing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youfilter-youtube-advanced-search-filter |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
