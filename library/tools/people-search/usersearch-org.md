---
id: usersearch-org
name: Usersearch.org
description: Use when you have a `username`, `email`, `phone` or profile `image` and want to find matching accounts across social/dating/gaming/crypto sites — returns social profiles and linked accounts.
url: https://usersearch.org/index.php
category: people-search
path:
- people-search
bestFor: Reverse username/email/phone/picture sweep across 3,000+ social, dating, gaming and crypto platforms.
selectorsIn:
- username
- email
- phone
- image
selectorsOut:
- social-profile
- name
- username
status: live
pricing: freemium
costNote: Username searches are free with no signup on usersearch.org; email/phone and deeper "20+ data type" checks moved to usersearch.com / usersearch.ai with free basics and premium tiers.
opsec: passive
opsecNote: Searches run server-side against the platform's index, so the target's accounts are not directly probed by you and receive no notification. You disclose the selector to Usersearch; use a sock-puppet browser. Nothing is sent to the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established reverse-lookup aggregator (since 2012) with large claimed coverage; results are candidate matches from public data, so expect false positives on common handles.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- UserSearch
- usersearch.org
tags:
- Universal Contact Search and Leaks Search
- reverse-username
- account-discovery
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- user-search
- username-search
---

# Usersearch.org

> A veteran reverse-lookup engine: take a username, email, phone, or photo and find the matching accounts across thousands of social, dating, gaming and crypto sites.

## When to use
You have a `username`, `email`, `phone`, or a profile `image` and want to map a subject's online footprint — especially across dating and niche/crypto communities that general username scanners miss. A strong pivot when one handle or contact needs to become a spread of `social-profile`s revealing a real `name` and further leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://usersearch.org/index.php in a sock-puppet browser.
2. Choose the lookup type (username / email / phone / image) and enter the selector.
3. Pick a scan depth (Lightning → Complete; more sites = slower). Username scans are free here; email/phone/advanced route to usersearch.com/.ai.
4. Read results: sites where the selector resolves to an account, with `social-profile` links; open each to confirm it is the same person.
5. Pivot: a confirmed dating/gaming profile with a real name feeds people-search; an avatar feeds `[[reverse-image-search]]`; a linked email feeds email-OSINT.

## Inputs → Outputs
- **In:** `username`, `email`, `phone`, or `image`
- **Out:** matching `social-profile`s (incl. dating/crypto), display `name`s and `username`s
- **Empty/negative result looks like:** few/no hits — a rare handle, a private person, or coverage gaps. Common handles return noisy unrelated matches. Absence is not proof of no accounts.

## Gotchas & OpSec
- False positives: same-handle ≠ same human. Verify each hit by opening the profile and cross-checking avatar/bio/links.
- The tiered domains (org/.com/.ai) gate email/phone and deep checks behind free-basic-plus-premium — the free username tier is the reliably no-cost piece.
- OpSec: **passive** — server-side scan, nothing reaches the target; still use a sock puppet.

## Overlaps ("do both")
- Pairs with `[[user-searcher]]` and Sherlock/WhatsMyName-class tools — coverage lists differ (Usersearch leans strong on dating/crypto), so run several and union the results.

## Trust & verifiability
`trust: community` — a long-running aggregator with no per-record provenance; treat hits as candidates to verify by opening each profile, and confirm identity across multiple corroborating accounts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usersearch-org |
| category | people-search |
| selectorsIn → selectorsOut | username, email, phone, image → social-profile, name, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
