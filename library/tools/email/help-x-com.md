---
id: help-x-com
name: help.x.com
description: Use when an X (Twitter) account tied to a person of interest is compromised and you need the official recovery/help procedure — not an OSINT search tool.
url: https://help.x.com/en/safety-and-security/x-account-compromised
category: email
path:
- email
bestFor: Reference to X's official "account compromised" help article.
selectorsIn:
- social-profile
selectorsOut: []
status: live
pricing: free
costNote: Free help/support article.
opsec: passive
opsecNote: Reading a public help page leaks nothing about the target.
humanInLoop: true
humanInLoopReason:
- manual-review
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: This is X's official help/recovery documentation, not an investigative tool. Harvested from a "Hacked / Breached Account Sites" list; it does not search or enrich data, so it cannot be verified as a useful OSINT lookup.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- hackedaccounts
- Hacked / Breached Account Sites
relatedTools: []
source: uk-osint
lastVerified: ''
enrichment: full
---

# help.x.com

> X (Twitter)'s official help article for recovering a compromised account — a support/reference page, not an OSINT search tool.

## When to use
Only when you (or a family member with legitimate access) need X's official procedure to recover or report a compromised account connected to a missing person — e.g. to regain access to a `social-profile` that may hold messages or contacts. It does not search, enrich, or return data about a target.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://help.x.com/en/safety-and-security/x-account-compromised.
2. Follow X's documented steps to recover/report the account (requires the legitimate owner's access and verification).
3. There is no query field and no investigative output.

## Inputs → Outputs
- **In:** none investigative (you bring an account you have a right to recover)
- **Out:** procedural guidance only
- **Empty/negative result looks like:** n/a — it is documentation, not a lookup.

## Gotchas & OpSec
- This is NOT a data source. It was harvested from a "Hacked / Breached Account Sites" link list but is just X's support page.
- Human-in-the-loop: recovery requires account login / X's manual review and proof of ownership.
- OpSec: passive; reading the page reveals nothing about any target.

## Trust & verifiability
`trust: unverified` — official X documentation, but it provides no searchable/investigative capability, so its value as an OSINT tool cannot be established. Treat as a reference link only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | help-x-com |
| category | email |
| selectorsIn → selectorsOut | social-profile → (none) |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review, account-login) |
