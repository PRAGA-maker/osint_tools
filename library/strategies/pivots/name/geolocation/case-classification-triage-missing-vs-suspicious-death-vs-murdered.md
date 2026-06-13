---
id: case-classification-triage-missing-vs-suspicious-death-vs-murdered
name: 'Case classification triage: missing vs. suspicious-death vs. murdered'
description: Use when At intake, before choosing pivot lanes, when you have a name, an approximate last-seen location, and a date.
type: technique
summary: 'Uncovered''s database organizes 49,955 cold cases by case status (Missing, Suspicious Death, Murdered) plus victim race, gender, and orientation/identity, with location and date attached to every entry. For a thin-selector missing-persons case, classify the disappearance type first (voluntary/runaway vs. endangered vs. foul-play-suspected) because it dictates which pivot lanes pay off: runaways and voluntary disappearances are most often solved through active social-media footprints and friend networks, while suspicious-death cases lean on last-known-location, surveillance, and records. The loc'
missingPersonsRelevance: high
phase: triage
pivotFrom:
- name
pivotTo:
- geolocation
- social-profile
- associate
steps:
- 'Establish disappearance classification: voluntary/runaway, endangered, or foul-play-suspected.'
- Anchor the case to a last-known location and date (city/state + day).
- Record demographic facets (gender, approx age, race) as image/face and physical-description pivot seeds.
- 'Route classification to pivot strategy: voluntary/runaway -> social-media + friend networks first; foul-play -> last-location, surveillance, records first.'
signals:
- A clean classification lets you discard whole pivot lanes early
- Location+date anchor produces overlapping geographic and temporal leads
pitfalls:
- Treating every missing case as foul-play and skipping the social-media-first lane that solves most runaway/voluntary cases
- Ignoring the date anchor, which is needed to scope archived social posts and tower/location data
toolsUsed:
- Uncovered case database
tags:
- intake
- classification
- missing-persons
- triage
evidence:
- type: case-db
  url: https://uncovered.com/cases?classification=missing
  note: Filterable by Case Status (Missing/Suspicious Death/Murdered), race, gender, orientation/identity; every case carries location + date.
trust: community
source: uncovered-missing
---

# Case classification triage: missing vs. suspicious-death vs. murdered

> Uncovered's database organizes 49,955 cold cases by case status (Missing, Suspicious Death, Murdered) plus victim race, gender, and orientation/identity, with location and date attached to every entry. For a thin-selector missing-persons case, classify the disappearance type first (voluntary/runaway vs. endangered vs. foul-play-suspected) because it dictates which pivot lanes pay off: runaways and voluntary disappearances are most often solved through active social-media footprints and friend networks, while suspicious-death cases lean on last-known-location, surveillance, and records. The loc

**When to use:** At intake, before choosing pivot lanes, when you have a name, an approximate last-seen location, and a date.

## Steps
- Establish disappearance classification: voluntary/runaway, endangered, or foul-play-suspected.
- Anchor the case to a last-known location and date (city/state + day).
- Record demographic facets (gender, approx age, race) as image/face and physical-description pivot seeds.
- Route classification to pivot strategy: voluntary/runaway -> social-media + friend networks first; foul-play -> last-location, surveillance, records first.

## Signals it's working
- A clean classification lets you discard whole pivot lanes early
- Location+date anchor produces overlapping geographic and temporal leads

## Pitfalls
- Treating every missing case as foul-play and skipping the social-media-first lane that solves most runaway/voluntary cases
- Ignoring the date anchor, which is needed to scope archived social posts and tower/location data

**Tools:** Uncovered case database

_Harvested from `uncovered-missing` — methodology only, no case PII. Promote/curate as needed._
