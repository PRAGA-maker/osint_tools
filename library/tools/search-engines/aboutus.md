---
id: aboutus
name: AboutUs
description: Use when you have a `domain` and want a legacy profile of a website/business — a wiki of site descriptions and contact info, now largely archival and best checked via web archives.
url: https://www.aboutus.com
category: search-engines
path:
- search-engines
bestFor: Pulling a historical, wiki-style description and contact details for a website or business domain (mostly of archival value now).
selectorsIn:
- domain
selectorsOut:
- domain
- employer-org
status: degraded
pricing: free
costNote: Free to browse; the wiki is no longer actively maintained, so treat entries as legacy/archival rather than current.
opsec: passive
opsecNote: Passive — you read a public wiki about a domain; the domain owner is not notified. Nothing to leak beyond your own visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A crowdsourced site-directory wiki that peaked around 2008–2014 (20M+ entries) and is now inactive/unmaintained; entries are user-generated, often stale, and should be corroborated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- aboutus.com
- AboutUs.org
tags:
- toddington
- curated-directory
- domain-profile
- legacy
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# AboutUs

> A once-huge crowdsourced wiki of website profiles — now inactive, so its value is archival: a possible legacy description, era, and contact details for a domain, best read as a historical snapshot.

## When to use
You have a `domain` (a company site, an old business, a defunct project) and want background on what it was — a description, its niche, historical contact/ownership hints. AboutUs built profiles for tens of millions of sites in its 2008–2014 heyday; the wiki is no longer maintained, so reach for it when you're researching a domain's *past* rather than its present, and expect to lean on web archives for anything time-sensitive.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.aboutus.com and search or navigate to the domain's page (e.g. its Domain Page entry).
2. Read the profile: site description, category, and any listed contact/ownership details.
3. Because entries can be stale, cross-check the same domain in the Wayback Machine for a dated snapshot, and against current WHOIS/infra tools for present-day data.
4. Pivot: a described `employer-org`/business feeds corporate-registry research; historical contact details feed people/email OSINT; the profile's era helps date a domain's activity.

## Inputs → Outputs
- **In:** a `domain`
- **Out:** a legacy wiki profile — site description, category, and historical contact/`employer-org` hints
- **Empty/negative result looks like:** no page for a domain (common for smaller or newer sites) means it was never profiled — and even where a page exists, the data may be years out of date.

## Gotchas & OpSec
- **Inactive/archival:** the wiki isn't maintained, so treat everything as historical and verify against current sources.
- User-generated entries are uneven in accuracy — corroborate before relying on any contact or ownership detail.
- For current domain intelligence, prefer WHOIS, passive DNS, and `/.well-known/` recon (`[[well-known-dev]]`); use AboutUs for the backstory.

## Overlaps ("do both")
- Pairs with the Wayback Machine and WHOIS/infra tools — AboutUs offers a human-written legacy description, archives give dated snapshots, and WHOIS/infra give the present-day technical ownership picture.

## Trust & verifiability
`trust: community` — a crowdsourced, now-unmaintained wiki; entries are user-generated and often stale, so use it for leads and historical context, and confirm anything decisive elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aboutus |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
