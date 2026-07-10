---
id: avatar-api
name: Avatar API
description: Use when you have an `email` and want the name, profile photo, and linked public profiles tied to it across 20+ platforms — returns name, image, and social-profile links.
url: https://avatarapi.com/
category: email
path:
- email
bestFor: Resolving an email to a display name, avatar image, and source platform in a single API call.
selectorsIn:
- email
selectorsOut:
- name
- image
- social-profile
status: live
pricing: freemium
costNote: 100 free API calls for new accounts (no card). Paid from ~$10 per 1,000 requests. Registration + API key required even for the free tier.
opsec: passive
opsecNote: Queries go to avatarapi.com, not to the target's providers, so the subject is not alerted. But you are disclosing the target email to a third-party US service that may log it — use for lookups you are comfortable logging.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: unverified
trustNote: Commercial third-party aggregator; sources include Gravatar, GitHub, and other public directories. Data quality and freshness are not independently verified.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools:
- gravatar
- epieos
aliases:
- avatarapi.com
tags:
- Emails
- email-to-name
- avatar-lookup
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Avatar API

> A commercial API that turns an email address into a name, avatar image, and links to the public profiles it is registered on across 20+ platforms.

## When to use
You have an `email` and want the fastest possible enrichment to a real name and face: the API returns the display name, profile photo, and which platform (Gravatar, GitHub, LinkedIn, Google, Microsoft, etc.) the data came from. Good as a first, low-friction step to attach an identity and photo to an otherwise bare address.

## How to use it (`bestInteractionPattern`: api)
1. Register at https://avatarapi.com/ and get your API key (100 free calls).
2. POST the target `email` (plus your key) to the documented endpoint.
3. Read the JSON: `Name`, image URL, and the source platform for the avatar/profile.
4. Pivot: the returned photo feeds face/reverse-image search; the source platform tells you which per-service tool to run next; the name feeds people-search.

## Inputs → Outputs
- **In:** `email`
- **Out:** `name`, `image` (avatar URL), `social-profile` (source platform)
- **Empty/negative result looks like:** a default/placeholder avatar or an empty name field means no public profile matched — the address may still be real but simply has no linked avatar.

## Gotchas & OpSec
- Human-in-the-loop: an API key and registration are mandatory; free tier is capped at 100 calls.
- OpSec: **passive** toward the target (no alert), but you hand the email to a third party that may retain it. Avoid for the most sensitive subjects.
- The avatar is only as fresh as the source (often Gravatar); an old photo may not reflect current appearance.

## Overlaps ("do both")
- Pairs with `[[gravatar]]` — Gravatar is the largest single source Avatar API aggregates; check it directly to confirm and grab full-res images.
- Pairs with `[[epieos]]` — Epieos maps an email to Google account details and other services; run both for wider platform coverage.

## Trust & verifiability
`trust: unverified` — a commercial aggregator with no public accuracy audit; treat a hit as a lead and confirm the name/photo against the named source platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | avatar-api |
| category | email |
| selectorsIn → selectorsOut | email → name, image, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
