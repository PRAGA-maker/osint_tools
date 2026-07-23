---
id: rug
name: Rug
description: Use when you need a plausible, randomly generated identity to build a sock-puppet account — returns a synthetic name, address, dob and photo (all fake).
url: https://github.com/rly0nheart/rug
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating throwaway random-identity data (name, address, DOB, avatar) for sock-puppet setup.
selectorsIn: []
selectorsOut:
- name
- address
- dob
- image
status: degraded
pricing: free
costNote: Free and open source. Repo was archived (read-only) in June 2024; the final 1.0.0 Windows installer still works.
opsec: passive
opsecNote: Runs locally and pulls sample identities from the randomuser.me API, so only randomuser.me sees a generic request — never your target. The generated identities are fictitious; never reuse them to impersonate a real person, and remember a determined platform can still trace the sock puppet by IP/device, so pair with a clean browser/VPN.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: unverified
trustNote: Small single-author hobby project, now archived. It only wraps the public randomuser.me data, so risk is low, but it is unmaintained — treat as a convenience generator, not critical tooling.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- reddit-post-scraping-tool
aliases:
- rug identity generator
- rly0nheart/rug
tags:
- Sock Puppets
- identity-generator
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Rug

> "Lorem Ipsum, but for people" — a tiny desktop app that spits out random fake identities (name, address, DOB, photo) to seed a sock-puppet persona.

## When to use
You are standing up a research sock puppet and need a coherent, throwaway identity — a name, a matching photo, a plausible address and date of birth — so the account doesn't look empty or obviously fabricated. Rug gives you consistent placeholder data in one click instead of inventing (and forgetting) details by hand.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the final release (`1.0.0`) `.msi` from the GitHub repo and install it on Windows (needs the .NET Desktop Runtime). The repo is archived, so use the last published installer.
2. Launch Rug; it fetches a random person from the randomuser.me API and displays a full synthetic identity — name, gender, address, DOB, phone, and an avatar image.
3. Copy the fields you need into your persona notes and reroll for a fresh identity if the first doesn't fit.
4. Use the details only to *populate* a puppet account — never to claim to be a specific real individual.
5. Pivot: once the puppet exists, use it (behind a clean browser/VPN) to view content that requires a login, e.g. scraping tools like `[[reddit-post-scraping-tool]]`.

## Inputs → Outputs
- **In:** none — it generates on demand
- **Out:** a synthetic `name`, `address`, `dob`, and avatar `image` (all fictitious)
- **Empty/negative result looks like:** the app fails to populate because it can't reach randomuser.me (no internet / API down); retry or pull an identity from randomuser.me directly.

## Gotchas & OpSec
- Windows-only, archived/unmaintained — no updates or fixes are coming; keep expectations low.
- The photo comes from randomuser.me's reused sample set and can be reverse-image-searched, exposing the account as fake. Swap in a fresh AI-generated face for anything that must withstand scrutiny.
- OpSec: **passive** as a generator (only randomuser.me is contacted), but the *use* of the puppet is where real OpSec risk lives — isolate identity, IP, and device.

## Overlaps ("do both")
- Complements a face generator (e.g. thispersondoesnotexist-style tools) — Rug supplies the biographical scaffold, a synthetic-face tool supplies a non-searchable avatar. Do both for a durable puppet.

## Trust & verifiability
`trust: unverified` — a small, now-archived hobby wrapper around a public fake-data API. Harmless and convenient, but unmaintained; don't build critical workflow around it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rug |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | (none) → name, address, dob, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
