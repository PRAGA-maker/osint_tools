---
id: tweet-machine
name: Tweet Machine
description: Use when you have a Twitter/X `username` and want to recover their deleted or otherwise-gone tweets and replies from the Wayback Machine — returns archived tweet links, live links, and per-tweet timeline metadata.
url: https://github.com/0xcyberpj/tweet-machine
category: social-networks
path:
- social-networks
bestFor: Pulling a target Twitter/X handle's deleted/removed tweets and replies out of web.archive.org as a link list.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source Bash script; it queries the public Wayback Machine, no account or API key.
opsec: passive
opsecNote: It hits the Internet Archive, not Twitter/X, so the target is never contacted or notified. Run it over Tor/VPN if you want to avoid the Archive logging your IP against the target handle; otherwise passive and low-risk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A single-author open-source Bash script; read the short source before running, but its data comes from the reputable Wayback Machine, so the underlying archive is trustworthy.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- tweetmachine
- 0xcyberpj tweet-machine
tags:
- Social Media
- Twitter
- deleted-tweets
- wayback
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Tweet Machine

> A Bash one-liner over the Wayback Machine that resurrects a handle's deleted tweets and replies — even from suspended accounts — as a list of archived links.

## When to use
You have a Twitter/X `username` and the account is deleted/suspended, or you suspect the person scrubbed tweets you need. Tweet Machine enumerates the handle's archived captures on web.archive.org and hands back links to tweets and replies that no longer resolve on X. Recovering what someone *deleted* is often the highest-value social signal in a missing-persons or vetting case.

## How to use it (`bestInteractionPattern`: cli)
1. Clone it: `git clone https://github.com/0xcyberpj/tweet-machine` and skim the script.
2. Make it executable (`chmod +x tweetmachine.sh`) and run `./tweetmachine.sh -u <username>`.
3. It produces three outputs: direct tweet/reply links, corresponding Wayback (web.archive.org) links, and per-tweet timeline metadata.
4. Open the Wayback links to read the archived content, since the live links may 404.
5. Pivot: recovered tweets expose mentioned handles (`associate`s), places, photos (for reverse-image/EXIF), and timeframes — each a fresh lead.

## Inputs → Outputs
- **In:** a Twitter/X `username`
- **Out:** archived + live tweet/reply links and timeline metadata (a reconstructed `social-profile` slice)
- **Empty/negative result looks like:** few or no archived links — the handle was never snapshotted by the Archive (low-follower or short-lived accounts often aren't), so absence is not proof they never tweeted.

## Gotchas & OpSec
- Coverage is limited to **what the Wayback Machine captured** — high-profile handles are well-archived, obscure ones barely at all.
- Live tweet links will often be dead (that's the point); rely on the archived versions.
- X's markup changes over time can break scraping-style tools; if output looks empty, check the repo for updates or fall back to manual Wayback searching of `twitter.com/<handle>`.
- Inspect the Bash source before running (standard hygiene); it only calls the public Archive.

## Overlaps ("do both")
- Pairs with direct Wayback Machine searches and other X-archive tools — Tweet Machine automates the handle sweep; manual Wayback lets you target specific dates/URLs it missed.

## Trust & verifiability
`trust: unverified` — the tool is community code, but every result links back to a timestamped Wayback capture you can open and verify yourself, which makes findings independently checkable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tweet-machine |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
