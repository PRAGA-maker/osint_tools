---
id: knowyourmeme
name: Know Your Meme
description: Use when you have a meme `image`, phrase, or symbol and want its origin and meaning — returns the documented history, spread, and cultural context of the meme.
url: http://knowyourmeme.com
category: documents-metadata
path:
- documents-metadata
bestFor: Identifying the origin, meaning, and context of a meme, image macro, phrase, or online symbol.
selectorsIn:
- image
status: live
pricing: free
costNote: Free to read (ad-supported); an account is only needed to submit/edit entries.
opsec: passive
opsecNote: Public reference site — you look up cultural context, not a person. Passive; the usual note about browsing from a non-attributable session applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established meme encyclopedia (since 2007, Literally Media); entries are community-written but editorially reviewed — good for context, cite the primary source it points to.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- KYM
- Knowyourmeme
tags:
- documents-metadata
- memes
- culture
- context
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- know-your-meme
---

# Know Your Meme

> An encyclopedia of internet memes — decode the origin, meaning, and spread of an image, phrase, or symbol you've encountered in an investigation.

## When to use
You've come across a meme, image macro, catchphrase, emoji/symbol, or in-group reference (in a subject's posts, a forum, an extremist channel) and need to understand what it means, where it came from, and what community uses it. Especially useful for reading the cultural signals in a subject's online activity — dog-whistles, subculture markers, and coded symbols are often documented here.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://knowyourmeme.com and search the phrase, image name, or symbol (browse by Cultures/People/Subcultures).
2. Open the entry: origin, first appearance, spread, meaning, and notable examples/variations.
3. Read the "About"/"Origin"/"Spread" sections and follow the cited sources.
4. Pivot: the identified meme/subculture points you to the communities and platforms where it lives, narrowing where else to look for the subject.

## Inputs → Outputs
- **In:** a meme `image`, phrase, or symbol
- **Out:** its documented origin, meaning, and cultural/community context
- **Empty/negative result looks like:** no entry — the meme is too new, too niche, or region-specific; try image reverse-search or the source community directly.

## Gotchas & OpSec
- Coverage skews to English-language/Western internet culture and established memes; new or niche ones may be missing.
- Entries are community-written — good for orientation, but cite the primary source it references, not KYM itself, for claims.
- It explains culture, not identity — it won't tell you who made or posted something.

## Overlaps ("do both")
- Pairs with reverse-image search — reverse-image finds where an image appears; Know Your Meme explains what it *means* and which community it signals.

## Trust & verifiability
`trust: community` — a well-established, editorially-reviewed meme encyclopedia; reliable for context, but trace claims to the primary sources it cites.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | knowyourmeme |
| category | documents-metadata |
| selectorsIn → selectorsOut | image →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
