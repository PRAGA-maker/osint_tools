---
id: search-craigslist
name: Search craigslist
description: Use when you have a keyword, `name`, `phone` or item and want to search Craigslist classified ads across every US city at once — returns matching listings that can leak `phone`, location and contact details.
url: http://searchcraigslist.org/
category: search-engines
path:
- search-engines
bestFor: Nationwide keyword search of Craigslist classified ads (Craigslist's own search is one-city-at-a-time).
selectorsIn:
- name
- phone
selectorsOut:
- phone
- address
status: live
pricing: free
costNote: Free to use; ad-supported, no account or payment required.
opsec: passive
opsecNote: You search a third-party aggregator, not the poster's account; posters are not notified of searches. Do NOT reply to a listing from your real identity — replying emails the poster and reveals you. Use a sock puppet if you must make contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent third-party aggregator over Craigslist's public postings; freshness lags Craigslist by minutes-to-hours and coverage is best-effort, not exhaustive.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- searchcraigslist.org
- Craigslist nationwide search
tags:
- classifieds
- craigslist
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Search craigslist

> A nationwide search box for Craigslist — one keyword query hits every US city at once, instead of Craigslist's own one-city-at-a-time search.

## When to use
You want to search Craigslist classified ads across the whole country in one go — for a subject's name, phone number, a distinctive item they're known to buy/sell (a vehicle, gear), or a business alias. Craigslist ads frequently leak a poster's phone number, first name, neighborhood, and the goods they're moving, so a nationwide sweep can place a subject in a region or surface a contact number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://searchcraigslist.org/.
2. Enter your keyword(s) — a name, phone number, or item description. You can require multiple terms and exclude terms with a minus sign (e.g. `bmw -blue`).
3. Submit; the tool returns a consolidated list of matching Craigslist posts nationwide with direct links.
4. Open the individual posts and read them for leaked details: phone number, poster's first name, neighborhood/city, and photos (which may carry EXIF or background clues).
5. Pivot: a phone number found in a listing feeds phone-OSINT; a city/neighborhood narrows geolocation; a recurring seller handle can be cross-referenced across cities.

## Inputs → Outputs
- **In:** `name`, `phone`, or item keyword
- **Out:** matching classified listings that may reveal `phone`, an approximate `address`/city, and item/contact details
- **Empty/negative result looks like:** "no results" — the term isn't in any current Craigslist post (ads expire, so this is a snapshot), or the region uses a different platform. Absence is not evidence the person isn't active.

## Gotchas & OpSec
- Craigslist posts expire and are frequently deleted, so this is a *live snapshot*, not an archive — a negative result today doesn't mean nothing existed last month.
- Coverage skews heavily US; other countries have thin or no Craigslist presence.
- OpSec: **passive to search, active to contact.** Searching is invisible, but *replying* to a listing sends the poster an email that reveals you — never do that from your real identity.

## Overlaps ("do both")
- Pairs with dedicated phone-OSINT and reverse-image tools — this surfaces the listing; those enrich the phone number and photos the listing leaks.

## Trust & verifiability
`trust: community` — a third-party aggregator, not Craigslist itself. Treat every hit as a lead to verify against the live Craigslist post (follow the link) before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-craigslist |
| category | search-engines |
| selectorsIn → selectorsOut | name, phone → phone, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
