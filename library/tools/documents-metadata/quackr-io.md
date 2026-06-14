---
id: quackr-io
name: quackr.io
description: Use when you need a disposable phone number for SMS verification (sock-puppet creation) — or to check whether a phone number a subject used is a public throwaway whose inbox is openly readable.
url: https://quackr.io
category: documents-metadata
path:
- documents-metadata
bestFor: Free temporary phone numbers for SMS verification, and recognizing/reading public disposable numbers used by a subject.
selectorsIn: [phone]
selectorsOut: [phone, metadata-exif]
status: live
pricing: freemium
costNote: Free public temporary numbers (shared, inboxes visible to anyone); a paid tier offers private numbers in more countries.
opsec: passive
opsecNote: Public quackr numbers are shared and their SMS inboxes are world-readable — never receive a real verification code you care about on a free number. Useful defensively to identify that a subject signed up with a throwaway. Reading public inboxes is passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: quackr.io is a widely used public disposable-number / SMS-receive service; function reasoned from known product, not re-verified. Available numbers rotate frequently.
missingPersonsRelevance: medium
coverage:
- global
- us
- gb
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- telephone-numbers
source: toddington-resources
lastVerified: ''
enrichment: full
---

# quackr.io

> Free public temporary-phone-number / receive-SMS-online service — both a sock-puppet utility and a way to spot when a subject registered with a throwaway number.

## When to use
Two cases. (1) You need a burner `phone` to receive an SMS verification code while creating a sock-puppet account for OSINT work. (2) You have a `phone` a subject used to register somewhere and want to check whether it is one of quackr's public throwaway numbers — if it is, the "phone" is shared and meaningless as an identity link, and you may even read the public inbox for context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://quackr.io and pick a country; the site lists currently available public numbers.
2. To use one as a burner: register the target service with that number, then open the number's public inbox on quackr to read the incoming verification SMS.
3. To check a subject's number: scan quackr's listed numbers (current and historical) for a match; if it appears, treat the number as a shared throwaway, not a personal line.
4. Pivot: a confirmed throwaway tells you the subject deliberately avoided a real number — adjust attribution accordingly; a real number routes to phone-OSINT/carrier lookups.

## Inputs → Outputs
- **In:** `phone` (a number to obtain, or one to check)
- **Out:** a usable temporary `phone` and its public SMS inbox; or a verdict that a queried number is a public throwaway, plus inbox `metadata-exif`-style content (sender, code, timestamp)
- **Empty/negative result looks like:** the subject's number is not in quackr's list — does not prove it is a real personal line (many other SMS-receive services exist); cross-check other disposable-number sites.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing.
- OpSec: public numbers are shared and inboxes are open — never use one for an account you want to keep private, and assume anyone can read messages sent to it.
- Number availability rotates constantly; a number present today may be gone tomorrow.

## Overlaps ("do both")
- Pairs with other receive-SMS-online services to rule a number "throwaway" with more confidence, and with phone-OSINT/carrier tools for genuinely personal numbers.

## Trust & verifiability
`trust: community` — well-known public service; entry reasons from its documented behavior, liveness/number list not freshly verified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | quackr-io |
| category | documents-metadata |
| selectorsIn → selectorsOut | phone → phone, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
