---
id: subreddits
name: subreddits
description: Use when you have a topic, interest, or location tied to a subject and want to find the Reddit communities where they might post — returns candidate subreddits to search.
url: https://subreddits.org/
category: social-networks
path:
- social-networks
- reddit
bestFor: Discovering topic- and interest-based subreddits to seed a Reddit username/activity hunt.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public directory; no account or payment required.
opsec: passive
opsecNote: Browsing a third-party static index only. No query touches Reddit or the target, and nothing is logged against the subject. Still, pivot into Reddit itself in a sock-puppet session so your real account is not tied to the search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent, unofficial static directory of subreddits; not affiliated with Reddit and may be stale, but it only points at public communities so the correctness risk is low.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- subreddits.org
tags:
- reddit
- subreddit-discovery
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# subreddits

> A categorized static directory of Reddit communities — use it to figure out *which* subreddits a subject with a given interest or location would plausibly frequent, before you go hunting for their posts.

## When to use
You know something about a subject's interests, hobbies, profession, or home town, and you want to narrow the ~100k+ subreddits down to the handful worth searching for their `username` or writing. This is a discovery/seed step: it does not find people, it finds the *rooms* people are in. Reach for it when a Reddit username search comes up thin and you want to pivot to activity-by-topic instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://subreddits.org/ in a normal browser.
2. Browse the topic categories (science, gaming, music, technology, local/city, etc.) or use the on-site search box to look up a keyword tied to your subject's interest.
3. Collect the candidate subreddit names (e.g. `r/CityName`, `r/HobbyX`).
4. Pivot: take each candidate into Reddit's own search or a Reddit-user tool — search the subreddit for the subject's known `username`, or read recent posters to spot the subject. Feed usernames you find into `[[reddit-com-2]]` / broader username tools.

## Inputs → Outputs
- **In:** a topic/interest/location associated with a `name` (no selector is entered into the tool itself)
- **Out:** a list of candidate subreddits (`social-profile` leads — communities, not people)
- **Empty/negative result looks like:** a category with only a few generic subreddits, or a keyword with no match — means the index is thin on that topic, not that no community exists. Confirm against Reddit's native search before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none; fully self-serve browsing.
- The index is static and unofficial — it can lag new or renamed subreddits and will miss private/quarantined ones. Treat it as a starting map, not an authority.
- OpSec: passive against the target. The real exposure comes at the next step (searching Reddit), so do that from a sock-puppet account.

## Overlaps ("do both")
- Pairs with `[[reddit-com-2]]` — this narrows *which* communities to look in; that searches within Reddit for the actual account/activity.

## Trust & verifiability
`trust: unverified` — a community-run static directory with no official standing; low correctness risk because it only points at public subreddits you then verify directly on Reddit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | subreddits |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
