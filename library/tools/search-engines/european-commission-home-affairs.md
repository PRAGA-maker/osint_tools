---
id: european-commission-home-affairs
name: European Commission (Home Affairs portal)
description: Use when you need EU-level entry points on internal security, migration, and anti-trafficking — returns links to official EU databases, agencies, and reports.
url: https://commission.europa.eu/index_en
category: search-engines
path:
- search-engines
bestFor: A jumping-off hub to official EU home-affairs, internal-security, and justice resources.
selectorsIn: []
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Official EU institutional site; entirely free and open, no account.
opsec: passive
opsecNote: Reading a public government portal is passive and unremarkable. Standard clean-browser hygiene is enough; there is no per-subject query here to leak.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party European Commission website; authoritative for EU policy and as a gateway to official EU agencies and databases.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- e-justice-europa-eu
- eu-consolidated-corporate-registers
- eu-sanctions-tool
- europa-eu
- europa-press-releases
- european-union-open-data-portal
- eurostat
- frontex-migratory-map
- inspire-geoportal
- vat-number-validation
aliases:
- European Commission Home Affairs
- DG HOME
- commission.europa.eu
tags:
- toddington
- curated-directory
- specialty-search
- government
- eu
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# European Commission (Home Affairs portal)

> The official EU Commission gateway — used not as a search engine but as an authoritative index into home-affairs, internal-security, and anti-trafficking resources.

## When to use
You are working an EU-cross-border angle — organised crime, migration, human trafficking, sanctions — and need the authoritative starting point rather than a third-party summary. This is the Commission's own site; from it you navigate to the Home Affairs (DG HOME) and Justice sections, which link out to the official agencies and databases (Europol, Frontex, e-Justice, EU sanctions map) that actually hold searchable records. Treat it as a hub that tells you *which* official tool to use next.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://commission.europa.eu/index_en.
2. Navigate via the topic menu to "Home affairs," "Internal security," "Borders and migration," or "Justice."
3. From the relevant DG page, follow links to the specific database, agency, or report you need — the Commission page is signposting, not the dataset itself.
4. Use the site's own search box for policy documents, press releases, and named initiatives.
5. Pivot: hand off to the linked official tools — `[[eu-sanctions-tool]]`, `[[e-justice-europa-eu]]`, `[[frontex-migratory-map]]`, `[[european-union-open-data-portal]]` — which are the actual searchable endpoints.

## Inputs → Outputs
- **In:** none (topic navigation, not a selector query)
- **Out:** authoritative links to EU agencies/databases and to policy documents; identifies the responsible `employer-org` (which EU body owns a dataset)
- **Empty/negative result looks like:** you land on a policy overview with no person-level data — expected. The Commission homepage holds no searchable people records itself; the value is correctly routing you to the body that does.

## Gotchas & OpSec
- This is a portal, not a database: do not expect to search a name here. Its worth is authoritative navigation and confirming which official tool is canonical.
- The bookmarked URL is the general Commission homepage; the home-affairs material lives a click or two in under DG HOME/Justice, and menus are periodically reorganised.

## Overlaps ("do both")
- Pairs with the specific EU endpoints it links to — `[[eu-sanctions-tool]]`, `[[eu-consolidated-corporate-registers]]`, `[[european-union-open-data-portal]]`, `[[eurostat]]` — use this to find the right one, then those to actually query.

## Trust & verifiability
`trust: trusted` — it is the first-party European Commission site, authoritative for EU policy and as a directory of official agencies; the caveat is only that it is a hub, so the real data lives in the tools it points to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | european-commission-home-affairs |
| category | search-engines |
| selectorsIn → selectorsOut | (none) → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
