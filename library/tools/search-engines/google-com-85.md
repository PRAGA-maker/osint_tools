---
id: google-com-85
name: google.com
description: Use when you have a `name` or `username` and want to surface video footage of or uploaded by a subject — returns `social-profile` (channels) and `name` leads.
url: https://www.google.com/advanced_video_search
category: search-engines
path:
- search-engines
bestFor: Filtering a web-wide video search by exact phrase, site, duration, and post date to find footage of a person.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free Google service; no account or payment required to build or run the query.
opsec: passive
opsecNote: Queries hit Google's infrastructure, not the target, so the subject is not alerted. Results are personalised to your Google session/IP and logged by Google — use a clean/sock-puppet browser and consider signing out to reduce filter-bubble skew.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google search surface; the video index itself is authoritative, though coverage depends on what platforms let Google crawl.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google Advanced Video Search
- advanced_video_search
tags:
- searchengines
- Search Engines
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# google.com

> Google's Advanced Video Search form — the same web-wide video index behind the main search box, but with structured filters for phrase, site, language, duration, and post date.

## When to use
You have a `name` or `username` and want to find video of the subject — a news clip, a livestream, an uploaded phone video, a tagged appearance — without wading through unrelated hits. The advanced form lets you pin an exact phrase, restrict to a single site (e.g. `youtube.com`, a local news domain), and bound the upload window, which is what turns "too many results" into "the clip that shows where they were."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.google.com/advanced_video_search in a clean/sock-puppet browser.
2. Fill the fields: put the subject's exact name in **"this exact word or phrase"**, add distinguishing terms (city, employer, event) in **"all these words"**, and use **"none of these words"** to drop a common namesake.
3. Narrow with the refinement rows: **site or domain** (restrict to YouTube or a regional outlet), **duration**, **last update** (past hour → past year — useful when a person went missing on a known date), and **language**.
4. Run the search and scan results — each hit is a video plus its hosting page.
5. Pivot: an uploader's channel is a `social-profile`; the on-screen or description text often yields a `name`, location, or associate to feed the next lookup.

## Inputs → Outputs
- **In:** `name`, `username` (plus optional location/event keywords)
- **Out:** video results linking to `social-profile` channels and corroborating `name` leads
- **Empty/negative result looks like:** zero or only namesake/unrelated videos — means the subject isn't in Google's video index for those terms, not that no footage exists (private/unindexed platforms won't appear).

## Gotchas & OpSec
- OpSec: **passive** — the target is never contacted; only Google sees the query. Sign out or use a sock account so results aren't skewed by your own history.
- Sustained automated querying can trigger a Google CAPTCHA; solve it manually and slow down.
- Coverage is only as good as what each platform lets Google crawl — restricted or login-walled video (private Facebook, Instagram) is invisible here.

## Overlaps ("do both")
- Pairs with `[[here-8]]` and `[[google-com-3]]` — those are prebuilt Google site-search dorks for social platforms, while this targets the video index specifically; run all three to cover text profiles and footage.

## Trust & verifiability
`trust: trusted` — it is Google's own search surface, so the index is authoritative; the only quality caveat is crawl coverage, not data fabrication.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-85 |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
