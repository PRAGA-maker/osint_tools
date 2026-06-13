---
id: instatracker
name: instatracker
description: Instagram tracking script that logs changes to an account (followers, following, posts, bio).
url: https://github.com/ibnaleem/instatracker
category: social-networks
path:
- social-networks
bestFor: Monitoring an Instagram account over time for changes
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- associate
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community Instagram change-logger (102 stars) by gosearch author.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- insta-tracker
tags:
- instagram
- monitoring
- change-detection
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# instatracker

> Instagram tracking script that logs changes to an account (followers, following, posts, bio).

- **URL:** https://github.com/ibnaleem/instatracker
- **Best for:** Monitoring an Instagram account over time for changes
- **Source:** harvested from `gh-topic-osint-framework`

Logs follower/following/post/bio changes for a target Instagram account. Useful when monitoring a known social profile during an active case; subject to Instagram rate limits/blocks.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
