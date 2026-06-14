---
id: hatless-investigations-group
name: Hatless Investigations Group
description: Use when you want to reach a private investigations firm rather than run a self-service tool — this is a LinkedIn company page for an OSINT/investigations provider, not a searchable capability.
url: https://www.linkedin.com/company/hatless-investigations-group-llc/
category: image-video-face
path:
- image-video-face
bestFor: Identifying/contacting an investigations firm; not a self-service OSINT tool.
selectorsIn: []
selectorsOut: []
status: unknown
pricing: freemium
costNote: A commercial PI/OSINT firm; engaging their services would be paid. The LinkedIn page itself is free to view.
opsec: passive
opsecNote: Viewing a LinkedIn company page is low-risk, but LinkedIn may surface your visit to the page owner if you are logged in. Use a sock/logged-out session.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: This is a LinkedIn company profile listed under "Profile Images" on uk-osint.net, not a verified tool. It appears to be a private investigations firm rather than a self-service capability; treat as a service lead, not a searchable resource.
missingPersonsRelevance: low
coverage: []
auth: account
api: false
localInstall: false
registration: false
aliases: []
tags:
- profileimages
- Profile Images
source: uk-osint
lastVerified: ''
enrichment: full
---

# Hatless Investigations Group

> A LinkedIn company page for a private investigations / OSINT services firm — a contact/referral lead, not a self-service OSINT tool.

## When to use
Rarely, and only as a service referral: if a missing-persons case needs paid professional investigative help rather than a tool you run yourself. There is no image search, lookup, or input field here — it is a corporate LinkedIn profile. It was harvested into the "Profile Images" bucket on uk-osint.net, but it provides no searchable capability.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the LinkedIn page to read the firm's stated services, location, and staff.
2. If professional engagement is warranted, contact them through their listed channels.
3. There is nothing to query and no output selectors to harvest.

## Inputs → Outputs
- **In:** none (no search interface)
- **Out:** none (company/contact info only)
- **Empty/negative result looks like:** not applicable — this is a static company page.

## Gotchas & OpSec
- Not an OSINT tool; do not treat it as a profile-image or face-search capability. Its placement in that category appears to be a harvest miscategorization.
- OpSec: if logged into LinkedIn, your profile view may be visible to the company. Browse logged-out or with a sock account.

## Trust & verifiability
`trust: unverified` — a third-party LinkedIn company listing with no verifiable tool functionality. Honestly described from URL and category; not feature-verified and not a self-service resource, hence low missing-persons relevance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hatless-investigations-group |
| category | image-video-face |
| selectorsIn → selectorsOut | none → none |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
