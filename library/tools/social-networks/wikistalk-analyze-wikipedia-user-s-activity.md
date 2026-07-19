---
id: wikistalk-analyze-wikipedia-user-s-activity
name: 'WikiStalk: Analyze Wikipedia User Activity'
description: Use when you have a Wikipedia `username` and want a behavioural profile — returns the pages they edit, activity timing and topic focus as pattern-of-life signal.
url: https://github.com/altilunium/wistalk
category: social-networks
path:
- social-networks
bestFor: Profiling a Wikipedia editor's contributions, active hours and topical interests from their public edit history.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free and open-source (Python script on GitHub); no account or payment. You run it locally.
opsec: passive
opsecNote: It reads Wikipedia's PUBLIC contribution API, so the target editor is not notified and you only touch Wikimedia's public endpoints. Run it from a research machine/IP; the analysis reveals nothing the public contributions page doesn't, it just aggregates it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: A small community Python project (altilunium/wistalk); it aggregates official Wikimedia data, so the underlying facts are authoritative even though the script itself is unverified — sanity-check results against Special:Contributions.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- wistalk
- WikiStalk
tags:
- Social Media
- Wikipedia
- pattern-of-life
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# WikiStalk: Analyze Wikipedia User Activity

> A small open-source Python tool that aggregates a Wikipedia editor's public contributions into a behavioural profile — what they edit, when, and about what.

## When to use
You have a Wikipedia `username` (or you've linked a subject to one) and want more than a raw contributions list: which articles and topics they concentrate on, how their activity is distributed over time (revealing time zone / pattern-of-life), and where their interests cluster. Topic focus can hint at a subject's expertise, location, or affiliations, and activity timing can corroborate a time zone. It's soft behavioural signal built from public data — supporting evidence, never an identifier.

## How to use it (`bestInteractionPattern`: python-lib)
1. Clone the repo: `git clone https://github.com/altilunium/wistalk` and ensure Python 3 is installed.
2. Run the script (`python wistalk.py`) and supply the target Wikipedia username when prompted.
3. Read the output: the pages the user has edited, edit counts, timing, and topic breakdown.
4. Cross-check anything notable against the live `Special:Contributions/<username>` page on Wikipedia.
5. Pivot: distinctive topic focus or edit timing helps match this account to the same handle elsewhere, or corroborate a claimed location/time zone.

## Inputs → Outputs
- **In:** `username` (a Wikipedia editor handle)
- **Out:** edited pages, activity timing, topic focus — a behavioural profile linkable to the same `username`/`social-profile` elsewhere
- **Empty/negative result looks like:** the user has few/no edits, or the handle doesn't exist on the queried Wikipedia — no meaningful profile to build.

## Gotchas & OpSec
- Human-in-the-loop: none, but it's a local script — expect to read/adjust code and confirm it targets the right Wikimedia project (language edition).
- Timing reflects UTC edit timestamps; inferring a time zone from them is a hint, not proof.
- It only aggregates public data; verify standout findings against the live contributions page.

## Overlaps ("do both")
- Pairs with a cross-platform username checker — this profiles the Wikipedia activity behind a handle, that tests whether the same handle exists on other sites.

## Trust & verifiability
`trust: community` — an unverified community script over authoritative Wikimedia data; trust the underlying contributions (checkable on-wiki), treat the script's derived summaries as convenience.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikistalk-analyze-wikipedia-user-s-activity |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
