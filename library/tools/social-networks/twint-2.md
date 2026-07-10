---
id: twint-2
name: Twint
description: Use when an old workflow references Twint for Twitter scraping — returns little now; it's archived and broken since the X API changes, so use a current method.
url: https://pypi.org/project/twint/
category: social-networks
path:
- social-networks
bestFor: Historical reference only — a Python library that once scraped tweets/profiles without the API; now defunct.
selectorsIn:
- username
selectorsOut:
- social-profile
- metadata-exif
status: down
pricing: free
costNote: Free and open-source, but archived (Mar 2023) and broken against the current X platform.
opsec: passive
opsecNote: When it worked, it scraped Twitter's front-end without your account (passive). It is not a live concern now — don't build workflows on it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: unverified
trustNote: The twintproject repo was archived on 30 Mar 2023 and last released in 2019; Twitter/X anti-scraping and API changes broke it. Treat this as a redirect, not a working tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- getdaytrends
aliases:
- twintproject/twint
- twint
tags:
- twitter
- scraping
- deprecated
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Twint

> An archived Python tweet-scraper — retained only so an agent recognises it's dead (broken since the 2023 X API/anti-scraping changes) and moves to a current approach.

## When to use
You find Twint cited in an older OSINT playbook for pulling a user's tweets, followers or search results without the Twitter API. It no longer works: the project was archived in March 2023, its last release was 2019, and X's platform changes broke front-end scraping. Use this entry to confirm the dead end.

## How to use it (`bestInteractionPattern`: python-lib)
1. Recognise Twint is deprecated — don't invest in patching it.
2. For current Twitter/X data, use the official X API within its terms, a maintained scraper that tracks X's current front-end, or archive sources (Wayback, archived tweet sites) for historical content.
3. For trend/context lookups that don't need a live scraper, see `[[getdaytrends]]`.
4. Pivot: once you have tweets/profile data from a working source, mine them for locations, associates and timelines as usual.

## Inputs → Outputs
- **In:** `username` (historically also search terms)
- **Out:** intended tweets/`social-profile`/`metadata-exif` — but **none reliably**, as the tool is broken
- **Empty/negative result looks like:** import/HTTP errors or empty output; that's the expected state, not a transient failure.

## Gotchas & OpSec
- **Archived and broken** — any tutorial using it is out of date.
- Front-end scraping of X is a moving target and often against ToS; use current, compliant methods.
- OpSec: moot — there's nothing live to run.

## Overlaps ("do both")
- For the context it used to provide, `[[getdaytrends]]` still gives trend data; for content, use a maintained X-data method.

## Trust & verifiability
`trust: unverified` — deprecated, read-only project; nothing it returns can be relied upon. Get Twitter/X data from a live source instead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twint-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
</content>
