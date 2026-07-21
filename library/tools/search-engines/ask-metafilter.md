---
id: ask-metafilter
name: Ask MetaFilter
description: Use when you have a `username`, `name`, or niche question and want a long-lived Q&A community's answers — returns posts, member profiles, and associate leads from AskMe threads.
url: http://ask.metafilter.com
category: search-engines
path:
- search-engines
bestFor: Searching a veteran Q&A community for a member's footprint or crowd-sourced answers to niche questions.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to read and search; posting requires a one-time paid membership, but reading is open.
opsec: passive
opsecNote: Reading and searching public threads is passive. Any question you post is public and tied to your account, so read-only for OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established, moderated Q&A community; content is user-generated opinion/experience, credible as community discussion but not authoritative record.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- metafilter
aliases:
- Ask MetaFilter
- AskMe
- ask.metafilter.com
tags:
- toddington
- curated-directory
- specialty-search
- qa-community
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Ask MetaFilter

> The question-and-answer arm of MetaFilter, a long-running moderated community — a place to find a member's posting history or unusually thoughtful crowd answers to niche problems.

## When to use
Two uses. First, footprint: if a subject uses a MetaFilter `username`, their AskMe questions and answers can reveal interests, location clues, life events, and connections in their own words. Second, tradecraft: for an obscure identification or "what is this" question, AskMe's veteran community often has detailed, sourced answers. Content is discussion, not record — treat it as leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://ask.metafilter.com and use its search, or a `site:ask.metafilter.com "term"` Google search.
2. Search the `username` or `name`, or the topic/object you're trying to identify.
3. Read threads and member profile pages for details the subject disclosed and who they interact with.
4. Note recurring co-posters and linked profiles as possible `associate`s.
5. Pivot: a confirmed handle feeds cross-platform username search; disclosed details feed people-search.

## Inputs → Outputs
- **In:** `username`, `name`, or a topic/identification question
- **Out:** posts/answers, member `social-profile`/`username` pages, and `associate` leads
- **Empty/negative result looks like:** no threads — expected for most people, since only members post; absence says nothing about a person's wider presence.

## Gotchas & OpSec
- Reading is free but posting needs paid membership; stay read-only for OSINT.
- User-generated opinions — self-disclosed details are leads to verify, not facts.
- OpSec: passive; never post your investigation as a question.

## Overlaps ("do both")
- Pairs with `[[metafilter]]` (the main site) and general forum/username search — AskMe covers the Q&A subsite; the broader MetaFilter and cross-platform tools widen the footprint.

## Trust & verifiability
`trust: community` — a credible, well-moderated community, but its content is discussion and personal experience, to be corroborated independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ask-metafilter |
| category | search-engines |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
