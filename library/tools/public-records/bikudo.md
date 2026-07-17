---
id: bikudo
name: Bikudo
description: Use when you have a company/product `name` and want manufacturer/supplier business listings and contact details — returns company profiles, `address`, and contact `email`/`phone`.
url: https://www.bikudo.com
category: public-records
path:
- public-records
bestFor: Looking up manufacturers and suppliers (often Asian B2B) and their business contact details.
selectorsIn:
- name
- employer-org
selectorsOut:
- address
- email
- phone
status: live
pricing: freemium
costNote: Browsing and searching the directory is free; registration is only needed to list your own company. Contact details on listings are free to view.
opsec: passive
opsecNote: Reading public business listings is passive and reveals nothing to the company. Only creating an account or contacting a supplier is active — use a sock-puppet identity if you do.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A self-listing B2B directory: companies add their own profiles, so details are self-reported and unverified — corroborate before relying on them.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- bikudo.com business directory
tags:
- business-directory
- b2b
- suppliers
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Bikudo

> A self-listing B2B directory of manufacturers and suppliers — a way to attach a company name to a business profile, address, and contact details, weighted toward Asian trade.

## When to use
You have a company or product `name` (a supplier on an invoice, a manufacturer stamped on a product, a business a subject is tied to) and want a business profile with contact details. Bikudo lists manufacturers/suppliers across dozens of categories, each with a company profile, location, and contact info — useful for attributing a business `name` to an `address`, `email`, or `phone`, or for corroborating that a claimed company exists.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.bikudo.com and search by company `name`, product, or browse by category.
2. Open a company profile and read the details: business name, location (`address`), listed contact `email`/`phone`, and product catalog.
3. Cross-check the details against other business registries — self-listed profiles are unverified.
4. Pivot: a contact email/phone feeds email/phone OSINT; a company address feeds registry and map lookups to confirm the business is real.

## Inputs → Outputs
- **In:** company/product `name` or `employer-org`.
- **Out:** business profile — `address`, contact `email`/`phone`, product listings.
- **Empty/negative result looks like:** no listing — the company hasn't self-registered here (very common; it's opt-in). Absence says nothing about whether the company exists.

## Gotchas & OpSec
- Self-listed and unverified: profiles can be stale, promotional, or fabricated. Never treat a listing as proof of a legitimate business.
- Heavily weighted toward manufacturers/suppliers (often China/Asia) — thin coverage elsewhere.
- Contact details may be shared marketing addresses, not a specific individual.

## Overlaps ("do both")
- Corroborate any listing against official company registries and WHOIS for the company's domain; combine with map/satellite tools to check the address is a real premises.

## Trust & verifiability
`trust: community` — an opt-in self-listing directory. Data is self-reported, so it's a lead source only; verify every detail against an authoritative registry before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bikudo |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → address, email, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
