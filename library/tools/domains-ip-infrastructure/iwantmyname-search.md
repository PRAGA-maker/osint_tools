---
id: iwantmyname-search
name: iWantMyName Search
description: Use when you have a `domain` and want to check availability and basic WHOIS — returns registration/expiry dates, status, and nameservers, or confirms the name is unregistered.
url: https://iwantmyname.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quick domain-availability check plus lightweight WHOIS (dates, status, nameservers) across 400+ TLDs.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Searching availability and viewing WHOIS is free; the site is a commercial registrar, so actually registering a domain costs money, but the lookup does not.
opsec: passive
opsecNote: A WHOIS/availability lookup queries registry data, not the domain owner — no notification is sent. Standard passive recon. As with any registrar search box, assume the query is logged by iWantMyName; use a VPN if the interest itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established independent domain registrar; its WHOIS reflects registry data but is a convenience view, not an authoritative WHOIS server — cross-check dedicated WHOIS/RDAP for full records.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- iwantmyname.com
- iWantMyName WHOIS
tags:
- toddington
- whois-ip-lookups-website-analysis
- domain-availability
- registrar
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# iWantMyName Search

> A registrar's domain search box doubling as a quick availability + WHOIS check across 400+ extensions.

## When to use
You have a `domain` (or a candidate name) and want to know whether it is registered and, if so, its basic registration facts — creation date, expiry, status, and nameservers. Useful early in infrastructure recon to confirm a domain exists, gauge its age, spot the hosting/nameserver provider, and generate related-TLD variants a subject might also own. This is a light-touch lookup, not a full pivot engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://iwantmyname.com and enter the `domain` (with or without extension) in the search box.
2. Read availability across TLDs — taken names are flagged as registered, free ones as available.
3. For a registered domain, open its WHOIS view: registration date, expiration date, status, nameservers, and full WHOIS data where the registry exposes it.
4. Note the nameservers/registrar as a pivot toward the hosting provider; note the creation date to gauge how long the subject has held the name.
5. Pivot: feed the domain/nameservers into dedicated WHOIS/RDAP, passive DNS, and certificate-transparency tools for the deeper record this convenience view omits.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` availability status + WHOIS facts (registration/expiry dates, status, nameservers)
- **Empty/negative result looks like:** the name shows as available/unregistered (no owner to pivot on), or WHOIS is redacted behind privacy — treat redaction as "protected," not "no owner."

## Gotchas & OpSec
- This is a registrar's sales tool; its WHOIS is a convenience summary — use a dedicated WHOIS/RDAP service for authoritative, complete records.
- Privacy/proxy registration hides registrant details on most modern domains; expect nameservers and dates, rarely a name.
- Passive lookup, but the query is logged by the registrar like any search box.

## Overlaps ("do both")
- Pairs with the deeper WHOIS/DNS tools in the [[domains-ip-infrastructure]] set — use iWantMyName for a fast availability/age read, then a full WHOIS/RDAP and passive-DNS tool for registrant history and related infrastructure.

## Trust & verifiability
`trust: community` — a legitimate registrar surfacing registry data. Reliable for availability and headline dates; verify detailed registrant/history claims against an authoritative WHOIS/RDAP source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iwantmyname-search |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
