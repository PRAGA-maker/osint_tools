---
id: gobuster
name: Gobuster
description: Use when you have a `domain` and want to brute-force its subdomains/paths/vhosts — returns discovered subdomains, directories and virtual hosts.
url: https://github.com/OJ/gobuster
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Fast wordlist brute-forcing of DNS subdomains, web directories/files, and virtual hosts to expand a target domain's attack/recon surface.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (Apache-2.0).
opsec: active
opsecNote: DNS mode is relatively quiet (resolver queries), but dir/vhost modes send many requests directly to the target web server and WILL appear in its logs as brute-force traffic. Only run against systems you are authorised to test; use attributable-safe infrastructure and throttle.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: A very widely-used, actively-maintained Go tool (14k+ stars); code is open and auditable. Results are only as good as your wordlist.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- OJ/gobuster
tags:
- Domain/IP/Links
- subdomain-enumeration
- brute-force
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Gobuster

> A fast Go CLI for brute-forcing DNS subdomains, web directories/files and virtual hosts from a wordlist — a staple recon tool.

## When to use
You have a `domain` and want to discover what isn't linked or listed: hidden subdomains (`dev.`, `vpn.`, `staging.`), unlinked directories/files, or virtual hosts sharing an IP. Gobuster expands the surface you can then investigate with passive tools. This is offensive-leaning recon, adjacent to infrastructure OSINT.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/OJ/gobuster/v3@latest` (or Docker).
2. Pick a mode: `dns` (subdomains), `dir` (directories/files), `vhost` (virtual hosts), plus S3/GCS/TFTP.
3. Run with a target and wordlist — e.g. `gobuster dns -d example.com -w subdomains.txt` or `gobuster dir -u https://example.com -w words.txt`.
4. Read discovered names/paths with their status codes; validate live hits before relying on them.
5. Pivot: discovered subdomains feed passive DNS, WHOIS, certificate-transparency and urlscan (which are non-intrusive).

## Inputs → Outputs
- **In:** target `domain` (+ wordlist)
- **Out:** discovered sub`domain`s, directories/files, or virtual hosts
- **Empty/negative result looks like:** nothing found — usually a weak/short wordlist or wildcard DNS masking results, not proof nothing exists; try a better wordlist and handle wildcards.

## Gotchas & OpSec
- **Active (esp. dir/vhost):** noisy, logged brute-force traffic against the target — authorised targets only, and throttle.
- Wildcard DNS produces false positives in `dns` mode; use its wildcard handling.
- Coverage is entirely wordlist-dependent — prefer curated lists (SecLists).

## Overlaps ("do both")
- Pairs with passive subdomain sources (crt.sh, Amass passive, certificate transparency) — do the passive collection first, then use Gobuster to brute-force the gaps.

## Trust & verifiability
`trust: trusted` — mature, auditable, widely-used tooling; every hit is directly verifiable by resolving/requesting it yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gobuster |
