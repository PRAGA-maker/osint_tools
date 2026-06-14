---
id: ghunt
name: GHunt
description: Use when you have a Gmail address or Google account ID and need to enumerate the linked Google services, public photos, reviews, and account metadata.
url: https://github.com/mxrch/GHunt
category: email
path:
- email
- email-search
bestFor: Investigating a Google/Gmail account — maps an email to its GAIA ID, public Google services, and account creation/activity signals.
input: Gmail address or GAIA ID
output: GAIA ID, profile photo, Maps reviews, public Google Photos, calendar/services presence
selectorsIn:
- email
selectorsOut:
- name
- social-profile
- image
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (CLI / Python).
opsec: active
opsecNote: Requires authenticating with a real (preferably sock-puppet) Google account whose cookies GHunt uses; queries run under that account, so Google can associate the activity with it. Use a burner Google account, never your own.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: GHunt by mxrch is a widely used, actively maintained open-source Google-OSINT project; capabilities track what Google's people/services endpoints expose and have shifted over time as Google tightens APIs.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- ghintel-secrets-ninja
- gmail
aliases: []
tags:
- email
- email-search
- google
source: arf-seed
lastVerified: ''
enrichment: full
---

# GHunt

> Open-source CLI that turns a Gmail address into a profile of the underlying Google account — GAIA ID, public photos, Maps reviews, and service presence.

## When to use
You have a Gmail `email` (or a GAIA ID) for a missing person or associate and want to learn what is linked to that Google account: a profile `image`, public Google Maps reviews (which can reveal `geolocation` patterns), public Google Photos albums, and whether services like Calendar/Chat are active. Strong pivot for confirming an account is real and tying it to a person.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install ghunt` (or clone the repo) and run `ghunt login` to authenticate with a **burner** Google account (GHunt stores its cookies).
2. Run `ghunt email target@gmail.com`.
3. Read the output: GAIA ID, display `name`, profile `image`, last-edit timestamps, Maps reviews, public Photos, and which Google services the account uses.
4. Pivot: use GAIA ID for deeper lookups; map review locations for `geolocation`; cross-check the profile photo with face/reverse-image tools.

## Inputs → Outputs
- **In:** Gmail `email` (or GAIA ID)
- **Out:** `name`, profile `image`, `social-profile`/service presence, `geolocation` (from public reviews/photos), account `metadata-exif` (IDs, timestamps)
- **Empty/negative result looks like:** "account not found" (address is not a Google account or is hidden), or a valid account with everything private — only the GAIA ID and minimal metadata return.

## Gotchas & OpSec
- ACTIVE: queries run under your authenticated Google account. Always use a dedicated burner — Google can correlate the lookups with that account, and aggressive use risks the burner being flagged.
- Capabilities drift: Google periodically removes endpoints, so some fields may stop returning. Check the repo for the current feature set and breaking changes.
- Human-in-the-loop: one-time `ghunt login` (cookie/account auth) is required.

## Overlaps ("do both")
- Complement with `[[ghintel-secrets-ninja]]` for GitHub identities (different platform) and treat `[[gmail]]` as the source address you feed in.

## Trust & verifiability
`trust: community` — popular, actively maintained open-source project (mxrch); outputs come from Google's own public endpoints and are inspectable in the CLI results, though feature coverage changes as Google tightens access.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghunt |
| category | email |
| selectorsIn → selectorsOut | email → name, social-profile, image, geolocation, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes |
