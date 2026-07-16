---
id: socialcatfish
name: Social Catfish
description: Use when you have an `image`, `email`, `phone`, `username` or `name` and want a reverse-lookup that verifies identity and surfaces linked profiles — returns social-profile, aliases, contact info and associates. Freemium.
url: https://socialcatfish.com/
category: people-search
path:
- people-search
bestFor: Reverse identity verification — especially catching catfish/romance-scam personas by reverse-searching a photo, email or phone into linked profiles.
selectorsIn:
- image
- email
- phone
- username
- name
selectorsOut:
- social-profile
- name
- associate
- address
status: live
pricing: freemium
costNote: Freemium — you can start a search and see limited previews free, but full reports and deep results require a paid plan (subscription). Budget for the plan and cancel deliberately.
opsec: active
opsecNote: A search runs against a broker index and is passive toward the subject (no notification), but full access requires a paid account tied to your billing identity. Its signature use — verifying a romance-scam persona — means you may be searching a photo/email the subject supplied; use a research account and payment method, never your own.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known commercial reverse-lookup aggregator marketed for catfish/scam detection. Data is aggregated from public and broker sources — useful leads, not authoritative facts; expect false and stale matches.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- socialcatfish.com
- SocialCatfish
tags:
- people-investigations
- reverse-lookup
- catfish
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- social-catfish-reverse-image-search
---

# Social Catfish

> A reverse-lookup service built for identity verification — feed it a photo, email, phone, username or name and it tries to tie that fragment to real linked profiles, its headline use being to unmask catfish and romance-scam personas.

## When to use
You have a single fragment — most powerfully an `image`, but also `email`/`phone`/`username`/`name` — and want to know who it really belongs to and whether a claimed identity is genuine. Especially apt when a subject presents a persona (dating/romance context) and you need to check if the photo or contact detail traces to a different, real person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://socialcatfish.com/ and pick the search type (image, name, phone, email, username, or address).
2. Enter the fragment (for image search, upload the photo) and run it.
3. Read the free preview — it indicates whether matches exist. Full details (linked profiles, aliases, contacts) require a paid plan.
4. Use a **research account and payment method** if you subscribe.
5. Pivot: a matched profile/alias feeds username enumeration (`[[aliens-eye]]`) and reverse-image/face search; a real name feeds people-search and public records; mismatches (photo → different person) are the catfish signal.

## Inputs → Outputs
- **In:** `image`, `email`, `phone`, `username`, or `name`
- **Out:** `social-profile`s, real `name`/aliases, `associate`/contact info, `address` and public-record hints
- **Empty/negative result looks like:** preview shows no/weak matches — the fragment isn't in its index, or (for images) the photo is unique/AI-generated. A null isn't proof the identity is genuine, and a match isn't proof it's the same person.

## Gotchas & OpSec
- **Paywall:** the free preview only tells you matches exist; details cost money via subscription — set a cancellation reminder.
- Broker data is error-prone; treat every match as a lead to confirm, never a fact. Reverse-image matching can false-positive on lookalikes.
- OpSec: **active** in that access is tied to your billing identity — isolate with a research persona.

## Overlaps ("do both")
- Pairs with dedicated reverse-face search (`[[pimeyes-com]]`) for images and with `[[people-looker-us]]` for US contact depth — Social Catfish is strongest at the verification/catfish angle; those go deeper on faces and records respectively.

## Trust & verifiability
`trust: community` — a commercial aggregator, not an authority. Its leads are genuinely useful for verification, but confirm any identity claim against an independent, authoritative source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socialcatfish |
| category | people-search |
| selectorsIn → selectorsOut | image, email, phone, username, name → social-profile, name, associate, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (payment-wall-partial, account-login) |
