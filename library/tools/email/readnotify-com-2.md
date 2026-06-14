---
id: readnotify-com-2
name: readnotify.com
description: Use when you want to covertly track whether a sent document/email was opened and capture the reader's IP/geolocation — ReadNotify's tracking/doc-tracking page.
url: https://www.readnotify.com/readnotify/pmdoctrack.asp
category: email
path:
- email
bestFor: Covert read-tracking of an email or attached document with reader IP/geolocation capture — an active tactic.
selectorsIn:
- email
selectorsOut:
- ip-address
- geolocation
- device-id
- metadata-exif
status: live
pricing: freemium
costNote: Free trial; paid subscription for ongoing tracking and document tracking.
opsec: active
opsecNote: ACTIVE / covert tracker — embeds a beacon in mail or a tracked document. The target may detect it; image-blocking and mail proxies defeat it. Legal/ethics implications — get authorization.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Same ReadNotify service; this deep-link points at its document-tracking feature (pmdoctrack). Duplicate of the other ReadNotify entries. Geolocation is IP-derived and approximate.
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
- readnotify-com
aliases:
- ReadNotify
tags:
- emailtrackers
- Email - Covert IP Trackers
- email-tracking
- ip-tracker
- document-tracking
source: uk-osint
lastVerified: ''
enrichment: full
---

# readnotify.com

> Deep link to ReadNotify's document-tracking feature — embed a beacon in an email or attached document to learn when it was opened and the reader's approximate IP/geolocation. (Duplicate of `[[read-notify]]`.)

## When to use
You have a sendable `email` and authorization to covertly confirm a recipient opened your message or attached document and to capture their IP/geolocation. Active maneuver; use only when passive routes are exhausted and sending is legal and ethical.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at readnotify.com and enable document tracking.
2. Send the tracked email or upload/send a tracked document via the pmdoctrack feature.
3. On open with images/content loaded, ReadNotify logs open time, reader IP, approximate location, and client.
4. Pivot captured `ip-address`/`geolocation` to network/geo tooling.

## Inputs → Outputs
- **In:** `email` (real, sendable) or a tracked document.
- **Out:** open timestamp, `ip-address`, approximate `geolocation`, `device-id`/client (`metadata-exif`).
- **Empty/negative result looks like:** "not yet read," or no IP when content/images are blocked or a privacy proxy is used.

## Gotchas & OpSec
- Human-in-the-loop: account-login; you must send a real email/document.
- OpSec: ACTIVE/covert — reaches the target and may alert them; image/content-blocking and Apple/Gmail proxies defeat it; IP geolocation is coarse and may be a VPN. Covert third-party tracking raises consent/legal issues.

## Overlaps ("do both")
- Identical service to `[[read-notify]]`, `[[readnotify]]`, `[[readnotify-com]]`; this one just deep-links the document-tracking page.

## Trust & verifiability
`trust: community` — established service; corroborated behavior, but results depend on the recipient's mail client and any IP obfuscation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | readnotify-com-2 |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, geolocation, device-id, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
