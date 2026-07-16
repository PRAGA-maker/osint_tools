---
id: rdrs-icann-org
name: ICANN RDRS
description: Use when you have a `domain` and want the nonpublic (redacted) registrant data — returns a channel to formally request name, email, and address from the registrar.
url: https://rdrs.icann.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Submitting a legitimate, documented request for redacted gTLD WHOIS registrant data through ICANN's central Registration Data Request Service.
selectorsIn:
- domain
selectorsOut:
- name
- email
- address
status: live
pricing: free
costNote: Free ICANN service. Requires a free requestor account; fulfilment is at each registrar's discretion, not guaranteed.
opsec: active
opsecNote: This is an identified, logged legal process — you create an account and state a lawful basis; the registrar (and ICANN) records who requested what, and the registrant may be notified per the registrar's policy. Do NOT use it for casual snooping; only submit requests with a genuine, documentable basis.
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official ICANN service — the authoritative, sanctioned route to request post-GDPR redacted registrant data; not a scraper.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- icann-lookup
- icann-whois-lookup
- lookup-icann-org
- icann-org
aliases:
- Registration Data Request Service
- ICANN RDRS
tags:
- domainsandips
- Domains & IPs
- whois
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# ICANN RDRS

> ICANN's official Registration Data Request Service — the sanctioned channel to formally request the nonpublic registrant details that GDPR redaction removed from public WHOIS.

## When to use
You have a `domain` whose public WHOIS is redacted ("REDACTED FOR PRIVACY"), and you have a legitimate, documentable need for the registrant's identity — a legal matter, safety/abuse investigation, or law-enforcement/authorized inquiry. RDRS routes one request to the relevant participating registrar instead of you contacting each registrar separately. It is a formal process, not an instant lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free requestor account at rdrs.icann.org.
2. Enter the `domain` and confirm the registrar participates in RDRS.
3. Complete the request: state your identity, lawful basis, the specific data fields you need, and your justification.
4. Submit and wait — the registrar manually reviews and either discloses the data or declines; response times and outcomes vary.
5. Pivot: if granted, the registrant `name`/`email`/`address` feeds people-search and contact verification; if declined, fall back to historical WHOIS or other domain-ownership signals.

## Inputs → Outputs
- **In:** a `domain` (with a stated lawful basis)
- **Out:** upon registrar approval, the registrant's `name`, `email`, and `address`
- **Empty/negative result looks like:** the registrar isn't in RDRS, or reviews and denies the request — you receive no data; disclosure is discretionary, not a right.

## Gotchas & OpSec
- Not a scraper and not instant — it's a reviewed legal request with a paper trail tied to you.
- Coverage is limited to participating registrars; many aren't enrolled.
- Approval is discretionary; expect denials without a strong, lawful basis.
- OpSec: inherently active and identified — only use with a genuine basis; misuse has consequences.

## Overlaps ("do both")
- Pairs with `[[icann-whois-lookup]]` and historical-WHOIS tools — check public/historical WHOIS first (often pre-redaction records exist); use RDRS only when you truly need the current redacted data and have standing.

## Trust & verifiability
`trust: trusted` — ICANN's official service; any data returned is authoritative registrar-held data, making it the highest-confidence (but access-gated) route to registrant identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rdrs-icann-org |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → name, email, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, legal-gate, manual-review) |
