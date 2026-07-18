---
id: mxtoolbox-com
name: mxtoolbox.com
description: Use when you have a `domain` and want its DNS Start-of-Authority record — returns the authoritative nameservers, the hostmaster contact, and the zone serial/refresh settings.
url: https://mxtoolbox.com/SOALookup.aspx
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Pulling a domain's SOA record (nameservers, hostmaster email, zone serial) without touching the target's own DNS.
selectorsIn:
- domain
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free web lookups; MXToolbox sells monitoring/API subscriptions, but the on-demand SOA/DNS lookups need no account or payment.
opsec: passive
opsecNote: MXToolbox resolves the query from its own servers, so your IP never contacts the target's DNS — the target sees nothing. MXToolbox itself logs the domain you looked up; use a sock-puppet account if you sign in for higher rate limits.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: MXToolbox is a long-established, reputable commercial DNS/email diagnostics provider; the records it returns are live DNS pulled from authoritative servers, not a cached third-party dataset.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- email-header-analyzer
- mx-toolbox-blacklist-check
- mx-toolbox-email-header-analyzer
- mx-toolbox-reverse-ip-search
- mx-toolbox-whois-lookup
- mxtoolbox
- mxtoolbox-blacklists
- mxtoolbox-com-2
aliases:
- MXToolbox SOA Lookup
- MX Toolbox DNS lookup
tags:
- domainsandips
- Domains & IPs
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# mxtoolbox.com

> MXToolbox's web DNS toolbox — this page pulls a domain's SOA (Start of Authority) record, a passive first look at who runs a domain's DNS and how the zone is configured.

## When to use
You have a `domain` (from an email address, a website, or a WHOIS pivot) and want to fingerprint its DNS setup: which nameservers are authoritative, the hostmaster/administrative contact encoded in the SOA, and the zone serial/refresh timers that hint at how actively the zone is maintained. Useful as the opening move before MX, A, TXT, or blacklist lookups on the same host.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mxtoolbox.com/SOALookup.aspx.
2. Enter the target `domain` (e.g. `example.com`) in the "Domain Name" box and run the lookup.
3. Read the SOA record:
   - **Primary Nameserver** — the authoritative DNS host (often reveals the registrar or hosting provider).
   - **Responsible (hostmaster) email** — SOA encodes it as `hostmaster.example.com`, i.e. `hostmaster@example.com`; a real contact address for the zone.
   - **Serial / Refresh / Retry / Expire / Minimum TTL** — a recently-incrementing serial means the zone is actively edited.
4. Pivot: switch the same domain through MXToolbox's MX, DNS, and Blacklist tabs; feed the nameserver/provider into `[[mx-toolbox-reverse-ip-search]]`, and the hostmaster email into email OSINT.

## Inputs → Outputs
- **In:** `domain`
- **Out:** authoritative `domain` (nameservers), hostmaster `email`, zone serial/timers
- **Empty/negative result looks like:** "DNS Record not found" or an NXDOMAIN/SERVFAIL error — the domain is unregistered, mistyped, or has no published SOA; not proof the org doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none for a single lookup; heavy use hits an anonymous rate limit that a free account raises.
- OpSec: **passive** — MXToolbox does the resolving, so the target's DNS never sees your IP. The only party that logs you is MXToolbox.
- The SOA hostmaster address is frequently a generic role mailbox (`hostmaster@`, `dns-admin@`) or a privacy/registrar placeholder — corroborate before treating it as a person.

## Overlaps ("do both")
- Pairs with `[[mx-toolbox-whois-lookup]]` and `[[mx-toolbox-reverse-ip-search]]` — SOA gives the nameservers and hostmaster contact, WHOIS gives the registrant, and reverse-IP maps co-hosted domains; together they profile the whole infrastructure.
- Feed a discovered mail host into `[[email-header-analyzer]]` when you also hold headers from the target.

## Trust & verifiability
`trust: trusted` — MXToolbox is a well-known commercial DNS/deliverability provider; results are live authoritative DNS queries, so the data is as current as the zone itself rather than a stale scrape.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mxtoolbox-com |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
