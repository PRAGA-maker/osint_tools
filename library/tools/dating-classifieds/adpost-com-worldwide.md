---
id: adpost-com-worldwide
name: Adpost.com (Worldwide)
description: Use when you have a name/username/phone/email and want their classified ads worldwide — returns matching listings with seller contact details and location.
url: http://www.adpost.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching a long-running global classifieds site for a person's ads and the contact details attached to them.
selectorsIn:
- name
- phone
- email
selectorsOut:
- phone
- email
- address
- social-profile
status: live
pricing: free
costNote: Free to browse and search listings; posting/registration is free too. No paywall for reading ads.
opsec: passive
opsecNote: Browsing and searching public ads is passive — the seller isn't notified. Contacting a seller through the site (reply form/messaging) is active and reveals your interest; stop at reading the listing's public details unless direct contact is warranted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established global classifieds platform (since the late 1990s); listings are user-posted and unverified, so contact details are leads, not confirmed facts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Adpost classifieds
- adpost.com
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Adpost.com (Worldwide)

> A veteran worldwide classifieds site — searched in OSINT for the ads a person posted and the phone, email, and location they attached to them.

## When to use
You have a `name`, `phone`, `email`, or username and suspect the subject buys/sells or advertises online (goods, vehicles, services, personals, rentals). Classified ads often expose contact details and a rough location the person didn't put on their social profiles, and old ads can reveal past addresses, phone numbers, and interests. Adpost's global/regional coverage makes it worth a sweep alongside the mainstream classifieds.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.adpost.com and choose the relevant region/country or use the site search.
2. Search for the subject's `name`, seller handle, `phone`, or `email`; also try product/service terms you associate with them.
3. Open matching ads and read the seller's posted details: contact `phone`/`email`, city/`address` hints, other items they list (a pattern of ads builds a profile).
4. Pivot: a phone/email from an ad feeds reverse-phone/email OSINT; a location narrows people-search; a recurring seller handle feeds username search across platforms.

## Inputs → Outputs
- **In:** `name` / seller handle / `phone` / `email` / product terms
- **Out:** classified listings → `phone`, `email`, `address`/location hints, seller `social-profile`/handle
- **Empty/negative result looks like:** no listings match — the subject hasn't advertised here (try Craigslist/Gumtree/Facebook Marketplace and regional boards); a nil result is not evidence they don't advertise elsewhere.

## Gotchas & OpSec
- Human-in-the-loop: none for searching; replying to an ad is active contact — avoid unless intended.
- OpSec: passive while reading. Contact details are user-supplied and may be burner/fake — treat as leads to verify, not confirmed identity.
- Coverage and freshness vary by region; some sections may hold old or spam listings.

## Overlaps ("do both")
- Pairs with other classifieds (Craigslist, Gumtree, Marketplace) and reverse phone/email tools — Adpost catches ads the majors miss, and any contact detail found feeds straight into identity-resolution tools.

## Trust & verifiability
`trust: community` — an established but user-generated platform; listings are unverified, so corroborate any phone/email/address against independent sources before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | adpost-com-worldwide |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone, email → phone, email, address, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
