---
id: didtheyreadit-com
name: didtheyreadit.com
description: Use when you (as sender) want to know if an email you sent was opened and from where — an invisible read-receipt/tracking service that returns open time, duration, and the reader's IP/location; it does not look up a person from an address.
url: http://www.didtheyreadit.com/
category: email
path:
- email
bestFor: Covert email open-tracking (read receipts with IP/geolocation) on mail you send.
selectorsIn:
- email
selectorsOut:
- ip-address
- geolocation
- metadata-exif
status: degraded
pricing: freemium
costNote: Historically a paid subscription with a limited free trial; the legacy service may no longer be reliably operational.
opsec: active
opsecNote: This is an ACTIVE technique — you embed a tracking pixel in an email you send to the subject. It contacts the subject, can tip them off, and may breach platform terms, privacy law, and evidentiary integrity. Treat as engagement, not passive collection.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
- legal-gate
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-standing read-receipt/email-tracking brand whose current operational status is uncertain (http-only legacy site). Verify it still functions before relying on it; tracking-pixel accuracy is easily defeated by image-blocking clients.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- DidTheyReadIt
tags:
- emailtrackers
- read-receipt
source: uk-osint
lastVerified: ''
enrichment: full
---

# didtheyreadit.com

> A covert email read-receipt service: it tells the *sender* whether and where a sent email was opened — not a tool that resolves identity from an address.

## When to use
Only when you are lawfully and authorisedly *sending* an email to a subject and want to confirm it was opened and approximate where (IP/geolocation). It takes the recipient `email` as the send target; it does **not** take an address and return the owner's name or accounts. For missing-persons work this is a high-risk engagement technique, rarely appropriate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register/sign in to the service.
2. Send the email through its tracking mechanism (e.g. an appended tracking domain) so an invisible pixel is embedded.
3. When the recipient opens the email and loads images, the service logs open time, how long it was viewed, and the reader's `ip-address`/approximate `geolocation`.
4. Pivot: a captured IP/location can corroborate a subject's region — but only if images loaded and the lead is legally usable.

## Inputs → Outputs
- **In:** recipient `email` (as the send target)
- **Out:** open confirmation, view duration, reader `ip-address`, approximate `geolocation` (`metadata-exif`-style read metadata)
- **Empty/negative result looks like:** no open recorded — the recipient never opened it, blocked remote images, used a privacy proxy (e.g. Apple Mail Privacy Protection), or the service is defunct.

## Gotchas & OpSec
- **Active and intrusive:** sending a tracked email contacts the subject, can alert them, and may violate law, platform terms, and chain-of-custody. Get authorisation first.
- Accuracy is weak: modern mail clients block tracking pixels or proxy image loads, producing false "unopened" or masked/proxy IPs.
- Status degraded: legacy http-only site; confirm it still operates before use.

## Trust & verifiability
`trust: unverified` — established brand but uncertain current operation and inherently spoofable signal. Never treat a captured IP/location as conclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | didtheyreadit-com |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, geolocation, metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
