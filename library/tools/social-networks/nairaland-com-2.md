---
id: nairaland-com-2
name: nairaland.com
description: Use when you have a `username` or `name` and want to surface a person's posts, profile and self-disclosed details on Nairaland (Nigeria's largest forum) — returns social-profile, name, associate.
url: https://www.nairaland.com/search?q=&search=Search
category: social-networks
path:
- social-networks
bestFor: Finding a Nigerian subject's forum footprint, posts and disclosed contact/location details on Africa's largest discussion board.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- associate
status: live
pricing: free
costNote: Free to read and search; a free account is only needed to view members' profile pages and some threads.
opsec: passive
opsecNote: Searching public threads is passive and leaves no trace to the target. Reading a member's profile page while logged in is still passive to the target but ties the view to your account — use a sock-puppet Nairaland account, never your real one, and browse over a clean IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: User-generated forum content; anything a member posts is self-asserted and unverified. Treat disclosed phone numbers, locations and jobs as leads to corroborate, not facts.
missingPersonsRelevance: high
coverage:
- ng
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Nairaland Forum
tags:
- gsocialmedia
- General Social Media Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
relatedTools:
- nairaland-com
---

# nairaland.com

> Nigeria's largest online community (3M+ members): full-text search across a decade of forum posts, usable as a people-search surface for Nigerian and diaspora subjects.

## When to use
You have a `username` or `name` for a subject with likely Nigerian ties and want to find their forum activity — posts, the boards they frequent, and details they've volunteered (phone number in a classifieds ad, hometown, employer, family references). Nairaland threads are heavily indexed and often the richest open source on ordinary Nigerians, who may have little other web presence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nairaland.com/search — enter the `username` or `name` (or a distinctive phrase, email fragment, or phone number the subject might have posted).
2. Optionally restrict by board (Jobs/CVs, Phones, Cars, Politics, Romance) or by a specific member's posts using the "posts by <username>" URL pattern `nairaland.com/<username>`.
3. Read the hits: each result links to the thread and the posting member. A member's profile page (`nairaland.com/<username>`) shows join date, post count, gender, location and signature.
4. Pivot: a disclosed phone/email feeds phone/email OSINT; a linked handle reused elsewhere feeds `[[social-search-engine]]`; named associates in a thread become new `name` selectors.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (Nairaland member page + post history), `name`, `associate` (people named/tagged in threads), plus any `phone`/`address`/`employer-org` the member self-disclosed
- **Empty/negative result looks like:** "Your search did not match any documents" or only unrelated common-word hits — a common name may return noise, so anchor on a username or an unusual token.

## Gotchas & OpSec
- Common Nigerian names return many false positives; corroborate with a second selector before attributing a post to your subject.
- Self-reported profile fields (location, gender) are unverified and easily faked.
- OpSec: reading is passive; only log in with a sock puppet, and note Nairaland occasionally rate-limits or Cloudflare-challenges heavy searching.

## Overlaps ("do both")
- Pairs with `[[social-search-engine]]` — Nairaland covers the Nigerian forum layer that broad social aggregators miss, while the aggregator catches a reused handle across other networks.

## Trust & verifiability
`trust: community` — Nairaland is a genuine, long-running forum (real, high-traffic site), but every datapoint is user-posted and must be treated as a lead, not a verified fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nairaland-com-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
