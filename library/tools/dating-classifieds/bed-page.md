---
id: bed-page
name: Bedpage
description: Use when you have a `name`, `phone`, or location and want classified/personal ads — returns ad listings with contact numbers, photos, and locality.
url: https://www.bedpage.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching a Backpage-style classifieds site (including adult/personal ads) by city and category.
selectorsIn:
- name
- phone
selectorsOut:
- phone
- image
- geolocation
status: live
pricing: free
costNote: Free to browse and search listings by city/category; posting some ads may cost, but reading is free and needs no account.
opsec: passive
opsecNote: Browsing is passive, but this is a sensitive adult-classifieds context associated with escort/trafficking investigations. Never contact an advertiser or pose as a client — that is active, unsafe, and can compromise a real safeguarding case. Use a clean browser/VPN and handle any PII with strict minimisation.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: community
trustNote: A Backpage-successor classifieds platform; ads are anonymous, unverified, and frequently use burner numbers and reused photos.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Bedpage
- bedpage.com
tags:
- classifieds
- adult-classifieds
source: metaosint
lastVerified: '2026-07-22'
enrichment: full
---

# Bedpage

> A Backpage-style classifieds site with a large adult/personals section — searched in trafficking and missing-persons work for reused phone numbers, photos, and locality tied to a subject.

## When to use
You have a `name`, `phone` number, distinctive photo, or a city and want to check classified/personal ads — a source that can matter in exploitation, trafficking, and missing-persons cases. Ads carry contact numbers, images, and a locality, so a reused `phone` or a recognizable `image` can tie a subject to a place and time. This is sensitive terrain: use it strictly to gather leads, coordinate with authorities where appropriate, and never engage advertisers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bedpage.com and select the city/region, then the relevant category.
2. Browse or use a scoped web search (`site:bedpage.com "<phone or name>"`) to hunt a specific number, name, or phrase.
3. Read listings for contact `phone`, photos, ad text, and locality; note recurring numbers/photos across ads and cities.
4. Capture evidence (screenshots) immediately — ads rotate and expire.
5. Do NOT contact advertisers. Pivot: a `phone` feeds caller-ID/breach and reverse-phone tools; a photo feeds reverse-image/face search; recurring numbers map a network to hand to investigators.

## Inputs → Outputs
- **In:** `name` / `phone` / location
- **Out:** ad listings with contact `phone`, `image`s, and `geolocation` (city/area)
- **Empty/negative result looks like:** no ads match the number/name/city — expected, since content is transient and heavily churned. Absence is weak evidence; re-check over time and across nearby cities.

## Gotchas & OpSec
- **Legal/ethical gate:** adult-classifieds tied to potential exploitation — operate under strict minimisation, preserve evidence properly, and involve law enforcement/NGOs rather than acting alone.
- Numbers are usually burners and photos are frequently stolen/reused; treat everything as a lead needing corroboration.
- Never message or "book" an advertiser; that endangers you and any victim and can taint a case.

## Overlaps ("do both")
- Pairs with reverse-phone/caller-ID tools and reverse-image/face search — a phone or photo from an ad becomes the pivot those tools resolve to an identity or to other ads across sites.

## Trust & verifiability
`trust: community` — an anonymous, unverified classifieds platform; ads are self-posted with burner contacts and reused media, so every detail is a lead to corroborate, never a fact on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bed-page |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone → phone, image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
