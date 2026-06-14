---
id: hinge
name: Hinge
description: Use when you have an `image` and rough `geolocation` and want to check a subject against Hinge — a relationship-focused app with richer, prompt-based profiles.
url: https://hinge.co/en-gb
category: dating-classifieds
path:
- dating-classifieds
bestFor: Confirming a subject via a richer prompt-based dating profile and photos
selectorsIn:
- image
- name
- geolocation
selectorsOut:
- social-profile
- physical-description
- associate
status: live
pricing: freemium
costNote: Free to use core matching; HingeX/Premium add preferences and visibility features.
opsec: active
opsecNote: App-only, requires an account; likes/comments are visible to recipients and can notify the subject. Profiles often reveal more context (work, school, prompts) than swipe apps.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: mobile-app
trust: unverified
trustNote: Hinge is a real, major dating app; per-subject presence and accuracy are case-specific and unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- dating
- arf-seed
source: arf-seed
lastVerified: ''
enrichment: full
---

# Hinge

> A relationship-focused dating app whose prompt-based profiles often expose more identifying context (workplace, school, lifestyle) than swipe apps — good for corroboration when a profile is found.

## When to use
Use it when you have a profile `image`, a first `name`, and an approximate `geolocation`, and want richer context than Bumble/Badoo provide. Hinge profiles frequently list employer, school, hometown, and detailed prompts, which can yield `physical-description`, lifestyle details, and `associate`/affiliation hints once a match is confirmed.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Hinge and register a sock-puppet account; set discovery preferences and location to the subject's suspected area.
2. Browse the recommended stack for photos matching your subject; read prompts for work/school/location disclosures.
3. Do not like/comment on the subject's profile (it notifies them); screenshot for comparison only.
4. Pivot: disclosed employer/school → people-search and social platforms; photo → reverse-image search.

## Inputs → Outputs
- **In:** `image`, first `name`, `geolocation`
- **Out:** `social-profile`, `physical-description`, `associate`/affiliation context
- **Empty/negative result looks like:** subject never surfaces in your stack; Hinge gates discovery heavily, so absence is weak evidence.

## Gotchas & OpSec
- Human-in-the-loop: account required; some preferences paywalled.
- OpSec: active — likes and comments are visible and notify the recipient. Never interact with the subject; use a clean puppet account.

## Overlaps ("do both")
- Pairs with `[[bumble]]` and `[[badoo]]` (overlapping audiences) and with people-search tools that confirm the employer/school a Hinge profile discloses.

## Trust & verifiability
`trust: unverified` — Hinge is real and widely used; presence and the accuracy of self-reported profile details must be corroborated per case.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hinge |
| category | dating-classifieds |
| selectorsIn → selectorsOut | image, name, geolocation → social-profile, physical-description, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes |
