---
id: rocketreach
name: RocketReach
description: Use when you have a `name` plus an `employer-org` (or a LinkedIn `social-profile`) and want that person's professional `email` and `phone` — returns verified work/personal emails, phone numbers, and social links.
url: https://rocketreach.co/person
category: people-search
path:
- people-search
bestFor: Finding professional contact details (email/phone) for a named person tied to a company.
selectorsIn:
- name
- employer-org
- social-profile
selectorsOut:
- email
- phone
- social-profile
status: live
pricing: freemium
costNote: Free tier is 5 lookups/month (personal + professional email, browser extension, no card). Phone numbers, exports and API require paid plans — Essentials ~$69/mo, Pro ~$119/mo (adds phones + CRM), Ultimate higher; a lookup credit is spent only when a contact is successfully revealed.
opsec: active
opsecNote: Semi-active — the subject is not contacted, but you must create an account and every lookup is tied to your identity/billing. RocketReach may email the person as part of its own "contributor" model. Use a dedicated investigative account, never your personal login.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A large, established B2B contact-data vendor (700M+ profiles); data is aggregated and can be stale or wrong, so verify a revealed email/phone before acting on it.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- rocketreach.co
tags:
- linkedin
- people-search
- contact-enrichment
source: osintambition-social
lastVerified: '2026-07-10'
enrichment: full
---

# RocketReach

> A B2B contact-enrichment engine over 700M+ professional profiles that turns a name + company (or a LinkedIn URL) into work/personal email addresses and phone numbers.

## When to use
You have a `name` and know where they work (`employer-org`) or have their LinkedIn `social-profile`, and you need a direct `email` or `phone` to make contact or to pivot into email/phone OSINT. In missing-person work this is strongest for adults with a professional/corporate footprint — a colleague, employer, or relative whose LinkedIn you've found and whose contact detail you now want.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in to https://rocketreach.co/person with a dedicated investigative account (5 free lookups/month).
2. Search by `name` + company, or paste a LinkedIn profile URL; the browser extension can also reveal a contact directly from an open LinkedIn page.
3. Open the matched profile and click to reveal contacts — a lookup credit is consumed only when an email/phone is actually returned.
4. Read the output: professional email(s), sometimes personal email, phone (paid tiers), and linked social profiles, each with a confidence/verification flag.
5. Pivot: validate a revealed `email` with an existence check like `[[account-live-com]]`; feed a `phone` into phone-OSINT; feed found profiles into username tooling.

## Inputs → Outputs
- **In:** `name` + `employer-org`, or LinkedIn `social-profile`
- **Out:** professional/personal `email`, `phone` (paid), linked `social-profile`s, job title/company
- **Empty/negative result looks like:** "no contact found" or only a low-confidence guessed email pattern (e.g. first.last@company.com marked unverified) — treat guessed patterns as leads, not confirmed contacts.

## Gotchas & OpSec
- Requires an account (human-in-the-loop): the free tier is only 5 lookups/month and phones are paywalled behind Essentials+.
- Data is aggregated and can be outdated — people change jobs; a "verified" email may be a former employer. Confidence flags are estimates.
- Every lookup ties to your billing identity; RocketReach's model involves emailing contacts, so it is not fully covert. Isolate the account.
- Overage lookups bill at ~$0.30–0.45 each beyond plan limits — watch usage.

## Overlaps ("do both")
- Pairs with `[[searchpeoplefree]]` and `[[canada411-advanced-search-whitepages-ca]]` — RocketReach is best for *professional* contact data; those cover consumer/residential phone and address.
- Complementary to `[[account-live-com]]` for validating that a returned email is a live account.

## Trust & verifiability
`trust: community` — a mainstream commercial data vendor with broad coverage but no guarantee of accuracy on any single record. Every revealed email/phone should be independently verified (bounce-check, existence oracle, or a second source) before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rocketreach |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org, social-profile → email, phone, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
