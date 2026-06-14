---
id: disposable-emails-registry
name: Disposable Emails Registry
description: Use when you have an email domain and want to know if it is a disposable/throwaway provider — returns a yes/no plus a full domain blocklist.
url: https://disposable-emails.github.io/
category: email
path:
- email
- email-verification
bestFor: Flagging whether an email address uses a known disposable/throwaway domain.
selectorsIn:
- email
- domain
selectorsOut:
- metadata
status: live
pricing: free
costNote: Free static list hosted on GitHub Pages; no account.
opsec: passive
opsecNote: You download or read a static list; the target's provider is never contacted, so the lookup leaks nothing to them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open community-maintained domain list on GitHub Pages; coverage depends on volunteer submissions and can lag new disposable services.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- email-verification
- disposable
source: arf-seed
lastVerified: ''
enrichment: full
---

# Disposable Emails Registry

> A community-maintained blocklist of disposable/throwaway email domains, served as a plain static list.

## When to use
You have an `email` (or just its `domain`) for a missing person, a tipster, or an account of interest and want to know whether it belongs to a disposable provider (Mailinator, Guerrilla Mail, 10minutemail, etc.). A disposable hit tells you the address is likely throwaway — low value for long-term pivoting and a sign the owner wanted to stay anonymous. A miss suggests a real, persistent mailbox worth pivoting on with breach/username tooling.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://disposable-emails.github.io/.
2. Take the domain portion of the email (after the `@`).
3. Either search the page/list or open the raw list (commonly `/list.txt` on the project) and check whether the domain appears.
4. Pivot: if it is NOT disposable, treat the address as durable and move to `[[email-breach-analysis]]`, `[[email-dossier]]`, or username pivoting; if it IS disposable, deprioritize the address as an identity anchor.

## Inputs → Outputs
- **In:** `email` / `domain`
- **Out:** boolean disposable verdict (`metadata`); the full domain list is downloadable for bulk checks.
- **Empty/negative result looks like:** domain not present in the list — meaning "not known-disposable," not "confirmed real." Absence is weak evidence given list lag.

## Gotchas & OpSec
- Human-in-the-loop: none — no captcha or login.
- OpSec: fully passive; you never touch the target's mail provider.
- The list lags new disposable services, so a "clean" result can be a false negative. Cross-check with a verifier if it matters.

## Overlaps ("do both")
- Pairs with `[[email-address-verifier]]` and `[[email-address-validator]]`, which test deliverability and flag disposable/role addresses live where this only checks a static domain set.

## Trust & verifiability
`trust: community` — open volunteer-maintained list on GitHub Pages; transparent and auditable, but completeness is not guaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | disposable-emails-registry |
| category | email |
| selectorsIn → selectorsOut | email, domain → metadata |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
