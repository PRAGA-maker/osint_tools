---
id: snoop-2
name: snoop
description: Use when you have a `username` and want to enumerate accounts across thousands of sites (with strong Russian/Cyrillic-segment coverage) — returns `social-profile` links.
url: https://github.com/snooppr/snoop
category: username
path:
- username
bestFor: Bulk username enumeration across 5000+ sites, including RU-segment platforms that Sherlock/Maigret miss.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (GPL). No account or API key. Optional plugins for geolocation/IP mapping are also free.
opsec: passive
opsecNote: snoop queries each target site directly from your machine, so your IP hits thousands of platforms in a burst — run it behind a VPN/proxy or Tor, and never from an attributable network. It does not authenticate to sites, so it leaves no logged-in trace, but the request pattern is noisy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source project on GitHub (Russian maintainers); popular in the RU OSINT community. Verify you cloned the genuine snooppr/snoop repo before running.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- snoop project
- snooppr/snoop
tags:
- username-enumeration
- cli
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# snoop

> A Sherlock/Maigret-class username hunter with an unusually large site list (5000+) and deep Russian-segment coverage — run from the command line, no accounts needed.

## When to use
You have a `username`/nickname and want to find every platform where it exists, especially when the subject is likely active on RU-segment or CIS platforms (VK-adjacent forums, Russian services) that Western-focused enumerators under-cover. Best as a wide first sweep to generate a list of candidate profiles to triage.

## How to use it (`bestInteractionPattern`: cli)
1. Get the tool: download a prebuilt release binary (Windows/Linux, no dependencies) or clone the source — `git clone https://github.com/snooppr/snoop` — and install Python 3.7+ requirements.
2. Route your traffic through a VPN/proxy/Tor first.
3. Run against a username: e.g. `python snoop.py "ivan_petrov"` (quote names with spaces), or `snoop_cli.bin ivan_petrov` for the release binary.
4. Use flags to scope: `--web-base` for the expanded site database, `--exclude ru` to drop a segment, and report options for CSV/TXT/HTML output grouped by country/alphabet.
5. Triage the hit list — each reported URL is a *candidate*; open and confirm it's the same person. Pivot confirmed profiles into content/photo analysis.

## Inputs → Outputs
- **In:** `username` (one or several)
- **Out:** `social-profile` URLs where the username resolves, exported as CSV/TXT/HTML reports
- **Empty/negative result looks like:** few or no hits — common for very short/common usernames (false positives) or highly unique ones (genuinely absent). As with all enumerators, expect both false positives (parked/placeholder pages) and false negatives (sites that block automated checks); verify each hit manually.

## Gotchas & OpSec
- Noisy: thousands of outbound requests in a short window — always proxy/VPN, never from your own IP.
- Site checks go stale; some "found"/"not found" verdicts are wrong when a platform changes its profile-URL scheme. Confirm manually.
- Confirm repo authenticity (`snooppr/snoop`) before executing — running arbitrary OSINT code has its own supply-chain risk.

## Overlaps ("do both")
- Run alongside `[[sherlock]]` and `[[maigret]]` — snoop's larger and RU-heavy site list catches accounts they miss, while they catch Western sites snoop may lag on. Union the results, then dedupe.

## Trust & verifiability
`trust: community` — open-source and inspectable, but coverage/accuracy depend on volunteer-maintained site definitions; treat every hit as a lead to verify, not a confirmed account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snoop-2 |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
