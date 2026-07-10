---
id: manycontacts-mail-check
name: ManyContacts Mail Check
description: Use when you have an `email` and want to know if it's valid/deliverable before pivoting on it — returns an existence/deliverability verdict, not a person profile.
url: https://www.manycontacts.com/en/mail-check
category: people-search
path:
- people-search
bestFor: Quickly validating whether an email address exists/is deliverable (syntax, domain, mailbox) to confirm a lead is worth pursuing.
selectorsIn:
- email
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free single-email check in the browser; no account needed for a basic lookup.
opsec: passive
opsecNote: Validation is done server-side by ManyContacts against the mail domain (SMTP-level checks), not by you emailing the target, so the person isn't messaged. Still, you disclose the address to a third-party vendor — use a sock-puppet context.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A marketing/email tool, not a people-search despite the seed category; deliverability verdicts are heuristic (catch-all domains and greylisting cause false positives/unknowns), so treat "valid" as probabilistic.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- account-live-com
aliases:
- ManyContacts Mail Check
- manycontacts.com mail check
tags:
- people-search
- email-verification
- deliverability
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# ManyContacts Mail Check

> A free email-verification tool — checks whether an address is syntactically valid and its mailbox likely deliverable. Despite the "people search" tag, it validates an email; it does **not** profile a person.

## When to use
You have an `email` and want to know if it's real/deliverable before investing in it — e.g. a candidate address from a guess, a breach, or a form. A "valid/deliverable" verdict says the mailbox probably exists (worth pivoting on); "invalid" says don't waste time. Use it as a cheap gate ahead of heavier email OSINT, not as a source of the owner's identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.manycontacts.com/en/mail-check and enter the `email`.
2. Run the check; read the verdict (valid / invalid / unknown) based on syntax, domain MX, and SMTP mailbox probing.
3. Treat "valid" as probable-exists, "unknown"/catch-all as inconclusive, "invalid" as a dead address.
4. Don't over-trust a single verdict on catch-all domains — cross-check with another validator.
5. Pivot: a validated address goes to account-existence and breach tooling — e.g. `[[account-live-com]]` for a Microsoft check — and to username/social pivots on the local-part.

## Inputs → Outputs
- **In:** `email`
- **Out:** `metadata-exif`-style verdict — valid / invalid / unknown (syntax, domain, mailbox signals)
- **Empty/negative result looks like:** "invalid" (dead/typo'd) or "unknown"/catch-all (domain accepts anything, so can't confirm) — neither profiles the person; "unknown" is not a yes or a no.

## Gotchas & OpSec
- It's an **email validator**, not a people-search — no name/address/associates come out of it (the seed category is misleading).
- Catch-all domains and greylisting produce false "valid"/"unknown"; corroborate with a second checker for important leads.
- OpSec: passive (server-side SMTP check); you hand the address to a third-party vendor.

## Overlaps ("do both")
- Validate first, then enrich: pair with `[[account-live-com]]` (Microsoft existence) and breach-search tools — this gates the address, those tell you what's tied to it.

## Trust & verifiability
`trust: unverified` — a heuristic deliverability checker; a "valid" verdict is probabilistic, so confirm existence via a second method before building on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | manycontacts-mail-check |
| category | people-search |
| selectorsIn → selectorsOut | email → metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
