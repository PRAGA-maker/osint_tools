---
id: enumerate-one-confirmed-profile-into-a-wide-selector-graph-via-people-search-and-linked-profiles
name: Enumerate one confirmed profile into a wide selector graph via people-search and linked profiles
description: Use when After confirming and triaging the MP's primary social profile, to maximize the selector set you can pivot from.
type: playbook
summary: 'A single confirmed account is a hub, not an endpoint. From the MP''s profile, pivot outward through linked profiles, people-search sites, and the connections the account exposes to build a broad selector graph: additional social accounts and link directories, usernames, emails, accounts tied to those emails, physical addresses, and relatives. In the documented case one confirmed Facebook profile expanded into 24 social/link directories, 14 usernames, 4 emails, 10 email-linked accounts, 2 addresses, and 2 relatives. Each new selector is a fresh pivot surface and a possible point of current conta'
missingPersonsRelevance: high
phase: enrichment
pivotFrom:
- social-profile
pivotTo:
- username
- email
- address
- associate
- social-profile
platforms:
- facebook
steps:
- Start from the confirmed MP profile and follow every linked profile and link-directory it exposes.
- Run people-search lookups on the MP's name and known selectors.
- Collect usernames, emails, and addresses; then pivot from emails to other accounts registered to them.
- Identify relatives and associates whose own profiles may carry tags/photos of the MP.
- Maintain a running inventory of every selector with its source for later documentation.
signals:
- A single hub profile yields dozens of new selectors
- Emails resolve to additional accounts on other platforms
- Relatives/associates surface who can be pivoted through next
pitfalls:
- 'Selector sprawl without verification: tie each new account back to the MP before trusting it'
- People-search sites can mix in same-name strangers' addresses/relatives
toolsUsed:
- Facebook
- people-search sites
tags:
- enumeration
- selector-graph
- people-search
- email-pivot
- facebook
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: Enumeration yielded 24 accounts/directories, 14 usernames, 4 emails, 10 email-linked accounts, 2 addresses, 2 relatives.
trust: community
source: osinti4l-mvo-writeup
---

# Enumerate one confirmed profile into a wide selector graph via people-search and linked profiles

> A single confirmed account is a hub, not an endpoint. From the MP's profile, pivot outward through linked profiles, people-search sites, and the connections the account exposes to build a broad selector graph: additional social accounts and link directories, usernames, emails, accounts tied to those emails, physical addresses, and relatives. In the documented case one confirmed Facebook profile expanded into 24 social/link directories, 14 usernames, 4 emails, 10 email-linked accounts, 2 addresses, and 2 relatives. Each new selector is a fresh pivot surface and a possible point of current conta

**When to use:** After confirming and triaging the MP's primary social profile, to maximize the selector set you can pivot from.

## Steps
- Start from the confirmed MP profile and follow every linked profile and link-directory it exposes.
- Run people-search lookups on the MP's name and known selectors.
- Collect usernames, emails, and addresses; then pivot from emails to other accounts registered to them.
- Identify relatives and associates whose own profiles may carry tags/photos of the MP.
- Maintain a running inventory of every selector with its source for later documentation.

## Signals it's working
- A single hub profile yields dozens of new selectors
- Emails resolve to additional accounts on other platforms
- Relatives/associates surface who can be pivoted through next

## Pitfalls
- Selector sprawl without verification: tie each new account back to the MP before trusting it
- People-search sites can mix in same-name strangers' addresses/relatives

**Tools:** Facebook, people-search sites

_Harvested from `osinti4l-mvo-writeup` — methodology only, no case PII. Promote/curate as needed._
