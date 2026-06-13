---
id: enumeration-is-not-validation
name: Enumeration is not validation
description: Use when Every time an enumeration tool returns a match you are tempted to act on.
type: antipattern
summary: 'A tempting but wrong move: finding a username on a site and treating that as proof the account belongs to your subject. TOFM is explicit that ''Enumeration ≠ Validation.'' Counting hits is easy; confirming identity is the real work. The fix is to cross-reference each hit against the source-of-truth seed data — same photos, same interests, same mutual connections — before relying on it.'
missingPersonsRelevance: high
phase: verification
pivotFrom:
- username
- social-profile
pivotTo: []
steps:
- Treat each enumeration hit as unverified.
- Check for the same pictures used on other confirmed accounts.
- Check for the same likes/dislikes/interests as your subject.
- Check whether a confirmed account of the subject follows/friends this one.
- Check for the same surrounding circle of people interacting across accounts.
- Only then mark the account as belonging to the subject.
signals:
- Multiple independent corroborations (face + interests + circle) all point to the same person
pitfalls:
- Building a whole theory on a single coincidental username match
- Reporting an account as the subject's with zero corroborating signal
toolsUsed:
- whatsmyname.app
tags:
- validation
- false-positive
- identity-confirmation
- tracelabs
evidence:
- type: doc
  url: https://raw.githubusercontent.com/tracelabs/tofm/main/tofm.md
  note: 'TOFM: ''Enumeration ≠ Validation. Just because you''ve found a person''s preferred handle on a website does not explicitly prove it belongs to them.'''
trust: community
source: tofm
---

# Enumeration is not validation

> A tempting but wrong move: finding a username on a site and treating that as proof the account belongs to your subject. TOFM is explicit that 'Enumeration ≠ Validation.' Counting hits is easy; confirming identity is the real work. The fix is to cross-reference each hit against the source-of-truth seed data — same photos, same interests, same mutual connections — before relying on it.

**When to use:** Every time an enumeration tool returns a match you are tempted to act on.

## Steps
- Treat each enumeration hit as unverified.
- Check for the same pictures used on other confirmed accounts.
- Check for the same likes/dislikes/interests as your subject.
- Check whether a confirmed account of the subject follows/friends this one.
- Check for the same surrounding circle of people interacting across accounts.
- Only then mark the account as belonging to the subject.

## Signals it's working
- Multiple independent corroborations (face + interests + circle) all point to the same person

## Pitfalls
- Building a whole theory on a single coincidental username match
- Reporting an account as the subject's with zero corroborating signal

**Tools:** whatsmyname.app

_Harvested from `tofm` — methodology only, no case PII. Promote/curate as needed._
