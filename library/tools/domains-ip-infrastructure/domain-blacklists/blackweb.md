---
id: blackweb
name: Blackweb
description: Use when you have a `domain` and want to check it against a massive aggregated blocklist (malware, trackers, porn, warez, etc.) — returns whether it appears among ~5.8M flagged domains.
url: https://github.com/maravento/blackweb
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- domain-blacklists
bestFor: Reputation-checking a domain against a huge consolidated blocklist, or bulk-screening many domains offline.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (GPL-3.0 for scripts). The full `blackweb.txt` is ~5.8M domains / ~140 MB — a large download.
opsec: passive
opsecNote: Fully offline once downloaded — you grep a local file, so no query about the domain leaves your machine and nothing tips off the domain owner. Ideal for OpSec-sensitive reputation checks.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A well-maintained aggregator (hundreds of GitHub stars) that consolidates public blocklists but does NOT independently verify domains — treat a hit as "listed by some source," not proven-malicious.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- blackweb.txt
- maravento blackweb
tags:
- domain-blacklist
- reputation
- malware
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Blackweb

> A consolidated ~5.8-million-domain blocklist (malware, trackers, adult, warez, and more) built for Squid — handy as an offline reputation check for a domain or a bulk screen of many.

## When to use
You have a `domain` (or a list of them) tied to a subject's infrastructure, an email, or a link, and want a quick offline reputation signal: does it appear on any of the many public blocklists Blackweb aggregates? Useful for flagging suspicious hosts and for bulk-screening domains without pinging any online service.

## How to use it (`bestInteractionPattern`: cli)
1. Download `blackweb.txt` from https://github.com/maravento/blackweb (large file, ~140 MB).
2. Check a single domain offline: `grep -F "example.com" blackweb.txt`.
3. For bulk screening, loop your domain list against the file (or load it into your Squid proxy as intended).
4. Treat a match as a flag to investigate the category (malware/tracker/etc.), not as proof — pivot to a live reputation tool for confirmation.

## Inputs → Outputs
- **In:** `domain` (single or list)
- **Out:** `domain` (listed / not-listed against the blocklist)
- **Empty/negative result looks like:** no match means the domain isn't on the aggregated lists — that's weak evidence of good standing, not a clean bill of health (new/obscure malicious domains won't be listed yet).

## Gotchas & OpSec
- It does not verify domains itself — it only reformats public blocklists, so both false positives and gaps exist.
- Huge file: intended for Squid; the maintainers warn against loading it into Pi-hole/DNSMasq for performance reasons. For ad-hoc checks, grep is fine.
- A listing spans many categories (porn, warez, social) beyond malware — check why a domain is listed before drawing conclusions.

## Overlaps ("do both")
- Pair with live domain-reputation/threat-intel lookups (VirusTotal-class): Blackweb gives an instant offline flag, the live services give current, verified verdicts.

## Trust & verifiability
`trust: community` — a reputable open-source aggregator; reliable as a first-pass offline filter, but every hit needs confirmation from a source that actually verifies maliciousness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blackweb |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
