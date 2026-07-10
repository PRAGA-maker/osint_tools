---
id: hiya-r
name: Hiya
description: Use when you have a `phone` number and want caller-ID and spam/scam reputation on it — returns caller name/org and a spam classification, mainly via the mobile app.
url: https://www.hiya.com/
category: phone
path:
- phone
bestFor: Checking whether a number is flagged spam/scam and what caller identity/organisation is associated with it.
selectorsIn:
- phone
selectorsOut:
- name
- employer-org
- metadata-exif
status: live
pricing: freemium
costNote: The consumer caller-ID app is free; richer identity/branded-calling data is an enterprise/network product. There is no simple free public web reverse-lookup — signals come through the app or carrier integration.
opsec: passive
opsecNote: Reputation lookups are service-mediated against Hiya's database, so the number's owner is not contacted. Using the app requires an account and grants Hiya access to call metadata; use a dedicated device/account, not your primary identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: Hiya is a major, legitimate caller-ID/anti-spam provider (28B+ calls/month, 40+ countries); reputation signals are strong, but caller-name data is crowdsourced/derived and can be wrong or generic.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- numberingplans-com
aliases:
- Hiya Caller ID
- hiya.com
tags:
- phone
- caller-id
- spam
- reputation
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Hiya

> A large-scale caller-ID and anti-spam service — tells you whether a `phone` number is flagged as spam/scam and what caller name/organisation is attached, mostly through its mobile app and carrier integrations.

## When to use
You have a `phone` number and want reputation and light identity context: is it a known spam/scam line, a business, or a plausible personal number, and what caller name/organisation does Hiya associate with it. It is most useful for triaging a number (ignore the spam/robocall, focus on the real one) rather than for resolving a person's identity — the identity data is generic (often just an org or "spam risk"), not a subscriber name.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install the Hiya app (iOS/Android) on a dedicated/sock-puppet device and sign in.
2. Use its number-lookup/caller-ID feature to check the target `phone`, or let it identify the number if it calls.
3. Read the output: caller name/organisation (if known), category (spam/scam/legit) and a risk score.
4. Cross-check the classification — a "spam" flag is high-confidence; a caller *name* is a lead, not proof.
5. Pivot: classify the number's country/type with `[[numberingplans-com]]` first; a Hiya business name feeds company/`employer-org` searches.

## Inputs → Outputs
- **In:** `phone` number
- **Out:** `name`/`employer-org` caller label (if known), and `metadata-exif`-style reputation (spam/scam category, risk score)
- **Empty/negative result looks like:** "no information" / unlabelled number — common for ordinary personal lines; absence of a label is expected and tells you little.

## Gotchas & OpSec
- No straightforward free web reverse-lookup — you generally need the app/account, which is human-in-the-loop.
- Caller-name data is crowdsourced/derived and can be stale, generic, or wrong; the *spam reputation* is the more reliable signal.
- OpSec: the app sees your call metadata; isolate it on a non-primary account/device.

## Overlaps ("do both")
- Pairs with `[[numberingplans-com]]` — that gives authoritative country/operator/number-type; Hiya adds crowd reputation and any business label. Use both to decide whether a number is worth pursuing.

## Trust & verifiability
`trust: community` — a major legitimate provider, so spam reputation is trustworthy, but caller-name attribution is derived data — treat any name as a lead to confirm elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hiya-r |
| category | phone |
| selectorsIn → selectorsOut | phone → name, employer-org, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | yes (account-login) |
</content>
