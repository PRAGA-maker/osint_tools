---
id: app-channelcrawler-com
name: app.channelcrawler.com
description: Use when you have a YouTube channel theme, language, country, or keyword and need to enumerate matching channels with creator contact/social handles.
url: https://app.channelcrawler.com/search
category: image-video-face
path:
- image-video-face
bestFor: Discovering YouTube channels by keyword, language, country, and subscriber count, with creator email/social handles attached.
selectorsIn:
- name
- username
- employer-org
selectorsOut:
- social-profile
- email
- username
status: live
pricing: freemium
costNote: 7-day free trial (no card) gives limited search/email credits; sustained use is paid (Starter ~$59-99/mo, Power ~$117-195/mo, Enterprise from $6,000/yr). Account/registration required even for the trial.
opsec: passive
opsecNote: Queries run against ChannelCrawler's own index of public YouTube metadata, not the target's account, so the subject is not notified. Account creation ties searches to your identity unless you use a sock-puppet email.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial creator-marketing/sponsorship-intelligence platform (channelcrawler.com); indexes 25M+ public YouTube channels. Useful for OSINT but built for influencer marketing, not investigations.
missingPersonsRelevance: medium
coverage: [global]
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- Channel Crawler
- ChannelCrawler
tags:
- youtube
- YouTube Related Sites
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# app.channelcrawler.com

> YouTube channel discovery engine: surface channels by keyword/language/country/subscriber band and pull the creator's published contact and social handles.

## When to use
You have a `name`, `username`, or topic/`employer-org` associated with a person who runs (or might run) a YouTube channel, and you want to enumerate candidate channels and pivot to the creator's `email` / `social-profile`. Useful when a missing person was a content creator, or when a known alias might map to a YouTube presence you can cross-reference.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://app.channelcrawler.com/search and create an account (free 7-day trial, no card).
2. Set filters: keyword/niche, language, country, subscriber count, views, creation date.
3. Run the search to get a channel list (`social-profile`), then open a channel to view published `email` and linked social `username`s (gated behind email credits).
4. Pivot: feed discovered handles into a username search such as `[[instant-username]]` or reverse-image the channel avatar.

## Inputs → Outputs
- **In:** `name` / `username` / topic / `employer-org`
- **Out:** `social-profile` (YouTube channels), `email`, `username` (linked socials)
- **Empty/negative result looks like:** no channels match the keyword+geo+language filter combination — broaden filters; a real person may simply not run a public channel.

## Gotchas & OpSec
- Human-in-the-loop: account login required; email/contact reveal consumes credits and is paywalled beyond the trial.
- Built for influencer marketing — coverage skews to channels with meaningful subscriber counts; tiny/private channels may be missing.
- OpSec: passive (no contact with the subject); use a sock-puppet account email so searches aren't tied to you.

## Trust & verifiability
`trust: community` — established commercial platform indexing public YouTube data. Results reflect YouTube's public metadata; always confirm a channel actually belongs to your subject before acting on the contact info.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | app-channelcrawler-com |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username, employer-org → social-profile, email, username |
| pricing / cost | freemium (7-day trial; paid plans) |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (login, paywall) |
