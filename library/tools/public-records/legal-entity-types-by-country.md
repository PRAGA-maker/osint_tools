---
id: legal-entity-types-by-country
name: Legal Entity Types by Country
description: Use when you have a company name whose suffix (GmbH, Sdn Bhd, Pty Ltd…) you want to decode — returns the likely jurisdiction and entity type to guide registry lookups.
url: https://en.wikipedia.org/wiki/List_of_legal_entity_types_by_country
category: public-records
path:
- public-records
bestFor: Reading a company's legal suffix to infer its country and structure before hitting the right registry.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free Wikipedia reference article; no account.
opsec: passive
opsecNote: Passive — a static reference page. You look up the meaning of a suffix, not the company itself, so nothing about your target is transmitted. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained Wikipedia list; broadly accurate as an orientation aid but crowd-edited, so confirm the definitive entity type against the country's official company register.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- List of legal entity types by country
- company suffix reference
tags:
- corporate
- reference
source: metaosint
lastVerified: '2026-08-05'
enrichment: full
---

# Legal Entity Types by Country

> A one-page decoder ring for company suffixes: what "GmbH", "Sdn Bhd", "Oy", or "Pty Ltd" tells you about a firm's country and legal form.

## When to use
You have an `employer-org` or company `name` carrying a legal suffix and you need to know which country's register to search and what kind of entity you are dealing with — before spending time in the wrong jurisdiction's records. A support tool for corporate/associate mapping, not a records source itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Wikipedia article at the URL.
2. Ctrl-F for the suffix on the company name (e.g. `GmbH`, `S.A.`, `Sdn. Bhd.`, `Oy`, `Pty Ltd`).
3. Read the entry: the country/countries that use it, the entity type (private limited, public, partnership, etc.), and cross-jurisdiction equivalents.
4. Use that to pick the right registry — e.g. `GmbH` → Germany's Handelsregister, `Sdn Bhd` → Malaysia's SSM, `Ltd` → check UK Companies House but beware many other countries reuse it.
5. Pivot: the identified jurisdiction feeds the correct national company register or an aggregator like OpenCorporates for the actual filing.

## Inputs → Outputs
- **In:** a company `name`/`employer-org` with a legal suffix
- **Out:** likely jurisdiction and entity type (a refined `employer-org` classification that points at the right registry)
- **Empty/negative result looks like:** the suffix isn't listed, or it maps to several countries — common for ambiguous forms like `Ltd`, `S.A.`, or `Inc`. Treat those as "needs corroboration from another signal" (address, phone country code, TLD), not as a settled jurisdiction.

## Gotchas & OpSec
- Many suffixes (`Ltd`, `S.A.`, `S.R.L.`) are reused across dozens of countries — the suffix narrows, it rarely proves, the jurisdiction.
- Companies can register in a jurisdiction unrelated to where they operate (offshore shells); the suffix reflects incorporation, not activity.
- Crowd-edited: use it to orient, then confirm the entity type in the official register.
- OpSec: fully passive; nothing about the target leaves your browser except the Wikipedia page load.

## Overlaps ("do both")
- Feed the identified jurisdiction into a company-registry or aggregator lookup — this article tells you *where* to look; the register tells you *what is actually filed*.

## Trust & verifiability
`trust: community` — a useful, broadly correct Wikipedia reference for orientation; the authoritative entity type and status always come from the country's official companies register, not from this list.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | legal-entity-types-by-country |
