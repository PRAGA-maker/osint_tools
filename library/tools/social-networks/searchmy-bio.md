---
id: searchmy-bio
name: Searchmy.bio
description: Use when you have a `name`, keyword, link or interest and want Instagram accounts whose bio contains it — returns matching Instagram profiles.
url: https://www.searchmy.bio/
category: social-networks
path:
- social-networks
bestFor: Keyword-searching Instagram bios (which Instagram's own search can't do) to find accounts by what people write about themselves.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to search; some advanced filtering/volume may be gated.
opsec: passive
opsecNote: You search a third-party index of Instagram bios, not Instagram directly, so no account is touched and no target is notified. Passive; just don't log into Instagram in the same session for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A useful niche index of Instagram bios; coverage is partial (not every account/bio is indexed) and can lag, so a miss doesn't rule an account out.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- instaloader-3
- osintgram
aliases:
- searchmy.bio
- search my bio
tags:
- instagram
- bio-search
- social-media
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Searchmy.bio

> A search engine over Instagram **bios** — find accounts by keywords, names, links or interests written in the bio, something Instagram's native search (username/display-name only) can't do.

## When to use
You have a `name`, a keyword (employer, hobby, hometown, a linked website/handle), or a phrase you expect in someone's Instagram bio, and want to find the matching accounts. It's powerful for finding a person when you don't know their handle but know something they'd state about themselves, or for finding members of a group/community who describe themselves similarly. Results can be sorted by relevance or follower count and filtered by follower range.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.searchmy.bio/ and enter the keyword(s), `name`, or a link you expect in a bio.
2. Sort by "most relevant" or "most followers"; set min/max follower filters to cut noise; optionally include hashtags.
3. Review the matching profiles and open promising ones on Instagram to confirm.
4. Combine multiple bio terms (e.g. a first name + city + profession) to narrow.
5. Pivot: a confirmed Instagram handle feeds `[[instaloader-3]]`/`[[osintgram]]` for full profile extraction, and username enumeration to find the person elsewhere.

## Inputs → Outputs
- **In:** `name`/keyword/link (bio text), or a `username` guess
- **Out:** matching Instagram `social-profile`s
- **Empty/negative result looks like:** no matches — the person may not state that term, or their account/bio isn't indexed; coverage is partial, so absence isn't conclusive (fall back to Google `site:instagram.com`).

## Gotchas & OpSec
- Index is **partial and can lag** — not every Instagram bio is covered; a miss isn't proof.
- Only searches bios, not captions/posts; pair with caption/hashtag tools for those.
- OpSec: passive; searches hit the third-party index, not Instagram.

## Overlaps ("do both")
- Feeds `[[instaloader-3]]` and `[[osintgram]]` (enrich a found handle) and complements a Google `site:instagram.com "<keyword>"` search, which covers accounts searchmy.bio hasn't indexed. Do both.

## Trust & verifiability
`trust: community` — a handy niche index, reliable for what it has indexed but incomplete; confirm each hit on the live Instagram profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchmy-bio |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
