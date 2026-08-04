---
id: 527-explorer
name: 527 Explorer
description: Use when you have a `name` or `employer-org` tied to US political money and want their 527 org's finances — returns officers, donors, expenditures and associate links.
url: https://projects.propublica.org/527-explorer/
category: financial-crypto
path:
- financial-crypto
bestFor: Examining a US 527 political organisation's officers, contributors and spending to map money and relationships around a person.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Free public database from ProPublica; no account required.
opsec: passive
opsecNote: A public filings database — you search IRS 527 disclosures, not the subject; nothing is revealed to anyone. Standard browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by ProPublica from official IRS Form 8872 filings; the data is authoritative to the extent the organisations filed accurately, and ProPublica documents its sourcing.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nonprofit-explorer
- coronavirus-bailouts-search-every-company-approved-for-federal-loans-over-150k
- credibly-accused
- nursing-home-inspect
- parler-capitol-videos
- police-protest-videos
- the-nypd-files
aliases:
- ProPublica 527 Explorer
tags:
- bellingcat-toolkit
- companies-finance
- political-finance
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# 527 Explorer

> ProPublica's searchable database of US "527" political organisations, built from IRS filings — surface an org's officers, its donors, and its spending to map the money and people around a subject.

## When to use
Your subject is connected to US political fundraising — as an officer, donor, vendor or beneficiary of a 527 (tax-exempt political groups outside FEC regulation). Searching a `name` or `employer-org` here returns the organisation's leadership, its contributors and contribution amounts, and its expenditures, letting you tie a person to funds, to an organisation, and to the other names (`associate`s) that appear alongside them in the filings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://projects.propublica.org/527-explorer/ and search by organisation, contributor or officer name (advanced operators: quotes, AND/OR/NOT, wildcards).
2. Open an organisation to read its officers, contributions (donors + amounts), expenditures, and state.
3. Note names co-occurring as officers/donors/recipients as `associate` leads, and addresses in the filings as location hints.
4. Pivot: take org and officer names into `[[nonprofit-explorer]]`, business registries and FEC data; feed donor names into people-search.

## Inputs → Outputs
- **In:** `name` (officer/donor) or `employer-org` (the 527)
- **Out:** officers, contributors and amounts, expenditures, filing `address`es, and `associate` links among them
- **Empty/negative result looks like:** no matching org/person, or an org that filed sparse data — coverage is only as good as what groups reported to the IRS; absence isn't proof of no involvement.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — a public-filings search; the subject learns nothing.
- Scope/currency: US-only, limited to 527s (not all PACs), and only as complete/timely as the underlying IRS filings.

## Overlaps ("do both")
- Pairs with `[[nonprofit-explorer]]` and FEC/campaign-finance databases because a person's political and nonprofit money often spans all of them — cross-referencing builds the full financial-relationship picture.

## Trust & verifiability
`trust: trusted` — ProPublica over official IRS 527 filings, with documented sourcing; authoritative subject to filers' own accuracy, and every record traces back to a public filing you can cite.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
