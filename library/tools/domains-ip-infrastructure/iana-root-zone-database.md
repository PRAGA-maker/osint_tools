---
id: iana-root-zone-database
name: IANA — Root Zone Database
description: Use when you have a `domain`'s TLD and want the authoritative registry/sponsoring organization behind it — returns the TLD operator (`employer-org`) and registry details.
url: https://www.iana.org/domains/root/db
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Authoritative lookup of every top-level domain, its type, and its sponsoring/registry organization.
selectorsIn:
- domain
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free authoritative public database; no account.
opsec: passive
opsecNote: Public reference data from IANA; nothing touches any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: IANA (a function of ICANN) operates the DNS root; this is the definitive, first-party registry of TLDs and their sponsors.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- iana-whois-service
aliases:
- Root Zone Database
- IANA Root Zone Database
tags:
- dns
- tld
- registry
- whois
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# IANA — Root Zone Database

> The authoritative index of every top-level domain on the Internet — and the organization responsible for each.

## When to use
You're investigating a `domain` and want ground truth about its TLD: who sponsors/operates it, what type it is (generic, country-code, sponsored, infrastructure), and where its authoritative WHOIS/registry lives. Especially useful for unusual or new-gTLD domains, ccTLDs, and IDN TLDs, where the registry operator and its jurisdiction matter for how far you can trace registration data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.iana.org/domains/root/db and locate the TLD (e.g. `.io`, `.ru`, `.museum`).
2. Open the TLD's entry to see its **type**, **sponsoring organization** (`employer-org`), the registry operator, and the designated WHOIS server / registry URL.
3. Follow the registry link to the authoritative WHOIS for that TLD.
4. Pivot: the sponsoring org and jurisdiction tell you which registry/WHOIS to query and how much registrant data is likely public; feed the WHOIS server into your domain-WHOIS workflow. Sibling: [[iana-whois-service]].

## Inputs → Outputs
- **In:** a `domain`'s TLD
- **Out:** TLD type, sponsoring/registry organization (`employer-org`), authoritative WHOIS/registry pointers
- **Empty/negative result looks like:** the string isn't a real TLD (not in the root) — the "domain" you were handed may be malformed, an internal name, or a non-existent TLD.

## Gotchas & OpSec
- This describes the **TLD/registry**, not any individual domain's registrant — use it to find *where* to look, then query that registry's WHOIS for the specific domain.
- Some ccTLD registries publish little or no registrant data; the IANA entry tells you which registry (and jurisdiction) you're dealing with.
- OpSec: passive; a public reference lookup.

## Overlaps ("do both")
- Pair with [[iana-whois-service]] and domain-WHOIS tools — IANA points you at the authoritative registry, those pull the specific domain's records.

## Trust & verifiability
`trust: trusted` — IANA is the authoritative operator of the DNS root; there is no more definitive source for TLD/registry facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iana-root-zone-database |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
