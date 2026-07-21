---
id: doteasy-canada
name: Doteasy (Canada)
description: Use when a WHOIS record names Doteasy as the registrar/host of a `domain` and you want context on this Canadian provider — background on the registrar, not a lookup engine.
url: http://www.doteasy.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Understanding Doteasy as a registrar/host when its name appears in a domain's WHOIS.
selectorsIn:
- domain
selectorsOut:
- employer-org
status: live
pricing: freemium
costNote: Domain registration and hosting are paid services; the site itself is free to browse but is a vendor, not a free lookup tool.
opsec: passive
opsecNote: Reading a registrar's public site is passive. Note that Doteasy historically offered privacy/proxy registration, so WHOIS behind it may mask the true registrant.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial Canadian domain registrar and web host, not an investigative tool; relevant only as the entity behind some WHOIS records.
missingPersonsRelevance: low
coverage:
- ca
- global
auth: none
api: false
localInstall: false
registration: true
aliases:
- Doteasy
- doteasy.com
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- registrar
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Doteasy (Canada)

> A Canadian domain registrar and web host — not a lookup engine, but the provider you'll sometimes see named in a domain's WHOIS, and the party to understand when it appears.

## When to use
Low-priority context. Doteasy is a registrar/hosting company, so it comes up in an investigation only when a target `domain` is registered or hosted through it. Knowing this tells you where to direct a preservation/lawful request, and warns you that a domain behind Doteasy may use its privacy/proxy service, hiding the true registrant. It is not a tool you query for a subject — treat it as reference on the registrar itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Run WHOIS/RDAP on the target `domain` in a dedicated WHOIS tool.
2. If the registrar or nameservers point to Doteasy, note it.
3. Visit http://www.doteasy.com only for provider context (abuse contact, services, whether privacy registration is offered).
4. Recognize that a Doteasy-privacy-protected record hides the registrant — pivot to historical WHOIS, site content, or mail/DNS records instead.
5. Pivot: registrar/abuse contact for formal process; site artifacts for identity leads.

## Inputs → Outputs
- **In:** a `domain` whose WHOIS/hosting references Doteasy
- **Out:** context on the registrar `employer-org` (services, abuse contact) — not registrant data
- **Empty/negative result looks like:** nothing about your subject here — this is a vendor site, so expect company info only, never a per-person lookup.

## Gotchas & OpSec
- **Not an OSINT lookup:** it's a registrar's homepage; the investigative data lives in WHOIS/RDAP, not here.
- Privacy/proxy registration through Doteasy can mask the real registrant — plan to pivot to historical WHOIS and site content.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with a real WHOIS/RDAP tool and historical-WHOIS services — those identify the registrar and any exposed registrant; this only explains the registrar.

## Trust & verifiability
`trust: community` — a legitimate commercial registrar/host; useful as context, but it holds no queryable investigative data itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | doteasy-canada |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
