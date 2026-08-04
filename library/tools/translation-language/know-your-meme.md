---
id: know-your-meme
name: Know Your Meme
description: Use when you have an `image`/meme or a slang term and want its origin, meaning and spread — returns a documented history, aliases and example instances.
url: https://knowyourmeme.com
category: translation-language
path:
- translation-language
bestFor: Identifying and decoding memes, viral images, internet slang and subculture references encountered in a subject's posts.
selectorsIn:
- image
- name
selectorsOut:
- name
status: live
pricing: free
costNote: Free to search and read; ad-supported. No account needed to browse.
opsec: passive
opsecNote: You search a meme/term, not a person — passive. Nothing about your subject is disclosed by looking up a reference.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Editorially-managed meme encyclopedia (Literally Media) with confirmed/submission statuses; entries are community-sourced and editor-vetted but not authoritative for identity attribution.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- knowyourmeme
aliases:
- KYM
- knowyourmeme.com
tags:
- translation
- reference
source: metaosint
lastVerified: '2026-08-04'
enrichment: full
---

# Know Your Meme

> An encyclopedia of internet memes, viral images and slang — a decoder for the cultural references in a subject's online footprint, not a person-lookup.

## When to use
A subject's posts, usernames, or messages contain a meme, viral image, or piece of internet slang you do not recognise, and you need its meaning, origin, and community context to interpret intent or affiliation. Also useful to trace where a specific viral image came from and how it spread.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://knowyourmeme.com and search the term, phrase, or (via the image upload/search) the visual.
2. Read the entry's Origin, Spread, and Meaning sections; note the confirmed vs submission status (confirmed entries are editor-vetted).
3. Collect aliases/variant names and example instances — these give you better search terms for pivoting elsewhere.
4. Pivot: feed the origin/first-appearance details or a source image into reverse-image search to trace earliest uses.

## Inputs → Outputs
- **In:** `image`/meme or a slang `name`/term
- **Out:** documented origin, meaning, aliases (`name`), example instances
- **Empty/negative result looks like:** no entry, or only an unconfirmed submission — the reference may be too new/niche; treat unconfirmed entries as leads, not facts.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; looking up a meme reveals nothing about your subject.
- Entries are community-authored — status flags matter; do not treat an unvetted submission as authoritative.

## Overlaps ("do both")
- Pairs with reverse-image search: KYM explains what a meme *means*, reverse-image search finds *where else* the specific image appears in your subject's footprint.

## Trust & verifiability
`trust: community` — an editorially-managed but community-sourced encyclopedia; good for cultural context, not for attributing identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | know-your-meme |
| category | translation-language |
| selectorsIn → selectorsOut | image, name → name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
