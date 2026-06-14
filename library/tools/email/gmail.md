---
id: gmail
name: Gmail
description: Use as a pivot point — confirming a Gmail address exists, reading its raw headers, and feeding it into Google-account OSINT tools.
url: https://gmail.com
category: email
path:
- email
bestFor: Google's webmail; in OSINT it is the source/target for header analysis and Gmail-address account investigation.
selectorsIn:
- email
selectorsOut:
- name
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free consumer webmail (Google account).
opsec: passive
opsecNote: Reading headers or checking your own inbox is passive. Actively probing whether a Gmail address exists, or contacting it, becomes active and may notify the subject. Use a sock-puppet Google account for investigative work.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Gmail is Google's first-party webmail service. As an OSINT asset it is reliable (you operate your own account); attribution value comes from pairing a Gmail address with tools like GHunt.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Google Mail
tags:
- email
- google
relatedTools:
- ghunt
- google-analyzeheader
source: metaosint
lastVerified: ''
enrichment: full
---

# Gmail

> Google's webmail — in an investigation it is both the place you read raw email headers and the address type you feed into Google-account OSINT.

## When to use
Two roles: (1) operationally, as your sock-puppet inbox and the source from which you copy raw headers ("Show original") for analysis; (2) as a selector — a target's Gmail `email` is the input for Google-account investigation, since Gmail addresses map to a Google account with public artifacts (photos, Maps reviews, profile).

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in to a dedicated investigative Google account at https://gmail.com.
2. To analyze a received message, open it → "Show original" → copy the full headers into a header analyzer (`[[google-analyzeheader]]`, `[[forensicosint-com]]`).
3. To investigate a target's Gmail address, hand it to `[[ghunt]]` to enumerate the linked Google account.
4. Pivot: header IPs → geolocation; Gmail address → GHunt → profile `image`, `name`, `geolocation` from reviews.

## Inputs → Outputs
- **In:** a Gmail `email` (target's, or your own inbox's received mail)
- **Out:** for your inbox, raw headers / `metadata-exif`; for a target address, downstream `name`/`social-profile`/`image` via Google-account tools
- **Empty/negative result looks like:** Gmail itself does not "look up" people — value comes from the headers it exposes and from pairing the address with GHunt.

## Gotchas & OpSec
- Gmail strips the sender's client IP from outbound headers, so messages *from* Gmail users rarely reveal their real IP.
- Human-in-the-loop: account login required; use a burner Google account for investigative activity, never your personal one.
- Do not send probing emails to a target from an attributable account.

## Overlaps ("do both")
- Always pair a target Gmail address with `[[ghunt]]`; pair received-message headers with `[[google-analyzeheader]]`.

## Trust & verifiability
`trust: trusted` — first-party Google service; you control your own account, and the header data it exposes is authoritative for messages you actually hold.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gmail |
| category | email |
| selectorsIn → selectorsOut | email → name, social-profile, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
