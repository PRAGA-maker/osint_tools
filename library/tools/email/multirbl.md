---
id: multirbl
name: Multirbl
description: Use when you have an IP address or mail domain and want to check it against hundreds of DNS blacklists (RBL/DNSBL) at once to gauge its spam/abuse reputation.
url: https://multirbl.valli.org/dnsbl-lookup
category: email
path:
- email
bestFor: Bulk DNS-blacklist (RBL/DNSBL) reputation lookup for an IP or domain.
selectorsIn:
- ip-address
- domain
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free public web tool, no account.
opsec: passive
opsecNote: Passive — it queries public DNSBL/RBL servers about the IP/domain, not the person. Nothing is sent to the target's mail server beyond standard DNS reputation queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: multirbl.valli.org is a long-standing, well-regarded free DNSBL aggregator maintained by Ralf Hildebrandt (valli.org). Reliable for its narrow purpose.
missingPersonsRelevance: low
coverage: []
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mxtoolbox
- mxtoolbox-blacklists
aliases: []
tags:
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Multirbl

> Free DNS-blacklist aggregator — checks an IP or mail domain against hundreds of RBL/DNSBL lists in one pass.

## When to use
Mostly an infrastructure/deliverability tool. In an investigation it is a niche pivot: you have an `ip-address` or `domain` (e.g. the sender of a suspicious email to/from a subject, or the host behind a profile) and want to know its spam/abuse reputation — heavy blacklist presence flags throwaway/bulk-mail or compromised infrastructure. It does not identify people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to multirbl.valli.org/dnsbl-lookup.
2. Enter the `ip-address` or `domain`.
3. Read the per-list results: listed vs. not, across blacklist, whitelist, and informational lists.
4. Pivot: a "listed" sender supports a "this address/host is disposable or abusive" read; combine with `[[mxtoolbox]]` for full MX/SPF/DKIM context.

## Inputs → Outputs
- **In:** `ip-address`, `domain`
- **Out:** blacklist-reputation report (`metadata-exif`-style infrastructure metadata)
- **Empty/negative result looks like:** "not listed on any" — normal for clean mail hosts; tells you little about a person.

## Gotchas & OpSec
- Low direct value for finding a missing person; it characterizes infrastructure, not identities.
- Blacklist presence can be stale or shared-IP collateral; don't over-read it.
- For email-header tracing or MX/SPF context, pair with MxToolbox.

## Trust & verifiability
`trust: community` — established, openly documented DNSBL aggregator with a long maintenance history; reliable for its narrow purpose. MP relevance lowered to `low` because it characterizes mail infrastructure, not people.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | multirbl |
| category | email |
| selectorsIn → selectorsOut | ip-address, domain → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
