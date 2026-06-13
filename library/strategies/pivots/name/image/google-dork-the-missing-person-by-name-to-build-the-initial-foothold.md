---
id: google-dork-the-missing-person-by-name-to-build-the-initial-foothold
name: Google Dork the missing person by name to build the initial foothold
description: Use when At case start, immediately after being assigned a missing person, before any platform-specific enumeration.
type: technique
summary: Before touching social platforms, run a focused Google search (dork) on the missing person's full name. This surfaces news stories about the disappearance and posts by family members, which in turn yield multiple photographs from different angles plus loose selectors (usernames, social handles, associates). The photos are reusable later for facial-recognition confirmation of candidate profiles, and the selectors become the data points you pivot from. Treat this as the foothold step that seeds everything else.
missingPersonsRelevance: high
phase: intake
pivotFrom:
- name
pivotTo:
- image
- username
- social-profile
- associate
platforms:
- google
steps:
- Pick one missing person to own (in a team, divide MPs so efforts don't overlap).
- Google the MP by full name, including variations and quoted exact-name searches.
- Harvest news articles about the disappearance and family social posts.
- Save every distinct photo of the MP, especially multiple face angles, for later facial recognition.
- 'Record loose selectors found in passing: usernames, social account links, associate names.'
signals:
- News coverage or family posts about the disappearance appear
- Multiple photos of the MP from different angles are recovered
- Initial usernames or profile links are discovered to pivot from
pitfalls:
- Common names dilute results; without disambiguators you waste time on the wrong person
- Treating the foothold search as the goal rather than a launch pad
toolsUsed:
- Google
tags:
- foothold
- google-dork
- intake
- trace-labs
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: 'Initial Foothold section: ''A good starting point includes a Google Dork of the MP by name... Multiple images of the MP are typically found.'''
trust: community
source: osinti4l-mvo-writeup
---

# Google Dork the missing person by name to build the initial foothold

> Before touching social platforms, run a focused Google search (dork) on the missing person's full name. This surfaces news stories about the disappearance and posts by family members, which in turn yield multiple photographs from different angles plus loose selectors (usernames, social handles, associates). The photos are reusable later for facial-recognition confirmation of candidate profiles, and the selectors become the data points you pivot from. Treat this as the foothold step that seeds everything else.

**When to use:** At case start, immediately after being assigned a missing person, before any platform-specific enumeration.

## Steps
- Pick one missing person to own (in a team, divide MPs so efforts don't overlap).
- Google the MP by full name, including variations and quoted exact-name searches.
- Harvest news articles about the disappearance and family social posts.
- Save every distinct photo of the MP, especially multiple face angles, for later facial recognition.
- Record loose selectors found in passing: usernames, social account links, associate names.

## Signals it's working
- News coverage or family posts about the disappearance appear
- Multiple photos of the MP from different angles are recovered
- Initial usernames or profile links are discovered to pivot from

## Pitfalls
- Common names dilute results; without disambiguators you waste time on the wrong person
- Treating the foothold search as the goal rather than a launch pad

**Tools:** Google

_Harvested from `osinti4l-mvo-writeup` — methodology only, no case PII. Promote/curate as needed._
