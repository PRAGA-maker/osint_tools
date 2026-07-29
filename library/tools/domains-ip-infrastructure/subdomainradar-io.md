---
id: subdomainradar-io
name: SubDomainRadar.io
description: Use when you have a `domain` and want to enumerate its subdomains and exposed hosts across many data sources — returns domain, ip-address.
url: https://subdomainradar.io
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Enumerating a domain's subdomains and attack surface across 50+ data sources.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free account grants 100 points and basic enumerators (no card); paid plans from ~€29.99/mo unlock more sources, scanning, screenshots and full API access.
opsec: passive
opsecNote: The subdomain enumeration draws on passive data sources and won't touch the target. The optional port-scan, vulnerability-scan and screenshot features are active — they send traffic to the target's hosts, so only enable them with authorisation.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Independent commercial recon platform that aggregates 50+ public sources; results are cross-checkable against those upstream sources.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
aliases:
- SubDomainRadar.io
- subdomainradar.io
tags:
- domain-and-ip-research
- subdomains
- recon
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# SubDomainRadar.io

> An all-in-one recon platform that pulls a domain's subdomains from 50+ data sources — a fast way to map the full web footprint tied to a `domain` of interest.

## When to use
You have a `domain` (a subject's business, personal site, or an organisation tied to your case) and want to discover **every host under it** — dev/staging boxes, mail servers, regional sites, forgotten projects. Each subdomain and its resolved IP is a new pivot: more infrastructure, more contact surfaces, more content to search. It aggregates many enumerators at once, so it typically finds more than any single free subdomain tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at https://subdomainradar.io for a free account (100 points, no card).
2. Enter the target `domain` and launch an enumeration task.
3. Review the returned subdomains, their resolved `ip-address`es, and (on paid tiers) ports, tech fingerprints, and screenshots.
4. For automation, use the developer API with your account token to script recon into a pipeline.
5. Pivot: resolved IPs feed `[[bgpview-io]]` for ownership; interesting subdomains feed WHOIS/history and content search; a cluster of hosts on one IP suggests shared ownership.

## Inputs → Outputs
- **In:** `domain`
- **Out:** enumerated sub`domain`s and their `ip-address`es (plus optional ports/tech/screenshots on paid tiers)
- **Empty/negative result looks like:** few or no subdomains beyond `www` — a small footprint, or a domain fully behind a proxy/CDN that masks its hosts (not proof there's nothing there).

## Gotchas & OpSec
- Requires a free **account** (account-login) to run tasks; the free tier's points and basic enumerators cap how much you'll surface.
- Enumeration is passive, but the scanning add-ons are **active** — don't point them at infrastructure you're not authorised to probe.
- Subdomain lists can include stale/dead hosts; confirm each is live before treating it as current.

## Overlaps ("do both")
- Pairs with certificate-transparency and DNS-history tools — run both, since passive-source aggregation and CT logs each surface subdomains the other misses.
- Feeds `[[bgpview-io]]` for the network/owner behind the discovered IPs.

## Trust & verifiability
`trust: community` — a commercial aggregator over public sources; every finding can be re-derived from CT logs, DNS, and the other upstreams it queries, so verify anything critical directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | subdomainradar-io |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
