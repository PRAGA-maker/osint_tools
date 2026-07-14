---
id: medium-com-2
name: "Medium: Unconventional Guide to LinkedIn OSINT (article)"
description: Use when you have a `name`/`username` and want a methodology for investigating them on LinkedIn — a how-to article yielding techniques that produce `email`s and `social-profile`s while avoiding detection.
url: https://medium.com/ax1al/the-unconventional-guide-to-conducting-osint-on-linkedin-c9631b27935d
category: social-networks
path:
- social-networks
bestFor: Learning search-URL manipulation, tooling, and detection-avoidance for LinkedIn reconnaissance.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- email
status: live
pricing: free
costNote: Free to read on Medium (may hit Medium's metered paywall after a few articles/month; open in a private window if so).
opsec: passive
opsecNote: Reading the article is passive. The *techniques* it teaches include detectable actions — crucially, LinkedIn shows targets who viewed their profile via "Search Appearances"/"Who viewed your profile." Apply its methods only from a sock-puppet LinkedIn account with private mode enabled.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An individual practitioner's Medium write-up; the techniques are legitimate and widely used, but it's a personal guide (accuracy/currency not editorially verified), and LinkedIn's UI changes over time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ax1al LinkedIn OSINT guide
tags:
- linkedin
- LinkedIn & Similar Sites
- methodology
- reference
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Medium: Unconventional Guide to LinkedIn OSINT (article)

> A reference article — not a tool — collecting practical LinkedIn reconnaissance techniques, including the critical OpSec point that LinkedIn tells targets who looked at them.

## When to use
You are investigating a subject on LinkedIn (by `name`, `username`, employer, or title) and want a methodology rather than a lookup service: how to enumerate profiles, harvest emails, and manipulate search URLs — while staying undetected. Especially valuable for its OpSec warning: LinkedIn surfaces "Search Appearances" and "who viewed your profile," so naive browsing burns your investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the article at the URL (use a private window if Medium's paywall triggers).
2. Set up first: a sock-puppet LinkedIn account with **private/anonymous browsing mode** enabled — before touching any target.
3. Apply the techniques: `site:linkedin.com/in "Name" "Company"` Google dorks; LinkedIn search-URL parameters (firstName/lastName/company/title); export a profile to PDF; reverse-image the profile/background photos.
4. For email/employee discovery, the article points to InSpy + Hunter.io and theHarvester — verify any emails before use.
5. Pivot: discovered emails → email-OSINT and breach checks; confirmed profiles → cross-platform username matching.

## Inputs → Outputs
- **In:** `name`/`username` (plus company/title context)
- **Out:** methods that yield `social-profile`s and candidate `email`s
- **Empty/negative result looks like:** techniques that no longer work as LinkedIn changes its UI/anti-scraping — re-validate each method against current LinkedIn.

## Gotchas & OpSec
- Detection: LinkedIn notifies targets of profile views and shows search appearances — always use private mode on a sock puppet.
- The linked tools (Hunter.io etc.) have their own limits, keys, and costs; emails they return are guesses until verified.
- Personal blog content ages; cross-check steps before relying on them.

## Overlaps ("do both")
- Pairs with `[[recruitem]]`/X-ray search builders and `[[hunter-io]]` — this supplies the *method and OpSec*, those are the concrete tools it references.

## Trust & verifiability
`trust: community` — a practitioner write-up; the techniques are legitimate and commonly taught, but treat it as guidance to validate against current LinkedIn behaviour, not an authoritative or maintained tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | medium-com-2 |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
