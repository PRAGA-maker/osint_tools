---
id: corporationwiki
name: CorporationWiki
description: Use when you have a `name` (or `employer-org`) and want to map a person's US business ties — returns associated companies, co-officers, and known addresses.
url: https://www.corporationwiki.com/
category: public-records
path:
- public-records
bestFor: Linking a US person to the companies they are (or were) an officer of, and to the other people around those companies.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Core people/company search and connection graphs are free; the site sells a paid "Enhanced Business Search" but the free tier is fully usable for pivoting.
opsec: passive
opsecNote: Passive — you query CorporationWiki's aggregated copy of public corporate filings, not the registry or the subject directly, so nothing reaches the target. Use a sock-puppet browser out of habit; the site is ad-heavy and fingerprints visitors.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregator of US Secretary-of-State corporate filings; officer names and addresses are only as current as the underlying state filings, which lag reality by months to years.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- opencorporates
aliases:
- Corporation Wiki
- corporationwiki.com
tags:
- company-research
- business-registry
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# CorporationWiki

> A free graph of US business filings that turns a person's name into the companies and co-officers connected to them.

## When to use
You have a `name` and suspect the subject has run, owned, or been an officer of a US business — or you have an `employer-org` and want the people behind it. CorporationWiki indexes 40M+ people and 50M+ US companies from state Secretary-of-State filings, so it is a fast way to surface a person's corporate footprint, business partners (`associate`), and the addresses those filings list. Especially useful for a missing person who was self-employed or ran a small LLC.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.corporationwiki.com/ and search the subject `name` (or company name).
2. Pick the matching person profile — disambiguate by state/city, since common names collide.
3. Read the profile: it lists companies the person is tied to, their role (officer/agent/director), and a connection graph linking co-officers and shared addresses.
4. Pivot: each connected company page lists other officers (`associate`) and a registered `address`; each address can be cross-checked against people-search and property tools.
5. Corroborate every hit against the primary state registry before treating it as fact.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `employer-org` (linked companies), `associate` (co-officers/partners), `address` (registered/filing addresses)
- **Empty/negative result looks like:** "No results" or only unrelated same-name people — means no US corporate filing links this person, not that they have no business history (sole proprietors and out-of-scope states may be absent).

## Gotchas & OpSec
- Data is a stale mirror of state filings; a "current" officer may have resigned years ago. Treat as a lead, not proof.
- Common names produce merged or wrong profiles; always confirm with a second selector (city, middle name, company).
- The site hosts opt-out removals, so some people are deliberately absent.
- OpSec: passive lookup of public records — no notification to the subject.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` — OpenCorporates draws directly from official registers with better provenance, while CorporationWiki's connection graph surfaces the human network (co-officers, shared addresses) faster.

## Trust & verifiability
`trust: community` — a commercial aggregator, not an authoritative source; every company/officer/address claim should be verified against the originating Secretary-of-State record before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | corporationwiki |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
