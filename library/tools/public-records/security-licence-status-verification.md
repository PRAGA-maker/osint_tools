---
id: security-licence-status-verification
name: Security Licence Status Verification (BC)
description: Use when you have a `name`, business name or licence number and want to confirm a British Columbia security-worker/business licence — returns licence status from the official BC registry.
url: https://justice.gov.bc.ca/security/utilities/
category: public-records
path:
- public-records
bestFor: Verifying whether a person or company holds a valid BC (Canada) security-worker or security-business licence.
selectorsIn:
- name
- employer-org
- document-id
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free public verification utility from the BC government; no account needed to look up a licence status.
opsec: passive
opsecNote: An official government lookup; querying a licence does not notify the licence holder. Only the government-run platform at justice.gov.bc.ca is authoritative — beware lookalike/phishing sites. Use a sock-puppet browser for hygiene, though the query itself is not attributed to your subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the BC Ministry of Public Safety's Security Programs Division — the authoritative source for BC security-industry licence status. First-party government data.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- clicklaw
- cso
- search-for-open-information-documents
- search-the-open-information-catalogue
aliases:
- BC Security Services Platform licence lookup
- Security Programs Division verification
tags:
- public-records
- licensing
- canada
- bc
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Security Licence Status Verification (BC)

> The British Columbia government's official utility to check whether a security worker or security business holds a valid provincial licence — an authoritative status lookup, not a marketing directory.

## When to use
You have a `name`, company name, or a licence `document-id` and want to confirm a person or firm is a licensed BC security worker/business, and in good standing. Useful for vetting someone who claims to work in the BC security industry (guard, alarm/locksmith, private investigator, etc.), corroborating employment, or checking a business's credentials. Because it is first-party government data, a positive result is authoritative for the fact of licensing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://justice.gov.bc.ca/security/utilities/ (the official BC Security Services Platform; let the app load).
2. Use the licence-lookup/verification utility — search by licensee name, business name, or licence number.
3. Read the returned status (valid/expired/suspended, licence class, and the licensee/business name).
4. Confirm you are on the genuine `justice.gov.bc.ca` domain — only that platform is authoritative; avoid lookalikes.
5. Pivot: a confirmed licence ties a `name` to an `employer-org`/role and a licence `document-id` you can cite; a lapsed/suspended status is itself a lead.

## Inputs → Outputs
- **In:** `name` / `employer-org` / licence `document-id`
- **Out:** licence status, licence class, licensee `name` / `employer-org`, licence `document-id`
- **Empty/negative result looks like:** no matching licence — the person/company isn't BC-licensed under that name/number, licenses in another province, or spells the name differently. Absence is specific to BC's registry.

## Gotchas & OpSec
- Human-in-the-loop: none for a status lookup; applying/managing a licence (a different function on the platform) needs a BC Services Card/BCEID, which you would not use for OSINT.
- OpSec: **passive**; the licensee is not notified. The main risk is phishing lookalikes — verify the government domain.
- Scope is British Columbia only; other provinces/countries have separate registries.

## Overlaps ("do both")
- Pairs with other BC public-records tools ([[cso]], [[clicklaw]]) and with equivalent provincial security-licensing registries for subjects outside BC.

## Trust & verifiability
`trust: trusted` — first-party BC government data from the Security Programs Division; the authoritative source for whether a BC security licence exists and its current status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | security-licence-status-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, document-id → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
