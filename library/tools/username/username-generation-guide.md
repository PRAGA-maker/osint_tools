---
id: username-generation-guide
name: username-generation-guide
description: Use when you have a `name` or a known `username` and want a systematic method to expand it into candidate handles before running enumerators — returns a wider set of username variants to search.
url: https://github.com/soxoj/username-generation-guide
category: username
path:
- username
bestFor: Expanding a known nickname or real name into candidate usernames to feed into namecheckers.
selectorsIn:
- username
- name
selectorsOut:
- username
status: live
pricing: free
costNote: Free, open GitHub repository (guide plus helper Python scripts); no account or payment.
opsec: passive
opsecNote: Reading the guide and generating variants happens entirely offline/local — nothing touches the target or any third party until you take the resulting handles to a lookup tool. The generation step is fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authored by soxoj, creator of Maigret and a well-known OSINT-username researcher; the methodology is widely referenced in the community.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- soxoj username generation guide
- username permutation guide
tags:
- username
- guide
- permutation
- methodology
source: gh-topic-osint-resources
lastVerified: '2026-07-14'
enrichment: full
---

# username-generation-guide

> soxoj's definitive methodology (with helper scripts) for turning a name or a single handle into a broad set of candidate usernames before you run enumerators.

## When to use
This is a **methodology/reference**, not a lookup service. Reach for it before username enumeration: you have a real `name`, a nickname, or one known `username`, and namecheckers came back thin. The guide shows how to widen the search space so the *next* tool has more handles to test — the single biggest lever on username-OSINT recall.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo at https://github.com/soxoj/username-generation-guide and read the three-part method:
   - **Combine basic info** — permute first/last/middle names, add birth years and separators (as an Email Permutator / NAMINT does).
   - **Mine primary info** — derive name variants via transliteration and diminutives (BehindTheName, BabelStrike) for non-English or nickname cases.
   - **Transform the handle** — apply rule-based edits: leetspeak, look-alike character swaps (l→I), trailing numbers, etc.
2. Optionally run the included Python helpers — `generate_by_real_info.py`, `transform_username.py`, `behind_the_names.py` — to produce the variant list programmatically.
3. Take the resulting candidate `username` list into an enumerator/namechecker.
4. Pivot: feed the variants to `[[user-sherlock]]`, `[[social-profiles-finder]]`, and platform-specific checks; a hit on any variant reopens the whole identity graph.

## Inputs → Outputs
- **In:** `name`, nickname, or a known `username`
- **Out:** an expanded set of candidate `username` variants to search elsewhere
- **Empty/negative result looks like:** not applicable — it always produces variants; the risk is a *too-broad* list, so prioritize the most plausible constructions to avoid drowning the enumerator in noise.

## Gotchas & OpSec
- It generates candidates only — it confirms nothing. Every variant still needs testing against real platforms.
- Guard against combinatorial blow-up: unconstrained permutation yields thousands of low-probability handles; keep the birth-year/known-token constraints tight.

## Overlaps ("do both")
- Upstream of every namechecker: run this first, then `[[user-sherlock]]` and `[[social-profiles-finder]]` — generation and enumeration are two halves of one workflow, and skipping generation is why searches miss accounts.

## Trust & verifiability
`trust: trusted` — authored by soxoj (Maigret author), an established OSINT-username researcher; the method is transparent and community-vetted, and you verify its output by testing the handles it produces.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | username-generation-guide |
| category | username |
| selectorsIn → selectorsOut | username, name → username |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
