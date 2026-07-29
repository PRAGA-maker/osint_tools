---
id: dumpitblue-plus
name: DumpItBlue+
description: Use when you have a Facebook `social-profile`/page open and want to capture it for offline analysis — returns a fully-expanded, saveable copy of the page's content.
url: https://chrome.google.com/webstore/detail/dumpitblue%2B/igmgknoioooacbcpcfgjigbaajpelbfe/
category: evidence-capture
path:
- evidence-capture
bestFor: Expanding and preserving Facebook pages/profiles/threads for offline review and evidence.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free Chrome extension by Le-tools (complements the DumpItBlue bookmarklet); no account.
opsec: passive
opsecNote: It manipulates the CACHED copy of the Facebook page already loaded in your browser (scroll/expand/isolate) — it doesn't post, like, or message, so it doesn't alert the target. But you must be viewing the page from some account; use a sock-puppet Facebook login, never your real one, and capture from a clean profile.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: A long-standing, actively-updated OSINT capture extension from Le-tools, widely listed in investigator toolkits; it modifies only your local page copy.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- hunchly
aliases:
- DumpItBlue+
- DumpItBlue
tags:
- evidence-capture
- facebook
- socmint
- browser-extension
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# DumpItBlue+

> A Chrome extension that expands and cleans a Facebook page in your browser so you can preserve the whole thing — long threads, hidden comments, media — for offline analysis or evidence.

## When to use
You're viewing a target's Facebook `social-profile`, page, group, or a long comment thread and need to **capture it before it changes or disappears**. Facebook lazy-loads and collapses content, so a naive save misses most of it. DumpItBlue+ auto-scrolls, expands comments/replies, removes clutter, and isolates the scrollable content so you can save or print a complete copy — turning a live, volatile page into a fixed record.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install DumpItBlue+ from the Chrome Web Store (pairs with the DumpItBlue bookmarklet from le-tools.com).
2. Log into a **sock-puppet** Facebook account and navigate to the target profile/page/thread.
3. Run the extension's functions: scroll-to-load, expand comments/replies, remove/isolate elements.
4. Save the resulting cached page (print-to-PDF / full-page capture) with the URL and timestamp for provenance.
5. Pivot: harvested `image`s go to reverse-image/face tools; named commenters/associates become new leads.

## Inputs → Outputs
- **In:** an open Facebook `social-profile`/page/thread
- **Out:** a fully-expanded, saveable copy of the content (`social-profile` data, `image`s, comments)
- **Empty/negative result looks like:** the page won't fully expand — Facebook layout changes or gating (login-walled/private content) can limit it; capture what's visible and note the gaps.

## Gotchas & OpSec
- **Use a sock-puppet login** — you must be signed into Facebook to view most content; never your real account.
- It edits only your local cached copy (no page modification server-side), so it's non-alerting — but preserve provenance (URL, time, hash) for evidentiary use.
- Facebook's frequent UI changes can break expansion; verify completeness before relying on a dump.

## Overlaps ("do both")
- Pairs with `[[hunchly]]` — Hunchly automatically preserves every page you visit with an audit trail; DumpItBlue+ specifically forces Facebook to *reveal* all its lazy-loaded content first. Use DumpItBlue+ to expand, Hunchly (or a full-page capture) to preserve.

## Trust & verifiability
`trust: community` — a reputable, maintained investigator tool that only manipulates your local copy; the captured content is verifiable against the live page while it exists.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dumpitblue-plus |
| category | evidence-capture |
| selectorsIn → selectorsOut | social-profile → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (account-login) |
