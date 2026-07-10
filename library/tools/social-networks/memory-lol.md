---
id: memory-lol
name: memory.lol
description: Use when you have a Twitter/X `username` and want that account's past handles/screen-name history — returns prior usernames and the dates they were observed.
url: https://memory.lol/app/
category: social-networks
path:
- social-networks
bestFor: Resolving old Twitter handles and mapping an account's screen-name change history so a renamed/abandoned account can still be traced.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free. Public access returns handle history observed in the last ~60 days of data; the full 12-year, ~half-billion-name dataset is reserved for a vetted group (researchers/journalists/activists) who authenticate via GitHub/Google.
opsec: passive
opsecNote: You query an archive derived from the Internet Archive's Twitter Stream Grab and Wayback Machine, not the live account, so the subject is not notified. No login needed for basic use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known handle-history service by Travis Brown, built from Internet Archive data. Authoritative for observed name changes, but coverage depends on what the archive captured.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- twitter-advanced-search
aliases:
- memory.lol
- Twitter handle history
tags:
- twitter
- handle-history
source: gh-topic-osint-resources
lastVerified: '2026-07-10'
enrichment: full
---

# memory.lol

> A handle-history archive for Twitter/X: give it a username or account ID and get the screen names that account used before — so a rename doesn't break your trail.

## When to use
You have a Twitter/X `username` (current or old) and the account has been renamed, abandoned, or you suspect it used to go by something else. memory.lol maps an account's numeric ID to every screen name it has been observed under, letting you (a) recover an old handle a source referenced, (b) prove two handles are the same underlying account, or (c) follow a subject who renamed to evade searches. Built from Internet Archive data, so it reaches back years.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://memory.lol/app/ and enter the `username` — or query the API directly at `https://memory.lol/tw/<username>` for JSON.
2. Read the history: prior screen names with the date ranges each was observed.
3. Public (unauthenticated) access is limited to recent (~60-day) observations; for the full 12-year history, sign in with GitHub/Google if you qualify for the trusted-researcher tier.
4. Cross-check that a claimed old handle maps to the same account ID as the current one — same ID = same account.
5. Pivot: old handles feed `[[twitter-advanced-search]]`, web search, and archived-tweet lookups to find content posted under the previous name.

## Inputs → Outputs
- **In:** `username` (Twitter/X handle or account ID)
- **Out:** prior `username`s (screen-name history with dates), tied to the same account `social-profile`
- **Empty/negative result looks like:** no history / only the current name. The account may have never renamed, be too new, or simply not be in the archive's captures — absence is not proof it never changed.

## Gotchas & OpSec
- Public tier is capped to recent observations; deep history needs the vetted-researcher login.
- Coverage is bounded by what the Internet Archive captured — obscure or short-lived accounts may be missing.
- It maps *handles to an account*, which is exactly why it's powerful: it defeats rename-based evasion.
- OpSec: passive; queries an archive, not the live account.

## Overlaps ("do both")
- Pairs with `[[twitter-advanced-search]]` — recover an old handle here, then use advanced search / archived-tweet tools to pull the content that handle posted before the rename.

## Trust & verifiability
`trust: community` — a well-regarded tool by Travis Brown sourced from Internet Archive data. Observed name changes are reliable (tied to a stable account ID); just remember coverage is limited to what the archive saw, and confirm same-account identity via the numeric ID.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | memory-lol |
</content>
