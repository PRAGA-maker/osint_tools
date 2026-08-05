---
id: smstome-com
name: SMSToMe
description: Use when you need a free disposable phone number to receive an SMS verification code for a sock-puppet account — returns public temporary numbers and the codes texted to them.
url: https://smstome.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Getting a throwaway number to catch a one-time SMS verification code without exposing your real phone.
selectorsIn: []
selectorsOut:
- phone
status: live
pricing: free
costNote: Every number is free with no subscription, account, or app; the site monetises via ads.
opsec: passive
opsecNote: Numbers are shared and public — anyone can read incoming SMS on the same number. Never use it for anything you need to stay private, and assume the code you receive may also be seen (or already consumed) by strangers. Do not tie it to any account containing real investigator identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free public receive-SMS site of the common disposable-number class; useful for throwaway verification, not for anything requiring integrity or privacy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- smstome
- smstome.com
tags:
- sock-puppet
- disposable-number
- receive-sms
- opsec
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# SMSToMe

> A free, no-signup pool of public phone numbers whose inbound texts are shown on the page — the standard way to catch an SMS code for a throwaway account without burning your own number.

## When to use
You are standing up a sock-puppet account (dating site, forum, social platform) that demands SMS verification, and you must not link it to your real or investigative number. SMSToMe hands you a public number, and any code texted to it appears on the page within seconds. Use it only for disposable one-time-code capture — the numbers are shared and visible to everyone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://smstome.com in a sock-puppet browser (no registration).
2. Pick a country (USA, Canada, UK, France, Sweden, Finland, Belgium, Netherlands are offered) and choose a number.
3. Paste that number into the service you are verifying and trigger it to send an SMS.
4. Refresh the SMSToMe number's page — inbound messages appear publicly within seconds; read the code off the list.
5. Move on quickly: messages auto-delete after ~2–3 days and numbers rotate roughly every 30 days.

## Inputs → Outputs
- **In:** nothing about a subject — you are provisioning your own throwaway `phone`
- **Out:** a public temporary `phone` number and the SMS codes sent to it
- **Empty/negative result looks like:** the number's page shows no new message (the target service refused a known-disposable range, or another user already grabbed the code) — pick a different number or country.

## Gotchas & OpSec
- Human-in-the-loop: none, but many platforms blocklist well-known disposable-number ranges, so a given number may simply not receive the code — expect to retry.
- OpSec: passive toward any subject, but the numbers are **public** — codes are readable by strangers and a shared number can already be "used" on the target service. Never use it for account recovery or anything sensitive.
- Nothing here identifies a person; this is a puppet-hygiene tool, not an investigative lookup.

## Overlaps ("do both")
- Pairs with [[dating-profile-generator]] and a synthetic-face source — number, bio, and photo together make a cover account survive verification.

## Trust & verifiability
`trust: community` — a generic free receive-SMS site. Reliable enough for throwaway verification, but assume zero privacy and zero durability; never depend on a number staying yours.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | smstome-com |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → phone |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
