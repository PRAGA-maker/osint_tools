---
id: dirt-diggers-digest-guide-united-states
name: Dirt Diggers Digest — Guide to Strategic Corporate Research
description: Use when you have a company or executive `name`/`employer-org` and want a methodology plus source list to map its ownership, directors, and accountability record — returns employer-org, associate, address leads.
url: https://www.corp-research.org/dddresearchguide
category: public-records
path:
- public-records
bestFor: A structured playbook and source directory for researching US companies, their owners, directors, and misconduct records.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: The guide is free; it points mostly to free sources but flags where key data sits behind paid/subscription or library-access services.
opsec: passive
opsecNote: Reading the guide exposes nothing about a target; the sources it recommends (SEC EDGAR, state registries, court dockets) are queried anonymously. No subject notification is involved in following its method.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authored by Philip Mattera, director of the Corporate Research Project and publisher of Dirt Diggers Digest; a respected, regularly updated corporate-research reference (last updated 2025).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- DDD Research Guide
- Guide to Strategic Corporate Research
tags:
- corporate-research
- company-search
- methodology
- curated-directory
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Dirt Diggers Digest — Guide to Strategic Corporate Research

> Phil Mattera's manual for digging into companies: which free (and paid) sources reveal a firm's ownership, directors, relationships, and accountability record — and how to work them in order.

## When to use
You have a company `name`/`employer-org` or an executive `name` and need to map the entity: who owns it (parent/subsidiary structure), who its directors, officers, and major shareholders are (`associate` links), where it operates (`address`), and what its accountability record is (court, environmental, labour, executive-pay). Use it when a person leads to a company and you need to follow the corporate thread rather than person-to-person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.corp-research.org/dddresearchguide.
2. Work its four sections in order: (1) basic company info (SEC filings, websites, financials), (2) company relationships (parents, directors, shareholders, suppliers), (3) accountability records (courts, environment, labour, exec comp), (4) industry-specific resources.
3. For each step, follow the recommended source (e.g. SEC EDGAR, state business registries, court dockets) and run the actual lookup there.
4. Note where the guide flags that data is only in paid/subscription tools — decide whether a library/academic gateway gives you free access.
5. Pivot: directors and shareholders become `associate`/`name` selectors to run through people-search; a registered address feeds location/records tools.

## Inputs → Outputs
- **In:** `name` (executive) or `employer-org` (company)
- **Out:** `employer-org` (corporate structure/ownership), `associate` (directors, officers, shareholders), `address` (registered/operating locations) — surfaced via the sources it directs you to
- **Empty/negative result looks like:** the guide can't itself be "empty"; a dead end is when its recommended sources return nothing — typically a private company with minimal filing obligations.

## Gotchas & OpSec
- It's a methodology + source list, not a database: it tells you where to look, you still run each query.
- US-centric; strongest for SEC-reporting and US-registered entities, thinner for private/foreign firms.
- Some highest-value sources it names are paid (subscription business-intelligence services) — the guide is honest about this.
- OpSec: passive throughout; the underlying public-records queries don't alert the company.

## Overlaps ("do both")
- Pairs with corporate-registry and SEC-filing lookup tools: the guide supplies the strategy and the ordered checklist, while those execute the individual record pulls.

## Trust & verifiability
`trust: trusted` — written and maintained by a named, credentialed corporate-research specialist (Philip Mattera / Corporate Research Project), updated as recently as 2025; the methodology is sound and the sources are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dirt-diggers-digest-guide-united-states |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
