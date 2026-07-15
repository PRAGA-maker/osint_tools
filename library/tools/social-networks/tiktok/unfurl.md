---
id: unfurl
name: Unfurl
description: Use when you have a URL (shared link, tracking URL, shortlink) and want to decode every hidden component — timestamps, account IDs, geolocation, tracking params — returns geolocation, device-id, and social-profile IDs.
url: https://github.com/obsidianforensics/unfurl
category: social-networks
path:
- social-networks
- tiktok
bestFor: Exploding any URL into a graph of decoded parts — timestamps, embedded IDs, coordinates and tracking data hidden in the link.
selectorsIn:
- social-profile
selectorsOut:
- geolocation
- device-id
- social-profile
status: live
pricing: free
costNote: Free and open-source (MIT). Use the hosted version at dfir.blog/unfurl (no account), or `pip install dfir-unfurl[all]` for local CLI/web use. Actively maintained (releases through 2026).
opsec: passive
opsecNote: Local/hosted parsing decodes the URL string itself and does not fetch the target platform, so you never touch the subject's account. Prefer local install (`unfurl`) for sensitive links so the URL never leaves your machine via the public web app.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by Ryan Benson (obsidianforensics), a respected DFIR practitioner; widely used in forensics/OSINT. Open-source and transparent about how each parser decodes values.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- epoch-converter
aliases:
- dfir-unfurl
- obsidianforensics unfurl
tags:
- url-forensics
- metadata
- dfir
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Unfurl

> Paste a messy URL and it draws a graph exposing everything baked in — creation timestamps, user/machine IDs, embedded coordinates, tracking codes — turning an opaque link into structured intelligence.

## When to use
You have a URL tied to your subject — a shared social post, a shortened link, a tracking URL from an email, a Google Maps link — and you want the intelligence hidden inside it. Unfurl decodes embedded timestamps (when a Tweet/Snap/message was created), account and device IDs, geolocation coordinates, and tracking parameters that reveal how the link was generated and shared.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dfir.blog/unfurl (hosted) — or run locally: `pip install dfir-unfurl[all]` then `unfurl_app` (web on :5000) or the `unfurl` CLI.
2. Paste the full URL into the input.
3. Read the expanding graph: each node decodes a component — hover/click to see timestamps rendered as dates, IDs broken out, coordinates mapped.
4. Note especially any decoded timestamp, geolocation, or embedded user/device ID.
5. Pivot: a decoded `geolocation` places an event; a decoded account/`device-id` links the URL to a specific user; a timestamp anchors a timeline.

## Inputs → Outputs
- **In:** a URL (`social-profile` link, shortlink, tracking URL, map link, etc.)
- **Out:** `geolocation` (embedded coords), `device-id`/account IDs, `social-profile` identifiers, decoded timestamps
- **Empty/negative result looks like:** the graph shows only the plain scheme/host/path with nothing decoded — the URL simply carries no encoded intelligence; not every link does.

## Gotchas & OpSec
- It decodes what's **in the string** — it doesn't fetch the page, so it won't reveal content behind the URL.
- For sensitive links, use the **local** install so the URL isn't submitted to the public web app.
- Decoded IDs/timestamps are authoritative for the platforms Unfurl has parsers for; unknown formats stay raw.

## Overlaps ("do both")
- Pairs with any tool that hands you a URL (shortlink expanders, social scrapers) — Unfurl squeezes the metadata out of the link they give you.
- Combine with an EXIF tool: Unfurl for URL metadata, EXIF tools for the media the URL points to.

## Trust & verifiability
`trust: community` — open-source, maintained by a well-known forensics author; decoding logic is inspectable, so results are verifiable against the documented parsers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unfurl |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → geolocation, device-id, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
