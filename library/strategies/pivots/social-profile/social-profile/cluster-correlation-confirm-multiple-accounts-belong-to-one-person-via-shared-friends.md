---
id: cluster-correlation-confirm-multiple-accounts-belong-to-one-person-via-shared-friends
name: 'Cluster correlation: confirm multiple accounts belong to one person via shared friends'
description: Use when When you have several candidate accounts and need to confirm they are the same individual before submitting linked flags.
type: technique
summary: A single person typically has several accounts across platforms. To prove a set of accounts all belong to the same subject (rather than namesakes), look for the same two or more mutual friends/associates appearing across each account. Shared close connections are a far stronger correlation signal than a matching display name, and they let you confidently merge accounts into one identity and advance the timeline. A winning team explicitly used 'two common friends across every account' as their verification rule.
missingPersonsRelevance: high
phase: verification
pivotFrom:
- social-profile
- associate
- username
pivotTo:
- social-profile
- associate
platforms:
- facebook
- instagram
- twitter
steps:
- List all candidate accounts plausibly belonging to the subject.
- Enumerate each account's visible friends/followers/frequent interactors.
- Look for the same individuals (ideally 2+) appearing across the accounts.
- If a consistent core of mutual connections is present, merge the accounts into one identity.
- Use TruePeopleSearch or similar to corroborate the relationship of those mutual connections (family/close friend).
signals:
- The same 2+ named people appear as friends on every candidate account
- Cross-account photos feature the same associates
pitfalls:
- Merging accounts on display-name match alone (namesakes)
- Ignoring that platform privacy may hide the friend overlap that exists
toolsUsed:
- TruePeopleSearch
tags:
- correlation
- verification
- network-analysis
- identity-resolution
evidence:
- type: writeup
  url: https://jack.bio/blog/tracelabs
  note: Finding two common friends across every account provided concrete verification that accounts were the same person
trust: community
source: searchparty-writeups
---

# Cluster correlation: confirm multiple accounts belong to one person via shared friends

> A single person typically has several accounts across platforms. To prove a set of accounts all belong to the same subject (rather than namesakes), look for the same two or more mutual friends/associates appearing across each account. Shared close connections are a far stronger correlation signal than a matching display name, and they let you confidently merge accounts into one identity and advance the timeline. A winning team explicitly used 'two common friends across every account' as their verification rule.

**When to use:** When you have several candidate accounts and need to confirm they are the same individual before submitting linked flags.

## Steps
- List all candidate accounts plausibly belonging to the subject.
- Enumerate each account's visible friends/followers/frequent interactors.
- Look for the same individuals (ideally 2+) appearing across the accounts.
- If a consistent core of mutual connections is present, merge the accounts into one identity.
- Use TruePeopleSearch or similar to corroborate the relationship of those mutual connections (family/close friend).

## Signals it's working
- The same 2+ named people appear as friends on every candidate account
- Cross-account photos feature the same associates

## Pitfalls
- Merging accounts on display-name match alone (namesakes)
- Ignoring that platform privacy may hide the friend overlap that exists

**Tools:** TruePeopleSearch

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
