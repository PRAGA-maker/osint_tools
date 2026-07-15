---
id: icas-org-uk
name: icas.org.uk (Find a CA)
description: Use when you have a `name` or firm and want to verify/locate a Chartered Accountant registered with ICAS — returns the member/firm, their firm's address and professional standing.
url: https://www.icas.com/find-a-ca
category: public-records
path:
- public-records
bestFor: Confirming that a person is a genuine ICAS-registered Chartered Accountant and finding their firm/location.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- name
- address
status: live
pricing: free
costNote: Free public directory run by ICAS; no account or payment to search.
opsec: passive
opsecNote: Searching a public professional directory does not notify the subject and is passive. You disclose your interest only to ICAS's website; a normal browser session is fine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by ICAS (The Institute of Chartered Accountants of Scotland), the statutory professional body — an authoritative first-party register of its members.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Find a CA
- ICAS member directory
- Institute of Chartered Accountants of Scotland
tags:
- professionlicensing
- Profession & Licensing Sites
- accountant
- uk
- verification
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# icas.org.uk (Find a CA)

> ICAS's official "Find a CA" directory — the authoritative way to confirm someone really is a Chartered Accountant and to locate their firm.

## When to use
You have a `name` (or a firm / `employer-org`) and need to verify a professional-accountant claim or find the practice a subject works for. "CA" is a trademark ICAS reserves for its members, so a directory hit both confirms the credential and gives you a firm name and business `address` to pivot on — useful for vetting an identity or tracing someone through their employer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.icas.com/find-a-ca.
2. Search by member name, firm name, or location/service to narrow to CAs and CA firms in a given area.
3. Read the listing: member/firm name, business address and contact, and areas of practice — confirming ICAS registration.
4. Pivot: the firm name/address feeds Companies House and corporate lookups; a confirmed full name feeds people-search; absence prompts checking sister bodies (ICAEW, ICAI).

## Inputs → Outputs
- **In:** `name` / `employer-org` / `address` (location)
- **Out:** `employer-org` (firm), confirmed `name`, business `address`
- **Empty/negative result looks like:** no matching member or firm. Note the directory chiefly surfaces CAs *in public practice / listed firms* — an in-house or non-listed member may not appear, so absence is not proof someone lacks the CA credential; it may just mean they aren't a searchable practising firm.

## Gotchas & OpSec
- Coverage is ICAS (Scotland) only — a UK accountant might instead be registered with ICAEW (England & Wales) or Chartered Accountants Ireland; check those if this misses.
- The directory is oriented to *finding a CA to hire*, so it emphasises firms in practice; individual membership isn't always exposed here.
- OpSec: passive — a public directory lookup with no subject notification.

## Overlaps ("do both")
- Pairs with Companies House / corporate registries and other profession-licensing directories — this confirms the accountancy credential, those tie the firm to filings, officers and addresses.

## Trust & verifiability
`trust: trusted` — a first-party register maintained by the statutory professional body. A listing is authoritative evidence of ICAS membership; treat contact details as current-at-publication and confirm via the firm directly if it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | icas-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
