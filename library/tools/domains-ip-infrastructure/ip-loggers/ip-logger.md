---
id: ip-logger
name: IP Logger
description: Use when you have a channel to reach a subject (`email`, `social-profile`) and want their `ip-address` and coarse `geolocation` — returns the visitor IP, geo, and device fingerprint of whoever opens your tracked link.
url: https://iplogger.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ip-loggers
bestFor: Turning a link a subject will click into their IP address, coarse geolocation, and browser/device fingerprint.
input: URL to wrap or a contact channel to deliver the trap link
output: Logging URL, visitor IP/location/device data
selectorsIn:
- email
- social-profile
selectorsOut:
- ip-address
- geolocation
- device-id
status: live
pricing: free
costNote: Free to create links and view logs without an account; a free account persists your loggers and history.
opsec: active
opsecNote: This is a lure, not a passive lookup — the subject must open your link, and delivering it is a deliberate contact that can tip them off and is legally sensitive (pretext/interception laws). Only use with clear authorization (e.g. law-enforcement/family consent in a missing-person case). The service itself logs the creator; use a sock-puppet account and a burner delivery channel, never your real infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party tracking service of unknown ownership; it sees every IP you collect and every link you make, so treat its data handling as hostile.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- grabify
- ki-tc
aliases:
- iplogger.com
- iplogger.org
- IP grabber
tags:
- ip-loggers
- honeypot-link
- ip-address
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# IP Logger

> A honeypot-link generator: wrap a URL (or an invisible pixel), get the subject to open it, and read back their IP, geolocation, and device fingerprint.

## When to use
You cannot see the subject directly but you *can* get a message in front of them — you have their `email`, a `social-profile` DM, or another channel — and you need a rough `ip-address` / `geolocation` to narrow where they are. Classic use is a consented missing-person case where you can send the subject a link and want to confirm they are online and roughly where. It is an **active, interventionist** technique, not a database lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a sock-puppet browser session, open https://iplogger.com/ (it redirects to iplogger.org).
2. Choose a logger type: a **URL/link shortener** (redirects to a real page you pick, e.g. an image or article the subject would plausibly open), or an **invisible image/pixel** you embed in a page or email.
3. Paste the destination URL and create the logger. You get two links: the public "logging" link to send, and a private stats/access link — save the stats link.
4. Deliver the logging link to the subject through your authorized channel. When they open it, the logger records IP, country/city geo, ISP, browser, OS, screen size, referrer, and timestamp.
5. Open your stats link to read the hits. Pivot the captured `ip-address` into [[grabify]]-style enrichment or a WHOIS/ISP lookup to place the connection geographically.

## Inputs → Outputs
- **In:** a delivery channel (`email`, `social-profile`) plus a destination URL to wrap
- **Out:** `ip-address`, coarse `geolocation` (country/city/ISP), `device-id` (browser/OS/screen fingerprint), click timestamp
- **Empty/negative result looks like:** the stats page shows zero hits (link never opened), or only *your own* IP / link-preview bot IPs (Facebook, WhatsApp, and Slack pre-fetch links, producing datacenter IPs that are **not** the subject) — discard obvious crawler hits.

## Gotchas & OpSec
- **Legal gate:** collecting someone's IP by deception can be unlawful without authority. Do not use this outside an authorized investigation.
- Messaging apps and email clients pre-fetch links, so the first hit is often a bot, not the target — corroborate with a hit that carries a real consumer ISP and a mobile/desktop user-agent.
- VPN, mobile carrier CGNAT, and Tor will mask or scramble the geo; a captured IP is a lead, not a home address.
- The service sees everything you do; a leaked stats link exposes your operation. Never reuse it across cases.

## Overlaps ("do both")
- Pairs with [[grabify]] and [[ki-tc]] — same honeypot-link concept from different providers; if one is blocklisted by the target's mail/security filter, another may pass. Grabify also adds richer per-click fingerprinting to compare against IP Logger's capture.

## Trust & verifiability
`trust: unverified` — anonymous third-party tracker with no accountable operator; the IPs and fingerprints it hands you are only as trustworthy as the service, and it retains a copy of everything you collect.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ip-logger |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | email, social-profile → ip-address, geolocation, device-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
