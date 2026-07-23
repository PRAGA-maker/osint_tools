---
id: facebook-applications-khalil-shreateh
name: Facebook Applications (Khalil Shreateh)
description: Use when you have a Facebook `social-profile` and want its numeric ID or full-size profile photo — a page of small Facebook utilities; the ID/photo viewers are useful, the automation bots are mostly ToS-violating and broken.
url: https://khalil-shreateh.com/khalil.shtml/social_applications/facebook-applications/
category: social-networks
path:
- social-networks
bestFor: Extracting a Facebook profile's numeric UID and viewing full-size profile/cover photos; other utilities on the page are largely defunct.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free web utilities; no account for the simple viewers, though some tools ask you to connect your own Facebook (avoid).
opsec: passive
opsecNote: The ID and photo viewers just resolve public Facebook data, which is passive. Do NOT use the automation bots (auto-like, auto-comment, group posters) — they violate Facebook's terms, can get an account banned, and require granting the site access to your Facebook.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A personal site of assorted, largely dated Facebook utilities; the useful ones are simple lookups, but the page is not maintained to current Facebook APIs, so expect breakage.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- khalil-shreateh-social-applications
aliases:
- Khalil Shreateh Facebook tools
tags:
- facebook
- automation
source: osintambition-social
lastVerified: '2026-07-23'
enrichment: full
---

# Facebook Applications (Khalil Shreateh)

> A grab-bag of small Facebook utilities — worth it for the numeric-ID and full-size-photo viewers; ignore the account-automation bots, which are ToS-violating and mostly broken.

## When to use
You have a Facebook `social-profile` (a vanity URL or page) and need its **numeric UID** — the stable identifier that survives username changes and unlocks graph-style pivots — or you want to see a **full-resolution profile/cover photo** for reverse-image search. Those two lookups are the reason to visit. The page also hosts auto-like/auto-comment/group-poster bots; those are not investigative tools and should be avoided.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the page and pick a **viewer** utility (Facebook ID Viewer / Profile Picture Viewer) — not an automation bot.
2. Paste the target's Facebook profile URL or username.
3. Read the output: the numeric UID, or a direct link to the full-size `image`.
4. Pivot: use the numeric ID with other Facebook OSINT techniques; run the full-size photo through reverse-image search.
5. If any tool asks you to log in with or connect your Facebook, stop — a lookup shouldn't need your account.

## Inputs → Outputs
- **In:** a Facebook `social-profile` (URL/username)
- **Out:** numeric UID (a stable `social-profile` identifier), full-size profile/cover `image`
- **Empty/negative result looks like:** an error or blank — the tool has broken against current Facebook, or the profile is private/removed; try a dedicated, maintained Facebook-ID resolver instead.

## Gotchas & OpSec
- **Avoid the automation bots** — auto-like/comment/post violate Facebook's terms and can burn an account; only the read-only viewers are appropriate.
- The site tracks current Facebook poorly; utilities break without notice — verify results and have a maintained alternative.
- Never grant the site access to a real Facebook account.

## Overlaps ("do both")
- Part of the same author's [[khalil-shreateh-social-applications]] collection; for the numeric-ID job specifically, a purpose-built, maintained Facebook-ID lookup is more reliable — use this as a fallback.

## Trust & verifiability
`trust: unverified` — an unmaintained personal utility page; the simple viewers can help, but confirm every result and prefer maintained tools for anything you'll rely on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-applications-khalil-shreateh |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
