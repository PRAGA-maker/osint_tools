---
id: intensedebate
name: IntenseDebate
description: Use when you have an IntenseDebate `username` and want that commenter's cross-site history and profile — returns their comment history, linked accounts, and profile details.
url: https://intensedebate.com
category: documents-metadata
path:
- documents-metadata
bestFor: Pulling a commenter's public profile and cross-blog comment history from the IntenseDebate comment platform to enumerate their footprint and views.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
- associate
status: live
pricing: free
costNote: Free comment platform by Automattic (WordPress); public commenter profiles and comment history are viewable without an account.
opsec: passive
opsecNote: Viewing a public IntenseDebate profile/comment history is passive read-only browsing — the commenter isn't notified. Don't log in or reply from a real account; a sock puppet keeps your interest hidden.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legitimate Automattic-owned comment system; the data is the user's own public comments, but linked "identities" are self-asserted and should be corroborated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- disqus
- disqus-comment-history
aliases:
- IntenseDebate comments
- intensedebate.com profile
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- comment-platform
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# IntenseDebate

> A third-party blog comment system (Automattic-owned, à la Disqus) whose public profiles let you pull a commenter's cross-site comment history and self-linked accounts.

## When to use
You have an IntenseDebate `username` (seen on a blog's comment thread) and want to expand it: their profile page aggregates the comments they've left across the many blogs using IntenseDebate, plus any social accounts they linked. That gives you a subject's opinions, activity timeline, other sites they frequent, and people they interact with — a classic comment-platform pivot, same idea as enumerating a Disqus profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a comment, note the commenter's IntenseDebate `username`/profile link.
2. Open their profile at `intensedebate.com/people/<username>` (or click through from the comment).
3. Read the profile: comment history across sites, join date, any linked social accounts/website, and their bio.
4. Work the history — recurring blogs reveal interests/communities; replies reveal `associate` links; a linked site/handle is a direct pivot.
5. Pivot: run linked handles/emails through username- and email-search tools; corroborate any real `name` against an independent source before relying on it.

## Inputs → Outputs
- **In:** `username` (IntenseDebate commenter handle).
- **Out:** `social-profile` (comment history + linked accounts), possibly a `name`, and `associate` links from reply interactions.
- **Empty/negative result looks like:** a private/empty profile, a deleted account, or a guest comment with no linked IntenseDebate identity — meaning nothing to pivot from here.

## Gotchas & OpSec
- Human-in-the-loop: none for viewing public profiles.
- OpSec: **passive** read-only browsing; the subject isn't alerted. Never reply/log in from an attributable account.
- Declining platform: IntenseDebate is legacy and lightly used now, so coverage is thin and skews to older blogs — absence means little.
- Linked identities are self-asserted; a claimed name/site on a profile is a lead, not proof.

## Overlaps ("do both")
- Pairs with `[[disqus]]` / `[[disqus-comment-history]]` — Disqus is the dominant comment platform with the same profile→history pivot; check both, since a subject may comment via one on some sites and the other elsewhere.

## Trust & verifiability
`trust: unverified` — a legitimate Automattic service, and the comments are the user's own public output, but any self-linked name/account is unverified. Confirm identity links independently before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intensedebate |
| category | documents-metadata |
| selectorsIn → selectorsOut | username → social-profile, name, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
