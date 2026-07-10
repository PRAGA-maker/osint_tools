---
id: defastra
name: Defastra
description: Use when you have an `email` or `phone` and want a fraud/risk score plus the social and digital profiles registered to it — returns linked `social-profile`s and enrichment signals via a paid API.
url: https://defastra.com/
category: email
path:
- email
bestFor: Enriching an email/phone into linked social profiles and a risk/reliability score.
selectorsIn:
- email
- phone
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Paid, prepaid-credit/wallet API (account + API key); a limited free trial is offered but there is no ongoing free tier. Each lookup consumes credit.
opsec: passive
opsecNote: Queries Defastra's databases about the email/phone; the subject is not notified. It is a commercial fraud-prevention vendor, so your queries and API key are logged by Defastra. Use a dedicated account; treat the returned linkages as leads, not proof.
humanInLoop: true
humanInLoopReason:
- api-key
- payment-wall-partial
bestInteractionPattern: api
trust: community
trustNote: A commercial fraud-prevention/data-enrichment vendor; the social-profile linkages are a useful OSINT by-product but are inferred and can be wrong or stale.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- epieos-tools
- ipqualityscore-com
aliases:
- Defastra fraud prevention
tags:
- Emails
- enrichment
- fraud-scoring
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Defastra

> A fraud-scoring API whose OSINT value is the by-product — the social and digital profiles it finds registered to an email or phone.

## When to use
You have an `email` or `phone` and want to know what online identity attaches to it: which social networks and digital services it is registered on (`social-profile`), plus a risk/reliability read on whether the contact looks genuine. Although sold as fraud prevention, that "which accounts exist for this contact" enrichment is exactly the email/phone-to-profile pivot investigators want. Reach for it when free enrichment tools come up short and you can spend a credit.

## How to use it (`bestInteractionPattern`: api)
1. Register at https://defastra.com/ and obtain an API key (top up prepaid credit; a free trial may cover initial tests).
2. Submit a single `email` or `phone` via the manual tool, batch, or API endpoint.
3. Read the response: a risk score (0–100) with level (low/medium/high/extreme) and, crucially, the social/digital data — accounts and services linked to the contact.
4. Treat linked profiles as leads; corroborate each on the platform itself.
5. Pivot: a discovered `social-profile` feeds cross-network enrichment; a "genuine, active" signal corroborates that the contact is real.

## Inputs → Outputs
- **In:** single `email` or `phone`
- **Out:** `social-profile`s registered to the contact, plus risk score and fraud/trust signals
- **Empty/negative result looks like:** a high-risk/low-data response with no linked profiles — meaning the contact is thin, disposable, or simply not in Defastra's sources. Absence of linkages is not proof the person has no accounts.

## Gotchas & OpSec
- Human-in-the-loop: **paid API with an API key** (`api-key` + `payment-wall-partial`) — no ongoing free tier; each lookup costs credit.
- Linkages are inferred by a vendor and can be wrong or outdated — always verify on-platform.
- OpSec: **passive** toward the subject, but your queries/key are logged by the vendor.

## Overlaps ("do both")
- Pairs with `[[epieos-tools]]` (free email/phone-to-account discovery) and `[[ipqualityscore-com]]` (risk scoring) — run the free tools first; use Defastra when you need broader linkage coverage and can pay.

## Trust & verifiability
`trust: community` — an established commercial vendor, but the social-profile links are inferred enrichment; corroborate every linkage before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | defastra |
| category | email |
| selectorsIn → selectorsOut | email, phone → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key, payment-wall-partial) |
