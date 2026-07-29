---
id: sitebroker
name: SiteBroker
description: Use when you have a `domain` or `ip-address` and want automated recon (WHOIS, reverse-IP, subdomains, nameservers, Cloudflare detection) — returns `domain`, `ip-address`, and related infrastructure.
url: https://github.com/Anon-Exploiter/SiteBroker
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-command domain/IP reconnaissance bundling WHOIS, reverse-IP, subdomain scanning and Cloudflare detection.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: degraded
pricing: free
costNote: Free and open-source (MIT). No account or key needed; you provide the Python runtime.
opsec: active
opsecNote: Several modules (crawling, subdomain scanning, banner grabbing, admin-panel detection) send requests directly to the target's infrastructure from your IP — this is active recon. Run from a VPS/VPN you control, not your home IP, when the target could be hostile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Public MIT-licensed tool (429★) but archived/read-only since May 2024 — unmaintained, so some search-engine and third-party integrations may have broken.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- SiteBroker python recon
tags:
- Domain/IP/Links
- Domain/IP investigation
- recon
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# SiteBroker

> A cross-platform Python recon utility that bundles the common domain/IP information-gathering steps behind one menu — now archived, so treat outputs with caution.

## When to use
You have a `domain` or `ip-address` and want a quick automated first pass: WHOIS, reverse-IP lookup, nameserver identification, subdomain scan, Cloudflare detection, banner grabbing, and admin-panel discovery, without running each tool separately. Useful for the infrastructure side of an investigation (mapping a site's hosting and related domains).

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/Anon-Exploiter/SiteBroker` and install dependencies (`requests`, `colorama`, `dnspython`, `bs4`) with Python 3.6–3.7, or use the provided Docker option.
2. Run the script and pick a module from the menu (e.g. reverse-IP, subdomain scan, WHOIS).
3. Enter the target `domain`/`ip-address`.
4. Read the output; correlate discovered subdomains, nameservers, and co-hosted sites.
5. Pivot: new subdomains/IPs feed passive-DNS and certificate-transparency tools; WHOIS contacts feed registrant OSINT.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** related `domain`s (subdomains, reverse-IP neighbours), `ip-address`, nameservers, WHOIS/banner data
- **Empty/negative result looks like:** a module erroring or returning nothing — on an archived tool this often means a broken upstream (e.g. a search API changed), not that the target has no data. Verify with a maintained tool.

## Gotchas & OpSec
- **Archived (read-only since May 2024)** and unmaintained — search-engine crawling and some lookups may silently fail against today's APIs. Don't trust a blank result; cross-check.
- **Active recon**: crawling/scanning modules hit the target directly; use controlled infrastructure.
- Pins old Python (3.6/3.7); run in a venv/container to avoid dependency conflicts.

## Overlaps ("do both")
- Pair with maintained recon suites and passive sources (crt.sh, SecurityTrails, amass) — SiteBroker gives a fast bundled sweep, but a maintained subdomain/passive-DNS tool will be more complete and current.

## Trust & verifiability
`trust: community` — open MIT source you can read and run yourself, but archived and unmaintained; confirm anything load-bearing against an actively maintained tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sitebroker |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
