---
id: ibm-x-force-exchange-current-malicious-activity
name: IBM X-Force Exchange Current Malicious Activity
description: Use when you want a live map of current malicious activity and a jump-off point to look up specific IPs/domains/hashes in X-Force's intel — returns aggregate activity plus (via the platform) per-indicator reputation.
url: https://exchange.xforce.ibmcloud.com/activity/map
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Situational-awareness map of current threats, backed by IBM X-Force Exchange's searchable threat-intel.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: freemium
costNote: The activity map is viewable free; searching indicators and accessing full X-Force Exchange intel needs a free IBMid registration, with paid enterprise tiers for API/volume.
opsec: passive
opsecNote: Passive — you query IBM's threat database, not the subject's host. Indicator lookups are tied to your IBMid account; use a research identity for sensitive work.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by IBM Security (X-Force); a mainstream, curated threat-intelligence platform.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- ibm-x-force-exchange
aliases:
- X-Force Exchange activity map
tags:
- live-cyber-threat-maps
- threat-intel
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# IBM X-Force Exchange Current Malicious Activity

> IBM X-Force's live "current malicious activity" map — a situational dashboard that fronts the searchable X-Force Exchange threat-intelligence platform.

## When to use
You want a quick read on current global threat activity, and — more usefully — a doorway into IBM X-Force Exchange to look up the reputation and history of a specific `ip-address`, `domain`, URL or file hash tied to your investigation (e.g. an IP from a header/log, or a suspicious domain). The map itself is context; the value for a case is the underlying indicator search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://exchange.xforce.ibmcloud.com/activity/map for the live activity view.
2. To investigate a specific indicator, sign in with a free IBMid (the human-in-the-loop gate) and search the IP/domain/URL/hash in X-Force Exchange.
3. Read the report: risk score, categorisation, associated malware/campaigns, passive DNS and history.
4. For automation/volume, use the X-Force Exchange API (enterprise tiers apply).
5. Pivot: an IP's categorisation/passive-DNS feeds infrastructure mapping; a flagged domain corroborates a scam/phishing lead.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, URL, or file hash (via the platform search)
- **Out:** `ip-address`/`domain` reputation, risk score, categorisation, passive DNS and threat history
- **Empty/negative result looks like:** an indicator with no adverse reporting / neutral risk score — meaning "not seen as malicious," not "does not exist."

## Gotchas & OpSec
- Human-in-the-loop: the live map is open, but indicator lookups require a free IBMid login (`account-login`).
- OpSec: passive — you query IBM's database, not the target; lookups tie to your account.
- The `/activity/map` view alone is just a visualisation; the investigative payoff is the searchable exchange behind it.

## Overlaps ("do both")
- Use with the broader `[[ibm-x-force-exchange]]` entry and other reputation sources (VirusTotal-style tools) — cross-checking an indicator across independent intel reduces single-vendor blind spots.

## Trust & verifiability
`trust: trusted` — IBM X-Force is a mainstream, curated intel provider; scores are opinion/telemetry-based, so corroborate a critical verdict with a second source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ibm-x-force-exchange-current-malicious-activity |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
