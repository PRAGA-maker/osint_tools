---
id: coalition-against-insurance-fraud
name: Coalition Against Insurance Fraud
description: Use when you have a subject/lead tied to possible insurance fraud and want the right reporting/lookup channel — returns a directory of US state fraud bureaus plus scam-type reference material.
url: https://insurancefraud.org/
category: search-engines
path:
- search-engines
bestFor: A gateway/directory to US state insurance-fraud bureaus and fraud-scheme reference, for routing and contextualising insurance-fraud leads.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Public resources (state-bureau directory, scam alerts, statistics) are free. Deeper databases (Fraud Tracker, arrests/convictions, legislative map) are member-only behind a login.
opsec: passive
opsecNote: A public non-profit advocacy site — you read reference material and a bureau directory, no target lookup and no subject-alerting. The gated databases require membership; do not attempt to access them without authorisation. Reporting a subject to a state bureau is an active real-world step — treat that as an escalation outside passive OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Coalition Against Insurance Fraud is an established national alliance of 300+ insurers, regulators and consumer groups; its bureau directory and statistics are authoritative reference.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- insurancefraud.org
- CAIF
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Coalition Against Insurance Fraud

> The national anti-insurance-fraud coalition's public site — a routing directory to every US state fraud bureau plus scam-scheme reference, rather than a person-lookup tool.

## When to use
You have a lead that touches suspected insurance fraud (staged accidents, fake claims, medical/workers'-comp schemes) and need to know where such activity is reported and investigated, or want reference on how a particular scheme works. It is a **gateway and context** resource: it points you to the correct state insurance-fraud bureau (each of which has its own reporting/lookup channel) and explains fraud typologies. Its own case databases (arrests/convictions, Fraud Tracker) are member-only.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://insurancefraud.org/.
2. For routing: use the "Report Fraud" / state-bureau directory to find the fraud bureau for the relevant US state and its contact/reporting portal.
3. For context: browse the scam-alert and statistics sections by fraud category (auto, workers' comp, medical, life, etc.).
4. Note which resources are gated (🔒 member-only) versus public.
5. Pivot: follow the state-bureau link to that agency's own site for actual case/lookup channels; use the typology reference to interpret documents you already hold.

## Inputs → Outputs
- **In:** a fraud-category or state context (no person selector required)
- **Out:** the appropriate state fraud-bureau contact/portal and scheme reference — leads to *other* sites' lookups, not a record itself
- **Empty/negative result looks like:** the specific data you want (a named case, a conviction record) sits behind the member login — this public site won't return it; go to the linked state bureau or a court-records source instead.

## Gotchas & OpSec
- Partial paywall: the Fraud Tracker and arrests/convictions databases need membership; the directory and reference are free.
- US-focused — not a source for non-US jurisdictions.
- This is a directory/reference, not a subject search; the actual lookups live on the state-bureau sites it links to.

## Overlaps ("do both")
- Complements court-records and public-records tools — this tells you *which* agency owns an insurance-fraud matter; those tools return the actual filings and dispositions.

## Trust & verifiability
`trust: trusted` — an established national coalition of insurers, regulators and consumer groups; its bureau directory and statistics are reliable, and any specific case claim should still be confirmed at the linked state agency or in court records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coalition-against-insurance-fraud |
| category | search-engines |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
