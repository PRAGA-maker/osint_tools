---
id: open-on-the-name-with-google-dorking-to-seed-every-other-selector
name: Open on the name with Google dorking to seed every other selector
description: Use when At the very start of any case where you have a real name and little else, before running specialized tools.
type: pattern
summary: 'Before touching any tool, the team simply Google-dorked the missing person by name. This surfaced news stories, social media posts, and public records, which immediately yielded multiple reference photographs (for later facial verification) plus a cluster of seed selectors: usernames, accounts, and contact details. The lesson is that the name is the cheapest, highest-yield first pivot in a thin-selector case; a few minutes of dorking converts one name into a working set of usernames, emails, and photos that feed every subsequent pivot.'
missingPersonsRelevance: high
phase: intake
pivotFrom:
- name
pivotTo:
- username
- email
- social-profile
- image
- associate
platforms:
- google
steps:
- Run name-based Google dorks for the MP (variations, quoted forms, plus location/age terms if known).
- Harvest news stories and public posts to pull reference photographs for later face comparison.
- Record every username, account, and contact detail surfaced as new seed selectors.
- Note any photos that look like official BOLO imagery to anchor identity verification.
signals:
- News stories or public posts return that clearly match the MP
- Multiple usable reference photos found
- New usernames/emails appear that you did not start with
pitfalls:
- Skipping straight to tools and missing free, high-context results from a plain name search
- Treating the first photo as ground truth without a BOLO/official image to compare against
toolsUsed:
- Google
- Google Dorks
tags:
- google-dorking
- intake
- name-pivot
- tracelabs
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: 'Trace Labs Nov 2025 MVO-winning writeup: ''Google Dork of the MP by name'' as the opening move'
trust: community
source: osinti4l-user
---

# Open on the name with Google dorking to seed every other selector

> Before touching any tool, the team simply Google-dorked the missing person by name. This surfaced news stories, social media posts, and public records, which immediately yielded multiple reference photographs (for later facial verification) plus a cluster of seed selectors: usernames, accounts, and contact details. The lesson is that the name is the cheapest, highest-yield first pivot in a thin-selector case; a few minutes of dorking converts one name into a working set of usernames, emails, and photos that feed every subsequent pivot.

**When to use:** At the very start of any case where you have a real name and little else, before running specialized tools.

## Steps
- Run name-based Google dorks for the MP (variations, quoted forms, plus location/age terms if known).
- Harvest news stories and public posts to pull reference photographs for later face comparison.
- Record every username, account, and contact detail surfaced as new seed selectors.
- Note any photos that look like official BOLO imagery to anchor identity verification.

## Signals it's working
- News stories or public posts return that clearly match the MP
- Multiple usable reference photos found
- New usernames/emails appear that you did not start with

## Pitfalls
- Skipping straight to tools and missing free, high-context results from a plain name search
- Treating the first photo as ground truth without a BOLO/official image to compare against

**Tools:** Google, Google Dorks

_Harvested from `osinti4l-user` — methodology only, no case PII. Promote/curate as needed._
