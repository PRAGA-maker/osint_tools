---
id: pointofmail-com-email-tracking-addons-mozilla-org
name: pointofmail com email tracking (addons.mozilla.org)
description: Use when you can send the subject an email and want a read-receipt that reveals when/where they opened it — leaks the recipient's IP, geolocation, and device. Active technique.
url: https://addons.mozilla.org/en-US/firefox/addon/pointofmail-com-email-tracking/?src=search
category: email
path:
- email
bestFor: Email read-receipts / tracking pixels to capture a recipient's IP and approximate location.
selectorsIn:
- email
selectorsOut:
- ip-address
- geolocation
- device-id
- metadata-exif
status: unknown
costNote: Pointofmail offers free and paid tiers; the Firefox add-on is free but the tracking service requires an account.
pricing: freemium
opsec: active
opsecNote: This sends an email containing a tracking pixel to the subject — direct contact. The recipient (or their security tooling) may detect the tracker. Only with proper legal authorization.
humanInLoop: true
humanInLoopReason:
- account-login
- browser-extension
- legal-gate
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Pointofmail is a real email-tracking/read-receipt service and this is its Firefox add-on listing; specific current features and reliability are unconfirmed. It is a sending tool, not a passive lookup.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Pointofmail
tags:
- emailtrackers
- Email - Covert IP Trackers
source: uk-osint
lastVerified: ''
enrichment: full
---

# pointofmail com email tracking (addons.mozilla.org)

> A Firefox add-on for the Pointofmail email-tracking service — embed a read-receipt/tracking pixel in an outbound email to learn when and where the recipient opens it.

## When to use
You have a working `email` for the subject, can lawfully email them (or a pretext that reaches them), and want to capture the `ip-address`, approximate `geolocation`, and device hints from when they open the message. This is an active, contact-based technique — only with authorization.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Pointofmail add-on from addons.mozilla.org and sign in / register.
2. Compose an email through the tracked workflow so a tracking pixel/link is embedded.
3. Send to the subject's `email`.
4. When they open it, read the dashboard: open time, IP, geolocation, device/client.
5. Pivot the captured `ip-address` to IP-geolocation/ISP lookups.

## Inputs → Outputs
- **In:** `email`
- **Out:** `ip-address`, `geolocation`, `device-id`, `metadata-exif` (open time, client/user-agent)
- **Empty/negative result looks like:** no open recorded — recipient never opened it, blocked remote images, or a privacy proxy masked the IP/location.

## Gotchas & OpSec
- OpSec: ACTIVE — you contact the subject; detectable by image-blocking, Apple Mail Privacy Protection, or corporate security. Can tip off the subject.
- Legal-gate: covert tracking of a person may be restricted; ensure lawful authority and a defensible pretext.
- Human-in-the-loop: browser extension + account login.

## Overlaps ("do both")
- Same service, Chrome build: `[[pointofmailcom-email-trac-chrome-google-com]]`. For passive alternatives, prefer breach/footprint tools — this is the opposite (engagement) approach.

## Trust & verifiability
`trust: unverified` — legitimate add-on listing for a real tracking service, but current behavior unconfirmed and results depend heavily on the recipient's email client.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pointofmail-com-email-tracking-addons-mozilla-org |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, geolocation, device-id, metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes |
