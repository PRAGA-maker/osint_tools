---
id: searchpof-com
name: SearchPOF.com
description: Use when you have a `username`/`name` and want to find a Plenty of Fish (POF) dating profile — provides Google-CSE site searches and guidance to surface public POF profiles.
url: https://searchpof.com/
category: username
path:
- username
bestFor: Locating public Plenty of Fish dating profiles via Google site-search techniques.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free informational tool built on Google Custom Search; not affiliated with POF. No account or payment.
opsec: passive
opsecNote: You search Google's index of POF, not POF's logged-in interface, so no visit is registered against your account and the subject is not alerted. Do not log into POF to view a profile from a real account; use a sock puppet if you must open the dating site itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party helper (not affiliated with POF/Plentyoffish) that wraps Google Custom Search; POF's own scraping/search has been restricted over time, so it is now largely a guided-search resource.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SearchPOF
- POF profile search
tags:
- dating
- plentyoffish
- pof
- google-cse
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# SearchPOF.com

> A Plenty of Fish profile-finder that leans on Google site-search — useful for surfacing public POF profiles without logging into the dating app.

## When to use
You suspect a subject has (or had) a Plenty of Fish dating profile and you have a `username`, `name`, or city to search on. Dating profiles are high-value in missing-person and identity work — they carry photos, self-description, location and interests. SearchPOF helps you find them from outside the app, using Google's index rather than POF's own (increasingly restricted) search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://searchpof.com/.
2. Use the guided Google site-search: query `"<username or name>" site:pof.com`, or `"<City Name>" site:pof.com` to browse an area.
3. Follow the site's guidance on POF's built-in Basic/Advanced search, "My Matches" and "My City" if you also work inside the app (via a sock puppet).
4. Open candidate results — a public POF profile shows the handle, photos, and self-description; confirm it is your subject by photo/detail.
5. Pivot: a profile photo feeds `[[reverse-image-search]]`; the handle feeds `[[user-searcher]]`/`[[usersearch-org]]`; stated location/interests feed geolocation and the associate graph.

## Inputs → Outputs
- **In:** `username` / `name` (+ optional city)
- **Out:** links to public POF `social-profile`s (via Google), with photos and self-description on the profile page
- **Empty/negative result looks like:** no indexed POF pages for the query — the profile may be private, deleted, un-indexed by Google, or the person isn't on POF. Absence is weak evidence.

## Gotchas & OpSec
- It is now mostly a **search-technique helper**, not a live scraper — direct POF profile scraping has been curtailed, so results depend on what Google has indexed.
- Not affiliated with POF; treat it as a convenience wrapper around Google dorks you could run yourself.
- OpSec: **passive** via Google; do not view profiles from a real POF login — use a sock puppet inside the app.

## Overlaps ("do both")
- Pairs with direct Google dorking (`site:pof.com`), `[[usersearch-org]]` (which covers dating sites), and `[[reverse-image-search]]` — combine index-search, cross-site username search, and photo matching to confirm a dating identity.

## Trust & verifiability
`trust: community` — an unaffiliated helper wrapping Google Custom Search; reliability tracks Google's index. Verify any profile by photo/detail, not by the handle alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchpof-com |
| category | username |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
