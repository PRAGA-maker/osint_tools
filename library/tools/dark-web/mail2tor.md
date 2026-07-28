---
id: mail2tor
name: Mail2Tor
description: Use when you encounter a `@mail2tor` `email` and want to understand it — a Tor-only anonymous mail service, so the address signals deliberate anonymity rather than a pivotable identity.
url: http://mail2torjgmxgexntbrmhvgluavhj7ouul5yar6ylbvjkxwqf6ixkwyd.onion/
category: dark-web
path:
- dark-web
bestFor: Recognising and understanding Mail2Tor addresses — an anonymous Tor-hosted email provider with no clearnet identity to unmask.
selectorsIn:
- email
selectorsOut: []
status: degraded
pricing: free
costNote: Free, donation-funded anonymous email; reachable only over Tor (no clearnet). Uptime is variable.
opsec: active
opsecNote: Reachable only via Tor Browser. Merely visiting is dark-web browsing; never register or send from it to a subject. Treat encountering a mail2tor address as intelligence about the sender's intent, not as a lookup you can enrich.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-running but anonymous hidden service with no accountable operator; existence and uptime are community-verified, not guaranteed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- mail2tor.com
tags:
- darkweb
- Dark Web Links
- anonymous-email
source: uk-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Mail2Tor

> A Tor-only anonymous email service — worth knowing not as a lookup tool but because a `@mail2tor` address in evidence tells you the sender deliberately chose an untraceable mailbox.

## When to use
You've found an `email` on the `@mail2tor.com` (or related) domain attached to a subject, message, or account. The OSINT value is interpretive: this is a hidden-service mail provider that keeps minimal logs and has no clearnet presence, so there is no registrant, IP, or recovery trail to pivot on. Recognising it tells you the correspondent wanted anonymity — useful context, not a data source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Recognise the domain: `@mail2tor.com` / `.onion` Mail2Tor addresses indicate Tor-hosted anonymous mail.
2. If you must reach the service itself, open the `.onion` URL in Tor Browser (it is unreachable over normal browsers).
3. Do NOT expect any account-existence or recovery oracle — unlike mainstream providers, Mail2Tor exposes nothing about who owns an address.
4. Redirect effort: pivot on where the address was *used* (accounts it registered, posts it signed) rather than on the mail provider.

## Inputs → Outputs
- **In:** an `email` on a Mail2Tor domain (recognition)
- **Out:** none — no registrant, IP, or profile is obtainable; the signal is "sender chose anonymity"
- **Empty/negative result looks like:** the expected state — there is intentionally nothing to enrich from the provider itself. The service may also simply be down (variable uptime).

## Gotchas & OpSec
- Human-in-the-loop: none, but access requires Tor.
- OpSec: **active** dark-web access if you visit; never authenticate or send. Keep this at the level of recognition/interpretation.
- Uptime is unreliable and mirror URLs change; a dead link is not evidence about any subject.

## Overlaps ("do both")
- Where a mainstream address would send you to an account-existence oracle, a Mail2Tor address sends you the other way — focus on the accounts/services the address registered, using username and email-reuse tooling instead.

## Trust & verifiability
`trust: unverified` — an anonymous hidden service with no accountable operator; treat its existence as community-verified and draw conclusions only about sender intent, not identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mail2tor |
| category | dark-web |
| selectorsIn → selectorsOut | email → — |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
