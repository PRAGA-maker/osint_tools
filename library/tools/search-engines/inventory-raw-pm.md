---
id: inventory-raw-pm
name: Rawsec Cybersecurity Inventory
description: Use when you want to find a security/CTF/OSINT tool or resource by capability — returns a large searchable catalog of tools, platforms, and OSes (not selector lookups).
url: https://inventory.raw.pm/
category: search-engines
path:
- search-engines
bestFor: Searching a curated, tagged inventory (~1,700+ entries) of cybersecurity tools, CTF/bug-bounty platforms, operating systems, and resources.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open (MPL-2.0); no account or key. Fully browsable and searchable in-browser.
opsec: passive
opsecNote: A read-only tool directory — no target is queried and nothing about a subject is submitted. Only your own browsing (IP) is exposed to the host; the intelligence value is discovering the right tool, not data on a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: "Rawsec's CyberSecurity Inventory, maintained openly by Alexandre \"noraj\" Zanni under MPL-2.0 with a public git history; a well-known, actively curated meta-resource rather than an authoritative registry."
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Rawsec Inventory
- Rawsec's CyberSecurity Inventory
- inventory.raw.pm
tags:
- Search engines
- Bugbounty/vulnerabilities search tools
- curated-directory
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Rawsec Cybersecurity Inventory

> A large, tag-searchable catalog of security and OSINT tooling — when you know the capability you need but not the tool's name, search here.

## When to use
You need a tool for a specific job — a subdomain scanner, a CTF platform, a recon OS, an OSINT parser — and want to search by category/tag rather than guess names. The inventory indexes 1,700+ entries across tools, resources, CTF and bug-bounty platforms, operating systems, and certifications, each tagged and linked to its source. Use it as a discovery layer when this library or a task doesn't already point you at the right tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://inventory.raw.pm/.
2. Use the search box or browse by section (Tools, Resources, CTF platforms, OS, etc.) and filter by tag/language/category.
3. Open an entry to get its description, homepage/repo link, and metadata.
4. Follow the outbound link to the actual tool.
5. Pivot: found a candidate tool → verify it's live and free before use; if the inventory lacks your category, fall back to a broader awesome-list.

## Inputs → Outputs
- **In:** none — it is a searchable directory, not a selector query
- **Out:** matching tools/resources with descriptions, tags, and outbound links
- **Empty/negative result looks like:** a search with no matches — the capability may be uncatalogued here; try different tags or a larger index rather than concluding no tool exists.

## Gotchas & OpSec
- Human-in-the-loop: none; just search and read.
- Scope: security-engineering-leaning (pentest/CTF/bug-bounty), so people-search and missing-persons tooling is thinner than in dedicated OSINT directories — weight accordingly.
- OpSec: fully passive; no subject is touched.

## Overlaps ("do both")
- Pairs with OSINT-specific curated lists (e.g. [[appsec-fyi-osint-resources]] and awesome-osint indexes) — Rawsec is broad security tooling; the OSINT lists are narrower but denser for investigation work.

## Trust & verifiability
`trust: community` — an openly maintained (MPL-2.0, public git) inventory by a named, reputable maintainer; reliable as a curated discovery index, but it is a community catalog, not an authoritative or exhaustive registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inventory-raw-pm |
