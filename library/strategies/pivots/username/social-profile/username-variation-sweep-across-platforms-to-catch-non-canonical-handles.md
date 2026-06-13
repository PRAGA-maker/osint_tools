---
id: username-variation-sweep-across-platforms-to-catch-non-canonical-handles
name: Username variation sweep across platforms to catch non-canonical handles
description: Use when Any time you have one or more usernames and want to enumerate all platforms the subject uses.
type: technique
summary: Because platforms structure their URLs and handle rules differently, a single username spelling will miss accounts. The cupidcr4wl methodology is to run each target username in multiple variations - janedoe, jane_doe, jane-doe, jdoe - across the full platform list so that an account registered under a non-canonical form is not missed. For missing persons, the same handle (or near-variant) is often reused across many sites, so a variation sweep turns one discovered username into a much wider account map (the case profile yielded 14 usernames worth sweeping).
missingPersonsRelevance: high
phase: pivot
pivotFrom:
- username
pivotTo:
- social-profile
- username
- email
platforms:
- instagram
- reddit
- tiktok
- twitter
steps:
- Take each known username and generate spelling variants (separators removed, underscore, hyphen, first-initial+last).
- Run the full variant set through a username checker across many platforms.
- Collect hits and note which variant form each platform used.
- Feed newly discovered profiles back in for emails, real names, and further usernames.
signals:
- A variant form (not the canonical one) returns a real account
- Reused handles cluster the same person across unrelated sites
pitfalls:
- Searching only the canonical spelling and missing underscore/hyphen variants
- Treating a common handle as the subject without corroborating profile detail
toolsUsed:
- cupidcr4wl
tags:
- username-enumeration
- handle-variations
- pivot
- account-mapping
evidence:
- type: tool
  url: https://github.com/OSINTI4L/cupidcr4wl
  note: 'README: run target username in multiple variations (janedoe/jane_doe/jane-doe/jdoe) due to platform URL differences'
trust: community
source: osinti4l-user
---

# Username variation sweep across platforms to catch non-canonical handles

> Because platforms structure their URLs and handle rules differently, a single username spelling will miss accounts. The cupidcr4wl methodology is to run each target username in multiple variations - janedoe, jane_doe, jane-doe, jdoe - across the full platform list so that an account registered under a non-canonical form is not missed. For missing persons, the same handle (or near-variant) is often reused across many sites, so a variation sweep turns one discovered username into a much wider account map (the case profile yielded 14 usernames worth sweeping).

**When to use:** Any time you have one or more usernames and want to enumerate all platforms the subject uses.

## Steps
- Take each known username and generate spelling variants (separators removed, underscore, hyphen, first-initial+last).
- Run the full variant set through a username checker across many platforms.
- Collect hits and note which variant form each platform used.
- Feed newly discovered profiles back in for emails, real names, and further usernames.

## Signals it's working
- A variant form (not the canonical one) returns a real account
- Reused handles cluster the same person across unrelated sites

## Pitfalls
- Searching only the canonical spelling and missing underscore/hyphen variants
- Treating a common handle as the subject without corroborating profile detail

**Tools:** cupidcr4wl

_Harvested from `osinti4l-user` — methodology only, no case PII. Promote/curate as needed._
