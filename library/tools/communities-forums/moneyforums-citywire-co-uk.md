---
id: moneyforums-citywire-co-uk
name: Citywire Money Forums
description: Use when you have a `username` active in UK investing circles and want their forum posts/history — a live UK money/investment discussion board searchable for handles and topics.
url: https://moneyforums.citywire.com/
category: communities-forums
path:
- communities-forums
bestFor: Reading a Citywire member's posting history and finding UK investment/money discussions where a subject or topic appears.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to read; registration/login required to post (and to see some member details).
opsec: passive
opsecNote: Reading public threads is passive. Creating an account to view more, or interacting, is active and leaves a footprint — use a sock-puppet account and never engage the subject. Note the forum moved from the .co.uk to the .com host.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The official Citywire (UK financial media) member forums; real user-generated content, but posts are self-reported and pseudonymous.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Citywire Funds Insider Forums
- moneyforums.citywire.com
tags:
- forums
- uk
- investing
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Citywire Money Forums

> A live UK investing/money discussion board — mine a member's post history or find threads mentioning your subject.

## When to use
Your subject is active in UK investing/personal-finance communities and you have (or suspect) a Citywire `username`, or you want to search the forum for mentions of a person, company, or scheme. Forum posts often leak location hints, timelines, relationships, and opinions a person wouldn't put on a public profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://moneyforums.citywire.com/ (the old moneyforums.citywire.co.uk redirects here).
2. Browse the sections (Investing, Money, Economics, Retirement, Property, General) or use site/Google `site:` search for a `username` or keyword.
3. Read the output: threads and a member's posts. Note timestamps, cross-references, and any self-disclosed detail.
4. Pivot: reuse the username across other platforms (username-enumeration tools), and follow any leaked selectors (locations, employers, links).

## Inputs → Outputs
- **In:** a Citywire `username` or a keyword/name
- **Out:** the member's `social-profile`/post history and matching threads
- **Empty/negative result looks like:** no posts under a handle means it's unused here (or the member deleted content) — try `site:` search and alternate spellings.

## Gotchas & OpSec
- Pseudonymous, self-reported content — corroborate any "fact" from a post elsewhere.
- Reading is passive; registering/posting is active — use a sock puppet and never contact the subject.
- Human-in-the-loop: some member details may need a logged-in account.

## Overlaps ("do both")
- Do both with username-enumeration tools — this gives the on-forum history; those check whether the same handle exists elsewhere.

## Trust & verifiability
`trust: community` — genuine forum but pseudonymous; treat posts as leads and verify independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | moneyforums-citywire-co-uk |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
