---
id: onlyfinder
name: OnlyFinder
description: Use when you have a `username`, `name`, `geolocation`, or `face` and want to find a matching OnlyFans creator — returns creator `social-profile`s and handles.
url: https://onlyfinder.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Locating an OnlyFans creator by username, display name, location, or (paid) face image.
selectorsIn:
- username
- name
- geolocation
- face
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free text/username/location search; face-recognition ("search by image") and some advanced features are behind a paid tier.
opsec: passive
opsecNote: "Searching OnlyFinder queries its own index of public OnlyFans profile data, so you don't interact with the creator or OnlyFans itself — passive. OnlyFinder logs your searches; if you upload a `face` image, you disclose it to their service, so use a sock-puppet account and never upload a private/sensitive image of a person you're not authorized to search for."
humanInLoop: false
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party OnlyFans search index (not affiliated with OnlyFans); matches — especially face-based ones — are probabilistic leads that must be confirmed against the actual profile.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- onlyfinder-com
aliases:
- OnlyFinder
- onlyfinder.com
tags:
- onlyfans
- adult-platform-search
- username-search
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# OnlyFinder

> A search engine over public OnlyFans creator data: find a profile by username, display name, location, or — on the paid tier — by uploading a face.

## When to use
You are checking whether a `username`, `name`, or `face` maps to an OnlyFans presence, or enumerating creators in a `geolocation`. Useful for corroborating that a handle a subject uses extends to adult platforms, or for locating a specific creator profile from partial info. Note the sensitivity: this concerns adult content and real people, so it demands a clear investigative justification. Its stub relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onlyfinder.com/ in a sock-puppet browser.
2. Search by `username`/`name` (free), or filter by location (`geolocation`) to enumerate nearby creators.
3. For image search, upload a `face` (paid feature) to get probabilistic profile matches.
4. Read results: candidate creator `social-profile`s/handles with previews.
5. Confirm any match by opening the actual OnlyFans profile and cross-referencing other known selectors — do not treat a face match as identification on its own.

## Inputs → Outputs
- **In:** `username`, `name`, `geolocation`, or `face` (image)
- **Out:** OnlyFans creator `social-profile`s/handles
- **Empty/negative result looks like:** no matches — the person likely has no indexed OnlyFans profile under that selector, OnlyFinder hasn't indexed it, or a face simply doesn't match; absence is not proof of nonexistence.

## Gotchas & OpSec
- **Sensitive/legal:** this surfaces real individuals on an adult platform — have a legitimate basis, and be aware face-matching a private image raises consent and legal issues.
- Face search is paywalled and probabilistic; a "match" is a lead to verify, never a positive ID.
- It's an unofficial index, so coverage is partial and can lag or contain stale/duplicate entries.

## Overlaps ("do both")
- Pairs with its sibling [[onlyfinder-com]] and general username/face tools — cross-check a handle across mainstream platforms and reverse-image tools before concluding two profiles are the same person.

## Trust & verifiability
`trust: community` — an unaffiliated third-party index; every match (especially by face or location) is probabilistic, so confirm against the live OnlyFans profile and independent selectors before relying on it.
