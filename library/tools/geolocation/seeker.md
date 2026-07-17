---
id: seeker
name: Seeker
description: Use when you can get a subject to click a link (with authorization) and want their precise location — returns GPS geolocation plus ip-address and device-id from the clicked page.
url: https://github.com/thewhiteh4t/seeker
category: geolocation
path:
- geolocation
bestFor: Capturing precise GPS coordinates, IP, and device details when a target clicks a hosted consent-prompt link — authorized use only.
selectorsIn:
- social-profile
selectorsOut:
- geolocation
- ip-address
- device-id
status: live
pricing: free
costNote: Free, open-source (Python). No account or key; you supply your own hosting/tunnel (e.g. ngrok) for the capture page.
opsec: active
opsecNote: This is an ACTIVE social-engineering tool — you host a page that prompts the target for location permission and capture GPS/IP/device data when they click and consent. It directly interacts with and deceives the subject, is highly intrusive, and is unlawful without authorization (consent, or a law-enforcement/legal order). Never deploy against a person without a clear legal basis; the link and hosting also expose YOUR infrastructure.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: cli
trust: community
trustNote: Widely-known open-source tool (thewhiteh4t); it works as described, but it is an offensive social-engineering utility, so the "trust" is in the code, not in any claim of lawful safety.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- finalrecon
- nexfil
aliases:
- thewhiteh4t/seeker
tags:
- geolocation
- phishing
- social-engineering
- gps
source: gh-topic-reconnaissance
lastVerified: '2026-07-17'
enrichment: full
---

# Seeker

> An open-source social-engineering tool that hosts a consent-prompt web page (e.g. a fake "nearby" template); when the target opens it and grants location access, it captures precise GPS, IP, and device details. Authorized use only.

## When to use
Only when you have a lawful basis to actively engage the subject — documented consent, or law-enforcement/legal authorization in a missing-persons case — and you can plausibly get the person to open a link on their phone. This is not a passive lookup: it is the last-resort, intrusive option when open-source pivots have failed and a legal process (e.g. police working an exigent case) can justify inducing a click to obtain a real-time location.

## How to use it (`bestInteractionPattern`: cli)
1. Confirm authorization first — without it, do not proceed. Then clone `https://github.com/thewhiteh4t/seeker` and run its install script (Python; Docker image also available).
2. Launch `python3 seeker.py` and choose a page template; Seeker serves a local page that requests browser geolocation permission.
3. Expose it publicly with a tunnel (ngrok / your own domain) and deliver the resulting link to the subject through an appropriate, authorized channel.
4. When the target opens the link and **grants** location permission, Seeker logs GPS latitude/longitude + accuracy, plus IP, browser/OS, and device attributes.
5. Pivot: the captured `geolocation` is a real-time fix; the `ip-address` feeds ISP/geo lookups; `device-id`/UA details corroborate identity.

## Inputs → Outputs
- **In:** `social-profile` / a delivery channel to send the link, plus the subject's action of clicking and consenting
- **Out:** `geolocation` (precise GPS with accuracy radius), `ip-address`, `device-id` (browser/OS/device fingerprint)
- **Empty/negative result looks like:** the target never opens the link, or opens it but **denies** the location prompt — you then get at most IP-based coarse geolocation, not GPS. Modern browsers require an explicit permission grant, so a refusal yields no GPS.

## Gotchas & OpSec
- Human-in-the-loop / **legal-gate:** deploying this against a person without consent or lawful authority is illegal in most jurisdictions. Treat authorization as a hard prerequisite, not a formality.
- OpSec: **active and intrusive** — it deceives and directly touches the subject, and your hosting/link can be traced back to you. Use only sanctioned infrastructure.
- GPS requires an explicit permission grant in the browser; a denied prompt degrades the result to coarse IP geolocation.

## Overlaps ("do both")
- Unlike passive tools, Seeker requires target interaction. Pair a coarse `[[finalrecon]]`/IP-geolocation pass first; only escalate to Seeker under authorization when passive methods can't produce a location.

## Trust & verifiability
`trust: community` — the tool is well-known and functions as documented, but it is offensive tooling; verify the captured fix (accuracy radius, repeat pings) and remember the legal exposure rests entirely on your authorization, not the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seeker |
| category | geolocation |
| selectorsIn → selectorsOut | social-profile → geolocation, ip-address, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (legal-gate) |
