---
id: tweetvacuum
name: TweetVacuum
description: Use when you have a Twitter/X `username` and want to export that account's full timeline past the 3,200-tweet API cap — returns the scraped tweets saved locally (archived/deprecated tool).
url: https://github.com/UberKitten/TweetVacuum
category: social-networks
path:
- social-networks
- twitter
- archive-deleted-tweets
bestFor: Bulk-exporting a user's entire visible tweet history beyond the 3,200-tweet limit via a browser extension.
selectorsIn:
- username
selectorsOut:
- social-profile
status: down
pricing: free
costNote: Free and open-source Chrome extension. No fees; you supply a logged-in Twitter/X browser session.
opsec: active
opsecNote: It scrapes the timeline from YOUR logged-in browser session, opening many pages rapidly — that pattern is tied to the account/IP you use and can trip anti-abuse controls. Use a sock-puppet Twitter/X account, never your real one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A community Chrome extension, archived (read-only) on GitHub since September 2023. It scraped the old Twitter web UI; X's redesign and API changes make current functionality unreliable.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
deprecated: true
relatedTools: []
aliases:
- Tweet Vacuum
tags:
- twitter
- archive
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# TweetVacuum

> A browser extension that scraped a user's *entire* visible timeline by paging through the web UI — a workaround for the 3,200-tweet API cap, now archived and likely broken on modern X.

## When to use
You have a Twitter/X `username` and want their full timeline exported locally, deeper than the ~3,200 tweets the API exposes — for building a complete activity/timeline record. **Caveat:** the project was archived in September 2023 and predates X's redesign, so treat it as a last resort and verify it still works before relying on it; prefer a maintained alternative if one exists.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the unpacked extension from the GitHub repo (clone → Chrome → Developer Mode → Load unpacked), logged into a **sock-puppet** Twitter/X account.
2. Enter the target `username` in the extension popup.
3. It opens a window and pages through the timeline, saving tweets to a local database (Dexie.js) and restarting tabs when performance degrades (~every 1000 tweets).
4. Export/inspect the locally stored tweets when it finishes.
5. Pivot: the archived timeline feeds activity analysis in `[[tinfoleak-web]]` and cross-checks against `[[twitter-search]]`.

## Inputs → Outputs
- **In:** Twitter/X `username` (+ your sock-puppet logged-in session)
- **Out:** locally saved tweets for that `social-profile` (bulk timeline export)
- **Empty/negative result looks like:** it stalls, captures nothing, or errors — expected given the archived code no longer matches X's current UI. An empty run is almost certainly tooling breakage, not an empty timeline.

## Gotchas & OpSec
- Deprecated: `status: down` / archived since 2023 and built for the old Twitter UI — assume broken on current X until proven otherwise.
- Detectable scraping: rapid page-through from your session can trigger rate limits/locks; use a throwaway account.
- Local-only: data stays in your browser's local DB — export it before uninstalling.

## Overlaps ("do both")
- Pairs with `[[twitter-search]]` and `[[tinfoleak-web]]` — those work against the live platform, while TweetVacuum's niche was bulk history export; if it fails, fall back to a maintained scraper or native search.

## Trust & verifiability
`trust: unverified` — an unmaintained, archived community extension tied to the retired Twitter web UI; verify it functions at all before trusting any export.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tweetvacuum |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes |
