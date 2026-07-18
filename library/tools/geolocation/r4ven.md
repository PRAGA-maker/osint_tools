---
id: r4ven
name: r4ven
description: Use when a subject will open a link you control and you want their precise `geolocation`, real `ip-address`, and `device-id` — returns those plus optional front-camera capture.
url: https://github.com/spyboy-productions/r4ven
category: geolocation
path:
- geolocation
bestFor: Capturing GPS-grade location and device fingerprint the moment a target opens a hosted link (with consent/authorization).
selectorsIn:
- social-profile
selectorsOut:
- geolocation
- ip-address
- device-id
status: live
pricing: free
costNote: Free, open-source; self-hosted Python. A tunnel service (ngrok/Cloudflare/Serveo) is needed to reach mobile targets — free tiers exist.
opsec: active
opsecNote: Highly intrusive and active. It social-engineers the target into granting browser permissions; the target directly interacts with infrastructure you run, and browser permission prompts are visible to them. Only use with explicit authorization or the subject's consent (e.g. a cooperating family member locating a missing relative's device). Serving this to a non-consenting third party can be unlawful.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: cli
trust: community
trustNote: Open-source demonstration/pentest tool by spyboy-productions; author explicitly restricts it to education, research, and authorized testing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- cloakquest3r
- https-github-com-spyboy-productions-valid8proxy
aliases:
- spyboy-productions/r4ven
tags:
- geolocation
- phishing
- device-info
- gps
- active
source: gh-topic-reconnaissance
lastVerified: '2026-07-18'
enrichment: full
---

# r4ven

> A self-hosted "canary link": when the subject opens it and grants permission, it captures GPS location, IP, device details, and can snap front-camera photos — an authorization-gated tool, not a covert one.

## When to use
You have a channel to the subject (a `social-profile` / chat you can send a link through) **and** the legal/consent standing to do so — for example a cooperating relative trying to locate a missing person's phone, or an authorized investigation. r4ven yields GPS-grade `geolocation` (20–30 m) that passive IP geolocation can't, plus the device's real `ip-address` and `device-id` fingerprint. If you do not have consent or authorization, do not use it — see OpSec.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/spyboy-productions/r4ven.git`
2. Install deps: `pip3 install -r requirements.txt`
3. Run the server: `python3 r4ven.py`
4. Expose it publicly with a tunnel (ngrok / Cloudflare Tunnel / Serveo / SSH) — required for the link to work on a smartphone browser.
5. Deliver the tunnel URL to the subject; when they open it and allow location/camera, results stream to your dashboard.
6. Read: precise coordinates, IP + approximate ISP location, device/browser info, and any captured camera frames.

## Inputs → Outputs
- **In:** a delivery channel to the subject (`social-profile`) and their willingness to open the link + grant permission
- **Out:** `geolocation` (GPS coords), real `ip-address`, `device-id`/browser fingerprint, optional camera images
- **Empty/negative result looks like:** the target opens the link but **denies** permission → you get only the coarse IP-based location, no GPS; or they never open it → nothing at all.

## Gotchas & OpSec
- Human-in-the-loop / legal-gate: this is the defining constraint. It is intrusive by design and its own author restricts it to education and *authorized* testing. Establish consent or lawful authority first.
- The subject sees a browser permission prompt; a wary target will decline, leaving you only IP-grade location.
- OpSec: **active** — the target touches your server and tunnel. Run it on infrastructure that doesn't tie back to you, and remember your tunnel provider logs the session.
- Accuracy depends entirely on the target granting GPS; without it, prefer passive IP-geolocation methods.

## Overlaps ("do both")
- Pairs with [[cloakquest3r]] — that unmasks infrastructure/IP passively, while r4ven gets device-precise GPS but only through active, consented interaction.

## Trust & verifiability
`trust: community` — an open-source, inspectable pentest/demonstration tool; the code works as described, but the *legitimacy of any given use* rests on you having authorization, not on the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | r4ven |
| category | geolocation |
| selectorsIn → selectorsOut | social-profile → geolocation, ip-address, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (legal-gate) |
