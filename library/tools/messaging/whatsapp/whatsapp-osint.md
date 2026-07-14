---
id: whatsapp-osint
name: WhatsApp-OSINT
description: Use when you have a `phone` number and want to pull its WhatsApp profile photo, business/verification status, about-text, and linked-device signals — returns image, social-profile, and device-id data.
url: https://github.com/kinghacker0/WhatsApp-OSINT
category: messaging
path:
- messaging
- whatsapp
bestFor: Enriching a phone number into its WhatsApp profile photo, account type, and device/privacy signals via a scripted API.
selectorsIn:
- phone
selectorsOut:
- image
- social-profile
- device-id
status: live
pricing: freemium
costNote: The script is free (open source), but it calls a third-party WhatsApp OSINT API on RapidAPI that requires an API key; RapidAPI has a limited free tier with paid quotas beyond it.
opsec: active
opsecNote: Lookups route through a third-party RapidAPI service, not your own WhatsApp account, so the target is not directly notified — but you are handing the target's number to an unknown API operator who sees and may log every query. Use a dedicated key and never query numbers you must keep confidential from that operator.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: A community GitHub project (kinghacker0/WhatsApp-OSINT, ~700+ stars) wrapping a third-party API; the code is inspectable but the underlying data source is opaque and unverified.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- kinghacker0 WhatsApp-OSINT
tags:
- whatsapp
- messaging
- phone
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# WhatsApp-OSINT

> A Python CLI that turns a phone number into WhatsApp account intelligence — profile photo, business/verification status, about-text, and linked-device signals — through a third-party API.

## When to use
You have a `phone` number and want to know whether it has a WhatsApp account and enrich it: grab the public profile photo (a face/`image` to run through reverse-image and face search), determine if it is a business vs personal account, read the "about" status text, and check linked-device/privacy signals. This is a strong pivot in missing-persons and identity work because a profile photo and account type can confirm the number is live and tie it to a face.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/kinghacker0/WhatsApp-OSINT` and install deps: Python 3.8+, `requests`, `python-dotenv`, `colorama`.
2. Obtain a RapidAPI key for the WhatsApp OSINT API the tool uses and place it in the `.env` file.
3. Run the script and supply the target `phone` in full international format without `+` (e.g. `447700900123`).
4. Read the output: profile photo saved as JPG, business-account/verification flag, about/status text, linked-device and privacy details.
5. Pivot: feed the saved profile `image` into reverse-image/face tools; the business flag and about-text corroborate identity/occupation.

## Inputs → Outputs
- **In:** `phone` (international format)
- **Out:** profile `image` (photo), `social-profile` signals (account type, about-text, verification), `device-id`/linked-device hints
- **Empty/negative result looks like:** no photo and no account data — the number may not use WhatsApp, may have a hidden profile photo (privacy setting), or the API may have failed/rate-limited.

## Gotchas & OpSec
- **Human-in-the-loop:** requires a RapidAPI key; the free tier is quota-limited.
- Data quality depends entirely on an opaque third-party API — treat results as leads, and expect breakage if that API changes or dies.
- **OpSec (active):** you disclose the target's number to the API operator. The target isn't notified, but the operator sees your query — use a throwaway key and avoid sensitive numbers.
- A hidden profile photo reflects the owner's privacy setting, not tool failure.

## Overlaps ("do both")
- Pairs with `[[receive-sms-online-3]]` (is the number a burner?) and general phone-intelligence/line-type tools — do both, because those describe the *number* while this describes the *WhatsApp account and face* behind it.

## Trust & verifiability
`trust: community` — an open-source wrapper whose code you can read, but the WhatsApp data comes from an unverified third-party API; corroborate the photo and account details before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatsapp-osint |
| category | messaging |
| selectorsIn → selectorsOut | phone → image, social-profile, device-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
