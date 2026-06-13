---
id: find-the-facebook-profile-by-name-then-face-verify-against-the-bolo-before-trusting-it
name: Find the Facebook profile by name, then face-verify against the BOLO before trusting it
description: Use when As soon as a name search returns a plausible social profile and you have any reference/BOLO photo of the subject.
type: technique
summary: The team searched the MP's name directly on Facebook, located a candidate profile, then ran a face-comparison tool comparing the profile picture against the official BOLO image before treating the account as the real subject. Only after that identity lock did they mine the profile. This two-step (locate then verify) prevents the classic error of building an entire case on a same-name stranger. Facebook in particular was the single richest source in this case, yielding 24 linked accounts/directories, 14 usernames, 4 emails, and links to 2 addresses and 2 relatives.
missingPersonsRelevance: high
phase: verification
pivotFrom:
- name
- image
pivotTo:
- social-profile
- username
- email
- associate
- address
- face
platforms:
- facebook
steps:
- Search the MP's name directly on Facebook and shortlist candidate profiles.
- Pull the candidate's profile picture and run it through a face-comparison tool against the BOLO image.
- Only after a face match, treat the profile as the subject and begin enumeration.
- Mine the verified profile for linked accounts, usernames, emails, addresses, and named relatives.
signals:
- Face-comparison returns a high-confidence match to the BOLO
- Profile details (location, relatives) corroborate other case facts
pitfalls:
- Assuming a same-name profile is the subject without face verification
- Over-trusting an automated face score without a human sanity check on context
toolsUsed:
- Facebook
- FaceComparison
tags:
- facebook
- face-comparison
- identity-verification
- social-pivot
- tracelabs
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: Profile located by name on Facebook, validated with FaceComparison vs BOLO; yielded 24 accounts, 14 usernames, 4 emails, 2 addresses, 2 relatives
trust: community
source: osinti4l-user
---

# Find the Facebook profile by name, then face-verify against the BOLO before trusting it

> The team searched the MP's name directly on Facebook, located a candidate profile, then ran a face-comparison tool comparing the profile picture against the official BOLO image before treating the account as the real subject. Only after that identity lock did they mine the profile. This two-step (locate then verify) prevents the classic error of building an entire case on a same-name stranger. Facebook in particular was the single richest source in this case, yielding 24 linked accounts/directories, 14 usernames, 4 emails, and links to 2 addresses and 2 relatives.

**When to use:** As soon as a name search returns a plausible social profile and you have any reference/BOLO photo of the subject.

## Steps
- Search the MP's name directly on Facebook and shortlist candidate profiles.
- Pull the candidate's profile picture and run it through a face-comparison tool against the BOLO image.
- Only after a face match, treat the profile as the subject and begin enumeration.
- Mine the verified profile for linked accounts, usernames, emails, addresses, and named relatives.

## Signals it's working
- Face-comparison returns a high-confidence match to the BOLO
- Profile details (location, relatives) corroborate other case facts

## Pitfalls
- Assuming a same-name profile is the subject without face verification
- Over-trusting an automated face score without a human sanity check on context

**Tools:** Facebook, FaceComparison

_Harvested from `osinti4l-user` — methodology only, no case PII. Promote/curate as needed._
