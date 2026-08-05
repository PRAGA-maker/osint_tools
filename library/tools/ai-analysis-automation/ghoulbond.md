---
id: ghoulbond
name: Ghoulbond
description: Use when you have a `phone`, `username` or `ip-address` and want quick enrichment from one CLI — returns carrier/geo for a number, account presence for a handle, and IP geolocation.
url: https://github.com/hitesh22rana/ghoulbond
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A grab-bag command-line toolkit combining light phone/username/IP OSINT with local system info and a port scanner.
selectorsIn:
- phone
- username
- ip-address
selectorsOut:
- geolocation
- social-profile
- email
status: live
pricing: free
costNote: Free and open-source; Python (pip) with Docker support.
opsec: active
opsecNote: The username-verification and website email-scraping modules query third-party platforms/sites directly, and the port scanner touches targets — run from a sock-puppet/VPN context and only scan hosts you're authorised to. Note it can also read local Wi-Fi passwords, so run it on your own analysis box, not a client's.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small community project (few dozen GitHub stars); handy as a convenience wrapper but its lookups are only as good as the free sources behind them — verify hits elsewhere.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- ghoulbond CLI
tags:
- Tools collections/toolkits
- multi-tool
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Ghoulbond

> An all-in-one Python CLI that bundles small OSINT lookups (phone, username, IP, email scraping) with system diagnostics and a port scanner — a quick-and-dirty utility belt.

## When to use
You want fast, low-effort enrichment on a `phone` (carrier/country/timezone), a `username` (presence across platforms), or an `ip-address` (geolocation) without opening several separate tools — and don't mind that the results are shallow first-pass leads to confirm elsewhere.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/hitesh22rana/ghoulbond && cd ghoulbond && pip install -r requirements.txt` (or use the Docker image).
2. Run `python3 main.py` and pick a module from the menu.
3. Feed the selector: a `phone` for carrier/geo, a `username` for the multi-platform check, an `ip-address` for geolocation, or a URL for email scraping.
4. Pivot the hits — a confirmed handle into deeper username tools, a number into dedicated phone-OSINT, an IP into infrastructure tools.

## Inputs → Outputs
- **In:** `phone`, `username`, or `ip-address`
- **Out:** `geolocation` (number/IP), `social-profile` (username presence), `email` (site scraping)
- **Empty/negative result looks like:** "not found"/no accounts is a weak negative — this tool checks limited sources, so absence here doesn't mean absence everywhere.

## Gotchas & OpSec
- Mixed local/remote features: it also gathers local system data (including saved Wi-Fi passwords), so treat it as an analyst-box tool, not something to run on a subject's or client's machine.
- Active modules (username checks, scraping, port scan) reach out to third parties/targets — use a VPN/sock puppet and stay within authorisation.
- Shallow by design: good for triage, not authoritative.

## Overlaps ("do both")
- Its username check overlaps with Sherlock/Maigret and its phone module with dedicated phone-OSINT tools — use Ghoulbond for a fast look, those for depth and confidence.

## Trust & verifiability
`trust: community` — a small open-source convenience toolkit; inspect the code before running and corroborate every lookup against a stronger, single-purpose tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghoulbond |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | phone, username, ip-address → geolocation, social-profile, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
