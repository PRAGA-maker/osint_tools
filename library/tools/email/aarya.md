---
id: aarya
name: aarya
description: Email-to-digital-footprint tool that validates an email across platforms and extracts metadata (e.g. Google Maps contributions/reviews).
url: https://github.com/forshaur/aarya
category: email
path:
- email
bestFor: Mapping which online platforms an email is registered on and pulling Google Maps reviews/contributions tied to it
selectorsIn:
- email
selectorsOut:
- social-profile
- name
- geolocation
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: ~33 stars; community tool, validate platform checks.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- email-osint
- account-enumeration
- google-maps
source: gh-topic-footprinting
lastVerified: ''
enrichment: full
---

# aarya

> Email-to-digital-footprint tool that validates an email across platforms and extracts metadata (e.g. Google Maps contributions/reviews).

- **URL:** https://github.com/forshaur/aarya
- **Best for:** Mapping which online platforms an email is registered on and pulling Google Maps reviews/contributions tied to it
- **Source:** harvested from `gh-topic-footprinting`

Checks Instagram, Wattpad, Duolingo and others for the email; Google Maps contributions can reveal places a subject has visited/reviewed. Touches target platforms (active).

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
