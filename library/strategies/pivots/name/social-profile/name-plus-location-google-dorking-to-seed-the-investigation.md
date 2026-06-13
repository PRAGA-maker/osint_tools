---
id: name-plus-location-google-dorking-to-seed-the-investigation
name: Name + location Google dorking to seed the investigation
description: Use when First step for almost any subject, before reaching for specialized tools.
type: technique
summary: The most reliable opening move is targeted search-engine dorking on the subject's name combined with their city/region and disappearance-related terms. This surfaces news articles (which give additional photos for facial recognition, plus usernames, relatives, and employers), missing-persons posters, and social posts. A key refinement is to subtract the noise term 'missing' once you have located the person, so news clutter does not drown out their actual social presence, and to add discriminating terms like 'arrest', 'married', or a sports club to pull new identifiers.
missingPersonsRelevance: high
phase: intake
pivotFrom:
- name
- address
- geolocation
pivotTo:
- social-profile
- username
- associate
- employer-org
- image
platforms:
- facebook
- twitter
- tiktok
- youtube
- instagram
steps:
- Search the subject's first + last name plus their city.
- 'Add disappearance terms: inurl:missing "MP Name", intext:missing "MP Name".'
- Once the person is identified, subtract 'missing' to eliminate news clutter and reveal everyday social presence.
- Add discriminating terms (arrest, married, school, team name) to pull additional accounts and relatives.
- Run the same dorks through Bing and Yandex for results Google buries.
- Harvest every photo, username, relative name, and employer mentioned for later pivots.
signals:
- News articles yield multiple face photos and named relatives
- A username or handle appears that can be enumerated across platforms
pitfalls:
- Stopping at news results and never pivoting to the person's own social presence
- Only using Google and missing results that surface on Bing/Yandex
toolsUsed:
- Google
- Bing
- Yandex
- OSINTCurious Dorks page
tags:
- dorking
- search-engines
- intake
- seeding
evidence:
- type: writeup
  url: https://medium.com/@cyberbychase/osint-methodology-and-tradecraft-tips-for-winning-the-trace-labs-black-badge-from-team-federal-ebe737d70c6a
  note: 'Chase: inurl:/intext: missing dorks; subtract ''missing''; add arrest/married; use Bing and Yandex'
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: Opening move was a Google dork of the MP by name to find news + social, yielding photos and pivot points
trust: community
source: searchparty-writeups
---

# Name + location Google dorking to seed the investigation

> The most reliable opening move is targeted search-engine dorking on the subject's name combined with their city/region and disappearance-related terms. This surfaces news articles (which give additional photos for facial recognition, plus usernames, relatives, and employers), missing-persons posters, and social posts. A key refinement is to subtract the noise term 'missing' once you have located the person, so news clutter does not drown out their actual social presence, and to add discriminating terms like 'arrest', 'married', or a sports club to pull new identifiers.

**When to use:** First step for almost any subject, before reaching for specialized tools.

## Steps
- Search the subject's first + last name plus their city.
- Add disappearance terms: inurl:missing "MP Name", intext:missing "MP Name".
- Once the person is identified, subtract 'missing' to eliminate news clutter and reveal everyday social presence.
- Add discriminating terms (arrest, married, school, team name) to pull additional accounts and relatives.
- Run the same dorks through Bing and Yandex for results Google buries.
- Harvest every photo, username, relative name, and employer mentioned for later pivots.

## Signals it's working
- News articles yield multiple face photos and named relatives
- A username or handle appears that can be enumerated across platforms

## Pitfalls
- Stopping at news results and never pivoting to the person's own social presence
- Only using Google and missing results that surface on Bing/Yandex

**Tools:** Google, Bing, Yandex, OSINTCurious Dorks page

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
