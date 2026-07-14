---
id: amazon-co-uk
name: Amazon Wedding & Gift Registry Search
description: Use when you have a `name` and want to find their public Amazon wedding/gift registry — returns partner/associate names, approximate location, event date, and interests from the wishlist.
url: https://www.amazon.co.uk/wedding/search
category: public-records
path:
- public-records
bestFor: Finding a person's public Amazon wedding/gift registry to reveal a partner, rough location, event date, and interests.
selectorsIn:
- name
selectorsOut:
- associate
- name
- geolocation
- social-profile
status: live
pricing: free
costNote: Free to search; an Amazon account may be prompted to view some registry details but basic registry search is open.
opsec: passive
opsecNote: Searching public registries is passive and does not notify the registrant. Avoid purchasing or messaging through a registry, which would expose your identity. Prefer a clean/sock-puppet Amazon session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Amazon; registry contents are self-published by the registrant, so the data is genuine but user-supplied.
missingPersonsRelevance: medium
coverage:
- uk
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Amazon wedding registry search
- Amazon gift list search
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- registry
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Amazon Wedding & Gift Registry Search

> Amazon's public registry search as an OSINT source: a name can surface a wedding/gift registry that leaks a partner, an approximate location, an event date, and the couple's interests.

## When to use
You have a subject's `name` and want relationship, location, or lifestyle leads. Public Amazon wedding and gift registries are self-published and searchable by registrant name; a hit can reveal the partner's `name` (`associate`), an approximate delivery city/region (`geolocation`), the wedding/event date, and — via the wishlist items — hobbies and interests (`social-profile`). It's an underused corroboration source that ties a person to a partner and a place. (Equivalent registries exist on amazon.com and other locales.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.amazon.co.uk/wedding/search (and the same path on amazon.com for US subjects).
2. Search by the subject's first and/or last `name`; wedding registries are typically listed under both partners' names and an event date.
3. Open a matching registry and read: both partners' names, event date, shipping city/region if shown, and the wishlist items.
4. Pivot: the partner is an `associate` lead; the location narrows people-search; wishlist interests corroborate identity or provide rapport/context. Do **not** buy items or message through the registry.

## Inputs → Outputs
- **In:** `name`
- **Out:** partner/registrant `name`s (`associate`), approximate `geolocation`, event date, interests (`social-profile`)
- **Empty/negative result looks like:** no registry found — the subject may never have made one, kept it private, or registered on a different platform/locale (try amazon.com, Zola, The Knot).

## Gotchas & OpSec
- Registry data is **self-published** and may be partial, nicknamed, or private — absence proves nothing and details need corroboration.
- Search the correct locale: UK subjects on amazon.co.uk, US on amazon.com, etc.
- **OpSec:** browsing is passive; purchasing or messaging via the registry would reveal you — never do so from an attributable account.

## Overlaps ("do both")
- Do both with dedicated wedding-registry sites (Zola, The Knot, John Lewis) and social platforms — couples often register in multiple places, and each leaks slightly different partner/location/date detail.

## Trust & verifiability
`trust: trusted` — the platform is Amazon (genuine, first-party hosting), but the registry *content* is user-supplied, so treat names/locations as leads to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazon-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, name, geolocation, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
