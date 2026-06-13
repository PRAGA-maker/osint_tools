---
id: facial-recognition-to-confirm-a-candidate-profile-is-the-subject
name: Facial recognition to confirm a candidate profile is the subject
description: Use when After locating a candidate profile, before investing time pivoting through it.
type: technique
summary: When a name search returns a candidate social profile, confirm identity by comparing the profile's photos against the official missing-person photo using a face-comparison/recognition tool that returns a similarity score. This converts an uncertain 'maybe this is them' into a defensible match, which matters because everything you pivot to downstream depends on the profile actually belonging to the subject. Multiple teams used this to validate profiles in seconds and avoid wasting time on the wrong person.
missingPersonsRelevance: high
phase: verification
pivotFrom:
- image
- face
- social-profile
pivotTo:
- social-profile
platforms:
- facebook
- instagram
steps:
- Collect the official missing-person photo(s) from the intake packet.
- Collect photos from the candidate profile.
- Run a face-comparison tool to get a same/different similarity score.
- If confident, treat the profile as confirmed and begin friend/tag enumeration; if not, keep searching.
signals:
- High similarity score between official photo and profile photo
- Consistent secondary details (location, age, name) reinforce the match
pitfalls:
- Relying on the score alone for low-quality or angled photos
- Confirming on a single ambiguous image instead of corroborating with non-photo facts
toolsUsed:
- FaceComparison
- Microsoft Azure Face API
- facial recognition tools
tags:
- face
- verification
- identity-confirmation
evidence:
- type: writeup
  url: https://www.aaroncti.com/trace-labs-august-2020/
  note: Microsoft Azure facial recognition to compare social images against law-enforcement photos and score likely-same
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: Confirmed Facebook identity using FaceComparison before pivoting
trust: community
source: searchparty-writeups
---

# Facial recognition to confirm a candidate profile is the subject

> When a name search returns a candidate social profile, confirm identity by comparing the profile's photos against the official missing-person photo using a face-comparison/recognition tool that returns a similarity score. This converts an uncertain 'maybe this is them' into a defensible match, which matters because everything you pivot to downstream depends on the profile actually belonging to the subject. Multiple teams used this to validate profiles in seconds and avoid wasting time on the wrong person.

**When to use:** After locating a candidate profile, before investing time pivoting through it.

## Steps
- Collect the official missing-person photo(s) from the intake packet.
- Collect photos from the candidate profile.
- Run a face-comparison tool to get a same/different similarity score.
- If confident, treat the profile as confirmed and begin friend/tag enumeration; if not, keep searching.

## Signals it's working
- High similarity score between official photo and profile photo
- Consistent secondary details (location, age, name) reinforce the match

## Pitfalls
- Relying on the score alone for low-quality or angled photos
- Confirming on a single ambiguous image instead of corroborating with non-photo facts

**Tools:** FaceComparison, Microsoft Azure Face API, facial recognition tools

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
