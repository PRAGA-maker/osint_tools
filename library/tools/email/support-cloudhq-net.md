---
id: support-cloudhq-net
name: support.cloudhq.net
description: Use when you need to understand email tracking pixels — a reference article on how an opened email can reveal a recipient's IP/device; technique is active.
url: https://support.cloudhq.net/what-is-a-tracking-pixel-and-can-strangers-really-spy-on-me-through-email/
category: email
path:
- email
bestFor: Understanding how email tracking pixels work to capture a recipient's IP, device, and open time.
selectorsIn:
- email
selectorsOut:
- ip-address
- metadata-exif
- device-id
status: live
pricing: free
costNote: Free explainer article (cloudHQ's MailTrack-style tracking is its commercial product).
opsec: active
opsecNote: The technique it describes is ACTIVE and intrusive — you send the target a pixel-laden email and they must open it. This contacts/alerts the subject and may have legal limits. The article itself is passive to read.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A cloudHQ support article accurately explaining tracking pixels; it is an explainer, not a tool, and the underlying capability is a paid email-tracking product.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- tracking-pixel
- technique
- Email - Covert IP Trackers
source: uk-osint
lastVerified: ''
enrichment: full
---

# support.cloudhq.net

> An explainer article on email tracking pixels — how opening an email can leak a recipient's IP and device.

## When to use
You have a reachable `email` for a person of interest and want to learn how a tracking pixel could reveal their `ip-address`/`device-id` when they open a message. This article is the conceptual reference; executing the technique requires a tracking service and is an active, contact-based step.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the article at the URL to understand how invisible 1x1 pixels report opens, IP, client, and timing.
2. To act on it (separate, active step): use an email-tracking tool, send the subject a message containing the pixel, and wait for an open.
3. On open, the tracker logs the recipient's `ip-address`, approximate location, device/client `metadata-exif`, and timestamp.
4. Pivot: a captured IP can support geolocation/ISP leads; an open confirms the address is monitored and active.

## Inputs → Outputs
- **In:** `email` (target you can message)
- **Out:** `ip-address`, device/client `metadata-exif`, `device-id`-level signals — only if the target opens the email
- **Empty/negative result looks like:** the target never opens it, blocks remote images (so the pixel never loads), or uses a proxy that masks the real IP.

## Gotchas & OpSec
- ACTIVE and intrusive: you must contact the subject, which can compromise an investigation or alert a person who does not want to be found, and may be legally restricted.
- Many clients block remote images by default, defeating the pixel; VPN/proxy use yields a useless IP.
- Human-in-the-loop: running the technique needs a tracking-service account.

## Overlaps ("do both")
- Conceptually paired with `[[support-google-com]]` (reading received headers) — both extract IP/metadata, but headers are passive while pixels are active.

## Trust & verifiability
`trust: community` — accurate vendor explainer of a real technique; it is documentation, and the capability itself is a commercial product.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | support-cloudhq-net |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, metadata-exif, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
