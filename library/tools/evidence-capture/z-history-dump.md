---
id: z-history-dump
name: Z History Dump
description: Use when you have access to a Chrome browser profile (e.g. a seized/consented device) and want its full history as data — returns a downloadable JSON of visited URLs and timestamps.
url: https://chrome.google.com/webstore/detail/z-history-dump/ahpkicobhkchblogldpjchdhmdnblpkm/related
category: evidence-capture
path:
- evidence-capture
bestFor: Exporting a Chrome profile's browsing history to machine-readable JSON for timeline and link analysis.
selectorsIn: []
selectorsOut:
- domain
- social-profile
status: degraded
pricing: free
costNote: Free Chrome extension; no payment or account.
opsec: passive
opsecNote: Runs entirely locally in the browser and (per the developer) collects/transmits no data — the export never leaves the machine. The privacy concern is legal/consent, not network leakage: only run it on a device you are authorized to examine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Niche single-developer extension with a very small user base; the store listing may be delisted or Manifest-V2-retired, so verify it still installs before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Chrome history dump
tags:
- browser-history
- forensics
- downloaders
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Z History Dump

> A one-click Chrome extension that exports the browser's own history (URLs + visit timestamps) as a `history.json` file you can analyze offline.

## When to use
You have legitimate access to a Chrome profile — a consented device, a seized machine you're authorized to examine, your own sock-puppet browser — and you want its browsing history as structured data instead of scrolling `chrome://history/` by hand. The JSON export enables timeline reconstruction, frequency analysis, and mapping which sites and accounts the user visited within Chrome's ~90-day retention window.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Z History Dump" from the Chrome Web Store (verify the listing still exists; see trust note).
2. Open the extension on the profile you are authorized to examine.
3. Trigger the dump — it collects all available Chrome history via the history API and offers `history.json` for download.
4. Analyze offline: parse the JSON for visited `domain`s, `social-profile` URLs (linkedin.com/in/…, instagram.com/…), timestamps, and visit frequency.
5. Pivot: extracted profile URLs feed social-media OSINT; visited domains and their timing help build an activity timeline.

## Inputs → Outputs
- **In:** the local Chrome profile's history (no external selector)
- **Out:** JSON of visited `domain`s / `social-profile` URLs with visit timestamps
- **Empty/negative result looks like:** a near-empty JSON — the profile's history was cleared, or you're outside Chrome's retention window; it is not evidence the person never browsed.

## Gotchas & OpSec
- Human-in-the-loop: none technically, but this must be installed in the browser (`localInstall`, `browser-extension`).
- OpSec / legal: **passive** on the network — nothing is uploaded — but reading someone's browser history is legally sensitive. Only run it on a device you have authorization/consent to examine; document your authority.
- Scope limit: it only sees Chrome's local history within retention (~90 days) — not other browsers, not synced-then-deleted history, not incognito sessions.
- Availability is uncertain (small extension; possible Manifest V2 retirement) — confirm it installs before planning around it.

## Overlaps ("do both")
- Pairs with full forensic browser-history extractors — Z History Dump is a fast in-browser export, while a forensic tool reading the SQLite `History` database on disk recovers more (including some deleted rows) and is better for evidentiary work.

## Trust & verifiability
`trust: unverified` — a tiny single-dev extension; the raw history it emits comes straight from Chrome's API and is verifiable against `chrome://history/`, but treat the tool itself as convenience, not a forensic standard.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | z-history-dump |
