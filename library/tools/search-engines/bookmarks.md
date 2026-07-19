---
id: bookmarks
name: OSINT Toolkit Bookmarklets
description: Use when you're on a target's web page and want in-browser OSINT actions — a drag-to-toolbar bookmarklet set that runs Facebook/Twitter searches, link/email extraction, and image tools.
url: https://one-plus.github.io/Bookmarks
category: search-engines
path:
- search-engines
bestFor: A collection of 30+ OSINT bookmarklets you drag to your bookmarks bar to run searches and extraction directly on the current page.
selectorsIn:
- username
- image
selectorsOut:
- email
- social-profile
status: live
pricing: free
costNote: Free static GitHub Pages page; no account. It's a set of client-side bookmarklets — nothing to install beyond dragging links to your bookmarks toolbar.
opsec: passive
opsecNote: Bookmarklets run locally in your browser against the page you're viewing; some (e.g. Facebook actions) require you to be logged in, which is attributable — use a sock-puppet browser profile for logged-in ones. Read a bookmarklet's code before trusting it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A community-shared bookmarklet collection on GitHub Pages (one-plus). Each bookmarklet is small client-side JS; verify individual snippets before use.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- document-search
- google-and-bing
- google-plus-and-linkedin
- instagram-reddit-and-snapchat
- osint-toolkit
- twitter-monitoring
- website-information
- youtube-periscope-twitch-and-dailymotion
aliases:
- OSINT bookmarklets
tags:
- bookmarklets
- browser-tools
- osint4all
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# OSINT Toolkit Bookmarklets

> A drag-to-your-toolbar collection of ~30 OSINT bookmarklets that run searches and data-extraction directly on whatever page you're viewing — no login to a central toolkit needed.

## When to use
You're actively looking at a target's profile, post, or website and want to act on it in place: extract every link or email on the page, expand Facebook comments, pull a profile ID, run a Twitter/cluster search, grab images, check Google Cache or the Wayback Machine, or run a word-frequency pass. Reach for it when the fastest move is a one-click action on the current page rather than copying selectors into separate tools.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Open https://one-plus.github.io/Bookmarks in your (sock-puppet) research browser profile.
2. Drag the bookmarklets you want up onto your bookmarks toolbar — each has a short description and any usage notes (e.g. "requires being logged into Facebook").
3. Navigate to the target page (profile, post, website).
4. Click the relevant bookmarklet — it executes JS against the current page and returns results inline or opens a search (e.g. all emails found, extracted links, a pre-built Twitter search).
5. Pivot: feed extracted `email`/link/`social-profile` output into the matching category tool (email lookups, domain tools, etc.).

## Inputs → Outputs
- **In:** the current web page + selectors visible on it (`username`, `image`, on-page links)
- **Out:** extracted `email` addresses, links, `social-profile` IDs, image/archive lookups
- **Empty/negative result looks like:** a bookmarklet returns nothing (no emails/links found on the page, or a site changed its markup so the snippet no longer matches). Not proof the data doesn't exist elsewhere.

## Gotchas & OpSec
- Bookmarklets are brittle: they target specific site layouts and break when Facebook/Twitter change their DOM — expect some to be stale.
- Some require you to be logged into the platform, which is attributable — use a sock-puppet profile.
- Security: bookmarklets execute arbitrary JS in your session; read the code and only keep ones you trust.
- OpSec: passive for extraction; logged-in actions carry your (puppet) identity.

## Overlaps ("do both")
- Sits alongside `[[osint-toolkit]]` and the themed link sets (`[[google-and-bing]]`, `[[website-information]]`) — the bookmarklets are the in-page action layer; those are the destination-search layer.

## Trust & verifiability
`trust: community` — an individual's shared GitHub Pages collection. There's no vendor guarantee; each bookmarklet is inspectable client-side JS, so verify snippets and confirm their output against the actual page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bookmarks |
| category | search-engines |
| selectorsIn → selectorsOut | username, image → email, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
