---
id: arin-net
name: ARIN WhoWas
description: Use when you have an `ip-address` or ASN and want its full historical registration chain — returns the organizations, contacts, and domain/org changes that ever held it.
url: https://www.arin.net/reference/research/whowas/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reconstructing who historically held a North American IP block or ASN, including past org names and points of contact.
selectorsIn:
- ip-address
- domain
selectorsOut:
- employer-org
- domain
- name
status: live
pricing: free
costNote: Free service, but access is gated behind an approved ARIN Online account — no payment at any tier.
opsec: passive
opsecNote: Queries run against ARIN's own registry and are tied to your approved account; ARIN reviews intended use and can revoke access for high-volume querying. The target is not notified. Do not scrape.
humanInLoop: true
humanInLoopReason:
- account-login
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by ARIN, the Regional Internet Registry for North America; the authoritative source of record for allocations it administers.
missingPersonsRelevance: medium
coverage:
- us
- ca
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- account-arin-net
- arin
- search-arin-net
- whois-arin
- whois-arin-online
aliases:
- ARIN WhoWas
- arin.net historical whois
tags:
- domainsandips
- Domains & IPs
- historical-whois
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# ARIN WhoWas

> ARIN's historical registration lookup: the full ownership timeline of a North American IP address or ASN, not just who holds it today.

## When to use
You have an `ip-address` (or ASN) that resolved to your subject at some point in the past — from an old email header, forum log, or breach dump — and current WHOIS shows a different holder. WhoWas rebuilds the chain: every organization that ever registered that number, with the contacts and dates attached. Use it to tie a historical IP back to the org or person who controlled it at the relevant moment.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create an ARIN Online account at https://account.arin.net and request WhoWas access; state your intended use and expected query frequency.
2. Wait for ARIN staff to approve (about two business days). Approval is one-time.
3. In ARIN Online, submit a WhoWas report for an exact IP address or ASN — not CIDR, handles, Org IDs, or POC identifiers.
4. Download the resulting `.zip` (tab-separated files) and read the registration history: past org names, points of contact, and change dates.
5. Pivot: a past `employer-org` or contact `name` feeds people-search; the current holder feeds live WHOIS/RDAP.

## Inputs → Outputs
- **In:** `ip-address` or ASN administered by ARIN (includes legacy space)
- **Out:** historical `employer-org` names, contact `name`s, associated `domain`/network records and their change dates
- **Empty/negative result looks like:** no history returned for a number ARIN doesn't administer — it only covers North America, so use RIPE/APNIC/LACNIC/AFRINIC for other regions.

## Gotchas & OpSec
- Human-in-the-loop: you must register and be manually approved before any query works — budget for the two-day lag.
- Input must be the exact number; the tool rejects CIDR notation, handles, and POC IDs.
- OpSec: passive toward the target, but every query is logged against your account, and excessive querying can terminate access — treat it as a low-volume research tool, not a scraper.

## Overlaps ("do both")
- Pairs with `[[whois-arin]]` and `[[search-arin-net]]` — those give the current registration, while WhoWas supplies the historical chain the live record hides.

## Trust & verifiability
`trust: trusted` — ARIN is the Regional Internet Registry itself, so its historical record is authoritative for the space it administers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arin-net |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → employer-org, domain, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, manual-review) |
