---
id: angieslist-north-america
name: Angi (Angie's List)
description: Use when you have a contractor/business `name` in North America and want reviews and business details — returns customer reviews, business `address`/`phone`, and service history.
url: http://www.angieslist.com
category: search-engines
path:
- search-engines
bestFor: Finding reviews and contact/location details for a North American home-services business or tradesperson.
selectorsIn:
- name
- employer-org
selectorsOut:
- address
- phone
- social-profile
status: live
pricing: freemium
costNote: Free to search businesses and read reviews (redirects to angi.com); some features and quotes require a free account.
opsec: passive
opsecNote: Searching businesses and reading reviews is passive and reveals nothing to any subject. Requesting a quote or contacting a pro is active — use a puppet identity if you do.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Angi (formerly Angie's List) is an established home-services marketplace; reviews are user-generated and can be filtered/curated, so weigh them as leads, not proof.
missingPersonsRelevance: medium
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Angie's List
- Angi
- angieslist.com
tags:
- reviews
- business-directory
- home-services
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Angi (Angie's List)

> A North American home-services marketplace (formerly Angie's List, now Angi): reviews and business details for contractors and tradespeople — a way to attach a business name to reviews, a location, and contact info.

## When to use
You have the `name` of a home-services business or an individual tradesperson (a contractor on an invoice, a subject who runs a service business) and want reviews, a business address, phone, and service categories. Angi's listings can corroborate that a business is real and operating, place it geographically, and — through reviews naming the owner or describing work — add context and leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to angi.com (angieslist.com redirects there) and search the business `name` or service + location.
2. Open a matching listing: read the business profile (address, phone, categories, years in business) and customer reviews.
3. Note review details that name people, dates, or locations; check the business's claimed service area.
4. Pivot: a business `address`/`phone` feeds registry, map, and phone-OSINT; an owner name in reviews feeds people-search.

## Inputs → Outputs
- **In:** business/tradesperson `name` or `employer-org` (+ location helps).
- **Out:** reviews, business `address`, `phone`, service categories, possible owner/`social-profile` leads.
- **Empty/negative result looks like:** no listing — the business isn't on Angi (many aren't; it's opt-in/US-Canada). Absence says nothing about whether the business exists.

## Gotchas & OpSec
- Reviews are user-generated and can be curated or gamed — treat them as leads, not verified fact.
- US/Canada home-services focus; irrelevant outside that domain/region.
- Some features nudge you to create an account or request quotes — stay in read-only mode unless you need to, and use a puppet.

## Overlaps ("do both")
- Corroborate the business against state registries, BBB, and map/satellite tools; cross-check reviews on Google/Yelp for a fuller picture.

## Trust & verifiability
`trust: community` — an established marketplace, but listings and reviews are self/user-supplied. Use it to locate and contextualise a business; verify address, ownership, and licensing against authoritative records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | angieslist-north-america |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → address, phone, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
