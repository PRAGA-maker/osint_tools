---
id: free-carrier-lookup
name: Free Carrier Lookup
description: Use when you have a `phone` and want to know its carrier and whether it's mobile, landline, or VoIP — returns telecom metadata that shapes how you investigate the number.
url: https://www.freecarrierlookup.com
category: phone
path:
- phone
bestFor: Identifying the carrier and line type (mobile/landline/VoIP) behind a phone number before deeper phone OSINT.
selectorsIn:
- phone
selectorsOut: []
status: live
pricing: free
costNote: Free. The site asks for an email address and a CAPTCHA to run a lookup; no paid tier for the basic result.
opsec: passive
opsecNote: You submit only the target number to a lookup service; the subject is never contacted or notified. The site does capture the email you enter to unlock results — use a sock-puppet address, not your own.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing free carrier-lookup front-end over HLR/telecom data; carrier and line-type results are generally reliable but can lag number portability.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- freecarrierlookup.com
- Free Carrier Lookup
tags:
- phone
- carrier-lookup
- line-type
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Free Carrier Lookup

> Type a number, learn its carrier and whether it's a mobile, landline, or VoIP line — the orientation step before any deeper phone investigation.

## When to use
You have a `phone` and need to know what kind of number it is before spending effort on it. Whether it's a real mobile, a landline, or a disposable VoIP/burner (Google Voice, TextNow, etc.) changes everything downstream: a VoIP line suggests a throwaway identity, a mobile carrier can hint at the subscriber's country/region, and the carrier name matters for a legal-process request.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `https://www.freecarrierlookup.com` in a sock-puppet browser.
2. Select the country, enter the `phone` in full international/national format.
3. Enter a **burner** email address and solve the CAPTCHA to reveal the result.
4. Read: carrier/operator name and line type (mobile / landline / VoIP).
5. Pivot: a VoIP result → treat the number as a probable burner and pivot to the app that issued it; a mobile carrier → feeds reverse-phone tools like `[[www-spydialer-com]]` and messaging-app checks.

## Inputs → Outputs
- **In:** `phone`
- **Out:** carrier/operator name and line type (telecom metadata — not one of the tracked person-selectors, so `selectorsOut` is empty by design)
- **Empty/negative result looks like:** "no carrier found" or an error — the number may be invalid, unallocated, or in a country the data doesn't cover. Not proof the number is fake.

## Gotchas & OpSec
- Human-in-the-loop: an email + CAPTCHA gate every lookup — use a sock-puppet email.
- Number portability means the reported carrier can be stale (the number moved carriers); treat line type as more reliable than the exact carrier.
- OpSec: **passive** toward the subject; only your burner email is exposed to the site.

## Overlaps ("do both")
- Pairs with `[[www-spydialer-com]]` — this tool tells you the *type* of line; SpyDialer attempts to attach an owner name/location to it.

## Trust & verifiability
`trust: community` — a reliable free front-end over telecom lookup data; line type is dependable, exact carrier can lag portability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-carrier-lookup |
| category | phone |
| selectorsIn → selectorsOut | phone → (carrier / line-type metadata) |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
