---
id: mylostaccount-org-uk
name: mylostaccount.org.uk
description: Use when you (as holder, next of kin, or executor) need to trace a dormant UK bank, building society, or NS&I account for a person — returns an employer-org/provider match by name and address.
url: https://www.mylostaccount.org.uk/search
category: financial-crypto
path:
- financial-crypto
bestFor: The official free UK route to trace lost or dormant bank, building society, and NS&I accounts for a named person.
selectorsIn:
- name
- address
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free official service run jointly by UK Finance, the Building Societies Association, and NS&I. There is never a fee — treat any site charging for this as a scam.
opsec: passive
opsecNote: You must create an online profile and submit a claim, so this is only for legitimate holders/estates — the application is forwarded to the named provider(s), who respond by email or letter. It is not a covert lookup; only use it where you have a lawful basis (your own account, or as next of kin/executor).
humanInLoop: true
humanInLoopReason:
- account-login
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by UK Finance, the BSA, and NS&I — the authoritative UK dormant-account tracing scheme, not a third-party data broker.
missingPersonsRelevance: medium
coverage:
- uk
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- My Lost Account
- mylostaccount.org.uk
tags:
- financial-crypto
- dormant-accounts
- uk
- asset-tracing
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# mylostaccount.org.uk

> The UK's single official service for reuniting people (and estates) with lost or dormant bank, building society, and NS&I accounts — free, and the legitimate alternative to fee-charging "asset finders."

## When to use
You are handling a person's finances with a lawful basis — your own dormant account, or acting as next of kin/executor for a missing or deceased person — and need to find accounts they may have forgotten. Given a `name` and former `address`, My Lost Account routes a tracing request to the relevant UK providers. This is asset tracing you have standing to do, not covert surveillance of a third party.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.mylostaccount.org.uk/search and set up an online profile.
2. Complete the search form with the account holder's details (names used, addresses, approximate dates, and any known institutions).
3. Submit — your application is forwarded to the selected provider(s) across the banking, building society, and NS&I schemes.
4. Await the result: each provider replies by email or letter confirming a match (and next steps to reclaim) or no trace. Pivot: a confirmed provider (`employer-org` in the sense of the institution) tells you where assets sit; combine with probate/estate paperwork.

## Inputs → Outputs
- **In:** `name` (and prior names), `address` (current and former)
- **Out:** `employer-org` (the bank/building society/NS&I holding a matched account), plus reclaim instructions
- **Empty/negative result looks like:** each provider returns "no account found" — the person may hold nothing dormant with covered institutions, used a spelling/address you didn't supply, or the account isn't in scope.

## Gotchas & OpSec
- Human-in-the-loop: yes — you register an account, submit a formal claim, and providers manually review and respond over days/weeks. It is not an instant lookup.
- OpSec: this is an identified request tied to a legitimate claim, not a passive OSINT query — only use it where you have legal standing. Providers verify identity before releasing funds.
- Scam awareness: the service is always free. Anyone charging a percentage to "find lost accounts" is exploiting this free scheme.

## Overlaps ("do both")
- Complements probate/estate research and unclaimed-asset registers — My Lost Account covers UK banks/building societies/NS&I, while separate registers cover pensions, insurance, and Premium Bonds.

## Trust & verifiability
`trust: trusted` — it is the official joint scheme of UK Finance, the Building Societies Association, and NS&I; results come directly from the account providers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mylostaccount-org-uk |
| category | financial-crypto |
| selectorsIn → selectorsOut | name, address → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, manual-review) |
