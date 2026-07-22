---
id: svbtle
name: Svbtle
description: Use when you have a `username` and want to find a subject's minimalist blog on the Svbtle network — returns `social-profile`, long-form posts and disclosed personal detail.
url: https://svbtle.com
category: communities-forums
path:
- communities-forums
bestFor: Finding a person's long-form blog posts and profile on the invite-oriented Svbtle publishing network.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free to read published blogs; publishing is a paid/curated membership.
opsec: passive
opsecNote: Reading and dorking public blogs is passive and invisible to the author. Do not sign up or comment from an attributable identity if you need to interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small, design-led blogging network historically favoured by tech/design writers; posts are self-authored opinion/personal content, useful as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- svbtle.com
tags:
- blogging
- social-network
- long-form
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Svbtle

> A minimalist, curated blogging network popular with tech and design writers — a place a subject may keep long-form posts that reveal work, opinions and personal detail under a chosen handle.

## When to use
You have a `username` or `name` and want to find a subject's writing. Svbtle blogs are typically at `username.svbtle.com` or reachable from the network, and long-form posts often disclose employer, projects, location cues, interests and links to other profiles. Good for confirming a person's professional/creative identity, recovering a reused handle, and mining self-written content for pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try `https://<username>.svbtle.com` directly, browse the network, or Google-dork it: `site:svbtle.com "<username or name>"`.
2. Open the blog and read posts for volunteered detail — role, projects, city, linked socials, personal context.
3. Follow outbound links the author includes (Twitter/GitHub/personal site).
4. Pivot: a reused `username` feeds cross-platform enumeration; linked profiles feed platform lookups; disclosed employer/location feeds registry/geolocation checks.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (blog + posts), reused `username`, linked profiles and self-disclosed detail
- **Empty/negative result looks like:** no blog at the handle and no dork hits — the subject doesn't publish here (a small, curated network, so most people won't).

## Gotchas & OpSec
- Small, invite/curated network — expect nothing for most subjects; skews tech/design.
- Self-authored content is opinion/personal narrative; corroborate factual claims.
- Passive to read; interacting is attributable — sock puppet only.

## Overlaps ("do both")
- Pairs with Medium, personal-site discovery and cross-platform username tools — Svbtle is one blogging venue; those catch the writing a subject keeps elsewhere.

## Trust & verifiability
`trust: community` — a legitimate small blogging platform; content is self-authored, so treat disclosures as leads to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | svbtle |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
