---
id: name-com-bulk-search
name: Name.com Bulk Search
description: Use when you have a `domain` or brand stem and want to see, across many TLDs and permutations at once, which variants are registered vs available — returns registration status flagging a subject's other or impersonating domains.
url: https://www.name.com/names
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Bulk-checking domain permutations/TLDs to spot which are registered (a subject's other domains or typosquats).
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free to search availability; registering a domain costs money, but the availability search itself needs no payment.
opsec: passive
opsecNote: An availability search queries the registrar's system, not the target — passive. (Registering a domain is a different, attributable, active step; stay in search-only mode.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Name.com is an established ICANN-accredited registrar; availability status is authoritative (drawn from registry data), though it shows only registered-vs-available, not WHOIS ownership.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- name.com bulk domain search
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- domain-availability
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- name-com-united-states
---

# Name.com Bulk Search

> A registrar's bulk domain-availability checker — feed it a stem and it tells you, across many TLDs and permutations, which domains are registered (i.e. exist) and which are free.

## When to use
You have a `domain` or a brand/name stem and want to enumerate which related domains actually exist. "Registered = someone owns it" is a lead: a subject often holds several domains (personal, business, project) across TLDs, and impersonators register typo-variants. Bulk-checking permutations reveals the ones worth running through WHOIS/DNS. Use it as a discovery step before pivoting to ownership tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.name.com/names.
2. Enter the base name/stem; the tool checks availability across many TLDs at once.
3. Also enter deliberate permutations/typos (hyphens, plurals, common misspellings) to catch look-alike domains.
4. Note which variants come back "taken" (registered) — those exist and may be relevant.
5. Pivot: run each registered variant through WHOIS/RDAP ([[icann-whois-lookup]]) and DNS tools to find owner, host, and links back to the subject.

## Inputs → Outputs
- **In:** a `domain` / brand stem (and permutations)
- **Out:** registration status per variant → the set of registered `domain`s to investigate
- **Empty/negative result looks like:** all variants "available" — nothing registered under those spellings; try more permutations/TLDs, or the subject uses an unrelated domain name.

## Gotchas & OpSec
- Availability ≠ ownership: this only says registered-vs-free — it gives no WHOIS/owner data; that's the next tool.
- Registrar UI nudges you to buy — do NOT register anything; that's an attributable, active step and could tip off a subject holding the stem.
- Permutation coverage is only as good as the variants you supply — think like a typosquatter.
- OpSec: passive for search.

## Overlaps ("do both")
- Pairs with WHOIS/RDAP ([[icann-whois-lookup]]) and typosquat/permutation generators — this finds which variants exist; those reveal who owns them and how they're hosted.

## Trust & verifiability
`trust: trusted` — an accredited registrar reporting authoritative registry availability; reliable for existence, but by design it exposes no ownership, so confirm relevance via WHOIS.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | name-com-bulk-search |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
