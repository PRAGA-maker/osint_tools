---
id: establish-a-source-of-truth-before-pivoting
name: Establish a source of truth before pivoting
description: Use when At the very start of any case, before doing a single search, and as the reference point each time you find a candidate account.
type: pattern
summary: Trace Labs' TOFM stresses that the thin set of selectors you START with (a name, a photo, a physical description, a known social profile, hobbies/interests) is your 'source of truth' against which every later discovery must be validated. Good investigators anchor on this seed data first, write it down, and treat any newly found account as a hypothesis to confirm against the seed rather than as fact. This prevents you from chasing a same-named stranger and corrupting the whole investigation.
missingPersonsRelevance: high
phase: intake
pivotFrom:
- name
- image
- physical-description
- social-profile
pivotTo: []
steps:
- 'Inventory every confirmed selector you were handed: name, photos, physical description, existing profiles, hobbies/interests, background context.'
- Record these as the immutable 'source of truth'.
- 'For every later find, ask: does it corroborate the seed (same face, same interests, same circle)?'
- Only promote a find to 'confirmed' once it matches the seed on multiple independent points.
signals:
- A candidate account shares the same photos, the same like/dislikes, and the same circle of friends as the seed data
pitfalls:
- Treating a name match as identity confirmation
- Letting an unvalidated find become the new (wrong) anchor for further pivots
tags:
- intake
- validation
- seed-data
- tracelabs
evidence:
- type: doc
  url: https://raw.githubusercontent.com/tracelabs/tofm/main/tofm.md
  note: 'TOFM: ''The information you begin your investigation with will be the source of truth you''ll use to validate everything else you find.'''
trust: community
source: tofm
---

# Establish a source of truth before pivoting

> Trace Labs' TOFM stresses that the thin set of selectors you START with (a name, a photo, a physical description, a known social profile, hobbies/interests) is your 'source of truth' against which every later discovery must be validated. Good investigators anchor on this seed data first, write it down, and treat any newly found account as a hypothesis to confirm against the seed rather than as fact. This prevents you from chasing a same-named stranger and corrupting the whole investigation.

**When to use:** At the very start of any case, before doing a single search, and as the reference point each time you find a candidate account.

## Steps
- Inventory every confirmed selector you were handed: name, photos, physical description, existing profiles, hobbies/interests, background context.
- Record these as the immutable 'source of truth'.
- For every later find, ask: does it corroborate the seed (same face, same interests, same circle)?
- Only promote a find to 'confirmed' once it matches the seed on multiple independent points.

## Signals it's working
- A candidate account shares the same photos, the same like/dislikes, and the same circle of friends as the seed data

## Pitfalls
- Treating a name match as identity confirmation
- Letting an unvalidated find become the new (wrong) anchor for further pivots

_Harvested from `tofm` — methodology only, no case PII. Promote/curate as needed._
