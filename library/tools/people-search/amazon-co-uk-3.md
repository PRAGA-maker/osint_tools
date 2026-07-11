---
id: amazon-co-uk-3
name: Amazon.co.uk Wish Lists & Registries
description: Use when you have a `name` and want a UK subject's public Amazon wish list / gift registry — returns a display name, wanted items and sometimes a shipping town or delivery address.
url: https://www.amazon.co.uk/registries
category: people-search
path:
- people-search
bestFor: Finding a person's public Amazon wish list or baby/wedding registry to reveal interests, location and occasionally a shipping address.
selectorsIn:
- name
selectorsOut:
- address
- associate
- social-profile
status: live
pricing: free
costNote: Free to search; an Amazon account (any account) makes the registry/wish-list finder easier to use.
opsec: passive
opsecNote: Searching the public wish-list/registry finder does not notify the subject. However, buying an item ships it to them and reveals their address to you while alerting them to a gift — do NOT purchase; stop at the public listing. Browse in a sock-puppet Amazon session so the recommendation engine and order history stay clean.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Amazon feature; listings are self-published by the subject, so the display name and items are genuine but user-supplied (aliases/nicknames common).
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Amazon UK wish list search
- Amazon registry finder
tags:
- peoplesearch
- People Search Sites
- wishlist
- registry
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Amazon.co.uk Wish Lists & Registries

> Amazon's public wish-list and gift-registry finder, used as a soft-target people search: a subject's own published list of wanted items, interests and (sometimes) delivery location.

## When to use
You have a `name` (and ideally a town or email the person uses) and want lifestyle, interest and location signals. Public Amazon wish lists and baby/wedding registries are self-published, searchable, and frequently reveal a real name, a town, hobbies, and occasionally a partial or full shipping address plus co-registrants (`associate`). Useful for confirming an alias belongs to a real person and for enrichment when other people-search sites come up empty.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.amazon.co.uk/registries (or the "Find a List or Registry" search).
2. Search by the subject's `name` or email address.
3. Open matching lists — note the display name, item set (interests/kids' ages/wedding date), and any location or co-registrant shown.
4. Do NOT buy anything: purchasing ships to the subject and tips them off. Read-only.
5. Pivot: interests/town feed social-profile hunting; a co-registrant name feeds `associate` mapping; the same wish-list nickname can be searched across other platforms as a `username`.

## Inputs → Outputs
- **In:** `name` (or the email the subject registered with)
- **Out:** display `name`/nickname, interests, town or partial shipping `address`, co-registrant `associate`, links usable as `social-profile` leads
- **Empty/negative result looks like:** no lists found, or only unrelated same-name hits — most people either have no public list or keep it private, so absence is common and not meaningful.

## Gotchas & OpSec
- The vast majority of wish lists are private or third-party-address-hidden; a full delivery address is the exception, not the rule.
- Display names are user-chosen — a nickname/alias, not necessarily the legal name.
- Never add an item to a cart or purchase — that is active and exposes both parties.

## Overlaps ("do both")
- Pairs with mainstream people-search — Amazon lists surface interests and nicknames a records-based search won't, while records give the address/age the list omits.

## Trust & verifiability
`trust: trusted` — it is Amazon's own feature, so the data is genuinely user-published; reliability is limited only by the fact that users choose their own display names and choose what to make public.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazon-co-uk-3 |
| category | people-search |
| selectorsIn → selectorsOut | name → address, associate, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
