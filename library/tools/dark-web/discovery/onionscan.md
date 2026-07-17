---
id: onionscan
name: OnionScan
description: Use when you have a `domain` (.onion hidden service) and want to find operational-security leaks that can deanonymise or correlate it — returns exposed metadata, misconfigurations, and correlation indicators.
url: https://github.com/s-rah/onionscan
category: dark-web
path:
- dark-web
- discovery
bestFor: Scanning a Tor hidden service for metadata leaks and misconfigurations that link it to a real identity or to other sites.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
- crypto-wallet
- metadata-exif
status: degraded
pricing: free
costNote: Free and open source; run locally. Note the project is effectively unmaintained (last release 0.2, October 2016) — it still runs but won't detect newer service software or leak patterns.
opsec: active
opsecNote: This directly probes the target hidden service over Tor. The operator can see the requests in their logs, and aggressive scanning may tip them off. Route through Tor, throttle, and treat scanning of a live adversary's service as an active, potentially attributable action.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A well-known, widely-cited open-source dark-web OSINT tool (by s-rah); reliable for what it checks, but unmaintained since 2016, so pair it with current tooling and interpret findings yourself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- onioff
- torbot
- hunchly-hidden-services-report
aliases:
- OnionScan
- s-rah/onionscan
tags:
- dark-web
- hidden-service
- opsec-analysis
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# OnionScan

> The classic Tor hidden-service auditor: point it at a `.onion` and it hunts the operator's own OpSec mistakes — leaked metadata, misconfigurations, and fingerprints that correlate the site to a real identity or to other services.

## When to use
You have a `.onion` `domain` — a market, forum, leak site, or a service tied to your subject — and you want the deanonymisation angle. OnionScan checks for the human errors that break anonymity: exposed server-status pages, leaked real IPs, EXIF-laden images, reused SSH/SSL keys, Bitcoin addresses, and Apache/mod_status or open directories. Those artefacts can link a hidden service to a clearnet site, a wallet, or a shared operator across multiple onions.

## How to use it (`bestInteractionPattern`: cli)
1. Install: build from `github.com/s-rah/onionscan` (Go) and ensure a Tor SOCKS proxy is running locally.
2. Run a scan: `onionscan --verbose <address>.onion`, or `onionscan --jsonReport <address>.onion` for machine-readable output.
3. Read the findings: leaked IPs/status pages, EXIF in served images, SSH/SSL key fingerprints, Bitcoin addresses, open directories, and analytics IDs.
4. Correlate: match reused keys, wallets, or analytics IDs across other onions/clearnet sites to cluster operator infrastructure.
5. Pivot: a leaked IP feeds infrastructure/geolocation tools; an EXIF `metadata-exif` GPS feeds mapping; a `crypto-wallet` feeds blockchain analysis.

## Inputs → Outputs
- **In:** `domain` (a `.onion` hidden service)
- **Out:** OpSec-leak indicators — leaked `ip-address`, `metadata-exif` from served images, `crypto-wallet` addresses, reused key fingerprints, open directories, and cross-site correlation fingerprints
- **Empty/negative result looks like:** a clean scan with no leaks — the operator has good OpSec (or the tool's 2016-era checks don't cover their stack); not proof of anonymity, just no low-hanging fruit found.

## Gotchas & OpSec
- Unmaintained (2016): it won't understand newer server software or newer leak vectors — a clean result may be a blind spot, not real safety. Combine with current tools and manual review.
- Active probing: your scan hits the target's logs; on a live adversary's service this is attributable — throttle and use Tor.
- Interpretation required: correlations (shared keys/wallets) are hypotheses to confirm, not automatic identity.

## Overlaps ("do both")
- Pairs with `[[onioff]]` (onion availability/triage), `[[torbot]]` (crawling/OSINT of onions), and `[[hunchly-hidden-services-report]]` — use crawlers to discover and OnionScan to audit each service's OpSec, then correlate leaks across them.

## Trust & verifiability
`trust: community` — a respected, widely-referenced open-source tool whose checks are sound but frozen in 2016; its concrete findings (a leaked IP, an EXIF GPS) are verifiable and strong, while a clean report should not be over-read given its age.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onionscan |
| category | dark-web |
| selectorsIn → selectorsOut | domain → domain, ip-address, crypto-wallet, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
