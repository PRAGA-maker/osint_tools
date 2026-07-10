---
id: apollo-io
name: Apollo.io
description: Use when you have a `name`, company or `domain` and want a person's work contact details — returns business `email`, `phone`, `employer-org`, title and LinkedIn (`social-profile`).
url: https://www.apollo.io/
category: people-search
path:
- people-search
bestFor: B2B contact enrichment — resolving a professional's work email, phone, employer, and LinkedIn from a name + company, backed by a large sales-intelligence database.
selectorsIn:
- name
- employer-org
- domain
selectorsOut:
- email
- phone
- social-profile
- employer-org
status: live
pricing: freemium
costNote: Freemium sales-intelligence platform — a free plan gives limited monthly credits to reveal emails/phones; higher volume and phone numbers need paid tiers. Requires account signup.
opsec: passive
opsecNote: You query Apollo's aggregated B2B database, not the target — no notification reaches them. But you disclose the subject to a commercial vendor and, on signup, Apollo may scrape your own contacts if you connect email. Use a clean investigative account and don't grant contact access.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Large, reputable sales-intelligence vendor; data is aggregated from public/third-party sources and crowd-contributed, so contact details can be outdated or wrong — verify before use.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Apollo
- apollo.io
tags:
- people-investigations
- people-search
- b2b
- enrichment
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Apollo.io

> A sales-intelligence database repurposed for OSINT: give it a name and company and it hands back the person's work email, phone, title, and LinkedIn.

## When to use
You have a `name` plus an `employer-org`/`domain` and need the subject's professional contact details — work `email`, direct `phone`, current role, and LinkedIn. Apollo's strength is B2B/professional identities: it's excellent for corporate subjects, weak for people with no business footprint. Reach for it to turn a name-at-a-company into a reachable contact and a confirmed employer, or to enumerate people at an organization.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up for a free Apollo account (a clean investigative one; don't connect your real mailbox/contacts).
2. Use People Search: filter by `name`, company/`domain`, title, location.
3. Open a matching contact and "reveal" email/phone (this consumes credits; the free tier is limited).
4. Read the record: work `email`, `phone`, `employer-org`, job title, LinkedIn (`social-profile`), location.
5. Verify — aggregated contact data is often stale — then pivot: LinkedIn → deeper social mapping; email → breach/account checks (`[[account-live-com]]`) and `[[reversecontact]]`; employer → corporate registries.

## Inputs → Outputs
- **In:** `name`, `employer-org`, `domain`
- **Out:** `email` (work), `phone`, `social-profile` (LinkedIn), `employer-org`, job title, location
- **Empty/negative result looks like:** no match or a contact with locked/empty email/phone — the person isn't in Apollo's B2B data (common for non-corporate individuals), or you're out of reveal credits. A miss isn't proof the person doesn't exist, just that they're not in this dataset.

## Gotchas & OpSec
- **B2B bias:** great for professionals, poor for people without a work/company footprint.
- **Stale data:** emails/phones can be old or mis-attributed — verify (a quick send-test or cross-source check) before relying.
- Don't connect your real email on signup — Apollo can harvest your contacts.
- OpSec: **passive** toward the target; you disclose them to a vendor and need an account.

## Overlaps ("do both")
- Pairs with `[[reversecontact]]` and Hunter-style tools (email↔identity), and with `[[skopenow-com]]` for broader people-search. Apollo is contact-detail-first; those add different angles.

## Trust & verifiability
`trust: community` — a major commercial vendor, but its contact data is aggregated and crowd-sourced with a real error rate. Treat revealed emails/phones as leads and confirm against a primary source (LinkedIn, company site) before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | apollo-io |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org, domain → email, phone, social-profile, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
