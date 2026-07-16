---
id: epieos-check-phone-usage
name: Epieos (Check Phone Usage)
description: Use when you have a `phone` (or `email`) and want to see which online services it is registered on, plus any linked name/photo — returns `name`, `social-profile`, `image` leads.
url: https://tools.epieos.com/phone.php
category: phone
path:
- phone
bestFor: Reverse phone/email lookup revealing linked accounts (Google, WhatsApp, etc.) and profile details.
selectorsIn:
- phone
- email
selectorsOut:
- name
- social-profile
- image
status: live
pricing: freemium
costNote: Epieos consolidated its standalone tools into epieos.com; the reverse-email lookup has a free tier, while phone lookups and deeper results are credit-based and require an account.
opsec: passive
opsecNote: Passive from your side — Epieos performs the account-existence checks server-side, so you don't directly touch the target's services and the subject is not notified. Some underlying checks probe third-party services (which may log the query). Never advance any account-recovery flow. Use an account you're comfortable being tied to the lookup.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Epieos is a well-regarded, professionally-run OSINT company used widely by investigators; results are reliable indicators of account existence, though "registered" ≠ actively used.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: true
aliases:
- Epieos
- epieos.com
tags:
- phone
- reverse-lookup
- account-existence
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- epieos
- epieos-email-tool
- epieos-tools
- google-account-finder-epieos
---

# Epieos (Check Phone Usage)

> Epieos — a reputable reverse email/phone tool: give it a number (or email) and it shows which online services it's registered on, plus any leaked name, photo, or linked profile.

## When to use
You have a `phone` (or an `email`) and want to know the digital footprint behind it: which platforms it's registered on (Google, WhatsApp, and others), a linked display `name` or profile `image`, and connected `social-profile`s. Powerful for confirming a number/email is real and in active use, and for pivoting from a bare identifier to named accounts in a missing-persons or fraud trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to Epieos (the legacy `tools.epieos.com/phone.php` now redirects to epieos.com); create the account required for full features.
2. Enter the `phone` in E.164 format (or an `email` for the reverse-email lookup).
3. Read the results: services where the identifier is registered, any linked Google account/profile photo, display name, and connected accounts.
4. Free tier covers reverse-email basics; phone lookups/deeper results consume credits.
5. Pivot: a linked name/photo feeds reverse-image/face and people-search; connected accounts feed `[[sherlock]]`/manual review; a Google hit corroborates the email.

## Inputs → Outputs
- **In:** `phone` (E.164) or `email`
- **Out:** services the identifier is registered on, linked `name`, profile `image`, connected `social-profile`s
- **Empty/negative result looks like:** no registered services / no linked account — the number/email is unused online, is a burner, or checks were inconclusive. "Not found" isn't proof the person has no phone/email.

## Gotchas & OpSec
- Human-in-the-loop: **payment-wall-partial** — account required; phone/deep lookups are credit-based.
- OpSec: **passive** from your side (server-side checks); never proceed into any real account-recovery step.
- "Registered" ≠ actively used, and coverage of services shifts as platforms change their check surfaces. Corroborate.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` (Microsoft existence) and `[[sherlock]]` — Epieos maps an email/phone to services and a name; the others confirm specific platforms and spread a handle.

## Trust & verifiability
`trust: trusted` — a professional, widely-used OSINT service. Results are strong existence indicators; still verify a linked name/photo against an independent source before attributing identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | epieos-check-phone-usage |
| category | phone |
| selectorsIn → selectorsOut | phone, email → name, social-profile, image |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
