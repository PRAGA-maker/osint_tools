---
id: read-notify
name: Read Notify
description: Use when you legitimately need to know if/when/where an email you sent was opened — ReadNotify attaches a tracking pixel that reports open time and approximate IP/geolocation.
url: https://www.readnotify.com/
category: email
path:
- email
- email-verification
bestFor: Confirming an outbound email was opened and capturing the reader's approximate IP/geolocation and device — an active engagement tactic.
selectorsIn:
- email
selectorsOut:
- ip-address
- geolocation
- device-id
- metadata-exif
status: live
pricing: freemium
costNote: Free trial; paid subscription for ongoing tracking. Per-email read receipts via a special suffix on the recipient address.
opsec: active
opsecNote: ACTIVE — you send a real email containing a tracking beacon. The recipient may detect or be alerted by it (image-blocking defeats it), and your message reaches the target. Has legal/ethics implications; get authorization.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, well-documented email read-receipt/tracking service. Capabilities are accurately described by the vendor; geolocation is IP-derived and approximate.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- readnotify
- readnotify-com
- readnotify-com-2
aliases:
- ReadNotify
tags:
- email
- email-verification
- email-tracking
- ip-tracker
source: arf-seed
lastVerified: ''
enrichment: full
---

# Read Notify

> ReadNotify embeds an invisible tracking beacon in an email you send so you learn when it was opened and the reader's approximate IP/geolocation — an active, send-something tactic.

## When to use
You have a working `email` for someone (e.g. a suspected alias mailbox for a missing person, or a tip-line contact) and you have authorization to confirm they read your message and to capture the opening device's IP/geolocation. This is an active maneuver — only when passive options are exhausted and you can legally and ethically send the email.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at readnotify.com and start a trial/subscription.
2. Compose an email and append the ReadNotify suffix to the recipient address (or use their plugin/web compose) so the beacon is attached.
3. Send it; when the recipient opens it and loads images, ReadNotify logs the open time, reader IP, approximate location, and client/device.
4. Pivot the captured `ip-address`/`geolocation` to network/geolocation tooling.

## Inputs → Outputs
- **In:** `email` (a real, sendable address).
- **Out:** open/read timestamp, reader `ip-address`, approximate `geolocation`, `device-id`/client metadata.
- **Empty/negative result looks like:** "not yet read," or no IP if the recipient blocks remote images or reads via a privacy proxy (Apple Mail Privacy Protection, Gmail image proxy).

## Gotchas & OpSec
- Human-in-the-loop: account-login and composing/sending a real email.
- OpSec: ACTIVE and intrusive — your email reaches and may alert the target; image-blocking and mail proxies defeat the beacon; IP geolocation is coarse and can be a VPN exit. Sending tracked email to a third party may raise legal/consent issues — obtain authorization.

## Overlaps ("do both")
- Duplicate listings of the same service: `[[readnotify]]`, `[[readnotify-com]]`, `[[readnotify-com-2]]`. Functionally identical.

## Trust & verifiability
`trust: community` — established service; the vendor's described behavior is consistent and corroborated, but results depend entirely on the recipient's mail client and any IP obfuscation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | read-notify |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, geolocation, device-id, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
