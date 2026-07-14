---
id: facebook-directory-users-by-name
name: Facebook Directory (Users by Name)
description: Use when you have a `name` and want to enumerate public Facebook profiles matching it via Facebook's own alphabetical directory — returns candidate social-profiles.
url: https://www.facebook.com/directory/people
category: social-networks
path:
- social-networks
bestFor: Browsing/enumerating public Facebook profiles by name through Facebook's built-in people directory.
selectorsIn:
- name
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free. The public directory still exists but Facebook increasingly gates it behind login and has curtailed logged-out browsing, so coverage varies.
opsec: active
opsecNote: Meaningful use now generally requires a Facebook login — use a sock account, never your own. Browsing the directory doesn't notify targets, but any profile interaction from your session does. Stay read-only.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Facebook surface listing public profiles; the profiles are genuine, but the directory's completeness has degraded as Facebook restricts it.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- facebook-watch
aliases:
- facebook.com/directory
- FB people directory
tags:
- facebook
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Facebook Directory (Users by Name)

> Facebook's own alphabetical directory of public profiles — a way to enumerate accounts matching a name without relying on Facebook's flaky search box.

## When to use
You have a subject's `name` and want to see the public Facebook profiles that match it, especially when Facebook's regular search is returning noise or nothing. The directory lists public profiles alphabetically, which can surface accounts (and their photos) that search misses. Best as a name-to-candidate-profiles enumeration step before you disambiguate the right person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a **sock** Facebook account and open https://www.facebook.com/directory/people.
2. Drill down alphabetically to the surname/name, or append the name to the directory path.
3. Scan the listed public profiles: use profile photos (`image`), location, and other visible details to shortlist the likely subject.
4. Read the output: candidate `social-profile` links. Open promising ones and corroborate against known attributes (city, employer, photos).
5. Pivot: a confirmed profile feeds [[facebook-watch]] (video footprint), friend-list/associate mapping, and reverse-image on the profile photo.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile` (candidate public profiles), `image` (profile photos)
- **Empty/negative result looks like:** no matching public profiles listed — the subject may keep their profile non-public or not be indexed in the directory; try direct search and third-party FB tools.

## Gotchas & OpSec
- The directory has been progressively restricted; logged-out access is limited and coverage is incomplete, so a miss isn't conclusive.
- Common names return many candidates — disambiguate with independent attributes before acting.
- OpSec: **active** (login required); keep the sock session read-only.

## Overlaps ("do both")
- Pairs with [[facebook-watch]] — the directory finds the profile, Watch mines its video output. Also combine with Google `site:facebook.com` dorking, which catches profiles the directory omits.

## Trust & verifiability
`trust: trusted` — a first-party Facebook surface, so the listed profiles are real. The limitation is coverage (Facebook keeps narrowing the directory), not authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-directory-users-by-name |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
