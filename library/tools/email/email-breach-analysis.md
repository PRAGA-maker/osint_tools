---
id: email-breach-analysis
name: Email Breach Analysis
description: Use when you have an email address and want to know if it appears in known data breaches — returns an exposure summary (breach count, risk grade, exposed data types).
url: https://www.hotsheet.com/inoitsu/
category: email
path:
- email
bestFor: Checking whether an email address shows up in known breaches and what categories of data were exposed.
selectorsIn:
- email
selectorsOut:
- metadata
status: live
pricing: free
costNote: Free single-address breach exposure check (Inoitsu); no account required.
opsec: passive
opsecNote: You query Inoitsu's index, not the target's mailbox, so the owner is not alerted; the address is disclosed to Inoitsu, so use a clean environment.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Inoitsu is a known free breach-exposure checker that reports summaries rather than raw credentials; coverage is narrower than paid breach aggregators.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Inoitsu
tags:
- breach
- email
source: osint4all
lastVerified: ''
enrichment: full
---

# Email Breach Analysis

> Inoitsu's free email exposure checker: tells you whether an address appears in known breaches and summarizes the risk, without dumping raw credentials.

## When to use
You have an `email` for a missing person or associate and want to know if it has been involved in data breaches. Breach hits confirm the address is real and in use, reveal which services it was registered with (a pivot toward accounts/usernames), and hint at the person's online footprint and timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.hotsheet.com/inoitsu/.
2. Enter the email address and submit.
3. Read the exposure summary: whether it was found, an approximate breach count, a risk grade, and categories of data exposed.
4. Pivot: a hit confirms the address is live and worth deeper work; feed the address to `[[email-dossier]]` and run any associated services through username/social tooling.

## Inputs → Outputs
- **In:** `email`
- **Out:** breach exposure summary — found/not-found, breach count, risk grade, exposed data categories (`metadata`)
- **Empty/negative result looks like:** "not found / no exposure" — meaning not in Inoitsu's index, not proof the address is unbreached (coverage is partial; cross-check another breach service).

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive toward the target; you are disclosing the address to Inoitsu, so use a clean/sock-puppet context.
- Inoitsu deliberately summarizes rather than showing passwords, and its dataset is smaller than commercial aggregators — a "clean" result is weak evidence.

## Overlaps ("do both")
- Pairs with broader breach tooling (e.g. Have I Been Pwned / DeHashed-style services) — Inoitsu's coverage is narrower, so confirm a "no exposure" elsewhere.

## Trust & verifiability
`trust: community` — established free checker that reports summaries responsibly; coverage completeness is unverified, so treat negatives cautiously.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-breach-analysis |
| category | email |
| selectorsIn → selectorsOut | email → metadata |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
