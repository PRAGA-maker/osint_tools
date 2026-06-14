---
id: pointofmailcom-email-trac-chrome-google-com
name: pointofmailcom email trac (chrome.google.com)
description: Use when you can send the subject an email and want a read-receipt that reveals when/where they opened it — leaks the recipient's IP, geolocation, and device. Active technique (Chrome build).
url: https://chrome.google.com/webstore/detail/pointofmailcom-email-trac/fbfenljjbahpbnpffpepeiommncfckci?hl=en
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
costNote: Pointofmail offers free and paid tiers; the Chrome extension is free but the tracking service requires an account.
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
trustNote: Pointofmail is a real email-tracking/read-receipt service and this is its Chrome Web Store listing; current features and reliability are unconfirmed. Note Chrome Web Store listings of this age are often removed/unmaintained.
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

# pointofmailcom email trac (chrome.google.com)

> The Chrome extension for the Pointofmail email-tracking service — embed a read-receipt/tracking pixel in an outbound email to learn when and where the recipient opens it.

## When to use
You have a working `email` for the subject, can lawfully email them, and want to capture the `ip-address`, approximate `geolocation`, and device hints when they open the message. Active, contact-based technique — authorization required.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Pointofmail extension from the Chrome Web Store and sign in / register (listing may be removed — verify it loads).
2. Compose an email through the tracked workflow so a tracking pixel/link is embedded.
3. Send to the subject's `email`.
4. On open, read the dashboard: open time, IP, geolocation, device/client.
5. Pivot the captured `ip-address` to IP-geolocation/ISP lookups.

## Inputs → Outputs
- **In:** `email`
- **Out:** `ip-address`, `geolocation`, `device-id`, `metadata-exif` (open time, client/user-agent)
- **Empty/negative result looks like:** no open recorded — never opened, remote images blocked, or a privacy proxy masked IP/location.

## Gotchas & OpSec
- OpSec: ACTIVE — you contact the subject; detectable by image-blocking, Apple Mail Privacy Protection, or corporate security; can tip off the subject.
- Legal-gate: covert tracking may be restricted; ensure lawful authority and a defensible pretext.
- Human-in-the-loop: browser extension + account login; the Chrome listing may be defunct.

## Overlaps ("do both")
- Same service, Firefox build: `[[pointofmail-com-email-tracking-addons-mozilla-org]]`.

## Trust & verifiability
`trust: unverified` — legitimate listing for a real tracking service, but current availability/behavior unconfirmed; results depend on the recipient's email client.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pointofmailcom-email-trac-chrome-google-com |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, geolocation, device-id, metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes |
