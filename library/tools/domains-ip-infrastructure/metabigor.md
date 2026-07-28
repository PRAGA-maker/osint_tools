---
id: metabigor
name: metabigor
description: Use when you have an `employer-org`, ASN, or `ip-address` and want its network footprint with no API keys — returns IP ranges, related domains and org infrastructure.
url: https://github.com/j3ssie/metabigor
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: No-API-key CLI recon on IP ranges, ASNs, organizations and certificates.
selectorsIn:
- ip-address
- domain
- employer-org
selectorsOut:
- ip-address
- domain
- employer-org
status: live
pricing: free
costNote: Free and open-source (Go); no API keys required — it scrapes public sources itself.
opsec: active
opsecNote: metabigor queries public data sources (search engines, ASN/registry data, certificate transparency, and can drive scanners) from your machine — some modes touch third-party services and, if you enable active scanning, the target's infrastructure. Run reconnaissance modes from a VPN/sock-puppet host, and treat any scan-driving mode as active against the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: By j3ssie (author of Osmedeus); a well-known open-source recon tool focused on infrastructure enumeration.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- cdnstrip
aliases:
- j3ssie/metabigor
tags:
- asn
- ip-ranges
- go
- no-api-key
- reconnaissance
source: gh-topic-reconnaissance
lastVerified: '2026-07-28'
enrichment: full
---

# metabigor

> A no-API-key recon CLI: hand it an organization, ASN, or IP and it enumerates the network footprint — IP ranges, related hosts, certificates — by scraping public sources itself.

## When to use
This is **infrastructure** OSINT, low direct relevance to locating a person. Reach for it when a subject is tied to a company or a piece of infrastructure and you want to map that org's network: its ASN(s), owned IP ranges, related domains, and TLS certificates — without paying for or wiring up API keys. It scopes the attack/investigation surface of an organization; it doesn't find individuals.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/j3ssie/metabigor (Go: `go install`, or a release binary).
2. Run the mode you need, e.g. `echo "Target Org" | metabigor net --org` to find IP ranges for an organization, or `metabigor net --asn -a AS12345` to expand an ASN.
3. Use `ip`/`cert`/related modes to pivot from an IP or certificate to associated infrastructure.
4. Read the emitted ranges/hosts; feed them into scanners or WHOIS/reverse-DNS for detail.
5. Pivot: enumerated ranges/domains feed subdomain, port-scan, and certificate tooling.

## Inputs → Outputs
- **In:** `employer-org` name, ASN, or `ip-address`/`domain`
- **Out:** `ip-address` ranges, related `domain`s, and `employer-org` infrastructure mappings
- **Empty/negative result looks like:** no ranges/hosts returned — the org name didn't match registry/ASN data, or a source rate-limited the scrape; try an exact registered name or an ASN directly.

## Gotchas & OpSec
- OpSec: **active** — recon modes hit third-party sources from your IP, and any scan-driving mode hits the target directly; use a VPN/sock-puppet and know which mode you're running.
- No-API-key means it scrapes, so results depend on source availability and can be rate-limited or incomplete.
- It's an org/infra tool — don't expect person-level selectors from it.

## Overlaps ("do both")
- Pairs with `[[cdnstrip]]` and subdomain/cert tooling: metabigor gives the org's ranges and ASNs, while those resolve the individual hosts, real IPs behind CDNs, and subdomains within them.

## Trust & verifiability
`trust: community` — a mature open-source tool from a known recon author. It reports what public sources return, so cross-check critical ranges against authoritative registry (RIR) and ASN data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metabigor |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain, employer-org → ip-address, domain, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
