---
id: google-and-bing
name: Google & Bing (Search Operators Guide)
description: Use when you have almost any selector and want to widen the net with search dorks — returns a curated reference of Google and Bing operators to build precise queries.
url: https://one-plus.github.io/GoogleBing
category: search-engines
path:
- search-engines
bestFor: A quick reference of Google and Bing search operators for building precise OSINT dork queries.
selectorsIn:
- name
- username
- email
- domain
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free static reference page (part of an open OSINT Toolkit on GitHub Pages); no account or payment. The searches you run are subject to Google/Bing's own terms.
opsec: passive
opsecNote: The reference page itself is inert. OpSec risk is in the searches you run — Google/Bing log your queries and IP; heavy dorking can trip CAPTCHAs or rate limits. Use a research browser profile and consider a VPN; the target is never contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained cheat-sheet page; the operators are standard and verifiable, but it is a third-party guide, not an official Google/Bing reference.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bookmarks
- document-search
- google-plus-and-linkedin
- instagram-reddit-and-snapchat
- osint-toolkit
- twitter-monitoring
- website-information
- youtube-periscope-twitch-and-dailymotion
aliases:
- Google and Bing dorks
- OSINT Toolkit Google/Bing
tags:
- search-operators
- dorking
- reference
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Google & Bing (Search Operators Guide)

> A curated cheat-sheet of Google and Bing search operators — the reference you reach for to turn a loose selector into a precise dork query.

## When to use
You have a `name`, `username`, `email`, or `domain` and generic searching is returning noise. This page lists the operators — exact-phrase `"..."`, `site:`, `intitle:`, `inurl:`, `filetype:`, `cache:`, and Bing-only tricks like `ip:` and `feed:` — that let you build targeted queries: find every page on one site that names a person, surface exposed documents, or map a domain's footprint. It's a methodology reference, not a data source itself; the value is in the queries it helps you construct.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://one-plus.github.io/GoogleBing and skim the Google and Bing operator sections.
2. Build a query around your selector, e.g. `"Jane A. Doe" (site:facebook.com OR site:linkedin.com)`, `filetype:pdf "Jane Doe" resume`, or Bing's `ip:203.0.113.5` to find co-hosted sites.
3. Run it in Google and Bing separately — their indexes and operators differ, so each surfaces things the other misses.
4. Iterate: narrow with `-` exclusions and `intitle:`/`inurl:`, or broaden by dropping quotes.
5. Pivot: results feed straight into profile/domain lookups; a discovered `domain` or `social-profile` becomes the next tool's input.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, or `domain`
- **Out:** targeted result sets pointing to `social-profile`s, documents, and related `domain`s
- **Empty/negative result looks like:** an over-narrow dork returns zero hits — loosen operators before concluding nothing exists; zero on one engine doesn't mean zero on the other.

## Gotchas & OpSec
- Human-in-the-loop: none to read the guide; aggressive dorking triggers Google/Bing CAPTCHAs — slow down or rotate.
- Run BOTH engines: Bing indexes and operators (e.g. `ip:`, `feed:`) catch things Google doesn't.
- The page is a static third-party guide; operators occasionally change on the engines' side, so test rather than assume.

## Overlaps ("do both")
- Pairs with the sibling toolkit pages `[[google-plus-and-linkedin]]`, `[[instagram-reddit-and-snapchat]]` and `[[document-search]]` — this covers the general operators, those apply them to specific platforms.

## Trust & verifiability
`trust: community` — a community cheat-sheet of standard, testable operators; the guide is a convenience, the authority is the search engines themselves.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-and-bing |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email, domain → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
