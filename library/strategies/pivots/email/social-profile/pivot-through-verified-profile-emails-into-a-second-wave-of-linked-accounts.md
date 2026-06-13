---
id: pivot-through-verified-profile-emails-into-a-second-wave-of-linked-accounts
name: Pivot through verified-profile emails into a second wave of linked accounts
description: Use when Once you have a verified profile and have extracted one or more email addresses from it.
type: technique
summary: 'After verifying the Facebook profile, the team did not stop at the visible social accounts: they extracted email addresses and used those emails to discover an additional 10 accounts beyond the directly listed ones. Email is a strong cross-platform join key because the same address often registers accounts a username sweep alone won''t reveal. The transferable technique is to harvest every email tied to a verified profile and run an email-to-account pivot (breach/registration lookups, email-based people search) to expand the account map and surface fresh, possibly more current footprints.'
missingPersonsRelevance: high
phase: pivot
pivotFrom:
- email
- social-profile
pivotTo:
- social-profile
- username
- address
- associate
platforms:
- facebook
steps:
- Pull every email address listed on or linked to the verified profile.
- Run each email through email-to-account and registration/breach lookups.
- Map newly linked accounts and cross-check for more recent activity than the original profile.
- Feed any new usernames and associates back into the pivot loop.
signals:
- An email reveals accounts not visible from the username sweep
- Newly found accounts show more recent activity than the seed profile
pitfalls:
- Treating the visible profile links as the complete account set
- Not cross-checking that an email-linked account actually belongs to the subject
toolsUsed:
- Facebook
tags:
- email-pivot
- account-mapping
- enrichment
- tracelabs
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: 4 emails extracted led to 10 additional linked accounts
trust: community
source: osinti4l-user
---

# Pivot through verified-profile emails into a second wave of linked accounts

> After verifying the Facebook profile, the team did not stop at the visible social accounts: they extracted email addresses and used those emails to discover an additional 10 accounts beyond the directly listed ones. Email is a strong cross-platform join key because the same address often registers accounts a username sweep alone won't reveal. The transferable technique is to harvest every email tied to a verified profile and run an email-to-account pivot (breach/registration lookups, email-based people search) to expand the account map and surface fresh, possibly more current footprints.

**When to use:** Once you have a verified profile and have extracted one or more email addresses from it.

## Steps
- Pull every email address listed on or linked to the verified profile.
- Run each email through email-to-account and registration/breach lookups.
- Map newly linked accounts and cross-check for more recent activity than the original profile.
- Feed any new usernames and associates back into the pivot loop.

## Signals it's working
- An email reveals accounts not visible from the username sweep
- Newly found accounts show more recent activity than the seed profile

## Pitfalls
- Treating the visible profile links as the complete account set
- Not cross-checking that an email-linked account actually belongs to the subject

**Tools:** Facebook

_Harvested from `osinti4l-user` — methodology only, no case PII. Promote/curate as needed._
