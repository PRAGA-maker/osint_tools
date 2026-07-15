---
id: twitter-chat-schedule
name: Twitter Chat Schedule
description: Use when you have a subject's topic/interest or a hashtag and want to find the recurring Twitter/X chats and moderators around it — returns hashtags, usernames and communities to monitor.
url: http://tweetreports.com/twitter-chat-schedule
category: social-networks
path:
- social-networks
bestFor: Discovering recurring Twitter/X chats (by topic, day and hashtag) and the moderator accounts that run them.
selectorsIn:
- username
- employer-org
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free public directory (TweetReports); no account needed to browse the chat lists.
opsec: passive
opsecNote: Passive — you browse a public directory, not the target's accounts. No subject is contacted. If you then join or watch a live chat on X, do so from a sock-puppet account so your interest isn't attributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: TweetReports is an established, long-running curator of the largest public Twitter-chat directory; the listings are user-submitted recurring chats, so verify a given chat is still active on X.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- TweetReports Twitter Chat Schedule
- Twitter Chats List
tags:
- twitter
- xtwitter
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Twitter Chat Schedule

> TweetReports' directory of recurring Twitter/X chats — a map of hashtag communities and their moderators, organised by topic and day.

## When to use
You know a subject's interest area, profession, or an `employer-org`/hashtag they engage with, and want to find the recurring X chats and communities around it. Regular participants and moderators of a niche chat are a small, identifiable pool — a good place to spot a target's alternate handle, their real-world community, or associates who share their specialty. Use it to turn a broad "they're into X" into specific hashtags, weekly chat times, and moderator accounts to watch.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://tweetreports.com/twitter-chat-schedule (browse by day, or the full Twitter Chats List).
2. Sort/scan by topic or hashtag matching the subject's interest or industry.
3. Read each row: chat hashtag, topic, description, moderator `username`(s), day, time and timezone.
4. On X, search the hashtag and moderator accounts; watch a live session or the archived hashtag stream for the subject or their associates.
5. Pivot: moderator/participant `username`s feed username-search and profile analysis; a niche hashtag narrows a wider search dramatically.

## Inputs → Outputs
- **In:** a topic/interest, hashtag, or `employer-org`/industry linked to the subject
- **Out:** chat hashtags, moderator `username`s, `social-profile` leads, chat times to monitor
- **Empty/negative result looks like:** no chat matches the interest — the niche may be too small or inactive; note that only recurring (monthly+) chats are listed, so one-off events won't appear.

## Gotchas & OpSec
- Twitter/X chats have declined since the platform's API changes; a listed chat may be dormant — confirm recent activity on X before relying on it.
- Listings are user-submitted; treat times/moderators as leads to verify.
- OpSec: **passive** to browse; use a sock-puppet if you then engage on X.

## Overlaps ("do both")
- Pair with X search/username tools — this hands you the hashtags and moderator handles; those tools then expand each handle across platforms and pull post history.

## Trust & verifiability
`trust: community` — a reputable long-running community directory. The structure is reliable; individual entries are community-submitted, so verify a chat is still live on X before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-chat-schedule |
| category | social-networks |
| selectorsIn → selectorsOut | username, employer-org → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
