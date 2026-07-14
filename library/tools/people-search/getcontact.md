---
id: getcontact
name: GetContact
description: Use when you have a `phone` number and want the name(s) other people saved it under — returns crowdsourced name tags and profile hints.
url: https://www.getcontact.com/en/
category: people-search
path:
- people-search
bestFor: Revealing how a phone number is labeled in other people's address books via crowdsourced caller-ID data.
selectorsIn:
- phone
- name
selectorsOut:
- name
- social-profile
status: live
pricing: freemium
costNote: Free tier with limited lookups; a Premium subscription unlocks the full "tags" list showing every name the number is saved under. App registration (your own phone number) is required.
opsec: active
opsecNote: To use it you must install the app and register with a real phone number; the app pressures you to upload your entire contact list (do NOT — that leaks your contacts into the crowdsourced pool). Looking up a number does not directly notify its owner, but registering ties the activity to your device/number. Use a dedicated burner device and number, never your real one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: Commercial caller-ID app; data is crowdsourced from users' address books, so tags are unverified user-supplied labels, not authoritative records.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
relatedTools:
- truecaller
- eyecon
aliases:
- Get Contact
- getcontact.com
tags:
- bellingcat-toolkit
- people
- caller-id
source: bellingcat-toolkit
lastVerified: '2026-07-14'
enrichment: full
---

# GetContact

> A crowdsourced caller-ID app: see the names other people have saved a phone number under, drawn from millions of uploaded address books.

## When to use
You have a `phone` number and no name, or a name you want to corroborate, and you want to know how the number is labelled across other people's contacts. Because the tags come from real address books, they often reveal a person's real name, nicknames, employer, or role ("John Plumber", "Dad", "Maria Estate Agent") even when the number is otherwise unlisted — strong signal for identifying an unknown caller or confirming a number belongs to your subject.

## How to use it (`bestInteractionPattern`: mobile-app)
1. On a dedicated burner phone, install GetContact (iOS/Android/Huawei) or open the web version.
2. Register with a burner phone number. **Decline the contact-upload prompt** — do not grant address-book access.
3. Enter the target `phone` in full international format and search.
4. Read the returned "tags": the names/labels others have saved for that number, plus any linked profile hints.
5. Pivot: a real-name tag feeds people-search and social lookups; corroborate with another crowdsourced caller-ID like [[truecaller]] before trusting a single tag.

## Inputs → Outputs
- **In:** `phone` (or `name`, to find associated numbers on some tiers)
- **Out:** `name` (crowdsourced tags/labels), `social-profile` hints
- **Empty/negative result looks like:** "no tags" or a single generic label — the number simply isn't well-represented in uploaded contact books; absence is not proof of anything.

## Gotchas & OpSec
- **Never upload your real contacts.** The app's core mechanic is harvesting address books; granting it access dumps everyone you know into the crowdsourced pool.
- Tags are user-supplied and can be stale, joking, or malicious — treat them as leads, corroborate before acting.
- Human-in-the-loop: app install + phone-number registration required.
- OpSec: **active** — activity is tied to your registered device/number, so use a burner and never your real identity.

## Overlaps ("do both")
- Pairs with [[truecaller]] and [[eyecon]] — the crowdsourced pools differ by region and userbase, so a number blank in one often has tags in another; run several and look for agreement.

## Trust & verifiability
`trust: community` — data is crowdsourced, unverified, and self-reported. A consistent name across GetContact and Truecaller is a strong lead; a lone tag is not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | getcontact |
| category | people-search |
| selectorsIn → selectorsOut | phone, name → name, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
