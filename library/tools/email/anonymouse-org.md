---
id: anonymouse-org
name: anonymouse.org
description: Use when an investigation needs to send an anonymous email via Anonymouse's AnonEmail — an outbound pretext tool, not an email lookup; the endpoint is currently unreachable.
url: http://anonymouse.org/anonemail.html
category: email
path:
- email
bestFor: Sending an anonymous email from a research persona (when reachable).
selectorsIn:
- email
selectorsOut: []
status: down
pricing: free
costNote: Historically a free anonymous-email and anonymous-web-surfing service.
opsec: active
opsecNote: An outbound/contact tool that messages the recipient directly — the opposite of passive recon. Sending fake or spoofed mail can have legal consequences; only use for lawful, authorised contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing privacy/anonymizer project (Anonymouse / AnonWWW); listed by uk-osint. Connection refused on repeated attempts (2026-06-13), so currently down/unreachable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- anonymailer-net
aliases:
- AnonEmail
- Anonymouse
tags:
- email
- Email Related Sites
- anonymous-mailer
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# anonymouse.org

> Anonymouse's AnonEmail — a free anonymous-email sender (an outreach utility, not a lookup). Currently unreachable.

## When to use
Only when an authorised investigation needs to send a message from a sock-puppet identity and you do not want to expose your real address. It returns nothing about a target's `email`. For finding who is behind an address, use `[[behindtheemail-com]]` or `[[app-profiler-me]]`. As of 2026-06-13 the server refuses connections, so plan to use `[[anonymailer-net]]` instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. (When live) open http://anonymouse.org/anonemail.html.
2. Enter the recipient `email`, a subject, and the message body in the AnonEmail form.
3. Submit; Anonymouse relays the message while stripping your originating details.
4. If the page fails to load (connection refused, as observed), fall back to `[[anonymailer-net]]`.

## Inputs → Outputs
- **In:** recipient `email`, subject, body
- **Out:** none (a relayed message; no intelligence returned)
- **Empty/negative result looks like:** connection refused / page will not load — currently the expected state; mark unreachable.

## Gotchas & OpSec
- Status: **down** — repeated connection-refused errors on 2026-06-13. Retry later or substitute another anonymous mailer.
- OpSec: **active and contact-making**. Spoofed/anonymous mail is frequently filtered and may carry legal risk; use only for lawful, authorised outreach.

## Overlaps ("do both")
- Functionally equivalent to `[[anonymailer-net]]`; use whichever is reachable.

## Trust & verifiability
`trust: community` — a venerable anonymizer project, but unverified and currently unreachable; do not rely on availability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | anonymouse-org |
| category | email |
| selectorsIn → selectorsOut | email → (none) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
