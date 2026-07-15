---
id: recruitryte-com
name: recruitRyte
description: Use when you have a `name` / role / `employer-org` and want a ready-made LinkedIn X-Ray Boolean string to run in Google — returns a search query that surfaces matching `social-profile` links.
url: https://recruitryte.com/
category: social-networks
path:
- social-networks
bestFor: Generating LinkedIn X-Ray Boolean search strings for sourcing a person by role/skills/company.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: The Boolean-generator and a single resume↔JD match are free with signup; bulk resume matching (100/job, multi-job, 2,500 matches/mo) is a paid Pro tier. The OSINT-relevant Boolean generator sits in the free tier.
opsec: passive
opsecNote: Generating a Boolean string on recruitRyte is passive and reveals nothing to the target. The actual search you run afterward (Google X-Ray of linkedin.com) is what touches third parties — do that from a sock-puppet browser, and note LinkedIn may surface you if you click into profiles while logged in.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial AI recruiting product, not an OSINT tool per se; its Boolean generator is a convenience wrapper around standard `site:linkedin.com/in` X-Ray syntax you could hand-write.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- google-com-86
aliases:
- recruitryte
- recruitRyte Boolean generator
tags:
- linkedin
- LinkedIn & Similar Sites
- boolean-search
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# recruitRyte

> An AI recruiting copilot whose OSINT-useful feature is a free LinkedIn X-Ray Boolean query generator — turn a role/company/skills brief into a copy-paste Google search string.

## When to use
You want to enumerate people matching a role, skill set, or `employer-org` on LinkedIn and would rather have a well-formed Boolean X-Ray string than write one by hand. recruitRyte's core product (AI resume-to-job matching) is not an OSINT function — you do NOT feed it a person to find them. The relevant piece is the Boolean/X-Ray generator that outputs a `site:linkedin.com/in "…"` query you run in Google.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://recruitryte.com/ and open the Boolean / LinkedIn X-Ray generator tool (free signup may be required).
2. Enter the job title/role, required skills, and optionally location or company.
3. Copy the generated Boolean string (it will look like `site:linkedin.com/in ("title" AND "skill" AND "company")`).
4. Paste it into Google and review the `social-profile` results.
5. Pivot: matched LinkedIn profiles feed name/employer confirmation and further social-profile OSINT.

## Inputs → Outputs
- **In:** `name` / role / `employer-org` / skills (as query components)
- **Out:** a Boolean X-Ray string that, when run in Google, returns `social-profile` (LinkedIn) links
- **Empty/negative result looks like:** the generator always produces a string; "empty" is when running that string in Google returns no LinkedIn profiles — meaning your constraints are too narrow, not that the person doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: account signup/login is typically required to use the tools; use a sock-puppet account.
- It is a marketing/recruiting SaaS — the resume-matching features are a paywalled distraction from the free Boolean generator you actually want.
- You can replicate its output by hand; treat it as a convenience, not a unique data source.

## Overlaps ("do both")
- Pairs with `[[google-com-86]]` and general Google-dorking — recruitRyte just writes the dork; Google runs it. If you already know X-Ray syntax you can skip this entirely.

## Trust & verifiability
`trust: community` — a legitimate commercial recruiting tool, but it holds no data of its own for lookups; its OSINT value is purely the query it hands you, which you verify by running the search yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | recruitryte-com |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
