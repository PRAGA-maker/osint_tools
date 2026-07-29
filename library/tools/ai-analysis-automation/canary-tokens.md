---
id: canary-tokens
name: Canary Tokens
description: Use when you want to unmask who opens a document/link/email by planting a tripwire — returns the opener's `ip-address`, approximate `geolocation`, and user-agent when triggered.
url: https://canarytokens.org/generate
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Planting a honeytoken (in a file, link, or email) that phones home with the viewer's IP and metadata the moment it's opened.
selectorsIn: []
selectorsOut:
- ip-address
- geolocation
- device-id
status: live
pricing: freemium
costNote: The public canarytokens.org generator is free; Thinkst also offers a paid Canary/Canarytokens enterprise product. Free tier covers the common token types.
opsec: active
opsecNote: This is an ACTIVE trap. A token only fires when someone interacts with the bait you plant, and it captures THEIR IP/metadata — so its legality and ethics depend entirely on how you deploy it. Never embed a token in content you send under false pretences to entrap an uninvolved person; the classic legitimate use is instrumenting your own documents/accounts to detect intruders. Consider legal-gate review before offensive use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Thinkst (a well-known security vendor); the service and its alerting are reliable and widely used in the industry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- Canarytokens
- Thinkst Canarytokens
tags:
- honeytoken
- counterintelligence
- opsec
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Canary Tokens

> A free honeytoken generator: plant an invisible tripwire in a document, URL, email address, or image, and get alerted with the opener's IP and metadata when it's triggered.

## When to use
You want to learn who is accessing something — the classic defensive use is instrumenting your own sensitive files/accounts to detect an intruder, and it can help confirm a location signal (an alert fires with the viewer's `ip-address` and rough `geolocation`). Because a fired token reveals data about *whoever opens the bait*, deployment must be lawful and targeted at your own assets or a consenting scenario, not at unwitting third parties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://canarytokens.org/generate and pick a token type (Word/PDF doc, web URL, DNS, unique email, QR, etc.).
2. Enter a notification email/webhook and a memo describing where you'll place it.
3. Embed the generated token in the bait (e.g. inside a document or as a link) and deploy it in your controlled location.
4. When someone opens it, you receive an alert with the opener's `ip-address`, user-agent/`device-id`, and approximate `geolocation`.
5. Pivot: the captured IP feeds IP-reputation/geolocation OSINT; the user-agent narrows device/OS.

## Inputs → Outputs
- **In:** none (you create bait; the target supplies data by opening it)
- **Out:** on trigger — `ip-address`, approximate `geolocation`, user-agent/`device-id`, timestamp
- **Empty/negative result looks like:** the token never fires — the bait wasn't opened, was opened offline, or was stripped/sandboxed; silence is not proof of anything.

## Gotchas & OpSec
- **Active trap with legal/ethical limits**: only deploy on assets you own or with clear authorization. Entrapping an uninvolved person is unlawful in many places — treat offensive use as a legal-gate decision.
- IP may be a VPN/proxy/corporate egress, and geolocation is coarse — corroborate, don't over-read.
- Some mail gateways and sandboxes pre-open links, producing false triggers from scanners, not the human target.

## Overlaps ("do both")
- Pair with IP-geolocation and reputation tools — Canary Tokens delivers the raw IP/metadata on trigger; those turn it into hosting, ASN, and location context.

## Trust & verifiability
`trust: trusted` — run by Thinkst, a reputable security company; the mechanism and alerts are dependable. The *interpretation* of a captured IP (VPN, shared egress) is where care is needed, not the tool's reliability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canary-tokens |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → ip-address, geolocation, device-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
