---
id: xsint
name: xsint
description: All-in-one CLI OSINT aggregator that takes an email, phone, username, IP, or address and fans the query out across 67+ services and modules.
url: https://github.com/h1lw/xsint
category: search-engines
path:
- search-engines
bestFor: Quickly pivoting from a single identifier (email/phone/username/IP/address) to account-presence hits, breach exposure, phone metadata, and geocoded addresses in one command.
selectorsIn:
- email
- phone
- username
- ip-address
- address
selectorsOut:
- email
- phone
- social-profile
- geolocation
- address
- username
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source (GPL v3) Python CLI by GitHub user h1lw; small/new project, verify behavior before relying on results. Some modules require third-party logins/API keys (Google session, GitHub PAT, HIBP, IntelX, Telegram).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- h1lw/xsint
tags:
- aggregator
- account-enumeration
- email-osint
- phone-osint
- username
- breach
- cli
- python
source: xsint
lastVerified: ''
enrichment: full
---

# xsint

> All-in-one CLI OSINT aggregator that takes an email, phone, username, IP, or address and fans the query out across 67+ services and modules.

- **URL:** https://github.com/h1lw/xsint
- **Best for:** Quickly pivoting from a single identifier (email/phone/username/IP/address) to account-presence hits, breach exposure, phone metadata, and geocoded addresses in one command.
- **Source:** harvested from `xsint`

Requires Python 3.10+; install via the repo install.sh (Mac/Linux). Input can be type-prefixed (email:, phone:, user:, addr:, ip:). email_enum checks ~67 services across 18 categories; phone_enum checks Amazon and Snapchat presence; instagram module pulls masked recovery email/phone from IG's recovery flow; phone_basic returns carrier/line-type/timezone; osm module geocodes addresses via OpenStreetMap. Optional modules wrap GHunt (Google), GitFive (GitHub), HaveIBeenPwned, IntelX, and a Telegram breach bot (Haxalot) and require their own auth. Supports Tor/Burp proxying for OPSEC. Many modules

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
