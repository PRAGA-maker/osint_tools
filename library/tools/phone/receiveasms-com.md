---
id: receiveasms-com
name: receiveasms.com
description: Use when you have a `phone` number and want to check whether it is a public disposable/receive-SMS number (and read its public inbox) — returns a disposable-number flag and other `phone` numbers in the same pool.
url: https://receiveasms.com/
category: phone
path:
- phone
bestFor: Determining whether a suspect number is a throwaway public receive-SMS line rather than a real personal number.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: freemium
costNote: A rotating set of numbers is free to browse, with all inbound SMS shown publicly. Private/dedicated numbers cost money via the "Buy Numbers" section.
opsec: passive
opsecNote: Browsing the public number list and inboxes is passive and anonymous — you are looking at a service, not contacting the target. Note the flip side: because inboxes are fully public, any OTP or code sent to these numbers is world-readable; never route your own verification through them for sensitive accounts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A real, widely-used public SMS-receiving service; useful as a reference set of known-disposable numbers, not as an identity source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ReceiveaSMS
- receive-sms-online
tags:
- mobilephone
- Mobile & Phone Related
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# receiveasms.com

> A free public receive-SMS service — used in OSINT as a reference to recognise disposable numbers and to read what codes landed in a shared public inbox.

## When to use
You have a `phone` number tied to a suspicious account and want to know whether it is a personal line or a **public throwaway**. If the number appears on receiveasms.com's list, it is a shared disposable number — anyone could have used it to pass an SMS verification, so it identifies nobody. Also useful defensively: to see whether an account you're investigating was verified against a public, world-readable inbox.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://receiveasms.com/ and browse the list of available numbers (grouped by country: US, CA, UK, AU, BR, etc.).
2. To check a specific number, look for it in the current pool; open its page to see the live public inbox of received messages.
3. Interpret: if the target `phone` is (or recently was) in the pool, treat it as disposable — the account behind it is likely burner/anonymised.
4. Note related pool numbers (`phone`) — investigators sometimes see the same actor cycle through several public numbers.
5. Pivot: a "disposable" verdict downgrades the number as an identity lead and redirects effort to username/email/device signals instead.

## Inputs → Outputs
- **In:** `phone` (to test against the public pool)
- **Out:** disposable-yes/no signal, the public inbox contents, and other pool `phone` numbers
- **Empty/negative result looks like:** the number is not in the pool — this is only weak evidence it is personal, because public receive-SMS numbers rotate and this is just one of many such services. Absence here ≠ "a real person's number."

## Gotchas & OpSec
- Pools rotate; a number absent today may have been public last month. Cross-check other disposable-SMS sites before concluding a number is personal.
- Inboxes are fully public — treat anything sent to these numbers as compromised; do not use them for your own operational accounts.
- The site cannot attribute a number to a person; its only OSINT value is the disposable/not-disposable classification.

## Overlaps ("do both")
- Pairs with other receive-SMS aggregators (e.g. `[[receive-smss-com]]`, `[[sms-online]]`) — a number missing here may be listed on another, so check several before ruling "personal".

## Trust & verifiability
`trust: community` — a genuine, long-lived service; reliable for confirming a number is public/disposable, but it holds no identity data to verify against.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | receiveasms-com |
| category | phone |
| selectorsIn → selectorsOut | phone → phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
