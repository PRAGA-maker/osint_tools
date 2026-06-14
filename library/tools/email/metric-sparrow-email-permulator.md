---
id: metric-sparrow-email-permulator
name: Metric Sparrow email permulator
description: Use when you know a person's first/last name and an organization domain and need to generate the likely email-address permutations to then verify.
url: http://metricsparrow.com/toolkit/email-permutator/
category: email
path:
- email
bestFor: Generating candidate email permutations from a name plus a domain.
selectorsIn:
- name
- domain
selectorsOut:
- email
status: live
pricing: free
costNote: Free browser-based generator; no account.
opsec: passive
opsecNote: Fully passive — runs in your browser to build a candidate list; it does not contact any mail server or the target. The verification step afterward is what touches mail servers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Metric Sparrow's email permutator is a long-referenced free OSINT toolkit utility. Pure client-side string generation; trivially verifiable.
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mailtester
- mailscrap
aliases:
- email permutator
tags:
- Emails
source: cyb-detective
lastVerified: ''
enrichment: full
---

# Metric Sparrow email permulator

> Free in-browser email-permutation generator — turns a name + domain into the full set of plausible address formats to test.

## When to use
You have a subject's `name` (first/last, maybe middle) and a likely `domain` (their employer, school, or known provider) but not their actual address. This builds every common format (`john.doe@`, `jdoe@`, `doe.john@`, etc.) so you can then verify which one exists.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the email-permutator page.
2. Enter first name, last name, (optional middle), and the `domain`.
3. Copy the generated list of candidate `email` addresses.
4. Pivot: feed each candidate into a verifier — `[[mailtester]]` or `[[mailscrap]]` — to find the live one(s); the survivor feeds breach/profile enrichment.

## Inputs → Outputs
- **In:** `name`, `domain`
- **Out:** `email` (a list of permutation candidates)
- **Empty/negative result looks like:** N/A — it always produces candidates; the meaningful "negative" is when none of them verify as deliverable.

## Gotchas & OpSec
- This only *generates* guesses; it proves nothing until each address is independently verified.
- Catch-all domains make verification ambiguous (every guess looks valid) — note this when you verify.
- Garbage in, garbage out: wrong domain or misspelled name yields a useless list.

## Trust & verifiability
`trust: community` — established, widely cited free toolkit; logic is transparent client-side string permutation, so output is trivially checkable. The accuracy depends entirely on your inputs and the downstream verifier.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metric-sparrow-email-permulator |
| category | email |
| selectorsIn → selectorsOut | name, domain → email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
