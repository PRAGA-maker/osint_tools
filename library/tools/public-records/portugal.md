---
id: portugal
name: Portugal
description: Use when you have a Portuguese `employer-org` or `name` and want its beneficial owners from the national UBO register — returns `name`, `associate`, and `employer-org` links.
url: https://rcbe.justica.gov.pt/Autenticacao?ReturnUrl=%2fConsulta
category: public-records
path:
- public-records
bestFor: Identifying the natural persons who ultimately own or control a Portuguese company via the RCBE beneficial-ownership register.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- associate
- employer-org
status: live
pricing: free
costNote: Filing and the service itself are free of charge, but consulting the register requires Portuguese electronic authentication, which non-residents generally cannot obtain — so open access is effectively gated.
opsec: active
opsecNote: Consulting the RCBE requires logging in with a Portuguese Cartão de Cidadão or Chave Móvel Digital, tying the query to a real, government-verified identity. There is no anonymous access — do not treat this as passive. Only use it where an authenticated, attributable lookup is acceptable.
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Portugal's Ministry of Justice / IRN (Instituto dos Registos e do Notariado); the authoritative Central Register of Beneficial Owners (RCBE).
missingPersonsRelevance: high
coverage:
- pt
auth: account
api: false
localInstall: false
registration: true
aliases:
- RCBE
- Registo Central do Beneficiário Efetivo
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Portugal

> Portugal's Central Register of Beneficial Owners (RCBE) — the authoritative source for who really owns or controls a Portuguese company, but locked behind Portuguese electronic ID.

## When to use
Your subject is linked to a Portuguese company, foundation, association, or co-operative and you need to identify the ultimate natural-person owners/controllers (beneficial owners) — the people behind a corporate shell. Every entity incorporated in Portugal (and foreign entities doing business there) must declare beneficial owners to the RCBE, making it the definitive UBO source for Portugal.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://rcbe.justica.gov.pt/ and choose the consultation (Consulta) path.
2. Authenticate — you are redirected to log in with a **Cartão de Cidadão** (citizen card + reader) or **Chave Móvel Digital**. Without Portuguese electronic ID you cannot proceed; a Portuguese lawyer/accountant or local partner is the usual route for foreign investigators.
3. Search the `employer-org` (company name or NIPC/tax number).
4. Read the declared beneficial owners: `name`(s) of controlling individuals (`associate` of the company/each other) and the corporate structure.
5. Pivot: named beneficial owners feed Portuguese people-search, and the corporate links feed `[[opencorporates]]`/EU registers.

## Inputs → Outputs
- **In:** `employer-org` (company name / NIPC), or a `name` to test for ownership links
- **Out:** `name` of beneficial owner(s), `associate` relationships, `employer-org` structure
- **Empty/negative result looks like:** no declaration on file (some entities file late or are non-compliant), or — far more commonly for outside investigators — you simply cannot pass the Portuguese authentication gate and never reach the data at all.

## Gotchas & OpSec
- **Hard access gate:** requires Portuguese Cartão de Cidadão / Chave Móvel Digital. This is the single biggest limitation; plan for a local intermediary if you lack Portuguese e-ID.
- Authenticated and attributable — the login ties the query to a verified identity; never assume anonymity.
- Portuguese-language interface.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` and `[[e-justice-europa-eu]]` — those give open, cross-border company data with no login, while RCBE (when you can reach it) adds authoritative beneficial-ownership detail the open sources lack.

## Trust & verifiability
`trust: trusted` — first-party Portuguese government register (Ministry of Justice / IRN); beneficial-ownership data is authoritative, subject to filer compliance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | portugal |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, legal-gate) |
