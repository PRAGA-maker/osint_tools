---
id: unavatar
name: Unavatar
description: Use when you have an `email`, `username`, or `domain` and want the associated avatar/profile picture pulled from across platforms — returns the person's `image` (and hints which service hosts it) to feed into reverse-image/face search.
url: https://unavatar.io/john
category: username
path:
- username
bestFor: Retrieving a person's avatar/profile photo from an email, username, or domain by aggregating many platforms through one URL/API.
selectorsIn:
- email
- username
- domain
selectorsOut:
- image
- social-profile
status: live
pricing: freemium
costNote: Free to use by URL (rate-limited); an optional API key / paid tier raises limits for heavy/automated use. Open-source project, self-hostable.
opsec: passive
opsecNote: Unavatar's server fetches the avatar from the underlying providers, so the target's platforms see Unavatar's IP, not yours — a useful buffer. Passive. You are still disclosing the selector (email/username) to a third-party service; use a research context for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: A popular open-source avatar-aggregation API (widely used, source on GitHub). It returns real avatars pulled live from providers like Gravatar, GitHub, social platforms; if none is found it can fall back to a generated placeholder, so confirm you got a real hit.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- imagewhisperer-org
- inflact-com-2
aliases:
- unavatar.io
- universal avatar API
tags:
- Nicknames
- avatar
- profile-image
source: cyb-detective
lastVerified: '2026-07-15'
enrichment: full
---

# Unavatar

> One URL that turns an email, username, or domain into a profile picture — the fastest way to get a face to reverse-search from nothing but a handle.

## When to use
You have an `email`, `username`, or `domain` for a subject and want their avatar/profile photo without manually checking each platform. Unavatar queries many providers (Gravatar, GitHub, and social networks) behind a single URL and returns whatever avatar it finds — giving you a `face`/`image` you can then run through reverse-image and face search, or use to visually confirm an account belongs to your subject.

## How to use it (`bestInteractionPattern`: api)
1. Build the URL: `https://unavatar.io/<selector>` — e.g. `https://unavatar.io/john@example.com` (email), `https://unavatar.io/github/johndoe` (a specific provider), or `https://unavatar.io/example.com` (domain).
2. Open it in a browser or fetch it programmatically; it 302s/serves the resolved avatar image.
3. Inspect the returned image. Add `?fallback=false` to suppress the generated placeholder so a *miss* returns nothing instead of a fake default — this tells you whether the avatar is real.
4. Save the image.
5. Pivot: run the avatar through `[[imagewhisperer-org]]` (authenticity) then a reverse-image/face engine; a strong avatar also corroborates that an account maps to your subject.

## Inputs → Outputs
- **In:** `email`, `username` (optionally provider-scoped), or `domain`
- **Out:** an avatar `image`, and by which provider resolved it, a hint at the hosting `social-profile`
- **Empty/negative result looks like:** with `fallback=false`, no avatar (404/blank) means none was found; without it, you get a generated placeholder that can be mistaken for a real hit — always disable fallback when you care whether an avatar truly exists.

## Gotchas & OpSec
- **Watch the fallback placeholder** — by default a miss returns an auto-generated image; use `?fallback=false` so absence is unambiguous.
- Coverage depends on the person having a public avatar on a supported provider; a null result is not proof of nonexistence.
- OpSec: **passive**, and Unavatar's server shields your IP from the providers — but you still reveal the selector to Unavatar; use a research setup for sensitive cases (or self-host, since it is open-source).

## Overlaps ("do both")
- Pairs with `[[inflact-com-2]]` (full Instagram profile media when you already have the handle) and `[[imagewhisperer-org]]` (verify the avatar is a real photo before building leads).

## Trust & verifiability
`trust: community` — an established open-source project. Avatars are pulled live from real providers, so hits are genuine; the caveat is the default placeholder fallback, which you should disable to avoid false positives.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unavatar |
| category | username |
| selectorsIn → selectorsOut | email, username, domain → image, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
