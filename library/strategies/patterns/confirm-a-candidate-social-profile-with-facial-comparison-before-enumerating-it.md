---
id: confirm-a-candidate-social-profile-with-facial-comparison-before-enumerating-it
name: Confirm a candidate social profile with facial comparison before enumerating it
description: Use when Right after a name search returns one or more candidate profiles, before enumerating connections, posts, or contact details.
type: pattern
summary: When a name search returns a candidate profile (e.g., a Facebook account matching the MP's name), do not assume it is the right person. Compare the profile picture against the official BOLO image using a face-comparison tool to confirm identity first. Only after a positive match should you invest time enumerating that account. This prevents building an entire intelligence picture on a same-name stranger and gives you a defensible verification step for your report.
missingPersonsRelevance: high
phase: verification
pivotFrom:
- name
- social-profile
- image
pivotTo:
- face
- social-profile
platforms:
- facebook
steps:
- Search the platform for the MP by name and collect candidate profiles.
- Pull the candidate profile picture(s).
- Run a face comparison between the profile picture and the BOLO / news photos collected at intake.
- Treat only matched accounts as the MP; discard or deprioritize non-matches.
- Document the match (tool + similarity result) for the report.
signals:
- Face-comparison tool returns a match between profile photo and BOLO
- Match lets you confidently attribute the account to the MP
pitfalls:
- Same-name accounts are common; skipping verification leads to investigating a stranger
- Low-quality or heavily filtered profile photos can produce false negatives, so test multiple BOLO angles
toolsUsed:
- FaceComparison (facecomparison.toolpie.com)
tags:
- facial-recognition
- verification
- attribution
- facebook
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: '''The profile picture... was compared against the MP BOLO image utilizing the FaceComparison facial recognition tool, resulting in a match.'''
trust: community
source: osinti4l-mvo-writeup
---

# Confirm a candidate social profile with facial comparison before enumerating it

> When a name search returns a candidate profile (e.g., a Facebook account matching the MP's name), do not assume it is the right person. Compare the profile picture against the official BOLO image using a face-comparison tool to confirm identity first. Only after a positive match should you invest time enumerating that account. This prevents building an entire intelligence picture on a same-name stranger and gives you a defensible verification step for your report.

**When to use:** Right after a name search returns one or more candidate profiles, before enumerating connections, posts, or contact details.

## Steps
- Search the platform for the MP by name and collect candidate profiles.
- Pull the candidate profile picture(s).
- Run a face comparison between the profile picture and the BOLO / news photos collected at intake.
- Treat only matched accounts as the MP; discard or deprioritize non-matches.
- Document the match (tool + similarity result) for the report.

## Signals it's working
- Face-comparison tool returns a match between profile photo and BOLO
- Match lets you confidently attribute the account to the MP

## Pitfalls
- Same-name accounts are common; skipping verification leads to investigating a stranger
- Low-quality or heavily filtered profile photos can produce false negatives, so test multiple BOLO angles

**Tools:** FaceComparison (facecomparison.toolpie.com)

_Harvested from `osinti4l-mvo-writeup` — methodology only, no case PII. Promote/curate as needed._
