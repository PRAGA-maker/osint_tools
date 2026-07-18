---
id: oh365userfinder
name: Oh365UserFinder
description: Use when you have an `email` and want to confirm it is a valid Microsoft 365 account — returns account existence (email validity).
url: https://github.com/dievus/Oh365UserFinder
category: social-networks
path:
- social-networks
bestFor: Validating whether one email (or a whole list) corresponds to a real Office/Microsoft 365 account, without alerting the owner.
selectorsIn:
- email
selectorsOut:
- email
- employer-org
status: live
pricing: free
costNote: Free and open-source (Python, GitHub); no account or key required.
opsec: active
opsecNote: It queries Microsoft's login/GetCredentialType endpoint about the target address. This is unauthenticated enumeration Microsoft may log; it does NOT notify the account owner, but tenant admins may see anomalous validation traffic. Run from a sock-puppet IP and keep volume low to avoid tripping tenant defenses.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool (dievus); relies on Microsoft's own account-validation response, so a positive is a reliable existence signal.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- account-live-com
- dork-dump
- geemail-user-finder
- mayorsecdnsscan
aliases:
- Oh365UserFinder
- dievus/Oh365UserFinder
tags:
- office365
- account-enumeration
- email
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Oh365UserFinder

> A Python enumerator that asks Microsoft "is this a real 365 account?" for one email or a whole list — a fast, quiet email-validity oracle for corporate/Microsoft targets.

## When to use
You have an `email` (or many) and need to know which addresses are live Microsoft/Office 365 accounts before investing effort. A positive confirms the address is real and Microsoft-backed — strong corroboration that a corporate/organizational identity exists — and lets you prune invalid guesses from an email-permutation list. Especially useful when a subject is tied to an organization on Microsoft 365.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and set up: `git clone https://github.com/dievus/Oh365UserFinder && pip install -r requirements.txt`.
2. Single check: `python3 oh365userfinder.py -e target@company.com`.
3. Bulk check: `python3 oh365userfinder.py -r emails.txt` (one address per line) to validate a whole list.
4. Read the output — each address is flagged VALID (a real 365 account) or not.
5. Pivot: valid addresses → mailbox/tenant OSINT, breach-DB lookups, and `[[account-live-com]]` for consumer-Microsoft cross-checks; the tenant/domain → `employer-org` confirmation.

## Inputs → Outputs
- **In:** `email` (single or a text-file list)
- **Out:** account-exists boolean per address (validates the `email`); implies the `employer-org`/tenant is on Microsoft 365
- **Empty/negative result looks like:** the address returns "not found"/invalid — meaning it is not a Microsoft 365 account (not proof the person has no email elsewhere), or Microsoft has rate-limited/changed the endpoint (throttle and retry).

## Gotchas & OpSec
- This is **active** enumeration against Microsoft's infrastructure — unauthenticated and not owner-notifying, but logged; keep volume low and use a sock-puppet egress.
- Microsoft periodically changes the validation endpoint/behavior; a sudden all-negative run can mean the technique broke, not that accounts vanished — check for an updated release.
- Consumer Outlook/Hotmail differ from tenant 365 — pair with `[[account-live-com]]` for the consumer side.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` — that confirms consumer Microsoft accounts and leaks masked recovery hints; Oh365UserFinder is built for organizational 365 tenants and bulk lists. Together they cover both halves of the Microsoft ecosystem.

## Trust & verifiability
`trust: community` — an open-source tool, but the signal comes from Microsoft's own endpoint, so a VALID result is a reliable existence check; treat negatives cautiously (technique breakage vs true absence).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oh365userfinder |
| category | social-networks |
| selectorsIn → selectorsOut | email → email, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
