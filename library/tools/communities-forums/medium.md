---
id: medium
name: Medium
description: Use when you have a `username` or `name` and want a person's Medium articles, profile, and the topics/people they engage with — returns social-profile and associate leads.
url: https://medium.com
category: communities-forums
path:
- communities-forums
bestFor: Finding a subject's long-form writing, profile, and interests on the Medium publishing platform.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Free to read profiles and much content; some articles are behind Medium's metered paywall. No account needed to view public profiles.
opsec: passive
opsecNote: Passive — reading public profiles/articles. Don't sign in with a real account to view a target (Medium logs reads and can show authors their stats); browse logged-out or with a sock-puppet, and avoid following/clapping which notifies the author.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Medium hosts self-published content — profiles and claims are user-authored, so treat biographical details as self-reported, not verified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- medium.com
tags:
- forums
- blogging
source: metaosint
lastVerified: '2026-07-29'
enrichment: full
---

# Medium

> A major long-form publishing platform — a subject's Medium profile can reveal their writing, professional interests, bio, linked accounts, and who they interact with.

## When to use
You have a `username` or `name` and want a person's Medium footprint: articles they've written (which expose expertise, opinions, employer, and sometimes personal detail), their profile bio and linked social/website, and the publications/authors they engage with. Long-form writing is often richer than social posts for understanding someone's work, views, and network. Good enrichment when a subject writes publicly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `medium.com/@<username>` directly, or search a `name`/topic (browse logged-out or sock-puppet).
2. Read their profile: bio, linked website/social, and article list.
3. Read their articles for professional/personal detail and cross-references; check who they follow and which publications they write for.
4. Note linked accounts and named collaborators.
5. Pivot: a linked website → domain tooling; the `username` → username search across platforms; co-authors/publications → `associate` and `employer-org` leads.

## Inputs → Outputs
- **In:** a Medium `username` (`@handle`) or a person's `name`
- **Out:** profile/bio, articles, linked accounts (`social-profile`), publications and interacting authors (`associate`)
- **Empty/negative result looks like:** no profile or no articles — the person isn't on Medium under that handle/name, or writes only privately; a common name yields many false matches, so confirm via bio/linked accounts.

## Gotchas & OpSec
- Self-published — bios and claims are unverified; corroborate.
- Some articles are paywalled/metered; a logged-out reader may hit limits.
- OpSec: passive — but avoid real-account interactions (follow/clap) that alert the author.

## Overlaps ("do both")
- Complements LinkedIn/personal-site discovery and username tools — Medium reveals a person's writing and views; cross-reference the same handle elsewhere to confirm identity.

## Trust & verifiability
`trust: unverified` — a self-publishing platform; content is authoritative for "what they wrote", not for the truth of biographical claims — verify independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | medium |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
