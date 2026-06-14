---
id: disposable-email-address-dea-detector
name: Disposable Email Address (DEA) Detector
description: Use when you have an email or its domain and want to know if it is a disposable/throwaway address — returns a yes/no disposable verdict, not identity data about the owner.
url: https://tools.verifyemailaddress.io/apps/disposable_email_address_detector
category: email
path:
- email
bestFor: Flagging whether an email is a disposable/temporary throwaway address.
selectorsIn:
- email
- domain
selectorsOut:
- domain
status: unknown
pricing: free
costNote: Free web utility; no account required for a single check.
opsec: passive
opsecNote: You submit a domain/email to a third-party checker, which the operator can log. The subject is not contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small single-purpose web checker (verifyemailaddress.io). It only judges disposability against a list — verify the page still resolves, since such utilities come and go. Not a person/identity lookup despite its harvested category.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- burner-email-providers
- disposable-email-domains
aliases:
- DEA Detector
tags:
- email
- email-verification
- disposable
source: metaosint
lastVerified: ''
enrichment: full
---

# Disposable Email Address (DEA) Detector

> A single-purpose web checker that tells you whether an email/domain is a disposable (throwaway) address — it classifies, it does not enrich identity.

## When to use
You have an `email` (or its `domain`) for a missing person, tipster, or associate and want to know if it is a burner/disposable address. A disposable verdict is an investigative signal (the account was meant to be untraceable) and tells you not to over-invest in pivoting on that mailbox. It does **not** return a name, accounts, or phone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL and paste the `email` or `domain` into the checker.
2. Submit and read the verdict: disposable/temporary vs not.
3. Pivot: a non-disposable address is worth deeper enrichment (breach search, provider lookup); a disposable one signals deliberate anonymity.

## Inputs → Outputs
- **In:** `email` or `domain`
- **Out:** boolean disposable/not verdict for the `domain`
- **Empty/negative result looks like:** "not disposable" — meaning the domain isn't on its list, which won't catch brand-new throwaway providers.

## Gotchas & OpSec
- Scope mismatch: harvested as a "person search / email" tool, but it only classifies disposability — no identity output. The previously listed name/social/phone outputs were incorrect and have been removed.
- List-based, so "not disposable" is not a guarantee; new burner domains slip through.
- OpSec: passive; the operator can log submitted domains. For zero-leak checks, prefer an offline list.

## Overlaps ("do both")
- For offline, no-leak checks use the open lists `[[burner-email-providers]]` and `[[disposable-email-domains]]`; this web tool is the quick one-off equivalent.

## Trust & verifiability
`trust: unverified` — minor third-party utility with uncertain longevity; confirm it still resolves and corroborate borderline cases against a maintained list.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | disposable-email-address-dea-detector |
| category | email |
| selectorsIn → selectorsOut | email, domain → domain (disposable y/n) |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
