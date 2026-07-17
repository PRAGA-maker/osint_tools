---
id: yelp-find-friends
name: Yelp Find Friends
description: Use when you have a `name`/`email` and want a subject's Yelp presence — their public reviews reveal places frequented and rough `geolocation`; the Find Friends flow matches contacts to Yelp accounts.
url: https://www.yelp.com/login?return_url=%2Ffind_friends
category: communities-forums
path:
- communities-forums
bestFor: Locating a subject's Yelp profile and mining their reviews/check-ins for frequented locations and habits.
selectorsIn:
- name
- email
selectorsOut:
- social-profile
- geolocation
- associate
status: live
pricing: free
costNote: Free with a Yelp account. Reading a public Yelp profile needs no login; the Find Friends contact-matching feature requires signing in.
opsec: active
opsecNote: Reading a public Yelp profile is passive. The Find Friends flow is ACTIVE — it asks you to connect an email account or upload contacts to match them to Yelp users, which discloses those contacts to Yelp and can surface *you* to the target as a suggested friend. Use a sock-puppet Yelp account and a burner contact list; never connect your real address book.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Yelp is a major, established review platform; profile/review data is first-party, though reviews are user-generated.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- yelp
aliases:
- Yelp Friends
tags:
- toddington
- online-communities-blogs
- yelp
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Yelp Find Friends

> Yelp as a location-habit source: a subject's public reviews map the restaurants, bars and businesses they frequent, and the Find Friends flow matches a contact (email) to a Yelp account.

## When to use
Your subject may use Yelp, and you want to (a) find their profile from a `name`/`email` and read their reviews — which are gold for patterns of life: which neighbourhoods and venues they visit, when, and with whom — or (b) use the Find Friends contact-matching to confirm an `email`/phone maps to a Yelp user. Yelp reviews often carry photos (with scenery/`geolocation` clues) and mention companions (`associate`s), making a review history a strong corroboration source for someone's routine and area.

## How to use it (`bestInteractionPattern`: web-manual)
1. **Profile first (passive):** search `site:yelp.com "<name>"` or Yelp's own user search to find `yelp.com/user_details?userid=...`. No login needed to read it.
2. On the profile, read the review list: businesses, cities, dates, ratings, and photos — build a map of frequented locations and a timeline.
3. Note review photos and text for `geolocation` clues and mentioned companions (`associate`s).
4. **Find Friends (active, optional):** sign in with a sock-puppet Yelp account at the Find Friends page and connect a *burner* email/contact list to see which entries match Yelp accounts.
5. Pivot: frequented venues + a home city feed address/geolocation work; the profile's linked info and photos feed image/social tools.

## Inputs → Outputs
- **In:** `name` or `email` (email for the Find Friends contact match)
- **Out:** `social-profile` (Yelp user page), reviewed businesses → `geolocation`/pattern-of-life, review photos, `associate`s mentioned
- **Empty/negative result looks like:** no matching Yelp user, or a profile with zero/private reviews — many people never review, so absence is weak evidence. A Find Friends "no match" only means that exact email isn't tied to a Yelp account.

## Gotchas & OpSec
- **Active feature:** connecting contacts/email uploads them to Yelp and can make you a "suggested friend" to the target — always use burner account + burner contacts.
- Reviews are self-selected and sparse for most people; treat as corroboration, not a complete movement log.
- Common names collide; confirm via photos, city, and review specifics.

## Overlaps ("do both")
- Extends the base `[[yelp]]` entry with the friend-matching angle. Pairs with people-search/social tools for the identity anchor, and with image tools for review-photo geolocation.

## Trust & verifiability
`trust: trusted` — Yelp is a mainstream, established platform and profile/review metadata is authentic first-party data. The review *content* is user-generated, so verify specific claims (a venue visit, a companion) against other sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yelp-find-friends |
| category | communities-forums |
| selectorsIn → selectorsOut | name, email → social-profile, geolocation, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
