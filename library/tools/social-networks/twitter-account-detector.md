---
id: twitter-account-detector
name: Twitter Account Detector
description: Use when you have a webpage/`domain` and want the Twitter/X accounts it references — a Chrome extension that surfaces all X handles linked on the page you're viewing.
url: https://chromewebstore.google.com/detail/twitter-account-detector/papcdbgfejihdinhieggiamjnkclhkck
category: social-networks
path:
- social-networks
bestFor: Quickly extracting every Twitter/X account linked from a website while browsing it.
selectorsIn:
- domain
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free Chrome extension; no account or payment.
opsec: passive
opsecNote: Passive to the accounts it finds — it only parses the page you already loaded and does not contact the handles. Standard extension caution applies (it can read page content); install from a research browser profile, not one tied to your identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: An unofficial open-source extension by developer Andrew Stilliard (stapps.io) with a public GitHub repo and ~4.7★ rating; small user base, code is auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Twitter account detector Chrome extension
tags:
- Social Media
- Twitter
- browser-extension
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Twitter Account Detector

> A lightweight Chrome extension that scans the page you're on and lists every Twitter/X account it links to — a fast way to harvest an organization's or site's associated handles.

## When to use
You're examining a website, company page, or link-heavy profile (`domain`) and want to pull all the Twitter/X handles referenced on it in one pass instead of hunting through the DOM. Handy for mapping an organization's staff/social presence, finding a subject's linked account from their personal site, or enumerating handles across a directory page. It's a convenience/collection aid, not a deep investigative engine.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Twitter account detector" from the Chrome Web Store into a research browser profile.
2. Navigate to the target website/page.
3. Activate the extension — it parses the current page and lists all Twitter/X accounts it finds.
4. Review the handles, then open each in X (from a sock-puppet session) to confirm relevance.
5. Pivot: each `username` feeds username-enumeration and profile-analysis tools to cross-map the person or org across platforms.

## Inputs → Outputs
- **In:** the current webpage (a `domain`/URL you're viewing)
- **Out:** the Twitter/X `username`s / `social-profile` links present on that page
- **Empty/negative result looks like:** no results means the page has no linked X handles in a form the extension recognizes — it won't discover accounts that aren't referenced on the page.

## Gotchas & OpSec
- **Only sees the current page:** it extracts what's linked there; it does not search or discover accounts beyond the page's own content.
- Browser-extension trust: it can read page content — install it in a segregated research profile, not one logged into your real accounts.
- Unofficial and small-scale; verify each handle actually belongs to the subject before drawing conclusions.

## Overlaps ("do both")
- Feeds username-enumeration tools (e.g. Sherlock/Maigret-style) — this collects the handles present on a site, and those expand each handle into a cross-platform footprint.

## Trust & verifiability
`trust: community` — an open-source, auditable extension from a named independent developer with a public repo; low risk but modest maintenance, so confirm it still functions after Chrome/X changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-account-detector |
| category | social-networks |
| selectorsIn → selectorsOut | domain → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
