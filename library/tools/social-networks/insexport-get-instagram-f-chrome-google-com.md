---
id: insexport-get-instagram-f-chrome-google-com
name: insexport get instagram f (chrome.google.com)
description: Use when you have an Instagram `username` and want to export that account's followers/following list to CSV/Excel for network mapping — returns social-profile, associate.
url: https://chrome.google.com/webstore/detail/insexport-get-instagram-f/okmokimdgjhndamggnkdojhbofdmepno
category: social-networks
path:
- social-networks
bestFor: Exporting an Instagram account's followers/following to a spreadsheet for relationship analysis.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free Chrome extension (~20k users). No IG password requested; it works through your already-logged-in Instagram browser session.
opsec: active
opsecNote: It scrapes follower/following data via YOUR logged-in Instagram session, so the activity is tied to whatever IG account you're signed into and generates API-like traffic Instagram can rate-limit or flag. Use a dedicated sock-puppet Instagram account in a separate browser profile — never your real account — and respect its cooldown to avoid a ban.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Third-party extension ("Save My Day App"), ~20k users / 3.6★, clean store record — but it's an unaffiliated scraper with access to your IG session; treat with caution and isolate it from real accounts.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- InsExport
- Instagram follower export
tags:
- instagram
- Instagram Related Sites
- follower-export
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# insexport get instagram f (chrome.google.com)

> A Chrome extension that exports an Instagram account's followers/following to CSV/Excel — turning a target's social graph into an analysable list.

## When to use
You have an Instagram `username` (public, or one your sock-puppet can view) and want its full followers or following list as data — to map the subject's network, spot mutual connections (`associate`), or find a specific person in their orbit. Manual scrolling of thousands of followers is impractical; this bulk-exports up to ~50k entries with cooldown handling.

## How to use it (`bestInteractionPattern`: browser-extension)
1. In a **separate browser profile** logged into a **sock-puppet** Instagram account, install the InsExport extension from the Chrome Web Store.
2. Enter the target `username`, choose export type (followers or following), and start the export.
3. Let it run with its rate-limit/cooldown mode to avoid tripping Instagram's protections.
4. Download the CSV/Excel and analyse: sort/filter for known handles, cross-reference against the subject's following, look for close-tie accounts.
5. Pivot: exported handles feed username enumeration ([[maigret-2]]) and relationship mapping; a mutual connection may be the real lead.

## Inputs → Outputs
- **In:** Instagram `username`
- **Out:** `social-profile`/`associate` — a spreadsheet of the account's followers or following (handles, names where shown)
- **Empty/negative result looks like:** empty export, an error, or a cooldown/rate-limit stall — often because the account is private (your session can't see it), the export was throttled, or Instagram changed its internals.

## Gotchas & OpSec
- OpSec (active): runs through your logged-in IG session — Instagram can rate-limit or **ban** the account used. Only ever use a disposable sock-puppet account, isolated in its own browser profile.
- Human-in-the-loop: needs a logged-in Instagram session; respect the cooldown or the export fails/bans.
- Private accounts your session can't view won't export.
- Third-party extension with session access — install cautiously; scraping IG may breach its ToS.

## Overlaps ("do both")
- Pairs with [[maigret-2]] / username enumerators (carry exported handles across platforms) and with follower-analysis tools that find mutual connections between two exported lists.

## Trust & verifiability
`trust: unverified` — a popular but unaffiliated scraper with access to your IG session; the exported data is real, but isolate it from real accounts and confirm identities before acting on connections.
