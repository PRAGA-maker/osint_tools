---
id: charitable-impact
name: CharitableImpact
description: Use when you have a Canadian charity or `employer-org` name and want to confirm it and its giving context — returns `employer-org` charity detail and donation-platform presence.
url: https://www.charitableimpact.com
category: communities-forums
path:
- communities-forums
bestFor: Confirming a Canadian charity exists on a major donation platform and researching giving/charity context.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free to browse and search charities; donating (the platform's core function) moves money but browsing is free.
opsec: passive
opsecNote: Browsing/searching charities is passive. Do NOT attempt to view or infer another person's private donation history — donor records are not public, and probing them is out of scope and likely a privacy violation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A legitimate Canadian donor-advised giving platform; charity listings draw on CRA-registered charities, but treat platform pages as directory context, not the authoritative registry.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Charitable Impact
- charitableimpact.com
tags:
- charity
- canada
- donations
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# CharitableImpact

> A Canadian donor-advised giving platform — mainly useful in OSINT for confirming a charity/`employer-org` exists and gathering its public giving context, not for exposing individual donors.

## When to use
You have a Canadian charity or nonprofit (`employer-org`) tied to a subject — as an employer, a fundraiser they ran, or an organisation they publicly support — and want to confirm it and gather context. CharitableImpact lists CRA-registered charities with descriptions and public giving pages (campaigns, fundraisers). Useful for verifying a charity is real and active, identifying a public fundraiser a person organised, or corroborating a claimed nonprofit affiliation. It is not a way to see who donated what.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.charitableimpact.com and search the charity/`employer-org` name.
2. Read the charity's page for description, cause area and any public campaigns/fundraisers.
3. If a subject ran a public fundraiser, note the public campaign detail (title, cause, public organiser name if shown).
4. Cross-check the charity against the CRA Charities Directorate registry for authoritative status. Pivot: a confirmed `employer-org` feeds nonprofit-registry and news checks; a public fundraiser feeds social/news follow-up.

## Inputs → Outputs
- **In:** `employer-org` / charity name (or an organiser `name` on a public campaign)
- **Out:** `employer-org` charity detail (cause, description, public campaigns) and platform presence
- **Empty/negative result looks like:** no listing — the charity isn't on this platform (check the CRA registry directly); private donor data is never shown, so absence there is expected, not a finding.

## Gotchas & OpSec
- Donor records are private — do not attempt to obtain or infer an individual's giving; that's out of scope.
- Platform listing is context, not the authoritative registry — verify charity status with the CRA Charities Directorate.
- Canada-focused; passive throughout.

## Overlaps ("do both")
- Pairs with the CRA Charities Directorate and other nonprofit registries plus news search — this confirms platform presence/campaigns; the registry confirms legal charity status.

## Trust & verifiability
`trust: community` — a legitimate giving platform; listings are directory context drawn from registered charities, so confirm authoritative status via the CRA registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | charitable-impact |
| category | communities-forums |
| selectorsIn → selectorsOut | employer-org, name → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
