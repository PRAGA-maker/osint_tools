---
id: linkedin-network-and-job-finder-mobile-ios
name: LinkedIn (iOS App)
description: Use when you have a `name`/`employer-org`/`email` and want the official LinkedIn app's authenticated view of a subject's professional graph — returns `social-profile`, `employer-org`, `associate` links.
url: https://apps.apple.com/us/app/linkedin-network-job-finder/id288429040
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Mobile, authenticated access to LinkedIn's people/company graph for professional-network mapping.
selectorsIn:
- name
- employer-org
- email
selectorsOut:
- social-profile
- employer-org
- associate
status: live
pricing: freemium
costNote: The app is free; the underlying LinkedIn account is free to create. Premium (recruiter/sales) tiers ($30–$120/mo) unlock deeper search and who-viewed data, but core profile/company browsing is free.
opsec: active
opsecNote: LinkedIn is heavily attributed — viewing a profile can notify the target ("who viewed your profile"), and the app is tied to YOUR logged-in identity. Investigate only from a maintained sock-puppet account with private/anonymous browsing mode enabled in settings; never use your real account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: trusted
trustNote: The official first-party LinkedIn Corporation app (App Store ID 288429040), actively updated; the data is LinkedIn's own, so authoritative for what users self-publish.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- LinkedIn Network and Job Finder
- LinkedIn iOS
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- professional-network
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# LinkedIn (iOS App)

> The official LinkedIn app — mobile, authenticated access to the largest professional-identity graph, useful for employer, colleague, and career-history pivots.

## When to use
You have a `name`, `employer-org`, or `email` and want the professional side of a subject: current/past employers, job titles, colleagues (`associate`), education, and location cues. LinkedIn is a primary source for career footprint. The mobile app matters when you want geo/context features or are working from a phone-based persona setup, but it is functionally the same graph as the web tools.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install from the App Store (ID 288429040) on a sock-puppet device/account. In Settings → Visibility, set profile-viewing to **private/anonymous mode** BEFORE searching.
2. Search by `name` (+ company/location to disambiguate) or paste a known `email` to find a matching profile.
3. Read the profile: employer, title, tenure, location, education, and the "People also viewed"/connections for `associate` leads.
4. Pivot: a confirmed employer feeds business-registry tools; a colleague list feeds network mapping; the profile URL feeds `[[linkedin-x-ray-search]]` and username tooling.

## Inputs → Outputs
- **In:** `name` / `employer-org` / `email`
- **Out:** `social-profile` (LinkedIn), `employer-org`, `associate` connections, career history
- **Empty/negative result looks like:** no matching profile, or a bare "LinkedIn Member" placeholder — meaning the person isn't on LinkedIn or has restricted visibility, not that they don't exist.

## Gotchas & OpSec
- **Active/attributed:** without private mode, profile views notify the target. Enable anonymous browsing and use a sock puppet, always.
- Free search is deliberately throttled and de-ranks results for non-connections; deep enumeration pushes you toward the paid tiers or triggers anti-scraping limits.
- Self-reported data — titles and dates are subject exaggeration; corroborate against registries.

## Overlaps ("do both")
- Pairs with `[[linkedin-x-ray-search]]` / `[[linkedin-search-engine]]` (Google-dork LinkedIn without logging in) and `[[linkedindumper]]` — use x-ray for passive discovery, then this app for the authenticated detail view.

## Trust & verifiability
`trust: trusted` — the genuine first-party LinkedIn app; the platform is authoritative for self-published professional data, with the usual caveat that users write their own profiles.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkedin-network-and-job-finder-mobile-ios |
