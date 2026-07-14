---
id: amazon-usernames
name: Amazon Usernames (Google dork)
description: Use when you have a username or name and want to find the subject's Amazon public profile, reviews, wish lists or lists — returns Amazon profile links and review activity.
url: https://www.google.com/search?q=site:amazon.com+%3Cusername%3E
category: username
path:
- username
- specific-sites
bestFor: Surfacing a person's public Amazon profile, reviews and wish lists via a site-scoped Google search.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- address
status: live
pricing: free
costNote: Free — just a Google query; no account or payment.
opsec: passive
opsecNote: The query goes to Google, not to Amazon, so the target is not alerted and Amazon does not see you. Google logs the search and your IP; use a sock-puppet/VPN for sensitive names. Opening the resulting Amazon profile is a normal public page view.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: This is a search technique, not a maintained tool — reliability depends on Google's index and on whether the subject left profile/review content public.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Amazon profile search
- Amazon reviews dork
- site:amazon.com username
tags:
- username
- amazon
- google-dork
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Amazon Usernames (Google dork)

> A site-scoped Google search that pulls a subject's public Amazon footprint — profile page, reviews, wish lists and lists — out of Amazon's otherwise unsearchable interior.

## When to use
You have a `username` or `name` and want to know whether the subject has a public Amazon presence. Amazon profiles, product reviews and (crucially) **wish lists** can leak real interests, a first name, a city, and sometimes a shipping address label — and Amazon's own site search won't find people by handle. A `site:amazon.com` Google dork reaches that content from the outside.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to Google and run `site:amazon.com "<username>"` (quote the handle for an exact match), swapping in the target's `username` or `name`.
2. Broaden or narrow: add terms like `profile`, `wishlist`, `reviews`, or a city to focus; drop the quotes if you get nothing.
3. Also try `site:amazon.com/gp/profile` and wish-list paths (`site:amazon.com/hz/wishlist`) directly.
4. Open promising hits — a public profile shows the reviewer's chosen name, review history and any public lists.
5. Pivot: a public wish list may expose a first/last name and a shipping city or address label; the reviewer name and interests feed cross-platform username/people search.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** Amazon `social-profile` link, reviewer `name`, and occasionally an `address`/city leaked via a public wish-list shipping label
- **Empty/negative result looks like:** no Amazon results, or only product pages (not profiles). That usually means the subject kept their profile/reviews private — not proof they have no account.

## Gotchas & OpSec
- Amazon aggressively de-indexes profile content, so Google's coverage is partial and often stale; a miss is weak evidence.
- Passive — the search hits Google, not Amazon, so the target is never alerted; still use a VPN for sensitive names.
- Wish-list "send to this address" labels are the highest-value leak but appear only when the user made the list public with a shipping address — verify any address against a second source.
- Common usernames produce noise; combine with a real name or location term.

## Overlaps ("do both")
- Pairs with a broad username-enumeration tool (e.g. `[[sultan-username-search-tool-builder]]`) — run the handle everywhere, then use this dork to pull the Amazon-specific detail those enumerators don't parse.
- Complements `[[github-io-2]]` (FilePhish) and general dorking for the same subject across other `site:` targets.

## Trust & verifiability
`trust: unverified` — this is a technique dependent on Google's index and the subject's privacy settings, not a maintained tool; always corroborate a leaked name/address from a wish list against an independent source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazon-usernames |
| category | username |
| selectorsIn → selectorsOut | username, name → social-profile, name, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
