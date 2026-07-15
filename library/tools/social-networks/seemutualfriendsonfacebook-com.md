---
id: seemutualfriendsonfacebook-com
name: seemutualfriendsonfacebook.com
description: Use when you have two or more Facebook friend lists (scraped) and want to find the people they have in common — returns overlapping social-profiles and names.
url: https://seemutualfriendsonfacebook.com/
category: social-networks
path:
- social-networks
bestFor: Cross-referencing scraped Facebook friend lists to surface mutual connections between two or more accounts.
selectorsIn:
- social-profile
- name
- username
selectorsOut:
- social-profile
- name
- associate
status: live
pricing: free
costNote: Free browser tool; all processing happens client-side, no account or payment.
opsec: passive
opsecNote: The comparison runs in your browser on CSV files you already have; the site never touches Facebook or the target, so it leaks nothing to Meta. The active/risky step is the upstream friend-list scraping you do separately — do that from a sock-puppet Facebook session, not your real account.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Independent third-party utility, not affiliated with or endorsed by Meta; it only does set-intersection on files you supply, so there is no data-quality risk beyond your own inputs.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- tweetbeaver
aliases:
- See Mutual Friends On Facebook
- mutual friends finder
tags:
- facebook
- Facebook General Links
- mutual-friends
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# seemutualfriendsonfacebook.com

> A client-side set-intersection tool: feed it two (or more) Facebook friend lists and it shows exactly who they share.

## When to use
You are triangulating a subject's social circle and already have the friend lists (as CSVs) of two or more Facebook accounts — e.g. a missing person and a suspected associate, or two accounts you think belong to the same person. You want the mutual connections, because a shared friend is a lead: someone who knows both parties and may know where the subject is. Facebook removed the public "see friendship" page, so this fills that gap for lists you can already export.

## How to use it (`bestInteractionPattern`: web-manual)
1. Separately obtain each account's friends list and save each as its own file. The lists must be publicly visible for you to have scraped them.
2. Rename the columns inside each file to exactly `facebookLink`, `image`, `fullName`, and `details`.
3. Open https://seemutualfriendsonfacebook.com/ and upload each friend-list file.
4. Press **Display mutual friends** — the tool shows the intersection (people appearing in every uploaded list).
5. Use the filter bar to narrow by full name, username, or profile details; press **Download mutual friends** to export the overlap as CSV.
6. Pivot: each mutual `social-profile` is a person to approach or investigate as an `associate` who bridges the two subjects.

## Inputs → Outputs
- **In:** two or more Facebook friend lists (each with `facebookLink`, `image`, `fullName`, `details` columns) — i.e. `social-profile` + `name` records.
- **Out:** the set of `social-profile` / `name` entries common to all uploaded lists (mutual `associate` links).
- **Empty/negative result looks like:** an empty results table — either there is genuinely no overlap, or (more often) the accounts have non-public friend lists so your inputs are incomplete. Absence of mutuals is not proof the two people are unconnected.

## Gotchas & OpSec
- Human-in-the-loop: you must manually scrape and reformat the friend lists first; the site does nothing but compare files you provide.
- The hard part is upstream: Facebook hides friend lists set to non-public, so this only works on accounts with public friends. The scraping step is where OpSec matters — use a sock-puppet account and expect Meta to rate-limit or flag aggressive list harvesting.
- The tool is browser-side, so nothing you upload leaves your machine — safe to run against sensitive lists.

## Overlaps ("do both")
- Pairs with `[[tweetbeaver]]` — Tweetbeaver finds common followers/friends between two Twitter/X accounts; this does the same for Facebook. Run both to see whether a shared associate exists on either network.

## Trust & verifiability
`trust: community` — an independent utility with no Meta affiliation. It performs deterministic set intersection on your own data, so results are only as good (and as complete) as the friend lists you feed it; there is no opaque third-party database to distrust.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seemutualfriendsonfacebook-com |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
