---
id: openhunting-io
name: OPENHUNTING.IO Threat Library
description: Use when you have a `domain`/`ip-address` or a malware/threat-actor name and want threat-intelligence context — returns associated IOCs, aliases, and infrastructure.
url: https://openhunting.io/threat-library
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Looking up malware families, threat-actor tools, and their indicators of compromise, with a built-in WHOIS lookup.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Public web interface with free access to the threat library and WHOIS lookup; some advanced hunting features and reports may be gated.
opsec: passive
opsecNote: Searching the threat library and running its WHOIS is a lookup against openhunting.io's own dataset, not a direct probe of the target host, so it does not alert an operator. As always, submitting a live domain/IP tells the service what you are investigating — use a sock-puppet account/IP if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent threat-intelligence project (openhunting.io) aggregating malware/tooling IOCs with update timestamps and a public GitHub presence; community-maintained, so coverage and freshness vary by entry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OpenHunting Threat Library
- openhunting.io
tags:
- threat-actor-search
- threat-intel
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# OPENHUNTING.IO Threat Library

> A community threat-intelligence catalog of malware, attacker tooling, and their IOCs — plus a WHOIS lookup — for enriching suspicious infrastructure.

## When to use
You have a suspicious `domain` or `ip-address` (from a phishing message, a scam tied to a case, or a device's network logs), or the name/alias of a malware family or tool (Emotet, Cobalt Strike, Mimikatz, etc.), and you want threat context: known aliases, capabilities (backdoor, keylogger, ransomware, credential theft), and associated indicators. In a missing-persons or fraud investigation this is a secondary/infrastructure tool — useful when a subject's trail runs through malicious infrastructure rather than for people-search directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://openhunting.io/threat-library.
2. Search a threat name/alias, or use the WHOIS lookup for a `domain`/`ip-address`.
3. Read the entry: aliases, capability tags, and IOCs with "last update" timestamps; cross-reference the timestamp to judge freshness.
4. For a domain/IP, note the WHOIS registrant/registrar/dates and any linked infrastructure.
5. Pivot: an IOC domain/IP → passive-DNS and infrastructure-mapping tools; a threat name → vendor threat reports for deeper attribution.

## Inputs → Outputs
- **In:** `domain` / `ip-address` (WHOIS + IOC match) or a malware/tool name
- **Out:** associated IOCs, threat aliases/capabilities, and WHOIS-derived `domain`/`ip-address` infrastructure
- **Empty/negative result looks like:** no matching library entry or an empty WHOIS response — the indicator may simply be uncatalogued here; a miss is not exoneration of the host.

## Gotchas & OpSec
- Human-in-the-loop: none for basic library/WHOIS lookups; some hunting features/reports may be gated.
- Coverage: community-maintained threat data — strong on well-known families, patchy on niche/new indicators; always check the IOC's update timestamp.
- OpSec: passive — you query openhunting.io's dataset, not the target host, so no operator is tipped off by the lookup itself.

## Overlaps ("do both")
- Pairs with passive-DNS, WHOIS-history, and IOC-enrichment tools — OpenHunting gives the threat framing and a quick WHOIS; dedicated infrastructure tools give historical resolutions and pivots the library omits.

## Trust & verifiability
`trust: community` — an independent, community-run threat-intel aggregator with dated IOCs and a public code presence; useful for orientation and corroboration, but confirm any indicator against a second threat-intel source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openhunting-io |
