---
id: blockint-nl
name: blockint.nl
description: Use when you have a company or person `name` and want to trace ultimate beneficial owners (UBOs) across EU corporate registers — returns a country-by-country map of where and how to look up ownership.
url: https://www.blockint.nl/kyc/ubo-registers-in-the-eu/
category: public-records
path:
- public-records
bestFor: Finding which EU country's UBO/beneficial-ownership register to query, and how to access it, for a company or its owners.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- associate
- name
status: live
pricing: free
costNote: Free reference article. The individual national registers it links to vary — some are free, some charge per extract or require an authenticated business account.
opsec: passive
opsecNote: Reading this Blockint guide is fully passive. OpSec risk only appears once you follow a link into a national register and submit a query there — several EU registers log the searcher and some (post-2022 CJEU ruling) require you to declare a legitimate interest, which is an identifiable action.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Blockint, a Netherlands-based OSINT/KYC practitioner; it is a curated compilation, not an official source, and the author notes it is still being tested and updated.
missingPersonsRelevance: high
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- opencorporates-com
aliases:
- Blockint UBO registers guide
- UBO registers in the EU
tags:
- companysites
- Company Related Sites
- ubo
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# blockint.nl

> A practitioner-maintained directory of EU ultimate-beneficial-owner (UBO) registers: which country holds ownership data, whether it is public, and how to reach it.

## When to use
You have a company `name` (or a person you believe controls one) and need to know who ultimately owns or benefits from it. This page does not search for you — it tells you *which* national UBO register to query for a given EU/EEA country, whether that register is publicly accessible, what it costs, what language it is in, and what fields it exposes (owner name, date of birth, nationality, ownership percentage). Use it as the routing layer before you dive into a specific country's register.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.blockint.nl/kyc/ubo-registers-in-the-eu/.
2. Find the country where the company is registered (or where you suspect the beneficial owner sits).
3. Read the entry: is the register public? Does it need an account or declared legitimate interest? Is there a fee? Can you search by UBO name (e.g. Estonia allows this) or only by company?
4. Follow the direct link into that national register and run the actual lookup there.
5. Pivot: a UBO name + date of birth feeds people-search and sanctions/PEP checks; corporate links feed `[[opencorporates-com]]` for cross-border structure.

## Inputs → Outputs
- **In:** `name` / `employer-org` (company), or a suspected owner's `name`
- **Out:** routing to the correct `employer-org` register, and downstream `name` / `associate` (beneficial owners) once you query it
- **Empty/negative result looks like:** a country entry marked "not publicly accessible" or "still testing" — meaning you cannot self-serve and may need a local agent or paid KYC provider.

## Gotchas & OpSec
- This is a guide, not a database — it never returns ownership data itself, so don't treat a country listing as a result.
- Since the 2022 CJEU ruling struck down blanket public access, many EU UBO registers now gate access behind a declared legitimate interest or a professional login; the page's "public" flags may lag those changes, so verify at the register.
- Reading the guide is passive; querying a national register can be logged and, in some jurisdictions, attributed to you.

## Overlaps ("do both")
- Pairs with `[[opencorporates-com]]` — OpenCorporates gives you the corporate entity and officers across borders, while Blockint tells you where the *beneficial* (not just legal) ownership is disclosed and how to get it.

## Trust & verifiability
`trust: community` — it is a single practitioner's curated compilation (Blockint, NL). The routing information is generally sound but self-described as a work in progress, so confirm access rules against the official register before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blockint-nl |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, associate, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
