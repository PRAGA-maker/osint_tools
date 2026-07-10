---
id: nuwber
name: Nuwber
description: Use when you have a US `name`, `phone` or `address` and want a person's contact profile — returns addresses, phone numbers, emails and relatives/associates.
url: https://nuwber.com/
category: phone
path:
- phone
bestFor: US people/reverse-phone search — resolving a name or number to addresses, phones, emails and relatives.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- email
- associate
status: live
pricing: freemium
costNote: Preview results (name, age, city, partial data) are free; the full report and detailed contacts require a paid Nuwber subscription.
opsec: passive
opsecNote: Queries hit Nuwber's aggregated public-records data, not the subject, so no alert is sent. Note Nuwber lists people's own profiles publicly — your searches/purchases tie to your account, so use a sock-puppet context.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A mainstream US data-broker people-search; useful for leads, but like all aggregators it carries stale addresses and same-name conflation — verify before relying.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- searchbug
- 411-us
- reverse-phone-lookup-2
aliases:
- nuwber.com
tags:
- people-search
- reverse-phone
- data-broker
- us
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Nuwber

> A US data-broker people-search — turn a name, phone or address into a contact profile with addresses, phones, emails and likely relatives/associates.

## When to use
You have a US `name`, `phone`, or `address` and want to expand it into a full contact picture. Nuwber aggregates public records into per-person profiles with address history, phone numbers, email addresses, age, and relatives — a solid US-jurisdiction option to run alongside other brokers, since each holds slightly different records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://nuwber.com/ and search by `name` (add city/state), or reverse a `phone`/`address`.
2. Review the free preview: name, age, city, relatives, and partial contacts.
3. Use age/relatives to pick the right person among same-name matches.
4. Unlock the full report (paid) for complete addresses, phones and emails.
5. Pivot: relative/`associate` names, new `phone`/`email` values feed `[[searchbug]]`, `[[411-us]]`, `[[reverse-phone-lookup-2]]` and messaging/social checks.

## Inputs → Outputs
- **In:** `name`, `phone`, or `address` (US)
- **Out:** `address` history, `phone` numbers, `email` addresses, and `associate`/relative links
- **Empty/negative result looks like:** no or only distant matches — the person may be young, recently moved, opted-out, or non-US; absence isn't conclusive.

## Gotchas & OpSec
- Aggregated public records — stale addresses and same-name collisions are common; corroborate before attributing.
- Human-in-the-loop: full detail is **paywalled**; the free preview confirms a match and gives relatives.
- Nuwber publishes people's profiles; subjects can opt out, so gaps exist. OpSec: passive toward the target; purchases log to your account.

## Overlaps ("do both")
- Pairs with `[[searchbug]]`, `[[411-us]]`, and `[[reverse-phone-lookup-2]]` — different brokers, different records; run several and reconcile.

## Trust & verifiability
`trust: community` — a mainstream broker, reliable for leads but not authoritative; verify any address/relationship against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nuwber |
| category | phone |
| selectorsIn → selectorsOut | name, phone, address → address, phone, email, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
</content>
