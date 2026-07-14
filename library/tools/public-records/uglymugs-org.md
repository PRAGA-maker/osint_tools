---
id: uglymugs-org
name: National Ugly Mugs (NUM)
description: Use when a subject is (or may be) an adult-industry worker and you need a vetted, members-only safety/alert scheme — returns `associate` / `physical-description` warning reports, but only to verified members.
url: https://nationaluglymugs.org/
category: public-records
path:
- public-records
bestFor: A UK sex-worker safety charity's incident/alert database — accessible only to vetted members, not the public.
selectorsIn:
- name
- phone
selectorsOut:
- physical-description
- associate
status: live
pricing: free
costNote: Free to join, but membership is vetted and restricted to sex workers and approved support/enforcement partners; the alert data is not open to the general public.
opsec: active
opsecNote: This is a closed, safeguarding-focused community for a vulnerable group. Accessing it requires a real, vetted membership — do NOT create a false identity to get in. Approach only through legitimate channels (e.g. police/partner referral) and treat all content as highly sensitive.
humanInLoop: true
humanInLoopReason:
- account-login
- manual-review
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established UK registered charity (National Ugly Mugs); data is genuine safeguarding reporting, but ethically and legally gated behind vetted membership.
missingPersonsRelevance: high
coverage:
- uk
auth: account
api: false
localInstall: false
registration: true
invitationOnly: true
aliases:
- Ugly Mugs
- NUM
- uglymugs.org
tags:
- professionlicensing
- Profession & Licensing Sites
- safeguarding
- sex-worker-safety
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# National Ugly Mugs (NUM)

> A UK charity's members-only safety and alert scheme for sex workers — a genuine safeguarding database, deliberately walled off from public/investigative access.

## When to use
Your subject is, or is plausibly, an adult-industry worker in the UK and you are working a safeguarding or missing-person angle. NUM holds incident reports, alerts about dangerous individuals, and a client-checking tool — potentially relevant intelligence. But it is not an open OSINT source: access is restricted to vetted members (sex workers) and approved partners (police, support services). For most investigators the correct action is a *referral*, not a login.

## How to use it (`bestInteractionPattern`: web-manual)
1. Recognise the gate: the public site at https://nationaluglymugs.org/ describes the scheme; the alert/report data sits behind vetted membership.
2. If you are law enforcement or an approved support agency, request access through NUM's official partner/referral process — never by fabricating a member identity.
3. Within the members' area (authorised users only): submit or search incident reports, view alerts, and use the client-checker.
4. Pivot: for the missing person, coordinate with NUM's casework team and local police rather than attempting external scraping.

## Inputs → Outputs
- **In:** `name`, `phone` (of a reported individual), or subject context
- **Out:** `physical-description` and `associate`/warning details from member-submitted safety reports (members only)
- **Empty/negative result looks like:** for a non-member, no accessible data at all — the public site exposes the scheme's existence, not its records.

## Gotchas & OpSec
- Ethical/legal gate: this protects a vulnerable population. Do not deceive your way in, scrape it, or repurpose reports outside a legitimate safeguarding context.
- Human-in-the-loop: vetted membership, manual review, and partner referral are required.
- Data is sensitive safety reporting; handle under appropriate legal basis and data-protection rules.

## Overlaps ("do both")
- Complements official police missing-person channels — NUM's casework and trusted-flagger services can act where open OSINT cannot, but only through proper referral.

## Trust & verifiability
`trust: trusted` — an established UK registered charity with genuine safeguarding data; the constraint is access legitimacy and ethics, not authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uglymugs-org |
| category | public-records |
| selectorsIn → selectorsOut | name, phone → physical-description, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, manual-review, legal-gate) |
