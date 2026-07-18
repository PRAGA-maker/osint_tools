---
id: sully-gnome
name: SullyGnome
description: Use when you have a Twitch `username`/channel and want its activity history — returns games streamed, schedule, growth, watch-time, and peak/average viewership over time.
url: https://sullygnome.com/
category: social-networks
path:
- social-networks
bestFor: Profiling a Twitch streamer's public history — what they stream, when, how often, and how their audience has changed.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse channel and game analytics; an optional Patreon supports the project. No account needed.
opsec: passive
opsecNote: Passive — you read aggregated public Twitch data; the streamer isn't notified. The site asks users not to scrape it (hobby project) — browse manually rather than automating.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known independent Twitch-analytics hobby project (not affiliated with Twitch); its numbers are aggregated from public Twitch data and are indicative rather than official.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- search-for-a-twitch-channel
aliases:
- sullygnome.com
tags:
- Social Media
- Twitch
- streamer-analytics
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# SullyGnome

> A Twitch analytics archive — turn a channel name into a behavioral timeline: which games they stream, their typical schedule and hours, and how their audience has grown or shifted.

## When to use
You have a Twitch `username`/channel tied to a subject and want to profile their streaming behavior over time: the games/categories they play (an interest signal), their streaming schedule and time zone (a routine/location clue), how active they are, and audience trends. Useful for building a pattern-of-life around a Twitch identity and for corroborating that an account is active and matches a person's stated interests.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://sullygnome.com/ and search the channel name (or browse by game).
2. Open the channel page for its history: games streamed, stream schedule/times, hours streamed, follower/viewer growth, and peak/average viewership.
3. Read the schedule/time-of-day pattern for routine and rough time-zone clues; read the games list for interests.
4. Browse manually — the operator asks that the site not be scraped.
5. Pivot: the Twitch handle feeds username enumeration across platforms; schedule/time-zone data narrows `geolocation`; game/interest signals corroborate identity.

## Inputs → Outputs
- **In:** a Twitch `username`/channel
- **Out:** the channel's public analytics (`social-profile` behavior) — games, schedule, hours, growth, viewership
- **Empty/negative result looks like:** a tiny, brand-new, or inactive channel may have little tracked history — sparse data means low activity/coverage, not necessarily a fake account.

## Gotchas & OpSec
- **Twitch only:** it profiles streaming behavior, not identity — it won't give a real name or location directly.
- Unofficial and aggregated: figures are estimates from public data and can lag or differ from Twitch's own numbers.
- Respect the no-scraping request; use it as a manual research surface.

## Overlaps ("do both")
- Pairs with `[[search-for-a-twitch-channel]]` and username-enumeration tools — SullyGnome deepens a *known* Twitch handle with behavioral history, while those help find and cross-map the handle elsewhere.

## Trust & verifiability
`trust: community` — a respected but unofficial hobby analytics site; its data is aggregated from public Twitch activity, so treat the figures as solid indicators and confirm anything decisive against Twitch directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sully-gnome |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
