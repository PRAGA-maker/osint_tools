---
id: justgetmydata-com
name: justgetmydata.com
description: Use when you have a `name`/`username` on a known service and want the direct data-access/subject-access route for that service — returns a link to obtain that account's held data (social-profile).
url: https://justgetmydata.com/
category: social-networks
path:
- social-networks
bestFor: A directory of direct links and instructions for exercising data-access (subject-access) rights on hundreds of online services.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Completely free directory; the underlying data requests to each service are also free (a statutory data-access right in many jurisdictions).
opsec: passive
opsecNote: Browsing the directory is passive. The critical caveat: actually requesting data via these links requires logging into (or emailing as) the account holder — this is an account-holder/legal action, NOT covert OSINT on a third party. Only use it against accounts you are authorized to access (your own, or a missing person's account where you have lawful authority/consent).
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained sister project to JustDeleteMe; the links and instructions are curated and generally accurate, but service processes change and it is not an official channel.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- justdeleteme
aliases:
- Just Get My Data
- justgetmydata
tags:
- gsocialmedia
- General Social Media Sites
- data-access
- gdpr
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# justgetmydata.com

> A directory of direct links and instructions for pulling the data a service holds on an account — the fast route to exercise data-access (subject-access) rights, rated by difficulty per service.

## When to use
This is a **data-subject-access** aid, not a tool for covertly profiling a third party. Its legitimate investigative use is when you (or, in a missing-persons context, a family member/legal authority acting for the subject with proper consent/authority) can access a specific account and want to extract everything the service holds on it — messages, login history, contacts, media. Use it when you have lawful access to `username`/`name` accounts and want the official export path rather than scraping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://justgetmydata.com/ and find the service (Google, Facebook, Instagram, etc.).
2. Read the entry: a direct link to that service's data-download page, step-by-step instructions, and a difficulty rating (easy → impossible).
3. Following the link requires signing in as (or emailing as) the account holder — do this only for accounts you're authorized to access.
4. Submit the data request; the service returns an export (often by email, sometimes after a delay).
5. Use the exported data as primary-source material: contacts and messages surface `associate`s, login/IP history surfaces devices/locations.

## Inputs → Outputs
- **In:** a known service + authorized account (`username`/`name`)
- **Out:** the official data export the service holds on that account (`social-profile` data, contacts, history) — via the account holder's own access
- **Empty/negative result looks like:** a service rated "impossible/limited" with no self-service export, or a request that returns little — some services provide minimal data or none.

## Gotchas & OpSec
- **Not third-party OSINT:** these requests authenticate as the account owner. Using them against someone else's account without authority is unlawful — restrict to your own accounts or lawful, consented missing-persons access.
- Legal gate: data-access rights and processes vary by jurisdiction and service; the directory's instructions can lag behind service changes.
- OpSec: browsing is passive; the request step is an attributable, authenticated action by the account holder.

## Overlaps ("do both")
- Pairs with [[justdeleteme]] (the sister directory for account *deletion* links) — both index per-service account-management routes; JustGetMyData is the data-export side.

## Trust & verifiability
`trust: community` — a well-regarded community directory. Links/instructions are curated but unofficial and can drift; the data you receive comes straight from the service, so it's authoritative once obtained.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | justgetmydata-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, legal-gate) |
