---
id: f5bot
name: F5Bot
description: Use when you have a `name`, `username` or keyword and want to be emailed whenever it's mentioned on Reddit/Hacker News/Lobsters — returns matching posts and posters' `social-profile`s.
url: https://f5bot.com/
category: social-networks
path:
- social-networks
bestFor: Standing keyword monitoring — get emailed the moment a subject's name, handle, phone, or unique phrase appears on Reddit, Hacker News or Lobsters.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Completely free. You register an email address and keyword list; alerts arrive by email, usually within minutes of a mention.
opsec: passive
opsecNote: Monitoring is server-side against public posts; the people posting are never told they're being watched. Use a dedicated (non-attributable) email for the alerts so the monitoring can't be tied back to your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known free monitoring service in the OSINT/marketing community; it only surfaces public posts and depends on the platforms' public feeds.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- f5bot.com
- F5 Bot
tags:
- bellingcat-toolkit
- other-platforms
- monitoring
source: bellingcat-toolkit
lastVerified: '2026-07-19'
enrichment: full
---

# F5Bot

> A free alerting service that emails you whenever your chosen keywords appear on Reddit, Hacker News, or Lobsters — set-and-forget monitoring for a name, handle, or unique phrase.

## When to use
You have a persistent selector — a subject's real `name`, a distinctive `username`, a phone number, an email, or a unique phrase they use — and you want ongoing coverage rather than a one-off search. F5Bot turns that selector into an email alert the next time it's posted on Reddit/HN/Lobsters, catching mentions you'd otherwise miss between manual checks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://f5bot.com/ and sign up with a **dedicated** email address.
2. Add your keywords (exact-match works best — quote distinctive phrases; use the handle, full name, phone, or email).
3. Choose which sources to watch (Reddit, Hacker News, Lobsters).
4. Wait: when a match posts, F5Bot emails you the post text and a link.
5. Pivot: open the linked post, note the poster's `username`/`social-profile`, read their history, and run the handle through username-search and Reddit-specific OSINT tools.

## Inputs → Outputs
- **In:** any keyword — `name`, `username`, phone, email, or phrase
- **Out:** email alerts linking to matching posts and the posters' `social-profile`s
- **Empty/negative result looks like:** no emails — either the term simply isn't being posted, or your keyword is too broad/misspelled. Silence is not proof of absence; also run a direct search of past posts, since F5Bot only catches mentions from when you added the keyword forward.

## Gotchas & OpSec
- It's **forward-looking only** — it won't find historical mentions from before you subscribed; pair it with a direct archive/search for the back-catalogue.
- Very common keywords flood your inbox; prefer distinctive phrases/handles.
- OpSec: passive and non-alerting, but the alert email is a record — use a burner address.

## Overlaps ("do both")
- Pairs with direct Reddit search tools and username-search — F5Bot watches the future, those cover the past and spread a found handle across platforms.

## Trust & verifiability
`trust: community` — a widely-used free service surfacing only public posts. It's a lead generator: always open and read the actual post rather than acting on the alert snippet alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | f5bot |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
