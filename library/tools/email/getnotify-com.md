---
id: getnotify-com
name: Getnotify.com
description: Use when you can email a person and want to confirm if/when they open it and capture their IP and approximate location via a tracking pixel.
url: https://getnotify.com
category: email
path:
- email
bestFor: Sending a tracked email so that opening it reveals the recipient's IP, approximate location, and read time.
selectorsIn:
- email
selectorsOut:
- ip-address
- geolocation
- metadata-exif
status: live
pricing: freemium
costNote: Free tier allows a limited number of tracked emails per day; higher volume is paid.
opsec: active
opsecNote: This is an ACTIVE technique — you send a real email to the subject. They may notice, and blocking remote images defeats it. Use a sock-puppet sender; never use it without a lawful, ethical basis.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: GetNotify is a long-established email read-receipt/tracking service. It works by embedding a tracking pixel; effectiveness depends on the recipient loading remote images.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- GetNotify
tags:
- email
relatedTools:
- getmailbird-com
source: metaosint
lastVerified: ''
enrichment: full
---

# Getnotify.com

> An email read-receipt / tracking-pixel service: send a tracked message and learn when the recipient opens it, plus their IP and approximate location.

## When to use
You already have a working `email` for a subject (e.g. a missing person who may still check an account, or a lead you can lawfully contact) and want to confirm the account is live and capture the opener's `ip-address` and `geolocation`. This is an active "send-and-see" technique, not a passive lookup — use only with proper authorization.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a GetNotify account (ideally a dedicated sock-puppet sender).
2. Configure your sending address per their instructions (append their tag / use their relay) so outgoing mail is pixel-tracked.
3. Send a plausible message to the subject's `email`.
4. When/if they open it with remote images enabled, GetNotify logs the open time, opener `ip-address`, browser, and approximate `geolocation`.
5. Pivot: geolocate the captured IP; correlate timing with other activity.

## Inputs → Outputs
- **In:** `email` (a deliverable address you can lawfully contact)
- **Out:** open confirmation + `ip-address`, approximate `geolocation`, device/`metadata-exif`, read time
- **Empty/negative result looks like:** no open recorded — could mean undelivered, ignored, opened in plain text, or images blocked. Absence is not proof the account is dead.

## Gotchas & OpSec
- ACTIVE and intrusive: you are contacting the subject. There are real legal/ethical limits — do not impersonate, harass, or contact a vulnerable subject without authorization.
- Many clients block remote images by default, which neutralizes the pixel and yields no data.
- Captured IP may be a VPN, mobile carrier NAT, or webmail proxy rather than the person's home connection.
- Human-in-the-loop: account login and per-day send limits.

## Overlaps ("do both")
- Read `[[getmailbird-com]]` to understand the same pixel mechanics from the blocking/defensive side.

## Trust & verifiability
`trust: community` — long-running tracking service; the mechanism (tracking pixel) is well understood and its outputs are directly observable in your GetNotify dashboard.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | getnotify-com |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, geolocation, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
