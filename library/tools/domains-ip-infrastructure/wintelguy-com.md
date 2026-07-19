---
id: wintelguy-com
name: wintelguy.com
description: Use when you have a `mac-address` or email headers and want free network utilities — returns MAC/WWN vendor, subnet math, and mail-trace decoding.
url: https://wintelguy.com/index.pl
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A free grab-bag of network/IT calculators — MAC/WWN vendor lookup, subnet calculator, and email header mail-trace.
selectorsIn:
- mac-address
- ip-address
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Entirely free browser tools; donation links only, no account or paywall.
opsec: passive
opsecNote: Calculations run against reference tables (e.g. IEEE OUI for MAC vendors) client/server-side; you are not touching the target's infrastructure. Note that data you paste (MAC, headers) is submitted to wintelguy's server — avoid pasting genuinely sensitive material.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running personal IT-tools site; the calculators are accurate and widely used, but it is an individual's hobby site, not an authoritative registry.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- WintelGuy tools
- wintelguy MAC lookup
tags:
- domainsandips
- Domains & IPs
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# wintelguy.com

> A free collection of network/IT calculators — most useful in OSINT for resolving a MAC/WWN to its hardware vendor and for subnet/mail-trace math.

## When to use
You have a `mac-address` (from device logs, a DHCP lease, a captured packet) and want to identify the hardware manufacturer via its OUI prefix; or you have an `ip-address`/CIDR block and need quick subnet math; or you have raw email headers and want a mail-trace decode of the hop path. It's a utility belt, not an investigative database — reach for it mid-analysis when you need to interpret a technical artifact.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wintelguy.com/ and pick the tool: "MAC/WWN lookup," "Subnet calculator," or "Mail trace."
2. Paste the artifact (MAC address, IP/CIDR, or email headers).
3. Read the output: MAC → registered `employer-org`/vendor (IEEE OUI); IP/CIDR → network/broadcast/range; headers → ordered relay hops and originating IPs.
4. Pivot: a MAC vendor narrows the device type; a mail-trace originating IP feeds IP-geolocation and reverse-DNS tools.

## Inputs → Outputs
- **In:** `mac-address`, `ip-address`/CIDR, or email headers
- **Out:** hardware vendor (`employer-org`), subnet ranges, mail relay path/originating IPs
- **Empty/negative result looks like:** MAC prefix not in the OUI table (unregistered/locally-administered address), or a malformed input — means "no vendor," not a match.

## Gotchas & OpSec
- MAC vendor lookup is only as current as its OUI dataset; randomized/locally-administered MACs (privacy MACs on modern phones) return no meaningful vendor.
- These are convenience calculators; for authoritative OUI data cross-check the IEEE registry.
- OpSec: passive; nothing you do reaches the target.

## Overlaps ("do both")
- Complements dedicated IP-geolocation and email-header analyzers — use wintelguy for a quick decode, a specialized tool when you need depth on the resulting IP.

## Trust & verifiability
`trust: community` — an established personal tools site with accurate, widely-used calculators; fine for interpretation, but verify vendor/registry facts against primary sources for anything that matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wintelguy-com |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | mac-address, ip-address → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
