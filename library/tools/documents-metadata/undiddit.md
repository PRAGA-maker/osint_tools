---
id: undiddit
name: Undiddit
description: Use when you have a Reddit thread/comment URL or username and want to recover content deleted or moderator-removed from Reddit — returns recovered post/comment text and the author username.
url: https://www.unddit.com
category: documents-metadata
path:
- documents-metadata
bestFor: Recovering deleted/removed Reddit posts and comments and surfacing the author behind them.
selectorsIn:
- username
- social-profile
selectorsOut:
- username
- metadata-exif
status: degraded
pricing: free
costNote: Free; depends on an upstream archive (Pushshift) whose public access was curtailed in 2023.
opsec: passive
opsecNote: You query a third-party mirror, not Reddit directly; no login and no contact with the subject. The mirror operator sees your queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run successor to removeddit; relies on Pushshift archives that are no longer reliably updated, so newer or recently deleted content often will not resolve.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- unddit
- removeddit
tags:
- toddington
- curated-directory
- social-media
- reddit
source: toddington-resources
lastVerified: ''
enrichment: full
---

# Undiddit

> A Reddit "deleted content" viewer that resurfaces posts and comments removed by moderators or deleted by users, including the author's username.

## When to use
You have a Reddit thread URL, a permalink to a now-`[deleted]`/`[removed]` comment, or a `username` (`social-profile`) tied to a missing person or an associate, and you want to read what was actually said before it was scrubbed — or confirm who authored a now-deleted comment. Useful when a subject's account or a tip thread was partially deleted.

## How to use it (`bestInteractionPattern`: web-manual)
1. Take a Reddit URL and replace the `reddit.com` host with `unddit.com` (e.g. `https://www.unddit.com/r/.../comments/...`), or paste the full Reddit link into the unddit.com homepage.
2. Removed-by-moderator content renders highlighted in red; user-deleted content in blue; intact content normally.
3. Read recovered text and note the `username` shown next to deleted comments — Reddit hides the author on deletion, but the archive often retains it.
4. Pivot: feed a recovered `username` into username-search / social-profile tools, or into the subject's other accounts.

## Inputs → Outputs
- **In:** `username` / `social-profile` (Reddit permalink or thread URL)
- **Out:** recovered post/comment text, author `username`, post timestamps (`metadata-exif`-style metadata)
- **Empty/negative result looks like:** the page loads but the comment still shows `[removed]`/`[deleted]` with no recovered text — meaning the archive never captured it (common for recent or fast-deleted content).

## Gotchas & OpSec
- Largely **degraded**: the underlying Pushshift archive lost public/bulk access in 2023, so recovery of content from mid-2023 onward is unreliable or fails outright. Treat a blank result as "not archived," not "never existed."
- OpSec: passive — you never touch the subject's account and there is no login. The mirror operator can log your queries; use a clean browser/sock-puppet context for sensitive cases.

## Overlaps ("do both")
- Pair with general Reddit user-history and username-pivot tools: unddit recovers the *deleted text*, while live tools give the *current* account footprint.

## Trust & verifiability
`trust: community` — community-maintained successor to removeddit/unddit; accuracy is bounded by what Pushshift archived and by archive staleness. Verify any recovered claim against a second source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | undiddit |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, social-profile → username, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
