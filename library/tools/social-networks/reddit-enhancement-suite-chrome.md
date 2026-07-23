---
id: reddit-enhancement-suite-chrome
name: Reddit Enhancement Suite (Chrome)
description: Use when you are analyzing a Reddit `username` and want power-user tools — returns inline user tagging, account-age/karma visibility, and faster history/thread review.
url: https://chromewebstore.google.com/detail/reddit-enhancement-suite/kbmfpngjjgdllneeigpgjifpgocmfgmb
category: social-networks
path:
- social-networks
bestFor: Power-user Reddit browsing — tag users, keep notes, and review post/comment history efficiently.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source browser extension; no account beyond your (sock-puppet) Reddit login.
opsec: passive
opsecNote: "RES is a client-side UI layer over your normal Reddit browsing — it adds no extra requests to a target and stores your tags/notes locally, so it's passive. Any account interaction (voting, subscribing, expanding profiles) still happens under whatever Reddit account you're logged into; use a sock-puppet account, and remember RES has broad access to Reddit pages in your browser (install only the official version)."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Long-established, open-source, widely-used Reddit extension (honestpuck/RES community); it only enhances the Reddit UI and does not exfiltrate data — install the official Web Store build.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- RES
- Reddit Enhancement Suite
tags:
- reddit
- browser-enhancement
- chrome-extension
source: osintambition-social
lastVerified: '2026-07-23'
enrichment: full
---

# Reddit Enhancement Suite (Chrome)

> A power-user layer over Reddit: private per-user tags and notes, at-a-glance account age/karma, never-ending scroll, and quicker history review — the analyst's Reddit workbench.

## When to use
You're investigating a Reddit `username` — building a pattern of life from their posts/comments, tracking multiple accounts you suspect are linked, or reviewing a subreddit's participants. RES lets you **tag and annotate users** (e.g. "same writing style as X", "claims to live in Y"), see account age/karma inline, and browse long histories without constant page loads. A workflow aid, not a data source, so low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the official RES from the Chrome Web Store (link above) into a sock-puppet browser profile.
2. Log into Reddit with a sock-puppet account.
3. On any `username`, use the RES user-tag feature to add a colored tag/note — persistent across your sessions for tracking suspected links.
4. Use never-ending reddit + account details to scan a user's history quickly; hover to preview linked profiles/threads.
5. Export/record findings elsewhere (RES notes are local to your browser).

## Inputs → Outputs
- **In:** a Reddit `username`
- **Out:** an enhanced view of that `social-profile` (age/karma inline, your tags/notes, faster history) — RES surfaces existing data, it doesn't fetch new sources
- **Empty/negative result looks like:** n/a — RES only augments Reddit's own pages; a deleted/suspended account still shows nothing, RES just makes what's there easier to work.

## Gotchas & OpSec
- Your tags/notes live **only in the local browser profile** — back them up; they don't sync unless you configure RES account link.
- All interaction happens under your logged-in account — vote/subscribe carefully from a sock puppet to avoid tipping off a subject.
- Install only the official build; a broad-permission Reddit extension is a supply-chain risk if sourced from elsewhere.

## Overlaps ("do both")
- Complements Reddit-specific OSINT tools (comment/history exporters, account analyzers) — RES is your live browsing/annotation layer, while dedicated tools bulk-pull a user's data for offline analysis. Use both.

## Trust & verifiability
`trust: trusted` — a mature, open-source, widely-audited extension that only enhances the Reddit UI; it adds no data of its own, so verifiability rests on Reddit's underlying content, which you should still corroborate.
