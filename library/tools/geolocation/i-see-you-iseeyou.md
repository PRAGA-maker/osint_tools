---
id: i-see-you-iseeyou
name: I-See-You (ISeeYou)
description: Bash/JS tool to find a user's exact location during social-engineering or phishing.
url: https://github.com/Viralmaniar/I-See-You
category: geolocation
path:
- geolocation
bestFor: Pinpointing a target's location via a crafted link in an authorized engagement.
selectorsIn:
- social-profile
selectorsOut:
- geolocation
- ip-address
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Active phishing-style geolocation tool; legally sensitive.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Viralmaniar/I-See-You
- ISeeYou
tags:
- geolocation
- phishing
- social-engineering
source: gh-topic-reconnaissance
lastVerified: ''
enrichment: full
---

# I-See-You (ISeeYou)

> Bash/JS tool to find a user's exact location during social-engineering or phishing.

- **URL:** https://github.com/Viralmaniar/I-See-You
- **Best for:** Pinpointing a target's location via a crafted link in an authorized engagement.
- **Source:** harvested from `gh-topic-reconnaissance`

Uses HTML5 Geolocation API behind a public link via Serveo/ngrok. Same caveats as Seeker - active, intrusive, requires authorization.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
