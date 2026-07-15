---
id: search-linkedin-intelligence-recruitment-software
name: Search LinkedIn - Intelligence Recruitment Software
description: Use when you have a `name`/`employer-org` and want to find someone's LinkedIn profile past LinkedIn's search limits — a free Chrome extension blending X-ray and direct search to return profiles.
url: http://www.intel-sw.com/blog/search-linkedin
category: social-networks
path:
- social-networks
bestFor: Finding LinkedIn profiles that X-ray-only or in-network-only searches miss, via a hybrid Chrome extension.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: The Chrome extension is free; the author invites feedback. A LinkedIn account improves the direct-search half but isn't required for the X-ray half.
opsec: active
opsecNote: The direct-search component runs queries inside LinkedIn while you're logged in, and LinkedIn records searches/profile views against your account (and may notify viewed users depending on your privacy setting). Use a sock-puppet LinkedIn account in private/anonymous-view mode; the X-ray (Google) component alone is passive.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: A free tool from Intelligence Software (intel-sw.com), a recruitment-search vendor; recommended across several OSINT lists, but a small third-party extension dependent on LinkedIn's shifting search behaviour.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- intel-sw Search LinkedIn
- Intelligence Software LinkedIn search
tags:
- linkedin
- browser-extension
- x-ray-search
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Search LinkedIn - Intelligence Recruitment Software

> Intelligence Software's free Chrome extension that combines X-ray (Google) and direct LinkedIn searching to surface profiles neither method finds alone.

## When to use
You have a `name` (optionally plus an `employer-org`, school, or location) and need their LinkedIn profile, but LinkedIn's own search is throttled by your network/account tier and a plain `site:linkedin.com` X-ray returns thin, stale snippets. This tool bridges the two — using X-ray's full-public reach and direct search's richer data — to catch professionals the standard approaches miss, useful for tying a subject to an employer, role, or location.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Chrome extension from http://www.intel-sw.com/blog/search-linkedin.
2. Enter the subject's name plus any qualifiers (company, title, city).
3. Run the hybrid search; review the merged results — public profiles found by X-ray and in-network profiles surfaced via direct search.
4. Open the profile for employer/role history and pivot: employer feeds corporate lookups; a confirmed identity feeds people-search; profile photo feeds face/reverse-image tools.

## Inputs → Outputs
- **In:** `name` (+ optional `employer-org`, school, location)
- **Out:** `social-profile` (LinkedIn URL), `employer-org` / role history
- **Empty/negative result looks like:** no distinct profile, or only generic company/search pages. LinkedIn increasingly restricts what non-connections can see, so a thin result may reflect its limits rather than the person having no profile — retry with different qualifiers.

## Gotchas & OpSec
- **Two engines, two OpSec profiles:** X-ray via Google is passive; the direct-LinkedIn half runs under your logged-in session and is logged by LinkedIn — use a sock-puppet account in anonymous-browsing mode (`account-login` human-in-loop).
- Small third-party extension tracking LinkedIn's changes — expect occasional breakage; the author notes it's still being improved.
- Verify identity on the live profile; name collisions are common in large companies.

## Overlaps ("do both")
- Pairs with plain `site:linkedin.com` dorks and dedicated LinkedIn X-ray builders (e.g. recruitin/recruitem) — run more than one, since each blends X-ray and direct search differently and surfaces different profiles.

## Trust & verifiability
`trust: community` — a reputable-vendor freebie widely cited in OSINT lists, but it only reaches into LinkedIn; the data and its completeness are LinkedIn's. Confirm every hit on the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-linkedin-intelligence-recruitment-software |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
