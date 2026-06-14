---
id: readnotify
name: ReadNotify
description: Use when you need to confirm an email you sent was opened and capture the reader's approximate IP/geolocation — ReadNotify embeds a tracking beacon in outbound mail.
url: http://www.readnotify.com
category: email
path:
- email
bestFor: Confirming an outbound email was read and capturing the reader's approximate IP/geolocation and mail client — an active tactic.
selectorsIn:
- email
selectorsOut:
- ip-address
- geolocation
- device-id
- metadata-exif
status: live
pricing: freemium
costNote: Free trial; paid subscription for ongoing tracking.
opsec: active
opsecNote: ACTIVE — sends a real email with a tracking pixel. The target may detect it; image-blocking and mail proxies defeat it. Legal/ethics implications — get authorization.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Same long-running read-receipt/email-tracking service as the email-verification entry; this is a duplicate listing from a different source list. Geolocation is IP-derived and approximate.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- read-notify
- readnotify-com
- readnotify-com-2
aliases:
- Read Notify
tags:
- email
- email-tracking
- ip-tracker
source: metaosint
lastVerified: ''
enrichment: full
---

# ReadNotify

> ReadNotify attaches an invisible beacon to an email you send so you learn when it was opened and the reader's approximate IP/geolocation. (Duplicate of the `[[read-notify]]` entry.)

## When to use
You have a sendable `email` for a subject and authorization to confirm they read your message and capture the opening device's IP/geolocation. Active maneuver — use only when passive options are exhausted and sending is legal and ethical.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at readnotify.com (start a trial).
2. Compose mail and append the ReadNotify suffix to the recipient address (or use their plugin) to attach the beacon.
3. On open with images loaded, ReadNotify logs open time, reader IP, approximate location, and mail client.
4. Pivot captured `ip-address`/`geolocation` to network/geo tooling.

## Inputs → Outputs
- **In:** `email` (real, sendable).
- **Out:** read timestamp, `ip-address`, approximate `geolocation`, `device-id`/client (`metadata-exif`).
- **Empty/negative result looks like:** "not yet read," or no IP when the recipient blocks remote images / uses a privacy proxy.

## Gotchas & OpSec
- Human-in-the-loop: account-login; you must compose and send a real email.
- OpSec: ACTIVE and intrusive — the email reaches the target and may alert them; image-blocking and Apple/Gmail proxies defeat it; IP geolocation is coarse and may be a VPN. Sending tracked mail to third parties raises consent/legal issues.

## Overlaps ("do both")
- Same service as `[[read-notify]]`, `[[readnotify-com]]`, `[[readnotify-com-2]]` — pick one; they are identical.

## Trust & verifiability
`trust: community` — established service, behavior consistently corroborated, but results hinge on the recipient's mail client and any IP obfuscation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | readnotify |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, geolocation, device-id, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
