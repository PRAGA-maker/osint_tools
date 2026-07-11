---
id: justice-gov-uk
name: Certificated Enforcement Agent Register (justice.gov.uk)
description: Use when you have a `name` or `employer-org` and want to verify a UK certificated bailiff/enforcement agent — returns certification status and the issuing County Court.
url: http://certificatedbailiffs.justice.gov.uk/CertificatedBailiffs/
category: public-records
path:
- public-records
bestFor: Confirming whether a named person is a certificated enforcement agent (bailiff) in England & Wales and which court certified them.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Official free GOV.UK register; no account needed. If a person isn't found, you can email the court (cbregister@justice.gov.uk) to verify.
opsec: passive
opsecNote: This is an official public register — searching it is passive and notifies no one. It confirms a professional status, not a home address, so the privacy exposure is minimal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by HM Courts & Tribunals Service (Ministry of Justice); certificates are issued by County Court judges, so the register is the authoritative source on bailiff certification.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Certificated Bailiffs register
- certificatedbailiffs.justice.gov.uk
tags:
- professionlicensing
- Profession & Licensing Sites
- uk-gov
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Certificated Enforcement Agent Register (justice.gov.uk)

> The official England & Wales register of certificated bailiffs — the authoritative check on whether someone is genuinely a certified enforcement agent, and which court vouches for them.

## When to use
You have a `name` (or an `employer-org`) and need to verify a claim of being a bailiff/enforcement agent — a common vector for intimidation scams and impersonation. The register holds everyone certificated to use the "Taking Control of Goods" procedure in England & Wales, with certificates issued by County Court judges. Reach for it to confirm/refute a professional identity, or to attach a person to an enforcement firm.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the register at the URL.
2. Search by the agent's `name` or `employer-org`; tick "include similar spellings" (e.g. Smith/Smyth) to catch variants.
3. Read the result: whether a valid certificate is held and which County Court issued it.
4. If not found, email cbregister@justice.gov.uk to ask the court to verify.
5. Pivot: a confirmed agent ties to an enforcement firm (`employer-org`) to research further; a *failure* to appear is strong evidence someone claiming to be a bailiff is not certificated.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** certificated `name`, certification status, issuing court, and firm (`employer-org`)
- **Empty/negative result looks like:** no match — the person is not a certificated enforcement agent (or the name is spelled differently); use the "similar spellings" option and the court-email fallback before concluding.

## Gotchas & OpSec
- Scope: England & Wales only, and only "certificated" enforcement agents (some enforcement roles don't require this certificate) — a miss doesn't cover every enforcement function.
- Impersonation angle: absence here is a useful red flag against someone falsely claiming bailiff powers.
- OpSec: passive official register.

## Overlaps ("do both")
- Pairs with `[[rics-org]]` and other professional registers — same pattern of verifying a claimed credential against the issuing body.
- Pairs with Companies House-style lookups to connect the agent to their enforcement firm.

## Trust & verifiability
`trust: trusted` — an authoritative HMCTS/Ministry of Justice register; certification facts are definitive, with a documented court-verification fallback for edge cases.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | justice-gov-uk |
