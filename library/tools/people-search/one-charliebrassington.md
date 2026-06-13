---
id: one-charliebrassington
name: one (charliebrassington)
description: OSINT tool with multiple scrapers including a cyberbackgroundchecks integration.
url: https://github.com/charliebrassington/one
category: people-search
path:
- people-search
bestFor: US people-search scraping (background-check style data)
selectorsIn:
- name
- phone
- address
- email
selectorsOut:
- address
- phone
- associate
- name
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Small community scraper (34 stars); scrapes third-party people-search sites (ToS-sensitive).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- people-search
- scraper
- cyberbackgroundchecks
- us
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# one (charliebrassington)

> OSINT tool with multiple scrapers including a cyberbackgroundchecks integration.

- **URL:** https://github.com/charliebrassington/one
- **Best for:** US people-search scraping (background-check style data)
- **Source:** harvested from `gh-topic-osint-framework`

Scrapes cyberbackgroundchecks and similar US people-search sites to return addresses, phones, and relatives. High relevance for US missing-persons leads, but scraping these sites may violate ToS and data can be stale; verify.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
