---
id: linkedin-email-reverse-lookup
name: LinkedIn Email Reverse Lookup
description: Use when you have an `email` and want the matching LinkedIn profile — returns the person's name, profile ID/username, and photo via a logged-in session.
url: https://osint.support/chrome-extensions/2019/09/03/linkedin-email-reverse-lookup.html
category: social-networks
path:
- social-networks
bestFor: Reversing an email address to a specific LinkedIn profile using LinkedIn's own contact-matching.
selectorsIn:
- email
selectorsOut:
- social-profile
- name
- image
status: degraded
pricing: freemium
costNote: The referenced Chrome extension is free but old (2019) and may be gone from the store; the underlying technique (query LinkedIn's contact-matching API with your session) still works via current extensions/scripts. Some tools that wrap this are paid.
opsec: active
opsecNote: The lookup runs through YOUR active, logged-in LinkedIn session, so LinkedIn attributes the queries to that account and can rate-limit or flag it — always use a well-aged sock-puppet LinkedIn account, never your real one. The target is not directly notified, but bulk querying is exactly what LinkedIn's anti-abuse watches for.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: A community technique/extension, not an official feature; the specific 2019 extension is obfuscated (may trip AV) and dated, so treat it as a pattern to reproduce with current tooling.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- LinkedIn Email Reverse Lookup
- LinkedIn email to profile
tags:
- linkedin
- email-to-account
- chrome-extension
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# LinkedIn Email Reverse Lookup

> Turns an email into a LinkedIn profile by abusing LinkedIn's "find contacts by email" matching from inside a logged-in session.

## When to use
You have an `email` and want to know whether — and whom — it belongs to on LinkedIn. LinkedIn will match an address to a member's profile (that's how "sync your contacts" works), and this technique/extension surfaces that match: the person's name, profile URL/ID, and photo. It's one of the most direct email→identity pivots when the subject is a professional.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Log into a **sock-puppet** LinkedIn account in your browser (the lookup needs a live session).
2. Install a current LinkedIn-email-lookup extension (the linked 2019 one is dated/obfuscated — prefer a maintained equivalent) or run a script that hits LinkedIn's contact-matching endpoint with your session cookie.
3. Enter the `email`; if LinkedIn has a match, you get the profile name, ID/username, and photo.
4. Open the profile to confirm and read employer/location detail.
5. Pivot: the confirmed profile → employer (`[[kompass]]`) and username pivots; the photo → `[[yandex-images]]`; the handle → `[[nexfil]]`.

## Inputs → Outputs
- **In:** `email`
- **Out:** `social-profile` (LinkedIn), `name`, profile ID/username, `image`
- **Empty/negative result looks like:** no match — the address isn't tied to a LinkedIn account (or LinkedIn declined to match it). Not proof the person has no LinkedIn under a different address.

## Gotchas & OpSec
- Human-in-the-loop: needs a live LinkedIn login — use a burner; the queries are attributed to it and can get it limited/banned.
- The specific 2019 extension may be removed and is obfuscated (AV may flag it); reproduce the method with current, inspectable tooling.
- Volume is risky: a handful of lookups is fine, bulk enumeration trips LinkedIn's abuse controls.
- OpSec: **active** — the searching happens as your LinkedIn account.

## Overlaps ("do both")
- Pairs with `[[gravatar-email-checker]]` and email-permutation tools — the permutator/verifier finds the real address, Gravatar and this LinkedIn technique each turn that address into a face and a profile on different platforms.

## Trust & verifiability
`trust: community` — an unofficial technique riding LinkedIn's own matching; a positive match is reliable (it's LinkedIn's data), but the tooling is dated and must be run carefully from a sock-puppet account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkedin-email-reverse-lookup |
| category | social-networks |
| selectorsIn → selectorsOut | email → social-profile, name, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
