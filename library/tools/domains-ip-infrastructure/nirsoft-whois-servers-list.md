---
id: nirsoft-whois-servers-list
name: NirSoft Whois Servers List
description: Use when you need the authoritative WHOIS server for a TLD — returns a reference list of 200+ WHOIS servers to query the right registry directly.
url: http://www.nirsoft.net/whois_servers_list.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Looking up which WHOIS server to query for a given TLD when doing direct/CLI WHOIS lookups.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free static reference page from NirSoft; no account.
opsec: passive
opsecNote: The page itself is just a reference list — reading it reveals nothing about any target. (The actual WHOIS queries you then run touch registry servers, not the domain owner, and are passive.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by NirSoft, a long-established and reputable freeware/utilities author; the server list is a stable technical reference.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whois
- iana-whois
- icann-lookup
aliases:
- NirSoft whois servers
- whois_servers_list
tags:
- toddington
- curated-directory
- whois
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# NirSoft Whois Servers List

> A reference list of 200+ WHOIS servers keyed by TLD — the lookup table you need when running direct WHOIS queries against the correct registry.

## When to use
You're doing WHOIS the manual/CLI way and hit a TLD whose WHOIS server you don't know (many ccTLDs and newer gTLDs use their own servers). This NirSoft page maps TLDs to their authoritative WHOIS servers so you can query the right one directly — bypassing rate-limited or incomplete aggregators. A small enabling/reference tool (low direct MP relevance) that makes precise domain research possible.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.nirsoft.net/whois_servers_list.html.
2. Find the target's TLD (e.g. `.uk`, `.de`, `.io`) and note its WHOIS server hostname.
3. Query that server directly: `whois -h <server> example.tld` (CLI), or point a WHOIS tool at it.
4. Read the raw registry response — often more complete/current than a third-party aggregator.
5. Pivot: the WHOIS record → registrant/registrar/name-server leads (subject to redaction); feed into `[[whois]]` workflows and domain-history tools.

## Inputs → Outputs
- **In:** a `domain`'s TLD (to find the right server)
- **Out:** the authoritative WHOIS server hostname → enables a direct WHOIS query of that `domain`
- **Empty/negative result looks like:** the TLD isn't listed, or its server changed — the list is static and can lag; cross-check IANA's TLD database for the current WHOIS/RDAP endpoint.

## Gotchas & OpSec
- It's a static list — WHOIS servers occasionally change; verify against `[[iana-whois]]` if a query fails.
- Many registries now prefer RDAP over legacy WHOIS and redact registrant PII (GDPR) — expect masked contact data regardless of which server you hit.
- The page reveals nothing about any subject; only the follow-up queries touch registries (passively).

## Overlaps ("do both")
- Pairs with `[[whois]]` — this tells you *which* server; the WHOIS tool runs the query. Use together for accurate ccTLD/gTLD lookups.
- Pairs with `[[iana-whois]]`/`[[icann-lookup]]` as the authoritative source when the static list is out of date.

## Trust & verifiability
`trust: trusted` — NirSoft is a reputable, long-standing utilities publisher and the list is a stable technical reference. Confirm a server against IANA if a direct query returns nothing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nirsoft-whois-servers-list |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
