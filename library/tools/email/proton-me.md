---
id: proton-me
name: proton.me
description: Use when an email ends in @proton.me/@protonmail.com and you need to understand the provider — an encrypted Swiss mail host that yields almost no subscriber data.
url: https://proton.me/mail
category: email
path:
- email
bestFor: Recognizing and reasoning about a Proton Mail address (privacy/encrypted Swiss provider) and using Proton as a sock-puppet mailbox.
selectorsIn:
- email
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free encrypted mailbox tier; paid plans add storage/custom domains. No OSINT lookup function.
opsec: passive
opsecNote: Recognizing the domain is passive. Proton can also be used to create a sock-puppet account for investigative outreach.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Proton Mail is a reputable encrypted provider, but it is NOT an OSINT lookup tool; it was harvested into an email list and is miscategorized.
missingPersonsRelevance: low
coverage:
- ch
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- protonmail
tags:
- email
- Email Related Sites
- provider
source: uk-osint
lastVerified: ''
enrichment: full
---

# proton.me

> Proton Mail is an encrypted Swiss email provider — not an OSINT search tool. Its investigative value is twofold: recognizing a privacy-conscious target, and providing a strong sock-puppet mailbox for the investigator.

## When to use
You have an `email` on `@proton.me` / `@protonmail.com` / `@pm.me` and want to understand the host before enriching, OR you need a hardened, free mailbox to register sock-puppet accounts for an investigation. Proton strips originating IP from outbound headers, so subject-side header geolocation will fail.

## How to use it (`bestInteractionPattern`: web-manual)
1. If reading a target address: note that the host is Proton and expect minimal metadata leakage; pivot the address elsewhere.
2. If building a persona: sign up at proton.me for a free encrypted mailbox to use as a research alias.
3. Do NOT attempt to access a subject's Proton account.

## Inputs → Outputs
- **In:** `email`
- **Out:** provider knowledge / `metadata-exif` (the host is encrypted, low-leak).
- **Empty/negative result looks like:** there is no lookup surface; proton.me is a product/sign-up page.

## Gotchas & OpSec
- Human-in-the-loop: none for recognition; account creation needs sign-up (sometimes phone/CAPTCHA).
- OpSec: passive. Proton hides sender IP and minimizes logs, so Proton addresses are low-yield for technical pivots. Good operational hygiene for your own alias.

## Overlaps ("do both")
- Pairs with breach-search (`[[scatteredsecrets-com]]`) and verifiers (`[[proofy]]`) — the address may still appear in breaches even though Proton itself reveals nothing.

## Trust & verifiability
`trust: unverified` — legitimate provider, mislisted as a research tool; returns no subject intelligence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | proton-me |
| category | email |
| selectorsIn → selectorsOut | email → metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
