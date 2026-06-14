---
id: snov-io
name: Snov.io
description: Use when you have a name + company/domain and want to find and verify the person's email address — returns candidate emails with deliverability status.
url: https://snov.io/email-finder
category: email
path:
- email
bestFor: Finding and verifying a person's professional email from their name and employer/domain.
selectorsIn:
- name
- domain
- employer-org
selectorsOut:
- email
status: live
pricing: freemium
costNote: Free account gives a small monthly credit allowance for finds/verifies; larger volumes and API need a paid plan.
opsec: passive
opsecNote: Lookups hit Snov.io's index and SMTP verification, not the subject's inbox directly; verification pings the recipient mail server but does not send a visible message. Requires account login, so your activity is tied to your Snov.io account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial email-finder/verifier widely used in sales and OSINT; results are generally reliable but coverage skews to business/professional addresses.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases: []
tags:
- email
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Snov.io

> Email finder and verifier — turns a name + domain into a verified, deliverable email address.

## When to use
You have a `name` plus an `employer-org` or `domain` for a missing person (or someone connected to the case) and need their actual `email`. Also use it to verify whether a guessed/constructed address is live before relying on it for breach lookups or contact.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register and log in at https://snov.io/email-finder.
2. Use "Domain Search" to list addresses for a company, or "Email Finder" with first/last name + domain to target one person.
3. Read the result: each address comes with a verification status (valid / risky / invalid) and confidence.
4. Pivot: a verified `email` feeds breach search engines, `[[skymem]]`, and username correlation; a "valid" status confirms an inferred address pattern.

## Inputs → Outputs
- **In:** `name`, `domain`, `employer-org`
- **Out:** `email` (with deliverability/verification status)
- **Empty/negative result looks like:** "no email found" or all candidates marked invalid/unknown — common for personal (non-corporate) identities.

## Gotchas & OpSec
- Strongest for business/professional addresses; weak for purely personal Gmail/Outlook identities.
- Credits are consumed per find/verify on the free tier.
- Human-in-the-loop: account login required, so activity is logged to your account — use a dedicated investigative account.
- OpSec: passive to the subject, but SMTP verification touches the destination mail server.

## Overlaps ("do both")
- Pairs with `[[skymem]]` (which reveals a domain's address pattern) — use Skymem for the pattern, Snov.io to verify the specific constructed address. See also `[[snov-io-2]]` (same service, browser-extension workflow).

## Trust & verifiability
`trust: community` — widely used commercial tool with a solid track record; verify edge-case results, as no finder is exhaustive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snov-io |
| category | email |
| selectorsIn → selectorsOut | name, domain, employer-org → email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
