---
id: contacthelp-com
name: contacthelp.com
description: Use when you want company customer-service contact details (phone, support email); despite its breach-site tag it is a consumer contact directory, not a breach lookup — returns business contact info, not personal breach data.
url: http://www.contacthelp.com/index.php
category: email
path:
- email
bestFor: Looking up a company's customer-support contact channels.
selectorsIn:
- employer-org
selectorsOut:
- phone
- email
status: unknown
pricing: free
costNote: Free directory of business contact info; no account required.
opsec: passive
opsecNote: Browsing a public business directory leaks nothing about your subject and contacts no one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Harvested under "Hacked / Breached Account Sites" but the site is a consumer customer-service contact directory, not a breach search engine — almost certainly mis-categorised by the source. Low investigative value for missing persons.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- contact-directory
- reference
source: uk-osint
lastVerified: ''
enrichment: full
---

# contacthelp.com

> A consumer-facing directory of company customer-service contacts — mis-tagged as a breach site; it does not search leaked data.

## When to use
You need a business's support `phone`/`email` (e.g. to contact a company that held records about a subject). It indexes companies, not people, and does **not** take an `email`/`username` to search breaches. For breach lookups use a real aggregator instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site and search/browse by company name (`employer-org`).
2. Read the listed customer-support phone numbers and contact channels.
3. Pivot: use a recovered support channel to make a lawful records request to that organisation; this is not a selector-pivot tool.

## Inputs → Outputs
- **In:** `employer-org` (company name)
- **Out:** business `phone` / `email` support contacts
- **Empty/negative result looks like:** company not listed — the directory is consumer-brand oriented and far from comprehensive.

## Gotchas & OpSec
- Category mismatch: this is **not** a breach/hacked-account site despite the harvested tag. Do not use it to check whether an email was leaked.
- Coverage skews US consumer brands; investigative value for missing-persons work is low.
- OpSec: passive — public directory browsing only.

## Trust & verifiability
`trust: unverified` — utility and currency of its listings are unconfirmed, and it is mis-categorised in the source directory. Verify any contact detail directly with the company.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | contacthelp-com |
| category | email |
| selectorsIn → selectorsOut | employer-org → phone, email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
