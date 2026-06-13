---
id: seeker
name: Seeker
description: Accurately locate smartphones using social engineering (geolocation via crafted phishing page).
url: https://github.com/thewhiteh4t/seeker
category: geolocation
path:
- geolocation
bestFor: Obtaining precise GPS coordinates and device info from a cooperating/target device click.
selectorsIn:
- social-profile
selectorsOut:
- geolocation
- ip-address
- device-id
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular but it is an active social-engineering/phishing tool; use only with authorization.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- thewhiteh4t/seeker
tags:
- geolocation
- phishing
- social-engineering
- gps
source: gh-topic-reconnaissance
lastVerified: ''
enrichment: full
---

# Seeker

> Accurately locate smartphones using social engineering (geolocation via crafted phishing page).

- **URL:** https://github.com/thewhiteh4t/seeker
- **Best for:** Obtaining precise GPS coordinates and device info from a cooperating/target device click.
- **Source:** harvested from `gh-topic-reconnaissance`

Hosts a fake page (e.g. nearby restaurant) that requests location permission; captures GPS, device, OS, IP. Active and intrusive - legally sensitive. For missing persons, only relevant if a subject can be induced to click a link, e.g. with law-enforcement involvement.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
