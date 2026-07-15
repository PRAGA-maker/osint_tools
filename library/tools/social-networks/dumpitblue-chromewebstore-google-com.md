---
id: dumpitblue-chromewebstore-google-com
name: DumpItBlue+ (Chrome extension)
description: Use when you are logged into Facebook viewing a `social-profile`/page and want to capture everything on screen — posts, comments, friends — for offline analysis; returns social-profile, name, and associate data.
url: https://chromewebstore.google.com/detail/dumpitblue+/igmgknoioooacbcpcfgjigbaajpelbfe
category: social-networks
path:
- social-networks
bestFor: Bulk-capturing a Facebook profile/page's visible content (auto-scroll, expand, strip clutter) into a saveable dump for evidence and analysis.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
- name
- associate
status: live
pricing: free
costNote: Free Chrome extension (le.tools.com). Complements the separate DumpItBlue web tool for parsing the captured page. No account with the extension itself.
opsec: active
opsecNote: It captures whatever the LOGGED-IN Facebook account can see, so you must be signed into Facebook — do that only from a sock-puppet account on a clean browser/IP. Auto-scrolling a target's profile generates real views/requests from your account; never use a real or attributable identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: Established research extension (10k+ users, v3.2.1 in 2025) by le.tools.com, listed under Facebook Account Research on uk-osint. It only reads what's on screen — no scraping of hidden data — so risk is your own OpSec, not the tool's integrity.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- facebook
- graph-tips
aliases:
- DumpItBlue
- dumpitblue+
tags:
- facebookaccountresearch
- Facebook Account Research
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# DumpItBlue+ (Chrome extension)

> A Facebook-research helper that auto-scrolls, expands and strips a profile/page so you can capture its full visible content in one pass — turning a live, infinite-scroll page into a fixed artifact for analysis.

## When to use
You're examining a Facebook `social-profile` or page and need to preserve everything it shows — posts, comment threads, friend/like lists — before it changes or you lose access. It expands truncated comments and removes chrome so the page is fully rendered and saveable, which is ideal for evidence capture and for feeding the content into the companion DumpItBlue parser.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install DumpItBlue+ from the Chrome Web Store (link above).
2. Log into Facebook with a **sock-puppet** account in a clean browser profile.
3. Navigate to the target profile/page/section.
4. Use the extension's controls to auto-scroll, expand comments, and isolate the scrollable area so all content loads.
5. Save the page (or run it through the DumpItBlue web tool) and extract names, associates and post history.
6. Pivot: friend/tag `associate`s feed network mapping; post content yields locations, dates and other selectors.

## Inputs → Outputs
- **In:** `social-profile` / `username` (a Facebook page you can see while logged in)
- **Out:** `social-profile`, `name`, `associate` (friends/taggers/commenters) — everything visible on the page
- **Empty/negative result looks like:** a page that stays sparse because Facebook is hiding content from your account — a friends list set to private, or a limited-visibility profile; the tool can't reveal what your account can't see.

## Gotchas & OpSec
- Human-in-the-loop: requires a logged-in Facebook session — use a throwaway account, never your own.
- It captures the **rendered view only**; it does not defeat privacy settings or pull hidden friends.
- Facebook's layout changes can break the auto-scroll/expand controls between versions.

## Overlaps ("do both")
- Pairs with Facebook Graph-search tricks (e.g. `[[graph-tips]]`) — those find the profiles/relationships, this preserves the page once you're on it.
- Combine with a screenshot/forensic-capture tool for a timestamped evidential copy alongside the data dump.

## Trust & verifiability
`trust: community` — a widely-used research extension that only reads on-screen content; the trust question is your own OpSec discipline, not the extension's behaviour.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dumpitblue-chromewebstore-google-com |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → social-profile, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
