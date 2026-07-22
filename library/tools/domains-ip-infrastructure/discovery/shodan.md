---
id: shodan
name: Shodan
description: Use when you have an `ip-address`, `domain` or `employer-org` and want its internet-exposed devices/services — returns open ports, banners, hostnames and geolocation.
url: https://www.shodan.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Finding a target's internet-facing infrastructure — servers, webcams, IoT, industrial systems — and the services/banners running on them.
selectorsIn:
- ip-address
- domain
- employer-org
selectorsOut:
- ip-address
- domain
- geolocation
status: live
pricing: freemium
costNote: Free account gives limited searches/filters; full filters, bulk results and the API require a paid membership (often available cheaply via periodic sales).
opsec: passive
opsecNote: Shodan scans the internet itself and you query its stored results, so you do NOT touch the target — searching is passive and safe. Do not confuse this with actively connecting to a discovered device (which would be active and attributable).
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: The canonical internet-of-things search engine, widely used across security/OSINT; banners are real captured scan data, though a given result may be hours-to-days old.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- shodan.io
- Shodan search engine
tags:
- Domain/IP/Links
- infrastructure
- device-search
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- internetdb-shodan-io
---

# Shodan

> The search engine for internet-connected devices — query an IP, domain or org and see the exposed ports, services, banners and locations Shodan has scanned.

## When to use
You are mapping a target's infrastructure: you have an `ip-address`, a `domain`, or an `employer-org` name and want to know what it exposes to the internet — web servers, mail servers, VPNs, cameras, ICS/SCADA, databases — plus the software versions and geolocation behind them. A core early-recon step in any infrastructure investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in to a (free or paid) Shodan account at https://www.shodan.io/.
2. Search by `ip:`, `hostname:`, `org:`, `net:` (CIDR), `port:`, `product:`, `country:`, etc. — e.g. `hostname:example.com` or `org:"Example Ltd"`.
3. Open a host to see its open ports, service banners, TLS certs, hostnames and geolocation.
4. Pivot on shared certs, favicons, or `org`/ASN to find related hosts; feed IPs/domains into WHOIS, passive DNS and urlscan.
5. Stay at the observation layer — reading Shodan's data is passive; do not connect to the devices yourself.

## Inputs → Outputs
- **In:** `ip-address`, `domain`/hostname, or `employer-org`/ASN
- **Out:** exposed `ip-address`es, hostnames/`domain`s, open ports & banners, TLS certs, `geolocation`
- **Empty/negative result looks like:** "no results" — Shodan hasn't scanned a matching host, or nothing is exposed; not proof the org has no infrastructure (it may be behind a CDN/firewall).

## Gotchas & OpSec
- Human-in-the-loop: an account is required, and most powerful filters/API are paywalled.
- Data is a snapshot from Shodan's scans — it can be stale; confirm anything decisive.
- OpSec: querying is passive; actually connecting to a discovered device is not — don't cross that line without authorisation.

## Overlaps ("do both")
- Pairs with Censys/ZoomEye (different scan coverage — run both), and with WHOIS, passive DNS, certificate-transparency and urlscan on the IPs/domains it surfaces.

## Trust & verifiability
`trust: trusted` — the reference internet-scan search engine; banners are genuine captured data, with staleness the only real caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shodan |
