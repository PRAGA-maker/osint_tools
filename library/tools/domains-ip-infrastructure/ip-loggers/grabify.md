---
id: grabify
name: Grabify
description: Use when you can get a target to click a link and want their IP and device details — returns `ip-address`, coarse `geolocation` and browser/device fingerprint from the click.
url: https://grabify.link
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ip-loggers
bestFor: Capturing a clicker's IP address, approximate location and device fingerprint via a disguised tracking link.
selectorsIn: []
selectorsOut:
- ip-address
- geolocation
- device-id
status: live
pricing: free
costNote: Free (ad-supported); optional free account to manage links and view dashboards.
opsec: active
opsecNote: This is an ACTIVE, engagement-based technique — you must get the target to click a link you created, which is a form of contact and may be entrapment/unlawful depending on jurisdiction and pretext. The link and its host see the URL; the target's ISP sees the click. Only use with clear legal authorisation, and never impersonate someone to induce the click.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely used free IP-logging service; the captured IP/geolocation is real but coarse (ISP-level city, easily masked by VPN/mobile NAT), so treat results as indicative, not precise.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- grabify.link
- Grabify IP Logger
tags:
- ip-logger
- tracking-link
- active-technique
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Grabify

> A free "IP logger": you create a disguised short link, get the target to click it, and Grabify records the click's IP address, approximate location, and device fingerprint — an active, high-caution technique.

## When to use
You need to place an otherwise-anonymous online contact (a chat handle, a marketplace seller, an extortion account) to a real network, and you have a lawful basis and a plausible reason to get them to click a link. Grabify turns that click into an `ip-address`, coarse `geolocation`, and a device/browser fingerprint. This is engagement-based and legally sensitive — treat it as a last-resort, authorised measure, not routine passive OSINT.

## How to use it (`bestInteractionPattern`: web-manual)
1. On https://grabify.link, paste a believable destination URL (something the target would genuinely open) to generate a tracking link; optionally disguise it further.
2. Deliver the link to the target through your existing, authorised channel — do NOT impersonate a real person or use a deceptive pretext that would be unlawful.
3. When they click, open the Grabify dashboard for that link to read the logged IP, ISP, city-level location, timezone, OS/browser, and Smart Logger extras.
4. Pivot: take the `ip-address` into IP-geolocation/WHOIS and ISP-abuse or legal process to move from coarse to precise.

## Inputs → Outputs
- **In:** none from the subject up front — you craft a link and induce a click
- **Out:** `ip-address`, ISP, coarse `geolocation` (city/region), timezone, `device-id`/browser fingerprint
- **Empty/negative result looks like:** the target never clicks (no data), or the IP resolves to a VPN/Tor/mobile carrier NAT — giving a datacenter/wrong city rather than the person's real location.

## Gotchas & OpSec
- Human-in-the-loop: none technically, but a human decision on legality and pretext is mandatory before use.
- OpSec: **active/engagement** — you are contacting and manipulating the target into an action; this can be unlawful (unauthorised tracking, entrapment) and can alert them. Get authorisation, log your justification, and never impersonate.
- Accuracy: consumer IP geolocation is city-level at best and defeated by VPN/proxy/mobile NAT; a VPN-detection flag means the location is likely bogus.

## Overlaps ("do both")
- Pairs with IP-geolocation and WHOIS tools because Grabify only captures the raw IP; those turn it into ISP, ranges and abuse contacts for follow-up (including legal process).

## Trust & verifiability
`trust: community` — a reliable capture mechanism, but the *interpretation* is the risk: the IP is real yet coarse and easily masked, so corroborate any location and never treat a single click as a confirmed home address.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
