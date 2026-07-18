---
id: godaddy-whois-lookup
name: GoDaddy Whois Lookup
description: Use when you have a `domain` and want its registration record — returns registrar, creation/expiry dates, name servers and (when not privacy-redacted) registrant `email`/`name`/`address`.
url: https://who.godaddy.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast, no-login WHOIS lookup of a domain's registration and name-server record.
selectorsIn:
- domain
selectorsOut:
- domain
- email
- name
- address
- ip-address
status: live
pricing: free
costNote: Free public WHOIS lookup from GoDaddy; no account or payment needed to query.
opsec: passive
opsecNote: Queries hit GoDaddy's WHOIS service, not the target's own infrastructure, so the domain owner is not notified. Standard registry-side logging only; no sock puppet required for a single lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by GoDaddy, an ICANN-accredited registrar; data comes from authoritative registry WHOIS, not a scraper.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cyclect
- godaddy
- godaddy-com
aliases:
- GoDaddy WHOIS
- who.godaddy.com
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# GoDaddy Whois Lookup

> GoDaddy's free public WHOIS front-end: paste a domain, get its registration record and name servers with no login.

## When to use
You have a `domain` tied to a subject (a personal site, a business, a domain from an email address or breach) and want to know who registered it, when, through which registrar, and what name servers/IP it points to. A registration date and registrar can corroborate that a site is genuinely the subject's, and an un-redacted registrant block occasionally leaks a real `name`, `email`, or `address`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://who.godaddy.com (redirects to https://www.godaddy.com/whois).
2. Enter the target `domain` (e.g. `example.com`) and submit.
3. Read the record: registrar, creation and expiry dates, last-updated date, and name servers. If registrant contact fields are shown, capture the `name`/`email`/`address`.
4. Pivot: name servers and creation dates cluster domains owned by the same person; an un-redacted `email` feeds email-OSINT; a redacted record still gives you dates and registrar to correlate elsewhere.

## Inputs → Outputs
- **In:** `domain`
- **Out:** registrar, creation/expiry/updated dates, name servers, and — when not privacy-protected — registrant `name`, `email`, `address`
- **Empty/negative result looks like:** "available" / not registered means no record; a fully redacted record shows "Registration Private" or GoDaddy's privacy-proxy contact instead of the real registrant.

## Gotchas & OpSec
- Human-in-the-loop: none for a single lookup; heavy automated querying will be rate-limited or CAPTCHA-gated.
- OpSec: passive — you query GoDaddy, not the subject; the domain owner is not alerted.
- Most modern domains are behind free WHOIS privacy, so expect redacted registrant fields; the dates and name servers are still useful even when the contact is masked.

## Overlaps ("do both")
- Pairs with `[[godaddy-com]]` and `[[godaddy]]` (same provider, adjacent lookups) and with `[[cyclect]]` — run a second WHOIS/history source because GoDaddy shows only the current record, not historical registrant snapshots.

## Trust & verifiability
`trust: trusted` — GoDaddy is an ICANN-accredited registrar and this is authoritative registry WHOIS data, not a third-party scrape.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | godaddy-whois-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, email, name, address, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
