---
id: scrt-link
name: scrt.link
description: Use when you (the investigator) need to share a secret — a `password`, credential, or sensitive note — via an end-to-end-encrypted, one-time, self-destructing link. An operational OpSec utility, not a subject lookup.
url: https://scrt.link/
category: communities-forums
path:
- communities-forums
bestFor: Sending passwords/credentials/sensitive notes to a teammate through a link that is destroyed after a single view.
selectorsIn:
- password
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier covers basic one-time secrets; paid upgrade extends limits and adds features (e.g. larger files, retention options).
opsec: passive
opsecNote: This is a tool you use, not one you point at a target. The encryption key lives in the URL fragment and is never sent to the server, so scrt.link cannot read your secret. Deliver the link over a separate channel from any password it protects, and remember the secret self-destructs on first open — a "already viewed" error can mean interception.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source, privacy-focused one-time-secret service; client-side encryption is verifiable, but as with any hosted service you extend some trust to the operator's uptime and integrity.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- scrt.link
- Scrt one-time secret
tags:
- pastebins
- opsec
- one-time-secret
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# scrt.link

> An end-to-end-encrypted, self-destructing one-time-secret sharing service — an OpSec tool for the investigator's own workflow, not a source of subject data.

## When to use
You need to hand a `password`, an account credential, an access token, or a sensitive note to a colleague and don't want it sitting in email, chat history, or a ticketing system. scrt.link generates a link that decrypts the secret exactly once and then destroys it. This is a tradecraft/OpSec utility — it produces nothing about a subject; it protects the sensitive artifacts you generate during an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://scrt.link and write your secret in the box.
2. Generate the encrypted link. The decryption key is embedded in the URL's fragment and never reaches the server.
3. Send the link to the recipient over a channel separate from whatever the secret unlocks (e.g. link by chat, but tell them the associated username by voice).
4. The recipient opens it once; the secret is then destroyed. If they get an "already viewed / not found" error and they were the first to open it, treat the secret as potentially intercepted and rotate it.

## Inputs → Outputs
- **In:** `password` / credential / sensitive text you want to transmit securely
- **Out:** none — there is no subject data returned; the output is a one-time link
- **Empty/negative result looks like:** a link that reports the secret is gone/already viewed — either it was already opened (by the intended recipient or someone else) or it expired.

## Gotchas & OpSec
- One-time by design: the first open destroys it. Coordinate so the right person opens it first.
- Not a searchable paste site — despite the "pastebins" tag, you cannot browse or recover others' secrets; it only sends, encrypted, once.
- OpSec: passive and self-directed. Never put a secret and the thing it unlocks (e.g. a login and its password) in the same message or channel.

## Overlaps ("do both")
- Serves the same operational role as PrivateBin/One-Time-Secret style tools — pick whichever your team trusts operationally; the value is client-side encryption plus single-view destruction.

## Trust & verifiability
`trust: community` — open-source and privacy-designed with client-side encryption you can inspect, but it is a hosted third-party service, so uptime and operator integrity are trust assumptions. For maximum control, self-host an equivalent.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scrt-link |
| category | communities-forums |
| selectorsIn → selectorsOut | password → — |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
