---
id: londonstockexchange-com
name: London Stock Exchange
description: Use when you have a company `employer-org` (or a director's `name`) and want issuer, regulatory-filing, and leadership detail — returns company records, addresses, and named directors.
url: https://www.londonstockexchange.com/
category: public-records
path:
- public-records
bestFor: Researching UK/internationally-listed companies and their regulatory announcements (RNS) and leadership.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Company pages, prices, and RNS regulatory announcements are free to browse. Deep historical data feeds and some professional tools are paid, but the public issuer/RNS pages need no account.
opsec: passive
opsecNote: Browsing the exchange's public company and announcement pages is passive and does not notify anyone. It is corporate disclosure data, but announcements and filings name real individuals (directors, major shareholders) — handle those personal pivots with normal care.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official exchange; issuer data and RNS announcements are authoritative regulatory disclosures, not third-party summaries.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- London Stock Exchange
- LSE
- londonstockexchange.com
tags:
- companysites
- Company Related Sites
- corporate-records
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# London Stock Exchange

> The official LSE site — issuer pages and RNS regulatory announcements that tie a listed company to its filings, addresses, and named directors.

## When to use
You have an `employer-org` you suspect is listed (or AIM-quoted), or a person's `name` you think sits on a listed company's board, and you want authoritative corporate detail: the company's registered identity, regulatory news (RNS) announcements, director/PDMR dealings, and major-shareholder disclosures. For a subject connected to public markets, RNS filings are a rich, timestamped, official trail of who did what and when.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://www.londonstockexchange.com/` and search the company name or ticker.
2. Open the issuer page: profile, registered details, and the **News/RNS** tab.
3. Scan RNS announcements for director dealings, appointments/resignations, and shareholder notifications — these name individuals (`associate`) and dates.
4. Note the company's registered address and officers for cross-referencing.
5. Pivot: named directors → Companies House and people-search; the company → `[[kompass]]` and registries; announcement dates → timeline.

## Inputs → Outputs
- **In:** `employer-org` (company/ticker), `name` (director)
- **Out:** `employer-org` (issuer record), `associate` (directors/shareholders named in filings), `address`, timestamped RNS announcements
- **Empty/negative result looks like:** no listed company matches — the firm is private/unlisted (use Companies House instead) or listed on a different exchange. A person with no board role won't appear.

## Gotchas & OpSec
- Only covers **listed** issuers; private companies belong on Companies House. Absence here ≠ the company doesn't exist.
- RNS is authoritative but reads in regulatory shorthand; know the announcement types (RNS, PDMR, TR-1) to extract names.
- OpSec: **passive** — public disclosure data, no subject notification.

## Overlaps ("do both")
- Pairs with Companies House and `[[kompass]]` — the LSE gives listed-issuer disclosures and RNS; Companies House gives the statutory filings and officers for any UK company, listed or not.

## Trust & verifiability
`trust: trusted` — the official exchange; issuer data and RNS announcements are authoritative regulatory records you can cite directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | londonstockexchange-com |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
