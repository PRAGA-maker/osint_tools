---
id: ipqualityscore-com
name: ipqualityscore.com
description: Use when you have an email address and want to validate it and assess risk/reputation — returns deliverability, validity, fraud score, and disposable/leak flags.
url: https://www.ipqualityscore.com/free-email-verifier
category: email
path:
- email
bestFor: Validating an email and scoring its risk (valid, disposable, recent abuse, leaked).
selectorsIn:
- email
selectorsOut:
- metadata
status: live
pricing: freemium
costNote: Free web email verifier with a daily cap; higher volume and API access require a paid plan/API key.
opsec: passive
opsecNote: Validation runs server-side at IPQS (may include SMTP/DNS checks); the subject's mail server could see a verification probe but no message is sent. No notification to the person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: IPQualityScore is a well-known commercial fraud-prevention and email-validation vendor with a documented API; results (validity, fraud score) are reliable as scores but are heuristic, not identity confirmation.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- IPQS
- IPQualityScore
tags:
- email
- Email Related Sites
- email-verification
source: uk-osint
lastVerified: ''
enrichment: full
---

# ipqualityscore.com

> Commercial email validation and fraud-scoring service — tells you whether an email is real/deliverable and flags disposable, recently-abused, or leaked addresses.

## When to use
You have an `email` for a subject and need to know if it is valid and currently in use, whether it is a throwaway/disposable address, and whether it carries fraud/abuse signals or appears in known leaks. In missing-persons work this confirms an email is live (a usable contact channel or sign of recent activity) and distinguishes a real personal address from a burner. Use early, before investing effort in an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ipqualityscore.com/free-email-verifier.
2. Enter the subject `email`.
3. Read the report: validity/deliverability, disposable flag, recent abuse, fraud score, and signals like leaked/honeypot. The free verifier is rate-limited.
4. Pivot: a valid, non-disposable address is worth running through breach engines ([[leakcheck]]) and reverse-email people search; an invalid/disposable one is low value.

## Inputs → Outputs
- **In:** `email`
- **Out:** validation/risk `metadata` — valid/invalid, deliverability, disposable flag, fraud score, recent-abuse and leak indicators
- **Empty/negative result looks like:** "invalid" / undeliverable / disposable — the address is likely dead or a burner.

## Gotchas & OpSec
- Human-in-the-loop: free tier is daily-capped; high volume needs an API key.
- OpSec: passive toward the subject. Validation may trigger an SMTP probe to the mail provider (not the person), so the receiving server — not the subject — could log a check.

## Overlaps ("do both")
- Pairs with [[ipvoid-com]] for header/mail-route analysis and with [[leakcheck]] for breach exposure — IPQS scores liveness/risk, the others give content.

## Trust & verifiability
`trust: trusted` — established commercial fraud-prevention vendor with a public, documented API. Scores are reliable heuristics, not proof of identity; treat the fraud score as a risk indicator, not a verdict.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipqualityscore-com |
| category | email |
| selectorsIn → selectorsOut | email → metadata |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
