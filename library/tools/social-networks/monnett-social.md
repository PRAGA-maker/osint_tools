---
id: monnett-social
name: Monnett
description: Use when you have a `username` or `name` and suspect the subject is on Monnett, a small privacy-focused European social app — returns a social-profile and name if they have an account.
url: https://monnett.social/
category: social-networks
path:
- social-networks
bestFor: Checking whether a subject has a profile on Monnett, a niche, ad-free, EU-made friends network (app-only).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to use; the whole pitch is "no AI, no ads, made in Europe." Operated by Monnet Social SA. It is app-only (iOS/Android), so meaningful search generally requires installing the app and creating an account.
opsec: active
opsecNote: There is no public web search — to look anyone up you must install the app and register, which ties an identity/device to the platform. Use a sock-puppet account on a clean device/number; the network is friend-oriented, so avoid sending connection requests to the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: A real, growing EU social app (self-reported 90k+ users) run by Monnet Social SA. Small and privacy-walled, so as an OSINT source it's low-yield and hard to query without an account.
missingPersonsRelevance: high
coverage:
- eu
- global
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
relatedTools:
- facebook
aliases:
- monnett.social
- Monnet Social
tags:
- gsocialmedia
- General Social Media Sites
- europe
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Monnett

> A small, ad-free, privacy-first European social app — a low-yield but occasionally decisive place to check when mainstream networks come up empty for an EU subject.

## When to use
Your subject is European and privacy-conscious, mainstream platforms show nothing, and you're doing exhaustive coverage. Monnett markets itself to people leaving Big Tech ("no AI, no ads, made in Europe"), so a subject who has abandoned Facebook/Instagram might surface here. Realistically this is a completeness check, not a primary lead source.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install the Monnett app (iOS App Store / Google Play) on a sock-puppet device or profile.
2. Register a throwaway account (there is no public web-based people search).
3. Use in-app search for the subject's `username` or `name`.
4. If found, note the profile, display `name`, and any public friends/content — do NOT send a connection request.
5. Pivot: a reused username feeds cross-platform enumeration; confirmed presence corroborates the subject is EU-based and privacy-aware.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile`, `name`
- **Empty/negative result looks like:** no in-app match — given the small user base (~90k), absence is common and weak evidence; don't over-read it.

## Gotchas & OpSec
- Human-in-the-loop: account-login is effectively mandatory — everything is behind the app; there's no scrape-friendly web front.
- Small network: low base rate of hits, so treat a miss as inconclusive.
- OpSec: active — installing/registering ties you to the platform; use a clean device and throwaway credentials.

## Overlaps ("do both")
- Pairs with mainstream Facebook/Instagram/Mastodon checks — Monnett only matters after those, as a tail-coverage source.
- If a username matches, run it through a username-enumeration sweep to link the same handle elsewhere.

## Trust & verifiability
`trust: community` — a legitimate operating company (Monnet Social SA), but a small, closed app; any profile you find is a self-declared account to corroborate, and absence proves little.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | monnett-social |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
