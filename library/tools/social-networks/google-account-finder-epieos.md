---
id: google-account-finder-epieos
name: Google Account Finder (EPIEOS)
description: Use when you have an `email` (Gmail) or `phone` and want the linked Google account's profile photo, public Maps reviews/photos, and which services the address is registered on — returns a Google profile plus a social-footprint map.
url: https://tools.epieos.com/google-account.php
category: social-networks
path:
- social-networks
bestFor: Turning a Gmail/phone into a Google profile (photo, Maps activity) and a map of where the address is registered.
selectorsIn:
- email
- phone
selectorsOut:
- social-profile
- name
- image
- geolocation
status: live
pricing: freemium
costNote: The core email/phone lookup (Google account + Maps + service checks) is free with no login. Epieos also sells paid Holehe-style deep reports/credits for heavier use.
opsec: passive
opsecNote: Passive — Epieos queries Google's public account/Maps data server-side; you never contact the subject and they get no notification. Your query is processed on Epieos's servers, so use a sock-puppet if you want to avoid the operator associating it with you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Epieos is a widely-trusted, Bellingcat-listed email/phone OSINT service; results are derived from Google's own public data, so the Google-account signal is reliable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Epieos Google account finder
- tools.epieos.com
tags:
- bellingcat-toolkit
- other-platforms
- email-osint
source: bellingcat-toolkit
lastVerified: '2026-07-10'
enrichment: full
---

# Google Account Finder (EPIEOS)

> Epieos's email/phone lookup: feed it a Gmail address (or phone) and it reveals the linked Google account — profile photo, public Google Maps reviews and photos — plus checks which other services the address is registered on.

## When to use
You have an `email` (especially a Gmail) or a `phone` and want to expand it into identity: a real name and photo from the Google profile, plus location intelligence from the subject's public Google Maps reviews (which places they've visited/rated). This is one of the highest-yield email pivots — a Gmail often leaks a face and a pattern of visited locations, and the service-registration checks show where else the address is used.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tools.epieos.com/google-account.php (redirects into the Epieos app at epieos.com).
2. Enter the `email` (or switch to the phone lookup and enter a `phone` in international format).
3. Read the output:
   - Google account: display `name`, profile `image`, and public **Google Maps reviews/photos** (each tied to a place = a `geolocation` lead).
   - Service checks: a list of platforms where the email/phone is registered (`social-profile` footprint).
4. Pivot: the Maps reviews place the subject at specific locations/times; the profile photo feeds face search (`[[pimeyes]]`); registered services feed account-specific OSINT.

## Inputs → Outputs
- **In:** `email` (Gmail best) or `phone`
- **Out:** Google display `name`, profile `image`, public Maps reviews/photos (`geolocation`), list of services the address is registered on (`social-profile`)
- **Empty/negative result looks like:** "no Google account found" (address isn't a Google account, or the profile is locked down) and few/no service hits — treat as thin footprint, not proof of no accounts.

## Gotchas & OpSec
- Google Maps leakage depends on the subject's privacy settings; many accounts show a name/photo but no reviews.
- Non-Gmail addresses can still be Google accounts — try them too.
- The service-registration checks (Holehe-style) can false-positive/negative as sites change; corroborate.
- Passive and login-free for the core lookup; heavy/automated use points toward Epieos's paid tier.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` (Microsoft-account oracle) — Epieos covers the Google/Gmail side; account.live.com covers Microsoft.
- Feed the profile photo into `[[pimeyes]]`/`[[face-recognition]]`; feed Maps locations into geolocation work.

## Trust & verifiability
`trust: trusted` — Epieos is an established, Bellingcat-referenced OSINT service and the Google-account data comes straight from Google's public surfaces, so the core signal (does this address map to a Google account, with this name/photo) is dependable. The auxiliary service-check results are best treated as leads to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-account-finder-epieos |
| category | social-networks |
| selectorsIn → selectorsOut | email, phone → social-profile, name, image, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
