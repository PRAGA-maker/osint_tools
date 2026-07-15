---
id: notetracker-socialmedialab-ca
name: NoteTracker Dashboard
description: Use when you have an X/Twitter `username` or a keyword/topic and want to see which of a subject's posts (or posts about a topic) drew Community Notes — returns `social-profile` context: noted posts, note status, and dispute trends.
url: https://notetracker.socialmedialab.ca/
category: social-networks
path:
- social-networks
bestFor: Searching X's Community Notes (visible and not-yet-visible) by keyword or handle to surface disputed or fact-checked posts.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public research dashboard; no account required.
opsec: passive
opsecNote: You query a third-party academic database of Community Notes, not X or the subject directly — the subject is not notified and nothing is sent to their account. Ordinary web-logging by the host only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built and maintained by the Social Media Lab at Toronto Metropolitan University (Ontario Tech collaboration); an academic, transparency-focused project rather than a commercial scraper.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- NoteTracker
- Community Notes dashboard
tags:
- xtwitter
- X / Twitter Related Sites
- community-notes
- fact-checking
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# NoteTracker Dashboard

> A searchable public database of X (Twitter) Community Notes — including proposed notes that never became publicly visible — for journalists and researchers.

## When to use
You are profiling an X account or a claim and want to know whether the subject's posts (or posts about a topic they touch) attracted Community Notes. Because only ~10% of proposed notes ever become visible on X itself, NoteTracker's window into the *not-yet-visible* notes surfaces disputes, corrections, and credibility signals you cannot see on X directly — useful for gauging whether an account spreads contested claims or has been repeatedly fact-checked.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://notetracker.socialmedialab.ca/.
2. Enter a keyword, topic, or the subject's handle in the search box.
3. Filter by note status — "Helpful", "Not Helpful", "No Consensus", "Insufficient Ratings" — to focus on which posts drew consensus corrections vs. contested ones.
4. Read the matched posts, their attached notes, and the aggregate statistics (trend over time, share of visible vs. proposed notes).
5. Pivot: a noted post links back to the live X `social-profile`; repeated "Helpful" notes on an account are a credibility flag worth carrying into the rest of the profile.

## Inputs → Outputs
- **In:** `username` (X handle) or keyword/topic
- **Out:** `social-profile` context — the subject's noted posts, each note's text and status, and dispute/correction trends
- **Empty/negative result looks like:** no matching notes for the handle or keyword — meaning none of the indexed posts drew a Community Note, not that the account is clean of all disputes.

## Gotchas & OpSec
- Scope is limited to X's Community Notes program; it says nothing about accounts on other platforms or posts that were never note-eligible.
- Note *status* reflects crowd rating, not ground truth — an "Insufficient Ratings" note may still be accurate.
- OpSec: passive; querying the dashboard is invisible to X and to the subject.

## Overlaps ("do both")
- Pairs with general X-profile and archive tools — those show what the subject posted, while NoteTracker shows which of those posts the crowd flagged and why.

## Trust & verifiability
`trust: community` — an academic transparency project (TMU Social Media Lab) with a stated methodology; the underlying data is X's own Community Notes corpus, so it is verifiable but reflects crowd ratings rather than authoritative fact-checks.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | notetracker-socialmedialab-ca |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
