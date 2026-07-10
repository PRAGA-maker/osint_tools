---
id: receive-sms-online-info
name: receive-sms-online.info
description: Use when you have a `phone` number and want to check if it's a public throwaway SMS line — or need a burner number for sock-puppet signups; returns disposable-number status.
url: https://www.receive-sms-online.info/
category: phone
path:
- phone
bestFor: Recognising a number as a public disposable/temporary SMS line, and sourcing burner numbers for account verification.
selectorsIn:
- phone
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free, no registration; a rotating pool of public numbers (USA, UK, Germany, France, Spain, Romania, Russia and others) for receiving SMS in-browser.
opsec: passive
opsecNote: Checking whether a target's number appears in the public inbox list is passive — you never contact the target. If you USE one of these numbers, every SMS to it is public and readable by anyone; never route password resets, banking, or anything sensitive through it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A real, functioning public temp-SMS site; it holds no personal identity data, so its OSINT value is classification (throwaway?) and sock-puppet support, not lookup.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- freephonenum-com
- numberingplans-com
aliases:
- receive-sms-online.info
tags:
- mobilephone
- disposable-number
- temp-sms
- sockpuppet
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# receive-sms-online.info

> A free public "receive SMS online" service on real SIMs — two OSINT uses: confirm a target's number is a shared throwaway, and grab a burner number to verify your own sock-puppet signups.

## When to use
Two cases. (1) **Classification:** you have a `phone` number a subject used to register somewhere and want to know if it's a real personal line or a public disposable one — if it appears in this site's (or a peer's) public inbox list, accounts "verified" with it aren't tied to a private owner. (2) **Tradecraft:** you need to receive an SMS/OTP for a sock-puppet account on a platform that accepts virtual numbers, readable in-browser without exposing a real number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.receive-sms-online.info/ and browse the available public numbers by country.
2. **To classify** a target's number: check whether it's listed here (and on peer temp-SMS sites); a match means it's a shared public line.
3. **To use as a burner:** pick a number, enter it at the target service's SMS step, then open that number's public inbox to read the code.
4. Pivot: decode the number's country/type with `[[numberingplans-com]]`; if it's disposable, downgrade any identity inferred from accounts on it.

## Inputs → Outputs
- **In:** `phone` number (to check), or none (to obtain a burner)
- **Out:** `metadata-exif`-style classification — "this number is a public disposable SMS line" (or not)
- **Empty/negative result looks like:** the number isn't in this site's pool — it may still be disposable elsewhere or a genuine line; a miss isn't proof it's real.

## Gotchas & OpSec
- Numbers are **public and shared** — anyone reads incoming SMS and numbers recycle; never use for anything sensitive.
- Many services (WhatsApp, banks, some dating apps) block these virtual numbers.
- OpSec: passive for classification; for sock-puppet use, treat everything sent to the number as world-readable.

## Overlaps ("do both")
- Same role as `[[freephonenum-com]]` — check a suspect number against **both** (and other temp-SMS sites), since pools differ; classify with `[[numberingplans-com]]`.

## Trust & verifiability
`trust: community` — a real, working service holding no personal data; use it strictly for number classification and sock-puppet support, and confirm "disposable" across several providers since numbers rotate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | receive-sms-online-info |
| category | phone |
| selectorsIn → selectorsOut | phone → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
