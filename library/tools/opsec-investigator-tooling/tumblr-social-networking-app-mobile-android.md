---
id: tumblr-social-networking-app-mobile-android
name: Tumblr (Android App)
description: Use when you have a `username`/keyword and want to explore a subject's Tumblr blog, tags, and reblog network — returns `social-profile`, `associate`, and interest/content leads.
url: https://play.google.com/store/apps/details?id=com.tumblr
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Mobile, authenticated browsing of Tumblr blogs, tags, and reblog chains for a handle or interest community.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free app and free account; no payment to browse public blogs.
opsec: active
opsecNote: Following, liking, or messaging from the app is attributed to your account and notifies the blog owner; even viewing can leave traces via Tumblr's activity features. Use a sock-puppet account, and note some NSFW-flagged blogs require being logged in to view at all.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: trusted
trustNote: The official first-party Tumblr app (com.tumblr); the data is Tumblr's own, authoritative for what users post, though blogs are pseudonymous by design.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Tumblr app
- com.tumblr
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- microblogging
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Tumblr (Android App)

> The official Tumblr app — mobile access to a subject's blog, tags, and reblog network on a pseudonymous microblogging platform rich in interest and community signal.

## When to use
You have a Tumblr `username` (or a name/handle to search) and want the subject's blog content, interests, tag usage, and the reblog/follow network that links them to others (`associate`). Tumblr is pseudonymous but people leak identity through cross-posted handles, personal photos, and tightly-knit fandom/community circles — useful for interest profiling and network mapping.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install the app (com.tumblr) and sign in with a **sock-puppet** account (needed for search and NSFW-flagged blogs).
2. Search the `username`/handle, or browse tags tied to the subject's known interests.
3. Read the blog: posts, linked social handles, images (grab for reverse-image/EXIF), and the reblog chains showing who they interact with.
4. Pivot: a cross-posted handle feeds username correlation; blog images feed reverse-image/EXIF tools; frequent reblog partners are `associate` leads.

## Inputs → Outputs
- **In:** `username` / `name` / interest keyword
- **Out:** `social-profile` (blog), `associate` links (reblog/follow network), interests, images
- **Empty/negative result looks like:** no blog at the handle, or a deactivated/"there's nothing here" page — the handle isn't on Tumblr or was deleted, not proof of no presence elsewhere.

## Gotchas & OpSec
- **Pseudonymous by design:** a blog rarely states a real name — treat identity links (cross-posted handles, selfies) as leads to corroborate.
- **Attributed actions:** follows/likes/asks notify the owner; browse read-only from a sock puppet.
- Login required for search and adult-flagged content — never use your real account.

## Overlaps ("do both")
- Pairs with cross-platform username tools and reverse-image search: those tie the Tumblr handle to the subject's other identities; the blog content supplies the interest/network context.

## Trust & verifiability
`trust: trusted` — the genuine first-party app; authoritative for posted content, with pseudonymity the main analytic caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tumblr-social-networking-app-mobile-android |
