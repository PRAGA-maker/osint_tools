---
id: ki-tc
name: Ki.tc
description: Use when you have a channel to reach a subject and want their `ip-address` — a Grabify-style link shortener that logs the IP, geolocation, and browser of whoever opens your tracked link.
url: https://ki.tc
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ip-loggers
bestFor: Wrapping a link a subject will click so their IP, coarse location, and browser fingerprint get logged.
input: Target URL or destination to wrap
output: Tracker link, visitor IP logs, browser info
selectorsIn:
- email
- social-profile
selectorsOut:
- ip-address
- geolocation
- device-id
status: live
pricing: free
costNote: Free to create tracking links and read the logs.
opsec: active
opsecNote: A lure, not a passive lookup — the subject must click, and delivering the link is a deliberate, potentially unlawful contact (pretext/interception). Use only with clear authorization, from a sock-puppet account and burner delivery channel; the service retains everything you collect.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous third-party tracking service; it sees every IP you capture and every link you make — treat its data handling as hostile.
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
- ip-logger
- grabify
aliases:
- ki.tc
tags:
- ip-loggers
- honeypot-link
- ip-address
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Ki.tc

> Another honeypot-link shortener in the Grabify mould: create a tracked link, get the subject to open it, and read back their IP, location, and device.

## When to use
You can get a message in front of the subject — via `email`, a `social-profile` DM, or another channel — and need a rough `ip-address` / `geolocation`. Ki.tc wraps a destination URL into a link that logs whoever clicks. Same interventionist technique as [[ip-logger]] and [[grabify]]: useful (e.g. in an authorized missing-person case) but active and legally sensitive, never a database lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a sock-puppet browser, open https://ki.tc and create a tracking link pointing at a plausible destination the subject would open.
2. You receive a short tracking link plus a private stats view — save the stats link.
3. Deliver the tracking link through your authorized channel.
4. When the subject opens it, ki.tc records IP, geolocation/ISP, browser/OS, and timestamp; read these on the stats view.
5. Pivot the captured IP into WHOIS/ISP geolocation; discard obvious link-preview bot hits (messaging apps pre-fetch links).

## Inputs → Outputs
- **In:** a delivery channel (`email`, `social-profile`) + a destination URL to wrap
- **Out:** `ip-address`, coarse `geolocation`, `device-id` (browser/OS fingerprint), click timestamp
- **Empty/negative result looks like:** zero hits (never opened), or only crawler/preview-bot IPs (datacenter ranges from Facebook/WhatsApp/Slack prefetch) — not the subject.

## Gotchas & OpSec
- **Legal gate:** collecting an IP by deception can be unlawful without authority; use only within an authorized investigation.
- First hits are often link-preview bots, not the target — wait for a hit with a real consumer ISP and mobile/desktop user-agent.
- VPN/mobile CGNAT/Tor will mask or scramble geo; an IP is a lead, not an address.
- The service keeps a copy of everything; a leaked stats link exposes your operation.

## Overlaps ("do both")
- Interchangeable with [[ip-logger]] and [[grabify]] — same honeypot concept, different providers; if one is blocked by the target's mail/security filters, another may deliver. No need to run all three on one target.

## Trust & verifiability
`trust: unverified` — anonymous tracker with no accountable operator; the IPs/fingerprints it returns are only as trustworthy as the service, which also retains everything you collect.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ki-tc |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | email, social-profile → ip-address, geolocation, device-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
