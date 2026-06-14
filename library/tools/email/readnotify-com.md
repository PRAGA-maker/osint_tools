---
id: readnotify-com
name: readnotify.com
description: Use when you need to covertly confirm a sent email was opened and capture the reader's IP/geolocation — ReadNotify's tracking-pixel ("covert IP tracker") service.
url: https://www.readnotify.com/readnotify/
category: email
path:
- email
bestFor: Covert email read-receipt and IP/geolocation capture via an embedded tracking beacon — an active tactic.
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
opsecNote: ACTIVE / covert IP tracker — sends a real email with a hidden beacon. The target may detect it; image-blocking and mail proxies defeat it. Legal/ethics implications — get authorization.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Same ReadNotify email-tracking service; duplicate listing categorized under "Email - Covert IP Trackers" on uk-osint. Geolocation is IP-derived and approximate.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- read-notify
- readnotify
- readnotify-com-2
aliases:
- ReadNotify
tags:
- emailtrackers
- Email - Covert IP Trackers
- email-tracking
- ip-tracker
source: uk-osint
lastVerified: ''
enrichment: full
---

# readnotify.com

> ReadNotify's covert IP-tracker page — embed an invisible beacon in an email so you learn when it was opened and the reader's approximate IP/geolocation. (Duplicate of `[[read-notify]]`.)

## When to use
You have a sendable `email` and authorization to covertly confirm the recipient read your message and to capture their opening IP/geolocation. Active maneuver; use only when passive routes are exhausted and sending is legal and ethical.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at readnotify.com.
2. Append the ReadNotify suffix to the recipient address (or use their plugin) to embed the beacon.
3. On open with images loaded, the service logs open time, reader IP, approximate location, and mail client.
4. Pivot captured `ip-address`/`geolocation` to network/geo tooling.

## Inputs → Outputs
- **In:** `email` (real, sendable).
- **Out:** read timestamp, `ip-address`, approximate `geolocation`, `device-id`/client (`metadata-exif`).
- **Empty/negative result looks like:** "not yet read," or no IP when images are blocked or a privacy proxy is used.

## Gotchas & OpSec
- Human-in-the-loop: account-login; you must send a real email.
- OpSec: ACTIVE/covert — your email reaches the target; image-blocking and Apple/Gmail proxies defeat it; IP geolocation is coarse and may be a VPN. Covertly tracking third parties raises consent/legal issues.

## Overlaps ("do both")
- Identical to `[[read-notify]]`, `[[readnotify]]`, `[[readnotify-com-2]]`.

## Trust & verifiability
`trust: community` — established service; corroborated behavior, but results depend on the recipient's mail client and any IP obfuscation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | readnotify-com |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, geolocation, device-id, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
