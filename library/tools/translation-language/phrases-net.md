---
id: phrases-net
name: Phrases.net
description: Use when you have text from a subject and want to decode an unfamiliar idiom, phrase, or expression — returns meaning/usage to interpret `name`/`username`-adjacent language cues.
url: https://www.phrases.com
category: translation-language
path:
- translation-language
bestFor: Looking up the meaning and usage of English idioms, informal expressions, and set phrases found in a subject's messages or posts.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free searchable phrase dictionary (part of the STANDS4 reference network); no account required to look words up.
opsec: passive
opsecNote: A reference-dictionary lookup reveals nothing about your target; you are querying a public language site, not the subject. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community-contributed phrase dictionary in the STANDS4 network; definitions are crowd-edited, so use it to understand language, not as authoritative fact.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- definitions-net
- abbreviations-com
- online-slang-dictionary
- noslang-dictionary
aliases:
- phrases.net
- Phrases.com
- STANDS4 Phrases
tags:
- toddington
- curated-directory
- language-translation-tools
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Phrases.net

> A crowd-built dictionary of idioms and set phrases (the `phrases.net` domain now resolves to `phrases.com` in the STANDS4 network) — a decoder for the figurative language in a subject's words.

## When to use
You are reading a subject's messages, captions, forum posts, or letters and hit an idiom or informal expression whose meaning changes how you interpret intent, mood, or a plan (e.g. slang for travel, money, or leaving). Understanding the phrase can matter when triaging a missing-person's last communications. This is a language-comprehension aid, not an investigative search — it takes phrases in and gives meanings out, not personal selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.phrases.com (the old `phrases.net` address redirects here).
2. Type the idiom or expression into the search box, or browse alphabetically.
3. Read the definition, example sentences, and any regional/usage notes; use the multilingual toggles (French, German, Spanish, Chinese, etc.) if the source text isn't English.
4. Apply the meaning back to the subject's text; if it's slang rather than a standard idiom, cross-check with `[[online-slang-dictionary]]` / `[[noslang-dictionary]]`.

## Inputs → Outputs
- **In:** an idiom / phrase / expression (free text — no personal selector)
- **Out:** its meaning, example usage, and register/tone
- **Empty/negative result looks like:** no entry for the phrase, or only loosely related matches. Coined slang and very new internet expressions often won't be here — fall back to a slang dictionary.

## Gotchas & OpSec
- Entries are community-contributed and can be incomplete or subtly wrong; corroborate any interpretation that would change a decision.
- It covers idioms and set phrases, not one-off internet slang or acronyms — for those use a dedicated slang/abbreviation resource.
- OpSec: passive; a dictionary lookup is invisible to the subject.

## Overlaps ("do both")
- Sits alongside `[[definitions-net]]` and `[[abbreviations-com]]` (same STANDS4 network) for word meanings and acronyms, and `[[online-slang-dictionary]]` / `[[noslang-dictionary]]` for the slang and shorthand this idiom dictionary won't have.

## Trust & verifiability
`trust: unverified` — crowd-edited definitions with no editorial guarantee; treat them as a comprehension aid and confirm anything load-bearing against a second reference.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phrases-net |
| category | translation-language |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
