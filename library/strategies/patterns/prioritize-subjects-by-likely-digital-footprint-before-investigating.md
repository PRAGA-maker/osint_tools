---
id: prioritize-subjects-by-likely-digital-footprint-before-investigating
name: Prioritize subjects by likely digital footprint before investigating
description: Use when At the start of a multi-subject investigation when time is limited and you must allocate effort across several people.
type: pattern
summary: When handed a batch of missing-person subjects in a time-boxed search, do not investigate them in list order. First do a quick triage pass to estimate which subjects have the richest online presence, and front-load effort there. Multiple winning teams note that people under ~40 are far more likely to have meaningful social media, and that subjects who have been missing for years or who are very young/elderly often have thin or stale footprints. Deprioritizing low-footprint subjects early concentrates effort where flags are actually findable.
missingPersonsRelevance: high
phase: triage
pivotFrom:
- name
- dob
- physical-description
pivotTo:
- social-profile
- username
platforms:
- facebook
- instagram
- twitter
- tiktok
steps:
- Skim each subject's intake packet (age, last-seen date, location, photos).
- 'Estimate digital footprint: younger subjects and recent disappearances tend to have active accounts; long-missing or very young/elderly subjects often do not.'
- Rank subjects by expected payoff and assign the richest ones to your strongest researchers first.
- Revisit deprioritized subjects later if higher-value subjects dry up.
signals:
- Early subjects yield quick, easy flags
- Found an active profile within minutes confirms a high-footprint subject
pitfalls:
- Spending equal time on a decades-old cold case with no online presence as on a recently-missing active teen
- Treating the subject list as a fixed order rather than a priority queue
tags:
- triage
- prioritization
- time-management
- tracelabs
evidence:
- type: writeup
  url: https://www.aaroncti.com/trace-labs-august-2020/
  note: 'AaronCTI: people younger than 40 more likely to be on social media; demographic-based prioritization accelerates early flags'
- type: writeup
  url: https://www.intelligencewithsteve.com/post/a-guide-to-participating-in-a-trace-labs-global-osint-search-party-ctf
  note: Deprioritize historically-missing individuals with minimal digital footprints
trust: community
source: searchparty-writeups
---

# Prioritize subjects by likely digital footprint before investigating

> When handed a batch of missing-person subjects in a time-boxed search, do not investigate them in list order. First do a quick triage pass to estimate which subjects have the richest online presence, and front-load effort there. Multiple winning teams note that people under ~40 are far more likely to have meaningful social media, and that subjects who have been missing for years or who are very young/elderly often have thin or stale footprints. Deprioritizing low-footprint subjects early concentrates effort where flags are actually findable.

**When to use:** At the start of a multi-subject investigation when time is limited and you must allocate effort across several people.

## Steps
- Skim each subject's intake packet (age, last-seen date, location, photos).
- Estimate digital footprint: younger subjects and recent disappearances tend to have active accounts; long-missing or very young/elderly subjects often do not.
- Rank subjects by expected payoff and assign the richest ones to your strongest researchers first.
- Revisit deprioritized subjects later if higher-value subjects dry up.

## Signals it's working
- Early subjects yield quick, easy flags
- Found an active profile within minutes confirms a high-footprint subject

## Pitfalls
- Spending equal time on a decades-old cold case with no online presence as on a recently-missing active teen
- Treating the subject list as a fixed order rather than a priority queue

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
