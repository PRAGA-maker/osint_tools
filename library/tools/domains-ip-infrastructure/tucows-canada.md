---
id: tucows-canada
name: Tucows
description: Use when a domain in your investigation is registered via Tucows/OpenSRS — context on the world's 2nd-largest registrar; the corporate site itself is not a lookup tool.
url: https://www.tucows.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Understanding the registrar (Tucows/OpenSRS/Hover) behind a domain you found in WHOIS; not a domain-lookup service itself.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: The corporate site is informational; domain registration is a paid service via Tucows Domains/OpenSRS/Hover.
opsec: passive
opsecNote: Passive — reading Tucows' corporate/informational pages transmits nothing about a target. Actual WHOIS lookups happen in a WHOIS tool, not here; and WHOIS queries themselves are logged by the registry.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Tucows is a major, publicly traded internet company and the world's second-largest domain registrar; authoritative as a registrar, but tucows.com is a corporate portal, not an OSINT lookup.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OpenSRS
- Hover
- Tucows Domains
tags:
- toddington
- registrar
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Tucows

> The world's second-largest domain registrar (OpenSRS/Hover) — context for a WHOIS "registrar: Tucows" line, not a lookup tool in itself.

## When to use
A domain in your investigation shows Tucows / OpenSRS / Hover as its registrar in WHOIS, and you want to understand who that is and how to route abuse/legal requests. The tucows.com site is a corporate portal — it does not let you search domains or people; use it for registrar context only.

## How to use it (`bestInteractionPattern`: web-manual)
1. Run WHOIS on the target `domain` in a dedicated WHOIS tool first.
2. If the registrar is Tucows/OpenSRS/Hover, open https://www.tucows.com for corporate/abuse-contact context (registration itself lives at Tucows Domains/OpenSRS/Hover).
3. Read the output: registrar background and contact/abuse routing — not domain records.
4. Pivot: submit abuse/legal requests through the correct registrar channel; do actual domain intel in WHOIS/DNS tools.

## Inputs → Outputs
- **In:** a `domain` whose registrar is Tucows (learned from WHOIS)
- **Out:** registrar context/abuse-contact routing (no domain database here)
- **Empty/negative result looks like:** N/A — it's informational; there is nothing to "search" for a person or domain on the corporate site.

## Gotchas & OpSec
- **Not a lookup tool** — do domain/WHOIS intel in a WHOIS service; this is registrar background only.
- Registration is via Tucows Domains/OpenSRS/Hover, not tucows.com.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Pairs with any WHOIS/DNS tool — those identify Tucows as the registrar; this explains who they are and how to escalate.

## Trust & verifiability
`trust: trusted` — established registrar; authoritative as a company, but contributes only context, not evidentiary domain/person data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tucows-canada |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
