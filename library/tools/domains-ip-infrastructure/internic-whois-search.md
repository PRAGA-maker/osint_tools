---
id: internic-whois-search
name: InterNIC Whois Search
description: Use when you have a `domain` and want the authoritative registry record — returns the sponsoring registrar, registration/expiry dates and name servers straight from the InterNIC registry whois.
url: http://www.internic.net/whois.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Authoritative registry-level whois to confirm a domain's sponsoring registrar and status.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free official registry whois service; no account or payment.
opsec: passive
opsecNote: Queries the registry whois, not the target's servers, so the domain owner is not alerted. Fully passive; no sock puppet needed for a lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated under ICANN as the InterNIC registry whois; authoritative for the thin registry data (sponsoring registrar, dates, name servers), which then points to the registrar's full whois.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- icann-whois-lookup
- godaddy-whois-lookup
aliases:
- InterNIC whois
- internic.net whois
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# InterNIC Whois Search

> The registry-level whois behind gTLD domains: enter a domain and get the authoritative record of which registrar sponsors it, when it was created/expires, and its name servers.

## When to use
You have a `domain` and want the authoritative "thin" registry record before diving into a registrar's fuller (often privacy-redacted) whois. InterNIC returns the sponsoring registrar of record, key dates, domain status codes (e.g. clientTransferProhibited), and name servers — useful to confirm a domain is genuinely registered, identify which registrar to query next, and read status/date signals that a reseller whois might obscure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.internic.net/whois.html.
2. Enter the `domain` (select the Domain radio option) and submit.
3. Read the registry record: sponsoring Registrar, Whois Server, creation/expiry/updated dates, name servers, and status codes.
4. Pivot: take the sponsoring registrar's whois server to pull the fuller registrant record; name servers and dates help cluster domains held by the same owner.

## Inputs → Outputs
- **In:** `domain` (gTLD such as .com/.net/.org/.edu)
- **Out:** sponsoring registrar, registration/expiry/updated dates, name servers, status codes (the authoritative registry `domain` record)
- **Empty/negative result looks like:** "No match for domain" — the name isn't registered in that registry (or is a ccTLD InterNIC doesn't serve); check the correct registry/whois for that TLD.

## Gotchas & OpSec
- Human-in-the-loop: none.
- This is *thin* registry whois — it names the registrar and dates but not the registrant contact; follow the pointed-to registrar whois for that (which is often privacy-redacted).
- Coverage is gTLDs InterNIC serves; ccTLDs (.uk, .de, .no, etc.) have their own registry whois you must use instead.

## Overlaps ("do both")
- Pairs with `[[godaddy-whois-lookup]]` and `[[icann-whois-lookup]]` — InterNIC gives the authoritative registrar/date/status layer, while registrar/aggregator whois tools attempt the fuller (or historical) registrant details; use both to separate registry facts from registrant leads.

## Trust & verifiability
`trust: trusted` — the official InterNIC registry whois under ICANN; the registrar/date/status data is authoritative and directly verifiable against the registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | internic-whois-search |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
