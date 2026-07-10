---
id: contactout
name: ContactOut
description: Use when you have a professional's `name`/LinkedIn `social-profile` and want their personal `email` and `phone` — returns contact data for 350M professionals via a browser extension or search portal.
url: https://contactout.com/
category: people-search
path:
- people-search
bestFor: Recovering a professional's personal email and phone from a LinkedIn profile or name+company.
selectorsIn:
- name
- social-profile
- employer-org
selectorsOut:
- email
- phone
status: live
pricing: freemium
costNote: Freemium — 5 free credits/day after signup; paid plans (from ~$299) unlock unlimited/bulk and API. A contact reveal costs a credit.
opsec: passive
opsecNote: Queries a contact-data broker, not the subject — the person is not notified. But you must register an account (and, for the extension, install it and log into LinkedIn), so your identity/LinkedIn session is exposed to ContactOut. Use a sock-puppet account and a dedicated browser profile; the extension can leak your LinkedIn activity to the vendor.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: browser-extension
trust: community
trustNote: An established B2B contact-data vendor (350M+ professionals); coverage of business contacts is strong, but personal emails/phones are broker-sourced and can be outdated or mismatched.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- email-finder-3
- peep-mail-search-tool
aliases:
- Contact Out
tags:
- people-investigations
- contact-data
- email-phone-finder
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ContactOut

> A B2B contact-data broker — turn a LinkedIn profile or name+company into a personal email and phone number, via a browser extension or search portal.

## When to use
You have a professional's `name`, `employer-org`, or LinkedIn `social-profile` and need a direct line to them — a personal `email` or `phone` — that isn't published on their profile. ContactOut claims contact data for 350M professionals and reaches personal (not just work) addresses, making it useful when a subject is reachable through their professional identity but you have no direct contact detail.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Sign up (use a **sock-puppet** account) at https://contactout.com/ — you get 5 free credits/day.
2. Either install the Chrome extension and open the target's LinkedIn profile (the extension surfaces contacts inline), or use the web search portal with `name` + `employer-org`.
3. Spend a credit to reveal the `email`/`phone`; note it may return several candidates.
4. Verify before trusting — broker data can be stale; cross-check an email with an existence/validation tool.
5. Pivot: a confirmed `email` feeds breach/account-existence checks; a `phone` feeds reverse-phone and messaging-app checks.

## Inputs → Outputs
- **In:** `name`, LinkedIn `social-profile`, or `name` + `employer-org`
- **Out:** personal/work `email`, `phone`
- **Empty/negative result looks like:** no contact found, or only a generic work email — meaning the subject isn't in ContactOut's data or the match is weak. A returned contact is still a broker guess to verify.

## Gotchas & OpSec
- Human-in-the-loop: **account required** (and the extension needs your LinkedIn session); full/bulk use is **paywalled** — free tier is 5 reveals/day.
- The extension exposes your LinkedIn browsing to the vendor — use a dedicated browser profile and puppet LinkedIn account.
- Personal contact data is broker-sourced and can be outdated or mis-attributed — always verify.
- OpSec: **passive** toward the subject, but leaks *your* footprint to ContactOut.

## Overlaps ("do both")
- Pairs with `[[email-finder-3]]` and `[[peep-mail-search-tool]]` — ContactOut looks up stored broker contacts, while those derive and validate likely addresses from name+domain; cross-check the two for agreement.

## Trust & verifiability
`trust: community` — a real, established contact-data vendor with strong professional coverage, but personal emails/phones are broker data of variable accuracy; treat every returned contact as a lead to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | contactout |
| category | people-search |
| selectorsIn → selectorsOut | name, social-profile, employer-org → email, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
