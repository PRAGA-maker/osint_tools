---
id: tracelabs-cluster-correlation-shared-friends
name: 'Trace Labs case: confirm multiple accounts are one person via two shared friends'
description: Use when you have several candidate accounts plausibly belonging to one subject and need a concrete, defensible rule to merge them into a single identity before submitting linked flags.
type: case-study
summary: 'Across winning Trace Labs Search Party teams, the highest-yield chain ran: triage subjects by likely digital footprint, canvass Facebook first (repeatedly called "a goldmine"), sweep any recovered username across platforms, face-verify candidate profiles against the BOLO, and then — the decisive verification — confirm that a set of candidate accounts all belong to the same person by finding the same two-or-more mutual friends/associates appearing across every account. A winning team used "two common friends across every account" as an explicit rule, because shared close connections are a far stronger correlation signal than a matching display name (which only catches namesakes). People-search was then used to corroborate that those mutual connections were genuinely family/close friends. The transferable lesson: enumeration and name-matches produce candidate clusters; a stable core of shared associates is what proves the cluster is one identity.'
missingPersonsRelevance: high
phase: verification
pivotFrom:
- social-profile
- username
- associate
pivotTo:
- social-profile
- associate
platforms:
- facebook
- instagram
- twitter
steps:
- Triage which subjects have a rich enough footprint to be worth deep work; front-load effort there.
- Canvass Facebook first; locate a candidate profile and face-verify it against the BOLO before investing time.
- Sweep any recovered username/handle (and variants) across platforms to surface a cluster of candidate accounts.
- For each candidate account, enumerate its visible friends/followers/frequent interactors.
- Look for the SAME individuals (ideally 2+) appearing across the accounts; a consistent core of mutual connections merges the accounts into one identity.
- Corroborate that those mutual connections are genuinely family/close friends with a people-search tool before submitting linked flags.
signals:
- The same 2+ named people appear as friends/interactors on every candidate account.
- Cross-account photos feature the same associates, reinforcing the merge.
pitfalls:
- Merging accounts on display-name match alone, sweeping in namesakes.
- Assuming no friend overlap exists when platform privacy is simply hiding it.
- Submitting a linked-identity flag without explaining how the merge was established.
toolsUsed:
- WhatsMyName
- Sherlock
- Namecheckr
- FaceComparison
- TruePeopleSearch
tags:
- tracelabs
- identity-resolution
- correlation
- network-analysis
- verification
evidence:
- type: ctf-writeup
  url: https://jack.bio/blog/tracelabs
  note: 'Finding two common friends across every account provided concrete verification that the accounts were the same person; TruePeopleSearch used to confirm the relationships.'
- type: ctf-writeup
  url: https://shandyman.online/blog/on-a-mission-a-tracelabs-ctf-missing-persons-writeup/
  note: 'Facebook called a goldmine and primary platform; Namecheckr/WhatsMyName for cross-platform discovery before correlation.'
trust: community
source: searchparty-writeups
relatedStrategies:
- Cluster correlation: confirm multiple accounts belong to one person via shared friends
- Username persistence across platforms
- Facial recognition to confirm a candidate profile is the subject
- antipattern-single-source-confirmation
- enumeration-is-not-validation
---

# Trace Labs case: confirm multiple accounts are one person via two shared friends

> Across winning Trace Labs Search Party teams, the highest-yield chain ran: triage by footprint, canvass Facebook first, sweep any recovered username across platforms, face-verify candidates against the BOLO, and then — the decisive step — confirm a set of candidate accounts are one person by finding the same two-or-more mutual friends across every account. Shared close connections beat a matching display name, which only catches namesakes. The transferable lesson: enumeration and name-matches produce candidate clusters; a stable core of shared associates is what proves the cluster is one identity.

**When to use:** When you have several candidate accounts plausibly belonging to one subject and need a concrete, defensible rule to merge them into a single identity before submitting linked flags.

## The pivot chain that worked
1. **Triage by footprint.** Front-load effort on subjects likely to have a rich online presence rather than working a list in order.
2. **Facebook-first canvass.** Repeatedly described as "a goldmine," Facebook was the primary platform; a candidate profile was located and **face-verified against the BOLO** before deeper work (`[[Facial recognition to confirm a candidate profile is the subject]]`).
3. **Username sweep.** Any recovered handle (and variants) was swept across platforms, surfacing a *cluster* of candidate accounts (`[[Username persistence across platforms]]`).
4. **Enumerate each account's circle.** For every candidate, the team listed visible friends/followers and frequent interactors.
5. **Merge on shared associates.** The decisive rule: the same **two or more** mutual friends appearing across *every* candidate account. A consistent core of shared close connections merged the accounts into one identity.

## The verification step
"Two common friends across every account" is the load-bearing check (`[[Cluster correlation: confirm multiple accounts belong to one person via shared friends]]`). Shared close associates are a far stronger correlation signal than a matching display name — names produce namesakes; a stable friend-core does not. People-search (TruePeopleSearch) then corroborated that those mutual connections were genuinely family/close friends, so the merge rested on a confirmed relationship, not an assumption.

## The lesson
Enumeration and name-matching produce *candidate* clusters, never confirmed identity — treating a hit list as proof is `[[enumeration-is-not-validation]]`, and merging on the display name alone is `[[antipattern-single-source-confirmation]]` (the name echoing itself across sites). The proof is a stable core of shared associates that recurs across every account, corroborated against records.

## Signals it's working
- The same 2+ named people appear as friends/interactors on every candidate account.
- Cross-account photos feature the same associates, reinforcing the merge.

## Pitfalls
- Merging accounts on display-name match alone, sweeping in namesakes.
- Assuming no friend overlap exists when platform privacy is simply hiding it.
- Submitting a linked-identity flag without explaining how the merge was established.

**Tools:** WhatsMyName, Sherlock, Namecheckr, FaceComparison, TruePeopleSearch

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._

---
## Metadata
| field | value |
|---|---|
| type | case-study |
| phase | verification |
| MP relevance | high |
| related | Cluster correlation: confirm multiple accounts belong to one person via shared friends; enumeration-is-not-validation |
