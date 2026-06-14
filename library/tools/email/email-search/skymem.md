---
id: skymem
name: Skymem
description: Use when you have a company domain (or person + domain) and want to find associated email addresses and the company's address pattern — returns emails.
url: https://www.skymem.info/
category: email
path:
- email
- email-search
bestFor: Finding email addresses tied to a company domain and inferring the org's address format.
selectorsIn:
- domain
- name
- employer-org
selectorsOut:
- email
status: live
pricing: freemium
costNote: Shows a handful of emails and the domain's address pattern for free; full bulk lists require a paid plan.
opsec: passive
opsecNote: Scrapes and aggregates public email data; you query Skymem's index, not the target, so the subject is not alerted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running public email-by-domain index widely cited in OSINT lists; coverage is uneven and data can be stale.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases: []
tags:
- email
- email-search
source: arf-seed
lastVerified: ''
enrichment: full
---

# Skymem

> Email-address finder by company/domain — surfaces known addresses and the org's email pattern.

## When to use
You have an `employer-org` or `domain` connected to a missing person (a current/former employer, a business they ran) and want candidate `email` addresses, or you have a `name` and a domain and want to derive their likely work address. Useful for pivoting from a workplace lead to a contactable/searchable email identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.skymem.info/.
2. Search by domain (e.g. `company.com`) or by person name to find associated domains.
3. Read the free preview: a few sample addresses plus the dominant pattern (e.g. `first.last@company.com`).
4. Pivot: apply the discovered pattern to the target's `name` to construct a likely address, then verify it elsewhere; feed found emails into breach/username searches.

## Inputs → Outputs
- **In:** `domain`, `name`, or `employer-org`
- **Out:** `email` addresses + the org's email-format pattern
- **Empty/negative result looks like:** "no emails found" for the domain, or only generic addresses (info@, sales@) with no personal patterns.

## Gotchas & OpSec
- Free tier caps how many addresses you see; bulk extraction is paywalled.
- Data is scraped and can be outdated — a found address may be a former employee's.
- OpSec: passive; you never contact the subject. Still query from a sock-puppet session as a hygiene default.

## Overlaps ("do both")
- Pairs with dedicated email-finders/verifiers like `[[snov-io]]` — Skymem gives the pattern, a verifier confirms a specific constructed address is deliverable.

## Trust & verifiability
`trust: community` — established OSINT-community index, but coverage and freshness vary; verify any address before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skymem |
| category | email |
| selectorsIn → selectorsOut | domain, name, employer-org → email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
