---
id: here-8
name: Here
description: Use when you have a `name` plus an approximate location and want to surface public Facebook profiles/posts via a Google site-search dork — returns `social-profile` links and `name` corroboration.
url: https://www.google.com/search?client=firefox-b-d&q=site%3Afacebook.com+%22Search+Name%22+%22Search+Location%22
category: social-networks
path:
- social-networks
bestFor: Google-dorking Facebook for a named person tied to a specific place, without logging into Facebook.
selectorsIn:
- name
- geolocation
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Uses only Google search; free, no account or payment.
opsec: passive
opsecNote: The query hits Google, not Facebook, so the subject is not notified and you never touch Facebook while logged in. Run it signed out / in a sock browser so results aren't tied to your identity or filter bubble.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Not a third-party tool — it is a Google `site:` dork template; reliability equals Google's index of publicly crawlable Facebook pages.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Facebook site search dork
- 'site:facebook.com name location'
tags:
- facebook
- Facebook General Links
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Here

> A fill-in-the-blanks Google dork — `site:facebook.com "Name" "Location"` — that pulls public Facebook profiles and posts out of Google's index without you ever logging into Facebook.

## When to use
You have a `name` and an approximate `geolocation` (city, town, employer, school) and want to find the subject's Facebook footprint. Facebook's own search is hostile to logged-out users and biased toward your friend graph; going through Google's index sidesteps both and only surfaces content Facebook has allowed to be publicly crawled.

## How to use it (`bestInteractionPattern`: web-manual)
1. Take the template URL and replace `Search Name` with the subject's name (keep the quotes to force an exact match) and `Search Location` with a city, workplace, or school.
2. Paste the edited query into Google (or just edit the two quoted strings in the address bar).
3. Read results — each hit is a publicly indexed Facebook page: a profile, a post, a photo caption, or a group thread.
4. Loosen or tighten: drop the location quotes if you get nothing; swap the location term (try employer instead of city) to catch people who don't list a hometown.
5. Pivot: open a promising `social-profile`, and harvest a confirmed `name`, friends (`associate`), and place tags for the next step.

## Inputs → Outputs
- **In:** `name` + `geolocation` (both as quoted exact strings)
- **Out:** links to public Facebook `social-profile`s and posts; corroborating `name`/location text
- **Empty/negative result looks like:** no results, or only unrelated namesakes — means nothing matching is publicly indexed (the person may have a locked-down profile that Google can't see), not that they aren't on Facebook.

## Gotchas & OpSec
- OpSec: **passive** — you query Google, never Facebook; the subject gets no notification. Stay logged out of Facebook so a stray click can't tie the visit to you.
- Only publicly crawlable Facebook content appears; private/friends-only profiles are invisible. A null result is not proof of absence.
- Heavy dorking can trip a Google CAPTCHA; solve it and slow down.

## Overlaps ("do both")
- Pairs with `[[google-com-3]]` (same technique aimed at other networks) and `[[google-com-85]]` (Google video search) — run them together to cover profiles, regional networks, and footage.

## Trust & verifiability
`trust: trusted` — there is no intermediary service to distrust; results come straight from Google's index of public Facebook pages. Verify each profile is the right person before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | here-8 |
| category | social-networks |
| selectorsIn → selectorsOut | name, geolocation → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
