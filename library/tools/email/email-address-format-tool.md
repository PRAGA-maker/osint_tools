---
id: email-address-format-tool
name: Email Address Format Tool
description: Use when you have a company `domain` (and maybe a `name`) and want the organization's likely email pattern — returns the email format and sample `email`s to construct or verify an address.
url: http://email-format.com
category: email
path:
- email
bestFor: Discovering an organization's email-address pattern (e.g. first.last@) to build or confirm a target's likely work email.
selectorsIn:
- domain
- name
selectorsOut:
- email
status: live
pricing: free
costNote: Free lookups on email-format.com; a paid/API tier exists for bulk or programmatic use.
opsec: passive
opsecNote: Looking up a domain's public email pattern is passive — you query email-format.com, not the target or their mail server, so nothing is sent to the subject. Constructing an address is inference; verifying it (SMTP/other tools) is a separate, more active step you should do knowingly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running aggregator of observed email formats per domain; patterns are inferred from public samples and can be outdated or have exceptions.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- email-format.com
tags:
- toddington
- curated-directory
- email-addresses
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- email-format
---

# Email Address Format Tool

> email-format.com — enter a company domain and see the email pattern its people use (first.last@, flast@, etc.), plus sample addresses.

## When to use
You know where your subject works (their company `domain`) and want to construct or confirm their likely work `email`. Given a `name` + the organization's format, you can derive a probable address to feed into breach checks, account-existence tools, and email OSINT. Also useful to sanity-check an email you already have against the org's known pattern.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://email-format.com and enter the company `domain` (e.g. `example.com`).
2. Read the reported format(s) and sample addresses observed for that domain (first.last@, f.last@, firstl@, etc.).
3. Apply the pattern to your subject's `name` to build the candidate `email`.
4. Note multiple/ambiguous patterns — larger orgs sometimes use several; treat the output as candidates.
5. Pivot: verify candidates with account-existence tools (`[[account-live-com]]`, `[[holehe]]`) and breach checks (`[[h8mail-trace-labs-fork]]`).

## Inputs → Outputs
- **In:** company `domain` (optionally a `name` to apply the pattern to)
- **Out:** the domain's email format(s) and sample `email`s → a constructed candidate address
- **Empty/negative result looks like:** no data for the domain, or conflicting formats — common for small orgs or those using multiple patterns. A constructed address is a guess until verified; don't treat it as confirmed.

## Gotchas & OpSec
- Patterns are inferred from observed samples and can be stale or have per-person exceptions (nicknames, duplicate-name suffixes).
- Constructing an address is passive; *verifying* it (SMTP probing, sending) is more active — do that deliberately.
- Personal webmail (Gmail/Outlook) has no org pattern; this only helps for corporate domains.

## Overlaps ("do both")
- Pairs with `[[hunter-io]]` (finds actual published addresses for a domain) and account-existence tools — email-format gives the pattern, Hunter gives confirmed addresses, and existence tools validate your constructed guess.

## Trust & verifiability
`trust: community` — a useful pattern aggregator, but outputs are inferred and must be verified before you rely on any constructed address.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-address-format-tool |
| category | email |
| selectorsIn → selectorsOut | domain, name → email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
