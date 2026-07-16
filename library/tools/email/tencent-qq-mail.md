---
id: tencent-qq-mail
name: Tencent QQ Mail
description: Use when you have a Chinese `email` (especially number@qq.com) and want to pivot it to a QQ number and Tencent social identity — returns social-profile and the QQ username/number.
url: https://exmail.qq.com
category: email
path:
- email
bestFor: Recognising and pivoting QQ/Tencent email addresses — a numeric @qq.com address is the person's QQ ID, linking to QQ IM and Qzone.
selectorsIn:
- email
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: The mail service is free; the OSINT value is the pivot from a QQ email to a QQ number, not a paid lookup.
opsec: passive
opsecNote: Deriving a QQ number from a numeric @qq.com address and searching public Tencent profiles is passive. Attempting a password-recovery/existence check on the mailbox, or messaging the QQ account, is active and can alert the owner — stop at passive pivots and use a puppet if you must probe Tencent services.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Tencent is the legitimate operator of QQ/QQ Mail; "unverified" here reflects that this is an email provider being used as an OSINT pivot, not a vetted lookup tool, and that Tencent profile visibility varies.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- QQ Mail
- QQ Mailbox
- exmail.qq.com
tags:
- toddington
- curated-directory
- email-addresses
- china
- qq
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- qzone
- qzone-china
- tencent-com
- tencent-maps
---

# Tencent QQ Mail

> Tencent's QQ email service — its OSINT value is that a numeric `number@qq.com` address *is* the person's QQ number, a direct bridge into China's QQ IM and Qzone social ecosystem.

## When to use
You have an `email` that is Chinese/Tencent-linked — especially the classic `<digits>@qq.com` form. Those digits are the account's QQ number, which ties to a QQ instant-messaging profile and often a Qzone (社交空间) with photos, posts and connections. Reach for this to convert an otherwise opaque email into a Chinese social identity (`social-profile`) and a stable QQ `username`/number to pivot on — a key move when a subject's footprint is on Chinese platforms rather than Western ones.

## How to use it (`bestInteractionPattern`: web-manual)
1. Inspect the address: if it's `<digits>@qq.com`, those digits are the QQ number. (Vanity/`foxmail.com` addresses may not expose the number directly.)
2. Search that QQ number in QQ/Qzone and Chinese search engines (Baidu) to find the associated profile, nickname and Qzone.
3. Read whatever is public — nickname, avatar, region, Qzone posts — to build identity and location leads.
4. Note the QQ number (`username`) as a durable identifier across Tencent services.
5. Pivot: the QQ profile/nickname feeds Chinese social OSINT; the region/avatar feeds geolocation and image search; the number feeds other QQ-lookup resources.

## Inputs → Outputs
- **In:** `email` (ideally `number@qq.com`)
- **Out:** `social-profile` (QQ/Qzone profile), `username` (the QQ number as a persistent ID)
- **Empty/negative result looks like:** a private/locked QQ profile, a non-numeric or enterprise address that doesn't expose a number, or no public Qzone — common, since many QQ users lock their profiles; absence isn't proof the account doesn't exist.

## Gotchas & OpSec
- Only numeric `@qq.com` addresses cleanly expose a QQ number; enterprise (`exmail.qq.com`) and Foxmail addresses may not.
- Much QQ/Qzone content is private or region-locked and behind a login; expect partial visibility.
- Stay passive — don't run recovery flows or message the account, which would alert the owner.

## Overlaps ("do both")
- Pairs with dedicated QQ-number lookup tools and Chinese search engines (Baidu) — this recognises the pivot; those enrich the QQ number into a fuller Tencent profile.

## Trust & verifiability
`trust: unverified` — Tencent is a legitimate operator, but this is an email provider repurposed as a pivot; confirm any identity via the actual QQ/Qzone profile and corroborating selectors.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tencent-qq-mail |
| category | email |
| selectorsIn → selectorsOut | email → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
