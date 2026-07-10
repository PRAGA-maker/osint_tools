---
id: what-mail
name: What Mail?
description: Use when you have a raw `email` header / .eml and want to parse and visualize it to trace the message's origin and path — returns sending `ip-address`, relay `domain`s, and `metadata-exif`-style header fields.
url: https://github.com/z0m31en7/WhatMail
category: email
path:
- email
bestFor: Parsing email headers into a readable table to expose originating IP, mail servers, and authentication/routing details.
selectorsIn:
- email
selectorsOut:
- ip-address
- domain
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (Python CLI); no account. Runs locally on header text you already have.
opsec: passive
opsecNote: Analysis is entirely local on a header you already possess — nothing is sent to the sender or any third party, so it's fully passive and leaves no trace. Handle the email content securely (it may contain sensitive data).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A simple community Python header parser; it presents header fields, so accuracy of any conclusion depends on the (spoofable) headers themselves.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- WhatMail
- What Mail
tags:
- Emails
- email-headers
- header-analysis
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# What Mail?

> A small Python tool that parses email headers into a clean table — read the originating IP, the relay chain, and authentication results to trace where a message really came from.

## When to use
You have an email (its raw headers or a `.eml`) tied to a subject and want to trace its origin: the sending `ip-address`, the mail servers/`domain`s it passed through, timestamps, and SPF/DKIM/DMARC results. Essential for attributing a message, geolocating a sender's server, or spotting spoofing.

## How to use it (`bestInteractionPattern`: cli)
1. Obtain the full email headers (in most clients: "Show original"/"View source") or the `.eml` file.
2. Clone https://github.com/z0m31en7/WhatMail and install its Python requirements.
3. Run it against the header input; it parses and visualizes the fields in a table.
4. Read out the `Received:` chain (bottom-up = origin), the originating `ip-address`, relay `domain`s, and auth results.
5. Pivot: originating IP → IP-geolocation / `[[numverify-api]]`-style enrichment and reverse DNS; sender domain → WHOIS; auth failures → likely spoofing.

## Inputs → Outputs
- **In:** raw email headers / `.eml` (`email`)
- **Out:** originating `ip-address`, relay `domain`s/servers, timestamps, SPF/DKIM/DMARC results (`metadata-exif`-style header fields)
- **Empty/negative result looks like:** minimal/obscured headers — webmail (Gmail/Outlook) often strips or masks the true origin IP, so you may only see the provider's servers. Sparse headers ≠ tool failure; it means the origin was hidden by the provider.

## Gotchas & OpSec
- **Headers can be spoofed** — `From:` and even some `Received:` lines can be forged; trust the chain critically and corroborate.
- Major webmail hides the client's originating IP; expect to see only the provider's infrastructure.
- Fully local/passive — but the email may hold sensitive data; store it securely.

## Overlaps ("do both")
- Pairs with online header analyzers (MXToolbox, Google Message Header) and IP-geolocation/WHOIS — WhatMail gives a quick local parse; the others cross-check the chain and enrich the origin IP/domain.

## Trust & verifiability
`trust: community` — a straightforward parser; it faithfully shows the headers, but the headers themselves are the (spoofable) evidence — verify the origin IP/domain independently before drawing conclusions.
