---
id: dark-fail
name: dark.fail
description: Use when you have (or need) a Tor `.onion` service and want its PGP-verified current address and up/down status — returns trustworthy onion `domain`s for markets, mail, search and news.
url: https://dark.fail/
category: dark-web
path:
- dark-web
bestFor: Finding the verified, currently-online .onion address for a known dark-web service.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free (optional Monero donations). No account, no tracking, no JavaScript.
opsec: passive
opsecNote: Access over Tor. dark.fail deliberately serves no direct links, JS, or trackers to avoid deanonymising visitors, but you are browsing dark-web infrastructure — use Tor Browser in a hardened/sock-puppet setup and never log into anything from your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, respected uptime/verification directory; PGP-signs the addresses it lists, which is the standard defence against onion phishing clones — but always verify signatures yourself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- dark.fail
tags:
- Search engines
- Darknet/deepweb search tools
- onion
- tor
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# dark.fail

> Trusted onion phone book: the PGP-verified, currently-online addresses for major dark-web services, with live up/down status.

## When to use
You're investigating on the dark web and need the *correct* `.onion` address for a service — a marketplace, a privacy mail provider, a dark-web search engine, a news mirror — without falling for a phishing clone. Onion addresses are unmemorable and constantly cloned to steal credentials/funds, so dark.fail's PGP-verified listings and real-time online/offline status are the safe starting point for reaching a known service or checking whether one is still up.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dark.fail/ in Tor Browser (a clearnet mirror exists, but treat onion services over Tor).
2. Browse the list: each service shows its address and a green/red online status.
3. Verify before trusting — dark.fail publishes PGP-signed canonical addresses; check the signature against the site's key rather than trusting the raw string.
4. Copy the verified `.onion` `domain` and open it in Tor (dark.fail intentionally uses no clickable direct links).
5. Pivot: use the confirmed address as the safe entry point; monitor the status page to know when a service goes down/returns.

## Inputs → Outputs
- **In:** the name of a known dark-web service (or a `.onion` `domain` you want to confirm)
- **Out:** the PGP-verified canonical `.onion` `domain` and its current online/offline status
- **Empty/negative result looks like:** the service isn't listed, or shows offline — many onion services are transient; "not listed" doesn't mean it doesn't exist, and "offline" may be temporary.

## Gotchas & OpSec
- Phishing clones of dark.fail itself exist — reach it via a known-good bookmark/mirror and verify its PGP key.
- Listing ≠ endorsement; dark.fail explicitly disclaims the legality/safety of listed services.
- OpSec: browse only over Tor in a hardened, sock-puppet setup; never authenticate with your real identity, and assume any dark-web service is hostile.

## Overlaps ("do both")
- Complements dark-web search engines — dark.fail gives the trusted address for services you already know, while a darknet search engine helps discover new ones (which you then verify).

## Trust & verifiability
`trust: community` — a well-established directory whose whole value is PGP-verified, phishing-resistant addresses; trust it as a starting point but verify the signatures yourself, since impersonation is the core threat here.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dark-fail |
| category | dark-web |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
