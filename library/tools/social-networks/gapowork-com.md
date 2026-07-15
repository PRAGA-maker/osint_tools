---
id: gapowork-com
name: gapowork.com
description: Use when a Vietnamese subject's `employer-org` uses GapoWork and you're identifying the platform — a closed enterprise workspace, so it yields context on the org, not open searchable profiles.
url: https://gapowork.com/
category: social-networks
path:
- social-networks
bestFor: Recognising GapoWork as a Vietnamese enterprise collaboration platform when it appears in a subject's digital footprint.
selectorsIn:
- employer-org
- username
selectorsOut:
- employer-org
status: live
pricing: freemium
costNote: GapoWork is a B2B SaaS "digital workplace" sold to organisations (like Meta's Workplace); there is a free tier for teams but content lives inside private company workspaces. There is no public people-search — you cannot look up a stranger.
opsec: passive
opsecNote: Passive from the outside — the public marketing site reveals nothing about individuals. Any actual member data sits behind an organisation's private login; attempting to access a workspace you don't belong to would be intrusion, not OSINT. Treat this as a platform-identification datapoint only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: GapoWork is a real, established Vietnamese workplace-software product (Gapo/GapoWork), used by 1000+ organisations; it is legitimate but is a closed enterprise tool, not an open OSINT source.
missingPersonsRelevance: high
coverage:
- vn
auth: account
api: false
localInstall: false
registration: true
invitationOnly: true
relatedTools: []
aliases:
- GapoWork
- Gapo Work
tags:
- gsocialmedia
- General Social Media Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# gapowork.com

> GapoWork — a Vietnamese enterprise collaboration platform (a "Workplace by Meta" equivalent); useful as a footprint/attribution signal, not as a searchable directory.

## When to use
You've found a reference to "GapoWork" in a Vietnamese subject's footprint — an email invite, a shared link, a mention of their company's internal tools — and need to know what it is. GapoWork is a **closed, per-organisation** digital workplace (chat, tasks, internal comms). Its value to you is contextual: it tells you the subject's `employer-org` is a Vietnamese company using this platform. It is **not** a place to search for a person; there is no public profile directory.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gapowork.com/ to confirm the platform's identity and read its public (Vietnamese-language) marketing pages.
2. Recognise it as an enterprise workspace tied to a specific organisation — the interesting fact is *which* organisation, which you learn from the surrounding context, not from Gapo itself.
3. Do not attempt to enter a workspace you have no legitimate access to.
4. Pivot: the platform points you at a Vietnamese `employer-org`; research that company through Vietnamese business registries and public social media instead.

## Inputs → Outputs
- **In:** an observed `employer-org`/platform reference (occasionally a `username` seen in a link)
- **Out:** confirmation of the `employer-org`'s tooling/context — no open personal data
- **Empty/negative result looks like:** the public site tells you nothing about any individual — that's expected; treat a member-only workspace as a dead end for external OSINT.

## Gotchas & OpSec
- Closed platform: no public search, no profile discovery. Anything member-level requires legitimate access.
- Vietnamese-language, VN-focused — relevance is essentially limited to subjects with Vietnamese employer ties.
- OpSec: **passive** at the marketing-site level; going further would be unauthorised access — don't.

## Overlaps ("do both")
- Pair with Vietnamese corporate/business-registry research and mainstream social platforms — those give you the actual people and org details GapoWork keeps private.

## Trust & verifiability
`trust: community` — a legitimate, well-established Vietnamese SaaS product. It is exactly what it claims to be; the limitation is that it's a closed enterprise tool, so it produces context, not open records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gapowork-com |
| category | social-networks |
| selectorsIn → selectorsOut | employer-org, username → employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
