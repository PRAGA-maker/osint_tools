---
id: internetdb-shodan-io
name: Internetdb.shodan.io
description: Use when you have an `ip-address` and want Shodan's fast free snapshot — returns open ports, hostnames (`domain`), software CPEs, tags, and known CVEs, no API key.
url: https://internetdb.shodan.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A free, keyless, one-request lookup of an IP's open ports, hostnames, and known vulnerabilities.
selectorsIn:
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free for non-commercial use with no Shodan account or API key; commercial use requires a Shodan enterprise license. Data refreshes roughly weekly.
opsec: passive
opsecNote: "InternetDB returns Shodan's pre-collected scan data, so your query never touches the target host — fully passive. You hit Shodan's endpoint (e.g. `curl https://internetdb.shodan.io/1.2.3.4`), which Shodan logs against your IP; use a proxy/sock-puppet if you don't want the lookup attributed."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: Operated by Shodan, the established internet-scan provider; data is authoritative for what Shodan last observed but lags real time (weekly cadence) and is a minimal subset (no banners).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- shodan
aliases:
- Shodan InternetDB
- internetdb
tags:
- shodan
- ip-recon
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Internetdb.shodan.io

> Shodan's free, keyless "fast IP lookup": one GET request returns an IP's open ports, hostnames, software CPEs, tags, and known CVEs — no account required.

## When to use
You have an `ip-address` tied to a subject or their infrastructure and want a quick, free read on what's exposed there — open ports, resolved hostnames (`domain`), the software fingerprints (CPEs), and any CVEs Shodan associates — without a Shodan subscription. Ideal for scripting a first-pass triage over many IPs. Infrastructure-focused, so low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: api)
1. Query directly: `curl https://internetdb.shodan.io/<IP>` (or open the URL with the IP appended in a browser).
2. Read the JSON: `ports`, `hostnames` (`domain`s), `cpes` (software), `tags` (e.g. `vpn`, `cloud`), and `vulns` (CVE IDs).
3. Script it over a list of IPs for bulk triage (no key, generous for non-commercial use).
4. Pivot: a hostname into passive-DNS/WHOIS, an open port/CVE into deeper investigation, or the same IP into full Shodan for banners.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** open `ports`, `hostnames` (`domain`), software `cpes`, `tags`, known `vulns` (CVEs)
- **Empty/negative result looks like:** `404`/empty for that IP — Shodan has no recent scan of it (not publicly reachable, or not yet scanned); it is **not** proof the host has nothing open right now.

## Gotchas & OpSec
- Data is a weekly-ish snapshot and minimal (no service banners) — for live/detailed data use full Shodan.
- A listed CVE is inferred from the software version, not confirmed exploitable; treat as a lead.
- Non-commercial only under the free terms; commercial use needs an enterprise license.

## Overlaps ("do both")
- The lightweight front door to [[shodan]] — use InternetDB for fast free triage, then pivot the interesting IPs into full Shodan for banners/history and into [[ipinfo-map]] for geolocation.

## Trust & verifiability
`trust: trusted` — first-party Shodan data, authoritative for what was last scanned; the caveats are freshness (weekly) and minimalism (no banners), so confirm anything time-sensitive against live Shodan.
