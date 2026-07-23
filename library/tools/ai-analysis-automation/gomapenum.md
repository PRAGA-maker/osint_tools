---
id: gomapenum
name: GoMapEnum
description: Use when you have an `employer-org` or `domain` and want to harvest employee `email` addresses and enumerate valid accounts across Microsoft/cloud services — returns emails, names and valid-account signals.
url: https://github.com/nodauf/GoMapEnum
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building an employee email list for a target company from LinkedIn/search engines, then validating which addresses are real accounts.
selectorsIn:
- employer-org
- domain
selectorsOut:
- email
- name
status: live
pricing: free
costNote: Free and open source (Go); build from source. LinkedIn/search-engine gathering may require your own session cookies or API keys.
opsec: active
opsecNote: The user-enumeration and password modules send real authentication probes to Microsoft/Azure/ADFS/O365/OWA endpoints, which are logged and can trigger alerts or lockouts. For pure OSINT, use only the email-gathering (LinkedIn/search-engine) modules and stop before any auth-probing or spray. Route through infrastructure you control and only against authorized targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Community Go project by nodauf; useful and actively released, but a single-maintainer tool — vet before running auth modules against live services.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- GoMapEnum
- nodauf/GoMapEnum
tags:
- email-harvest
- user-enumeration
- azure
- linkedin
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# GoMapEnum

> A Go toolkit that gathers employee emails (LinkedIn, Google/Bing dorking) and enumerates valid accounts across Azure/ADFS/O365/OWA and more.

## When to use
You have an `employer-org` (company name) or its `domain` and want to build a list of employee `email` addresses — for a due-diligence, missing-person-workplace, or attack-surface context — then confirm which addresses correspond to real accounts. GoMapEnum's OSINT value is the email-gathering side; its enumeration/spray side is a pentest capability to be used only with authorization.

## How to use it (`bestInteractionPattern`: cli)
1. Install Go, then `git clone https://github.com/nodauf/GoMapEnum && cd GoMapEnum/src && go build`.
2. Gather emails from LinkedIn: run the `linkedin` module with the target company name (supply LinkedIn session cookies if prompted) to pull employee names → emails.
3. Or gather via search engines: run the `searchEngine` module (Google/Bing dorking) against the `domain`.
4. (Authorized targets only) validate accounts: run the `o365` user-enumeration module to flag which emails are valid, MFA-enabled, or locked.
5. Read the output list of `email` + `name` pairs and account-status flags.
6. Pivot: confirmed emails feed email-verification and breach-lookup tools; names feed people-search.

## Inputs → Outputs
- **In:** `employer-org` (company name) and/or `domain`
- **Out:** employee `email` addresses, associated `name`s, and (from enum modules) valid/MFA/lockout status
- **Empty/negative result looks like:** no employees returned — the company may have a thin LinkedIn footprint, or your session/cookies expired; try the search-engine module as a cross-check.

## Gotchas & OpSec
- The auth-enumeration and password modules are **active and intrusive** — they hit Microsoft login infrastructure and can lock accounts or raise alerts. Only for authorized engagements.
- LinkedIn gathering typically needs a (sock-puppet) logged-in session; expect rate limits and captcha risk.
- Email formats are inferred and may be wrong — verify before trusting.

## Overlaps ("do both")
- Complements dedicated LinkedIn email-format tools and breach-lookup services — GoMapEnum builds the candidate list; a verifier confirms deliverability, a breach tool confirms exposure.

## Trust & verifiability
`trust: unverified` — an actively maintained but single-author community project; the email-gathering modules are safe OSINT, while the auth modules require explicit authorization and careful review before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gomapenum |
