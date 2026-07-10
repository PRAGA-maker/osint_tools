---
id: receive-smss-com
name: receive-smss.com
description: Use when you have a `phone` number (or want to see who else uses a public disposable number) and want to read the public SMS inbox for that number — returns message content, sender IDs, and OTP/verification traffic.
url: https://receive-smss.com/
category: phone
path:
- phone
bestFor: Reading the public inbox of a shared disposable/virtual number, and recognising when a target's number is actually a throwaway.
selectorsIn:
- phone
selectorsOut:
- phone
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Fully free; no account, no payment, unlimited receiving on the shared public numbers.
opsec: passive
opsecNote: Passive with a caveat — reading the site leaks nothing to your target. But everything received on these numbers is PUBLIC. Never send a verification code to one of these numbers for an account you care about, and assume anyone can read anything sent to them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known free disposable-SMS site of the same family as receivesms.org / freephonenum.com; useful but operator-anonymous, so treat displayed numbers/messages as public and unverified.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- receive-smss
- Receive SMS Online
tags:
- mobilephone
- Mobile & Phone Related
- disposable-number
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# receive-smss.com

> A free public bank of disposable virtual phone numbers whose inboxes anyone can read — useful both as a throwaway for your own sock-puppet signups and as a way to recognise when a target's "number" is really a shared throwaway.

## When to use
Two cases. (1) You have a `phone` number tied to a subject and want to check whether it is one of these public disposable numbers — if the number appears here with a live public inbox, any account "verified" with it is disposable and the subject is deliberately obscuring identity. (2) You are building a sock-puppet and need a burner number to receive a one-time verification SMS without exposing your own line. Both are common in missing-person and account-attribution work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://receive-smss.com/ in a browser (sock-puppet browser recommended for case 2).
2. To check a specific number: search or scan the country lists for the exact number. If it's listed, click it to view the live public inbox.
3. To get a burner: pick a country, choose an available number, and use it in the third-party signup; return here and refresh (~30s) to read the incoming OTP under that number.
4. Read the inbox: each entry shows sender ID, timestamp, and full message body (OTP codes, service names, links).
5. Pivot: sender IDs and message content reveal which services a number has been used against (`social-profile` hints); a number that appears here explains why an account trail dead-ends.

## Inputs → Outputs
- **In:** `phone` (to check) or none (to grab a burner)
- **Out:** public message bodies, sender/service IDs, OTP codes, timestamps
- **Empty/negative result looks like:** the number isn't in the public list (so it's not one of this site's shared numbers — it may still be a burner elsewhere), or the inbox shows only unrelated traffic from strangers using the same public number.

## Gotchas & OpSec
- Everything is PUBLIC and shared — dozens of strangers use the same number simultaneously, so inboxes are noisy and nothing is private. Never route a code for an account you value through these numbers.
- Numbers rotate and get blocked by major services (Google, WhatsApp) frequently; a listed number may already be dead for a given signup.
- No login/captcha, so it's frictionless, but the operator is anonymous — treat the site itself as untrusted infrastructure.
- Do not enter any personal data; assume the operator logs traffic.

## Overlaps ("do both")
- Pairs with `[[spy-dialer]]` and `[[searchpeoplefree]]` — those attribute a *real* number to a person; this one identifies when a number is instead a shared throwaway that will never attribute.
- Sibling services (receivesms.org, freephonenum.com) list different numbers; check more than one when hunting for a specific public number.

## Trust & verifiability
`trust: community` — a widely-used but operator-anonymous free service. The messages shown are genuine live traffic, but the site has no accountability; use it as a signal (this number is a public burner) rather than as evidence about any individual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | receive-smss-com |
| category | phone |
| selectorsIn → selectorsOut | phone → phone, social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
