---
id: kaspr-io
name: Kaspr
description: Use when you have a LinkedIn profile (`social-profile`)/`name` and want that person's direct contact details — returns `email`, `phone` and `employer-org` via a browser extension over LinkedIn. Paid/freemium.
url: https://www.kaspr.io
category: social-networks
path:
- social-networks
bestFor: Extracting a professional's email and (mobile) phone number directly from their LinkedIn profile via a Chrome extension, backed by a B2B contact database.
selectorsIn:
- social-profile
- name
selectorsOut:
- email
- phone
- employer-org
status: live
pricing: freemium
costNote: Freemium — a limited free credit allowance to reveal contacts, with paid plans for volume (especially phone numbers). Requires account signup and (for the main workflow) a LinkedIn login plus the browser extension.
opsec: active
opsecNote: The core workflow runs a browser extension while you view the target's LinkedIn as a logged-in user — LinkedIn can see the profile visit and may flag scraping-like automation. Use a sock-puppet LinkedIn account and a clean profile, never your real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: A commercial LinkedIn-prospecting/contact-enrichment vendor. Contact data is aggregated/crowd-sourced, so emails and especially mobile numbers can be wrong or outdated — verify before use.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- kaspr.io
- Kaspr LinkedIn
tags:
- linkedin
- contact-enrichment
- social-networks
- b2b
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Kaspr

> A LinkedIn contact-reveal extension: open someone's profile and Kaspr surfaces their work email and mobile number from its B2B database.

## When to use
You have a subject's LinkedIn (`social-profile`) or a `name`+company and need their direct contact details — `email` and, notably, a **mobile phone** number. Kaspr's niche is turning a LinkedIn identity into reachable contacts, which is valuable when you've confirmed who someone is professionally and now need a way to contact or further pivot on them. Best for corporate/professional targets; weak for people without a LinkedIn/business footprint.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Create a Kaspr account (free tier gives limited reveal credits) and install its Chrome extension.
2. Log into a **sock-puppet** LinkedIn account and open the target's LinkedIn profile.
3. Trigger Kaspr on the profile — it matches the person against its database and reveals available `email`(s) and `phone`(s), consuming credits.
4. Read the output: work/personal email, mobile/direct phone, and `employer-org`/title context.
5. **Verify** the contact (data is often stale), then pivot: email → breach/account checks and `[[reversecontact]]`; phone → phone-OSINT/carrier lookup; employer → registries.

## Inputs → Outputs
- **In:** `social-profile` (LinkedIn) or `name` + company
- **Out:** `email`, `phone` (incl. mobile where available), `employer-org`, title
- **Empty/negative result looks like:** "no contact found" / locked fields — the person isn't in Kaspr's data, or you're out of credits. A miss is common for non-corporate individuals and doesn't mean the person lacks contact details.

## Gotchas & OpSec
- **LinkedIn exposure:** the extension operates inside your logged-in LinkedIn session — profile visits are visible and automation can get accounts restricted. Puppet account essential.
- **Accuracy:** aggregated emails and especially mobile numbers are frequently outdated/mismatched — verify before contacting.
- Freemium credits are limited; phones usually cost more.
- OpSec: **active** — tied to your LinkedIn session and Kaspr account.

## Overlaps ("do both")
- Pairs with `[[apollo-io]]` and Hunter/RocketReach-style tools — different databases, so contact coverage differs; cross-check a revealed email/phone across two before trusting it.

## Trust & verifiability
`trust: community` — a legitimate commercial vendor, but contact data is aggregated with a real error rate; treat reveals as leads and confirm against a primary source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kaspr-io |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, name → email, phone, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
