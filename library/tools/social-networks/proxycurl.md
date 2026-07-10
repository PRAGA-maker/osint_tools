---
id: proxycurl
name: Proxycurl
description: Use when you have a `name`/`social-profile` and want enriched professional data (employer, role, contact) via API — but note the service has been discontinued; returns `employer-org`, `email`, `phone`.
url: https://nubela.co/proxycurl/
category: social-networks
path:
- social-networks
bestFor: (Historically) programmatic enrichment of LinkedIn-style profiles into structured person/company data.
selectorsIn:
- name
- social-profile
- employer-org
selectorsOut:
- employer-org
- email
- phone
status: down
pricing: freemium
costNote: Proxycurl is NO LONGER IN SERVICE (shut down; founder moved to a new venture, NinjaPear). It was formerly a paid API with limited free trial credits. Do not send new customers here — use it only to recognise legacy references and pivot to a live alternative.
opsec: passive
opsecNote: Was a server-side API — you queried Proxycurl, which fetched from professional networks; the target was not directly contacted by you. Moot now that the service is offline. Any archived Proxycurl data in a report should be treated as stale.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: Was a well-known commercial enrichment API (Nubela); data quality was decent but scraped from LinkedIn, raising ToS/accuracy caveats. Now defunct.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- Nubela Proxycurl
- LinkDB
tags:
- linkedin
- enrichment
- api
- defunct
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Proxycurl

> A once-popular commercial API for turning a name or LinkedIn URL into structured professional data — now shut down. Catalogued so you recognise legacy references and route to a live substitute.

## When to use
You encounter Proxycurl in an older playbook, tool list, or codebase and need to know its status, or you have a `name`/`social-profile` and want the *capability* it offered: programmatic enrichment of a person into `employer-org`, work history, `email`, and `phone`. **The service is offline** — treat any live dependency on it as broken and substitute an alternative.

## How to use it (`bestInteractionPattern`: api)
1. Recognise the reference: Proxycurl exposed People, Company, Contact, Jobs, and Search API endpoints keyed by an API key.
2. Check status: https://nubela.co/proxycurl/ now states "Proxycurl is no longer in service"; the LinkDB dataset and the API are discontinued.
3. Do **not** attempt to register or pay — the endpoint will not serve requests.
4. Pivot: for live LinkedIn-style enrichment use a currently-operating enrichment vendor, or fall back to manual profile review after finding the handle with `[[google-to-search-profiles-on-twitter]]`-style X-ray searches (LinkedIn variant).

## Inputs → Outputs
- **In (historical):** `name`, `social-profile` (LinkedIn URL), `employer-org`
- **Out (historical):** `employer-org`, role/work history, `email`, `phone`
- **Empty/negative result looks like:** any request today fails/returns service-discontinued — that is the expected result now, not a data miss.

## Gotchas & OpSec
- Human-in-the-loop: none historically (pure API); N/A now.
- OpSec: was passive/server-side. The real gotcha today is **staleness** — do not cite Proxycurl output as current.
- Data was scraped from LinkedIn; even historically it carried ToS and accuracy caveats.

## Overlaps ("do both")
- Was complementary to `[[google-to-search-profiles-on-twitter]]` (X-ray finds the handle; Proxycurl enriched it). With Proxycurl gone, lean on the X-ray + manual review path.

## Trust & verifiability
`trust: community` — reputable while it ran, but it is now **down**. Any Proxycurl-sourced field in an investigation must be re-verified against a live source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | proxycurl |
| category | social-networks |
| selectorsIn → selectorsOut | name, social-profile, employer-org → employer-org, email, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
