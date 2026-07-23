---
id: infooze
name: Infooze
description: Use when you have a `username`, `email`, `domain` or `image` and want a single CLI that runs 18 recon modules (user recon, mail finder, whois/DNS, Insta/Git recon, EXIF) — returns `social-profile`s, `email`s, `domain` data and `metadata-exif`.
url: https://github.com/devXprite/infoooze
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A quick one-command OSINT multitool wrapping username, email, domain, Instagram/GitHub and EXIF lookups.
selectorsIn:
- username
- email
- domain
- image
selectorsOut:
- social-profile
- email
- domain
- metadata-exif
status: live
pricing: free
costNote: Free and open source (MIT, Node.js); install via npm, no account.
opsec: active
opsecNote: Individual modules make live requests to the services they query (Instagram, GitHub, WHOIS, target sites), so some traffic originates from your host. Route through a VPN and avoid running the account-recon modules from an attributable IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source MIT project (~1k GitHub stars); source is auditable, but it wraps third-party endpoints whose APIs change, so some modules may have degraded since the last release.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- httpfy
aliases:
- infoooze
- devXprite/infoooze
tags:
- Tools collections/toolkits
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Infooze

> A Node.js CLI OSINT multitool bundling ~18 recon modules — username/user recon, mail finder, WHOIS/IP/DNS, Instagram and GitHub recon, subdomain/port scan, URL expand and EXIF extraction — behind one command.

## When to use
You want to run a quick first-pass sweep on a selector without opening a dozen separate sites. Give Infooze a `username`, `email`, `domain` or `image` and pick the matching module — it's a convenient wrapper for the routine lookups (who owns this domain, does this username exist across sites, what's in this photo's EXIF) early in an investigation.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `npm install -g infoooze` (Node.js required).
2. Launch the interactive menu with `infoooze` (or `oz`), or call a module directly, e.g. `infoooze -u <username>`, `infoooze -w <domain>`, `infoooze -e <image.jpg>` for EXIF.
3. Pick from the 18 modules — user recon, mail finder, WHOIS/IP/DNS/headers, Instagram recon + DP viewer, GitHub recon, subdomain/port scan, URL expand, website age, useragent, YouTube lookup.
4. Read the module's output.
5. Pivot: usernames feed a dedicated cross-site enumerator; EXIF `metadata-exif` (GPS/device) feeds geolocation; discovered emails feed breach/account tooling.

## Inputs → Outputs
- **In:** `username`, `email`, `domain`, or `image` (per module)
- **Out:** `social-profile` hits, `email`s, `domain` WHOIS/DNS data, `metadata-exif` from images
- **Empty/negative result looks like:** a module returning nothing or an error — often because the upstream service (Instagram, an API) changed or rate-limited since the tool's last release, not because the subject has no footprint. Cross-check with a maintained single-purpose tool.

## Gotchas & OpSec
- It wraps third-party endpoints; the project's last release predates recent API changes, so treat any single module's silence as possibly a broken wrapper, not a true negative.
- Instagram/GitHub recon modules make attributable requests — proxy them and use sock-puppet context.
- OpSec: active for the modules that hit target/third-party services; passive-ish for pure WHOIS/DNS.

## Overlaps ("do both")
- Pairs with maintained single-purpose tools (a dedicated username enumerator, a current EXIF viewer) — Infooze is a fast convenience sweep, but confirm anything important with a tool that's actively kept in step with the target service.

## Trust & verifiability
`trust: community` — auditable MIT open source, but its reliability depends on upstream services it can't control; use it to generate leads, then verify with a purpose-built, maintained tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infooze |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email, domain, image → social-profile, email, domain, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
