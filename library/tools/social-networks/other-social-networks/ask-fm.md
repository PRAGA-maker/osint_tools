---
id: ask-fm
name: ASKfm
description: Use when you have an `username` and want to check for an ASKfm profile — returns the public Q&A history, likes and follower links that often reveal candid personal detail.
url: https://ask.fm/%3Cusername%3E
category: social-networks
path:
- social-networks
- other-social-networks
bestFor: Finding a person's ASKfm profile from a handle and mining their public question-and-answer history for volunteered personal information.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free public profiles; no account needed to view a public ASKfm page.
opsec: passive
opsecNote: Viewing a public profile is a passive web request and is not shown to the target. If you interact (ask a question, follow), that IS visible — and anonymous questions can still be traced by the platform, so stay read-only from a clean browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: ASKfm is a real, long-running Q&A social network popular with younger users; content is user-generated and self-reported, so treat disclosures as leads to corroborate.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ask.fm
- Ask FM
tags:
- qa-network
- social-networks
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# ASKfm

> A Q&A social network where users answer questions — often candidly — making public profiles a rich, under-searched source of volunteered personal detail, especially for younger subjects.

## When to use
You have a `username` (frequently reused from Instagram/Snapchat/Twitter) and want to check for an ASKfm presence. Because the format invites people to answer personal questions publicly, profiles can reveal school, location, relationships, interests, and friend interactions that a curated Instagram won't. Reach for it when profiling a younger subject or expanding a handle's footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Visit `https://ask.fm/<username>`, substituting the target handle.
2. If the profile exists, read the public Q&A history, likes, and the accounts they interact with.
3. Note volunteered details (place names, school, relationships) and the handles asking/answering (`associate`s).
4. Stay read-only — do not ask questions or follow (that's visible; anonymity is not guaranteed to you as the asker either).
5. Pivot: reused handle confirms identity across platforms (feed `[[sherlock]]`-style hunts); named friends become new subjects; disclosed places feed geolocation.

## Inputs → Outputs
- **In:** `username`
- **Out:** a public `social-profile` (Q&A history, likes) and interacting `associate`s
- **Empty/negative result looks like:** a 404/"user not found" (no ASKfm account under that handle) or an empty/private profile; absence just means this platform/handle isn't used.

## Gotchas & OpSec
- Self-reported: answers are what the user chose to say — engaging, exaggerated, or false; corroborate factual claims.
- Sensitive population: ASKfm skews young — handle minors' data with particular care and legal awareness.
- OpSec: passive when read-only; any interaction is visible and traceable.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`-style username hunters — confirm the same handle across platforms.
- Pairs with `[[commentpicker-com]]`/`[[toutatis]]` on the linked Instagram once the identity is corroborated.

## Trust & verifiability
`trust: community` — a genuine social platform, but its content is user-generated and self-reported, so treat disclosures as leads to verify, not established facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ask-fm |
