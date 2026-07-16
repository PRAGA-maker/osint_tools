---
id: singlehire
name: SignalHire
description: Use when you have a `name` (+ `employer-org`/`geolocation`) or a work `email`/`phone` and want the person's contact details — returns email, phone, and linked social-profiles.
url: https://www.signalhire.com/candidates/47dc037faace4abeb0727d6f4d0f3079
category: people-search
path:
- people-search
bestFor: Turning a name + employer/title into direct email, phone, and social-profile links via a recruiter-grade contact database.
selectorsIn:
- name
- employer-org
- email
- phone
selectorsOut:
- email
- phone
- social-profile
- name
- employer-org
status: live
pricing: freemium
costNote: Free plan gives ~5 contact reveals/month after signup; paid plans buy more credits and API access. No unlimited free tier.
opsec: passive
opsecNote: Queries hit SignalHire's own aggregated database, not the target's infrastructure, so the subject is not alerted. But you must register and (for the extension) log in, so SignalHire knows your identity — use a dedicated research account, never a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: browser-extension
trust: community
trustNote: Commercial recruiting-data vendor; records are aggregated/scraped from the public web plus user contributions, so accuracy varies and entries can be stale.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
aliases:
- SignalHire
- signalhire.com
tags:
- Universal Contact Search and Leaks Search
- people-search
- contact-enrichment
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# SignalHire

> A recruiter-grade contact-enrichment engine: give it a person (or their profile) and it returns their email, phone, and linked social accounts from an 850M+ record database.

## When to use
You have a `name` plus a disambiguator (`employer-org`, job title, or `geolocation`), or you already hold one work `email`/`phone` and want the rest of the contact footprint. SignalHire is strongest when the subject has a professional/LinkedIn presence — it maps a person to reachable `email`/`phone` and cross-links their `social-profile`s, which is a fast way to open new pivots on someone last seen in a work context.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Create a free SignalHire account (research/sock-puppet identity, not personal).
2. Either: (a) install the Chrome/Firefox extension and open the subject's LinkedIn/Facebook/Twitter profile, then click the SignalHire button to reveal contacts; or (b) use the web app's People Search and filter by name, company, title, and location.
3. Spend a reveal credit to unmask the record — emails, phone numbers, and other linked social profiles appear.
4. Read the result: corroborate any returned email/phone against a second source ([[account-live-com]], a phone lookup) before trusting it.
5. Pivot: a revealed `email`/`phone` feeds account-existence and breach checks; linked `social-profile`s feed username/face searches.

## Inputs → Outputs
- **In:** `name` (+ `employer-org`/title/`geolocation`), or a known work `email`/`phone`
- **Out:** `email`, `phone`, `social-profile` links, current `name`/`employer-org`
- **Empty/negative result looks like:** "No contacts found," or a record with only a name and no revealed email/phone — common for people with no professional/LinkedIn footprint. Absence here means the person isn't in the recruiting-data pool, not that they don't exist.

## Gotchas & OpSec
- Human-in-the-loop: account signup is mandatory, and the free tier caps you at a handful of reveals per month (rate-limit) — budget credits for high-value targets.
- Data is aggregated/scraped and user-contributed, so expect stale or mismatched records; always verify a revealed contact independently.
- OpSec: passive toward the subject (no alert), but SignalHire logs which records *you* look up — use a dedicated research account and browser profile.

## Overlaps ("do both")
- Pairs with [[account-live-com]] — SignalHire proposes an `email`, that confirms whether it's a live Microsoft account.
- Complementary to broad people-search aggregators: SignalHire skews professional/contact data while general people-search skews address/relatives, so running both widens coverage.

## Trust & verifiability
`trust: community` — a legitimate commercial vendor, but the underlying data is scraped/crowd-sourced, so treat each returned email/phone as a lead to verify, not a confirmed fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | singlehire |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org, email, phone → email, phone, social-profile, name, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (account-login, rate-limit) |
