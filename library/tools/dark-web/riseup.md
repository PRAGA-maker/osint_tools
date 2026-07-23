---
id: riseup
name: RiseUp
description: Use when a target's email is @riseup.net (or you need activist-grade sock-puppet infra) — context on Riseup, a privacy collective whose services deliberately expose almost no user data.
url: http://vww6ybal4bd7szmgncyruucpgfkqahzddi37ktceo3ah7ngmcopnpyyd.onion/
category: dark-web
path:
- dark-web
bestFor: Recognizing a @riseup.net address as an activist privacy provider, and understanding why it yields little OSINT.
selectorsIn:
- email
selectorsOut: []
status: live
pricing: free
costNote: Free, donation-funded services (email, VPN, chat, lists); email accounts are gated (historically invite/registration-limited) to prevent abuse.
opsec: passive
opsecNote: Recognizing a Riseup address is passive. Riseup is run by an activist tech collective and is explicitly privacy-protective — it keeps minimal logs and resists data requests, so expect email-enrichment tools to return essentially nothing for a @riseup.net address. If you use Riseup yourself, note accounts are gated and intended for activists, not casual sock puppets. The .onion address requires Tor.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Riseup is a long-established, reputable activist-focused privacy provider; it is a genuine service, not an OSINT lookup tool, and was harvested into a dark-web link list because of its onion service.
missingPersonsRelevance: low
coverage:
- global
auth: invite
api: false
localInstall: false
registration: true
aliases:
- Riseup.net
- riseup
tags:
- darkweb
- Dark Web Links
- privacy-provider
source: uk-osint
lastVerified: '2026-07-23'
enrichment: full
---

# RiseUp

> Riseup is an activist tech collective providing privacy-protective email, VPN, and chat — recorded here as a provider to *recognize*, since a @riseup.net address signals a privacy-conscious subject and yields almost no data.

## When to use
You encounter a `email` at `@riseup.net`, or you're deciding where to stand up privacy-focused infrastructure. Reach for this entry to interpret the signal: Riseup is a well-known collective serving activists, journalists, and organisers, built to minimise logging and resist surveillance. Practically, that means email-lookup and breach-adjacent tools will return little for a Riseup address — treat the address itself as a *privacy signal* (the subject deliberately chose a hardened provider) rather than a dead lead. It is not an OSINT lookup service.

## How to use it (`bestInteractionPattern`: web-manual)
1. If you see a `@riseup.net` address, note what it implies: a privacy-conscious user on an activist-oriented provider; expect minimal enrichment.
2. Don't expect account-existence or profile tools to work as they might for mainstream providers — Riseup is built to leak little.
3. For your own use: Riseup's email is gated (historically invite-code / vetted registration), so it isn't a quick throwaway; its VPN and other services are more openly available.
4. The onion address requires the Tor Browser; the clearnet service is at riseup.net.
5. Pivot: pivot *off* the address to other selectors (the person's other accounts, usernames, content) rather than trying to squeeze data from Riseup itself.

## Inputs → Outputs
- **In:** a `@riseup.net` `email` (as a signal to interpret)
- **Out:** context/interpretation, not data — recognition that the subject uses a privacy-hardened provider
- **Empty/negative result looks like:** exactly what you should expect — enrichment tools return nothing for a Riseup address; that's the provider working as designed, not a failed lookup.

## Gotchas & OpSec
- Not a lookup tool: this is a provider you recognise, not a service you query for target data.
- Riseup email is intentionally gated (invite/vetted) and reserved for activist use — not a casual sock-puppet source.
- OpSec: recognition is passive; the onion service needs Tor. Respect that Riseup users are often at-risk people.

## Overlaps ("do both")
- Conceptually like `[[proton-me]]` — both are privacy providers whose addresses resist enrichment. When email tools stall on such a provider, pivot to username/content-based approaches instead of hammering the address.

## Trust & verifiability
`trust: trusted` — Riseup is a genuine, well-regarded privacy provider; the reliable takeaway is interpretive (a Riseup address means "privacy-hardened, expect little data"), not a data feed to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | riseup |
| category | dark-web |
| selectorsIn → selectorsOut | email →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
