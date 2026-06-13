---
id: anonymailer-net
name: anonymailer.net
description: Use when an investigation needs to send an anonymous/spoofed email from a sock-puppet identity (pretext/outreach), not when you need to look up data about an email.
url: http://www.anonymailer.net/send-free-email4.asp
category: email
path:
- email
bestFor: Sending an anonymous or sender-spoofed email from a research persona.
selectorsIn:
- email
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier sends with an advertising footer and a warning that your IP is logged; paid membership removes footers and offers SMTP servers that may pass SPF/DMARC.
opsec: active
opsecNote: This is an OUTBOUND/contact tool — it touches the recipient directly and is the opposite of passive recon. The free tier logs and discloses your IP. Sending fake email can constitute fraud; only use for legitimate, authorised contact, never to impersonate.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running anonymous-mailer service (claims operation since 2008); listed by uk-osint. It is a sending utility, not a verified intelligence source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- anonymouse-org
aliases:
- Anonymailer
tags:
- email
- Email Related Sites
- anonymous-mailer
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# anonymailer.net

> A web form for sending anonymous or sender-spoofed email — an outreach/pretext utility, not an email-lookup tool.

## When to use
Only when an authorised investigation legitimately needs to send a message from a sock-puppet identity (for example, structured outreach where revealing your real address would burn the operation). It produces nothing about a target's `email`; it is purely an outbound action. For looking up who is behind an address, use `[[behindtheemail-com]]` or `[[app-profiler-me]]` instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.anonymailer.net/send-free-email4.asp.
2. Fill the form: sender name + sender `email` (spoofable), recipient `email`, subject, message body, and an SMTP server choice.
3. Submit. On the free tier the message carries an advertising footer and a notice that your IP was recorded.
4. (Paid only) sign in to a membership for "clean" sends and SMTP servers that may pass SPF/DMARC.

## Inputs → Outputs
- **In:** sender `email`, recipient `email`, subject, body
- **Out:** none (a delivered message; no intelligence is returned)
- **Empty/negative result looks like:** N/A — this tool does not return lookup data.

## Gotchas & OpSec
- Human-in-the-loop: "clean" sends and SPF/DMARC-passing SMTP sit behind paid membership.
- OpSec: **active and contact-making**. The free tier records and discloses your IP, and modern mail providers usually quarantine spoofed mail. Sending fake email may be a criminal offence (the site says so itself) — only ever use for lawful, authorised contact, never impersonation of a real person.

## Overlaps ("do both")
- Same class as `[[anonymouse-org]]` (AnonEmail). Prefer whichever is reachable; both are sending utilities, not recon.

## Trust & verifiability
`trust: community` — an established but unaudited anonymous-mailer; treat it as an action tool whose reliability and legality depend entirely on lawful, authorised use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | anonymailer-net |
| category | email |
| selectorsIn → selectorsOut | email → (none) |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, payment-wall-partial) |
