---
id: reddit-archive
name: Reddit Archive (redditarchive.com)
description: Use when you have a Reddit `username`, subreddit, or keyword and want historical/deleted posts — but the site is currently offline; returns social-profile activity from archived Reddit datasets when reachable.
url: https://www.redditarchive.com/
category: social-networks
path:
- social-networks
- reddit
bestFor: Historical Reddit post/comment lookup by user, subreddit or keyword (when the service is up).
selectorsIn:
- username
selectorsOut:
- social-profile
status: down
pricing: free
costNote: Was a free web archive of Reddit content; the homepage currently returns HTTP 404 and the service appears offline. No payment involved either way.
opsec: passive
opsecNote: Read-only archive queries never touch the target's live Reddit account, so there is no notification risk. When the site is down, use the alternatives below rather than assuming Reddit history is unrecoverable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party Reddit archive of unclear maintenance; currently unreachable (404). Even historically, dataset coverage and freshness were unverified. Prefer better-maintained archives for anything you must rely on.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: true
relatedTools:
- wayback-machine
- pullpush-io
aliases:
- redditarchive.com
tags:
- reddit
- archived
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Reddit Archive (redditarchive.com)

> A third-party Reddit history lookup — historically useful for deleted/old posts, but currently offline; documented here so you know its state and reach for the working alternatives.

## When to use
You want a Reddit user's historical or deleted posts/comments, or want to reconstruct subreddit activity from before Reddit locked down its API and archives. Reddit itself hides deleted content and, since 2024–2026, has walled off the Internet Archive and API access — so an external archive is often the only route. **As of this check redditarchive.com returns 404**, so treat it as down and use the overlaps below.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try https://www.redditarchive.com/ — if it loads, enter a `username`, subreddit, or keyword and read the archived post/comment references.
2. If it 404s (current state), switch to a working archive:
   - PullPush.io (community successor to Pushshift) for author/subreddit/keyword queries.
   - Wayback Machine (`web.archive.org/web/*/reddit.com/user/<name>/*`) for snapshotted profile pages.
   - `undelete`-style viewers for individual removed threads.
3. Cross-check timestamps and usernames — deleted-then-archived content is the highest-value find.
4. Pivot: a username's post history reveals location tells, other handles, and `associate` interactions.

## Inputs → Outputs
- **In:** `username` (also subreddit / keyword)
- **Out:** `social-profile` (historical Reddit activity: posts, comments, timestamps)
- **Empty/negative result looks like:** the site not loading at all (current 404) — that means the tool is down, NOT that the user has no history; fall through to PullPush/Wayback.

## Gotchas & OpSec
- **Currently down** — do not rely on this domain; it is retained for completeness with pointers to live alternatives.
- Reddit's 2024–2026 lockdown (login walls on old.reddit.com, Internet Archive block, API pricing) has frozen or shrunk many archives — coverage of recent content is thin everywhere.
- OpSec: passive; archive reads never alert the account owner.

## Overlaps ("do both")
- Use PullPush.io as the primary live substitute for user/subreddit history.
- Pair with the Wayback Machine for snapshotted profile pages the JSON archives miss.

## Trust & verifiability
`trust: unverified` — unmaintained and presently unreachable; when it was up, dataset provenance was unclear. Verify any recovered content against a second archive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-archive |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
