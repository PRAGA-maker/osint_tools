---
id: optout-credit-prescreen
name: OptOutPrescreen
description: Use when you (the investigator) want to reduce your own `name`/`address` exposure to prescreened credit/insurance offers — the official US bureau opt-out, not a lookup tool.
url: https://www.optoutprescreen.com/?rf=t
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- privacy-clean-up
bestFor: Opting your own identity out of the four US credit bureaus' prescreened firm-offer lists to shrink your data-broker footprint.
selectorsIn:
- name
- address
selectorsOut: []
status: live
pricing: free
costNote: Free official service; the 5-year opt-out is done online at no cost, a permanent opt-out requires mailing a signed form.
opsec: active
opsecNote: This is a personal-privacy hygiene action for the INVESTIGATOR, not something to run against a subject. It requires submitting your own real name, address, SSN, and DOB to the bureaus — never enter a third party's data here.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official industry opt-out site jointly operated by Equifax, Experian, Innovis, and TransUnion — the authoritative endpoint, not a third-party broker.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- optoutprescreen.com
- prescreen opt-out
tags:
- privacy
- opsec
- data-broker-removal
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# OptOutPrescreen

> The official US credit-bureau opt-out for prescreened credit/insurance offers — a defensive privacy tool for the *investigator's own* footprint, not a way to look anyone up.

## When to use
Reach for this as part of your own OpSec hygiene, before or between investigations: opting out of prescreened "firm offers" reduces how much of your name/address the bureaus share with marketers and downstream data brokers, shrinking the trail an adversary could pull on you. It produces **no intelligence about a subject** — its place in an OSINT kit is purely investigator self-protection.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.optoutprescreen.com — confirm you're on the genuine, bureau-operated site (it's the only official one; avoid look-alikes).
2. Choose "Electronic Opt-Out for Five Years" (instant, online) or "Permanent Opt-Out" (requires printing and mailing a signed form).
3. Enter YOUR OWN identifying details (name, current address, and the SSN/DOB the bureaus use to locate your file). Do not enter anyone else's data.
4. Submit and retain the confirmation.
5. Pivot: pair with broader data-broker removal workflows (e.g. Whitepages/Spokeo opt-outs) to reduce your exposure across people-search sites too.

## Inputs → Outputs
- **In:** your own `name`, `address`, SSN, DOB
- **Out:** a confirmed opt-out from prescreened credit/insurance offers (no data returned about others)
- **Empty/negative result looks like:** not applicable — this is an action, not a query; the "result" is the confirmation of your opt-out.

## Gotchas & OpSec
- **Never use on a subject.** Entering a third party's SSN/DOB here would be both useless (no output) and a serious misuse.
- It only covers prescreen firm-offer lists — it does not remove you from people-search or broker sites; those need separate opt-outs.
- Human-in-the-loop: a permanent opt-out requires a mailed, signed form.

## Overlaps ("do both")
- Pairs with people-search opt-out tools — this handles the credit-bureau prescreen channel; those handle the aggregator/broker channel of your personal footprint.

## Trust & verifiability
`trust: trusted` — jointly run by the four major credit bureaus and mandated under US law (FCRA); it is the authoritative opt-out, not a third-party intermediary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | optout-credit-prescreen |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name, address → (privacy action) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (manual-review) |
