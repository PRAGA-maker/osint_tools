---
id: scan-qr-code
name: Scan QR Code from Image (4qrcode)
description: Use when you have an `image` of a QR code (a photo of a poster, billboard, sticker) and want to decode it — returns the QR's embedded content (URL, text, geolocation, contact).
url: https://4qrcode.com/scan-qr-code.php
category: documents-metadata
path:
- documents-metadata
bestFor: Decoding a QR code from an uploaded photo/screenshot to reveal the URL or data it points to.
selectorsIn:
- image
selectorsOut:
- domain
- geolocation
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: passive
opsecNote: You upload the QR image to 4qrcode's server to decode it, so the image is processed by a third party — strip any sensitive surroundings first. Crucially, do NOT auto-open the decoded URL from your real browser; the link may be attacker-controlled — inspect it in a sandbox/sock-puppet first.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple third-party QR decoder; the decode itself is deterministic and re-checkable with any offline QR reader.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Scan QR Code
- 4qrcode QR scanner
tags:
- qr-code
- decode
- image
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Scan QR Code from Image (4qrcode)

> A web tool that decodes a QR code from an uploaded image — turning a photographed code into the URL or data it encodes.

## When to use
You have an `image` containing a QR code — a photo of a poster, billboard, street pole, product, or a screenshot — and need to know what it points to. In geolocation and field-photo work, decoding QR codes visible in an image can reveal a business URL, a location, contact details, or an app link that anchors the scene or identifies an entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://4qrcode.com/scan-qr-code.php.
2. Upload the `image` containing the QR code (crop tightly to the code for a cleaner read).
3. Read the decoded content — commonly a URL, plain text, geo coordinates, Wi-Fi, or vCard contact.
4. **Do not** blindly open the decoded URL from your real browser — inspect it first (unshorten, sandbox).
5. Pivot: a decoded `domain` feeds domain-OSINT; geo coordinates feed mapping; a vCard feeds people-search.

## Inputs → Outputs
- **In:** an `image` of a QR code
- **Out:** the decoded payload — URL (`domain`), text, `geolocation` coordinates, Wi-Fi/contact data
- **Empty/negative result looks like:** "no QR code found"/garbled decode — the code is too small, blurry, angled, or partially obscured; re-crop, deskew, or enhance the image and retry.

## Gotchas & OpSec
- Decoded URLs can be malicious — never auto-open; unshorten and sandbox first.
- Poor image quality/angle is the usual cause of failure — crop and straighten the code.
- Uploading sends the image to a third party — remove sensitive context from the crop.

## Overlaps ("do both")
- Pairs with URL-unshortening/reputation tools and geolocation tools — this reveals the payload; those then vet a decoded link or place a decoded coordinate.

## Trust & verifiability
`trust: community` — a basic third-party decoder; the decode is deterministic, so you can confirm it with any offline QR reader on the same image.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scan-qr-code |
