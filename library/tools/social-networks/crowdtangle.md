---
id: crowdtangle
name: CrowdTangle
description: Use when you want historical Facebook/Instagram public-post monitoring — but note the tool was SHUT DOWN by Meta in August 2024 and is no longer usable; its successor is the Meta Content Library.
url: https://www.crowdtangle.com/videosearch
category: social-networks
path:
- social-networks
bestFor: (Retired) Was Meta's tool for monitoring and searching public posts across Facebook, Instagram, and Reddit.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: down
pricing: free
costNote: Was free to approved researchers/journalists. Decommissioned by Meta on 14 August 2024; access no longer available.
opsec: passive
opsecNote: Moot — the service is offline. Do not spend investigative time attempting to access it. For current work, pursue access to the Meta Content Library (its successor), which is gated to approved academics/nonprofits.
humanInLoop: true
humanInLoopReason:
- account-login
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Was a first-party Meta product with authoritative platform data. The trust rating is historical; the tool itself is retired.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: true
relatedTools:
- meta-content-library
- crowdtangle-link-checker
aliases:
- CrowdTangle
tags:
- toddington
- curated-directory
- social-media
- retired
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# CrowdTangle

> Meta's retired public-post monitoring tool — shut down 14 August 2024. Included here so agents don't waste time on a dead endpoint; use the Meta Content Library instead.

## When to use
Historically: to search and monitor public posts, pages, and groups across Facebook and Instagram (and some Reddit), with leaderboards and historical timelines — valuable for tracking a public figure's or page's activity. **Now: do not use.** Meta decommissioned CrowdTangle on 14 August 2024. If you find it referenced in an older playbook, treat those steps as obsolete.

## How to use it (`bestInteractionPattern`: web-manual)
1. There is no live workflow — the site and dashboards are offline.
2. For equivalent capability, apply for the **Meta Content Library** (its official successor), which is restricted to qualified academic and nonprofit researchers via an application process.
3. For public post/profile monitoring outside Meta's gated tools, pivot to third-party social listening or direct platform search.

## Inputs → Outputs
- **In:** (formerly) `name`/`username`/keyword
- **Out:** (formerly) `social-profile` post monitoring and historical metrics
- **Empty/negative result looks like:** every request now fails or redirects — the product is retired, not merely rate-limited.

## Gotchas & OpSec
- **Status: down** — the single most important fact about this entry.
- Human-in-the-loop: the successor (Content Library) requires an application and identity review (**manual-review**), so it is not open-access.
- Don't cite CrowdTangle data as currently obtainable; anything you have from it is a historical snapshot.

## Overlaps ("do both")
- Succeeded by `[[meta-content-library]]` — the only sanctioned Meta path for this kind of public-post research today.

## Trust & verifiability
`trust: trusted` (historical) — it was a first-party Meta product, so past data was authoritative. But the tool is retired; verify any current need against the Meta Content Library or live platform search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crowdtangle |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
