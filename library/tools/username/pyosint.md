---
id: pyosint
name: Pyosint
description: Use when you have a `username` (or a `domain`) and want a CLI that enumerates accounts across ~326 sites plus scrapes links and subdomains — returns `social-profile` URLs and `domain` leads.
url: https://github.com/d8rkmind/Pyosint
category: username
path:
- username
bestFor: Command-line username enumeration across ~326 sites, plus link scraping and subdomain discovery.
selectorsIn:
- username
- domain
selectorsOut:
- social-profile
- username
- domain
status: live
pricing: free
costNote: Free and open source (Python 3); clone the repo and install requirements with pip. No account or keys for the core Find module.
opsec: active
opsecNote: The Find module directly requests a profile URL on each of ~326 sites to test a username (like Sherlock), and Enum queries third-party services (VirusTotal, PassiveDNS, crt.sh, ThreatCrowd) — both touch external services, not the subject. Threaded runs are noisy; route through a proxy/VPN for sensitive work and expect rate-limiting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A small community Python tool (fork of the syamsv/Pyosint project); functional but not widely audited — expect some site adapters to be stale.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Pyosint
tags:
- Nicknames
- username
- enumeration
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- profounder
---

# Pyosint

> A three-in-one Python CLI: enumerate a username across ~326 sites (Find), scrape links from a page (Scrap), and discover subdomains of a domain (Enum).

## When to use
You have a `username` and want another enumerator to widen coverage beyond Sherlock/OSRFramework, or you have a `domain` and want quick subdomain discovery from passive-DNS/cert sources. The Find module turns a handle into a spread of `social-profile` URLs; Enum turns a domain into subdomains; Scrap harvests outbound links from a target page. A useful supplementary tool in a username-tracing kit.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `github.com/d8rkmind/Pyosint`, install deps (`pip install -r requirements.txt`).
2. Run `python3 pyosint.py` and choose a module:
   - **Find** — enumerate a `username` across ~326 sites (threaded); results saved to an output folder.
   - **Scrap** — extract all links from a given website.
   - **Enum** — discover subdomains of a `domain` via VirusTotal, PassiveDNS, crt.sh, ThreatCrowd.
3. For sensitive work, run behind a proxy/VPN.
4. Read the output folder; open each found `social-profile` to confirm it's your subject.
5. Pivot: cross-check hits with `[[sherlock]]` / `[[namechk]]`; feed subdomains into web recon.

## Inputs → Outputs
- **In:** `username` (Find) or `domain` (Enum); a URL (Scrap)
- **Out:** `social-profile`/`username` hits, extracted links, `domain` subdomains
- **Empty/negative result looks like:** empty output folder or all-not-found — the handle is unused, adapters are stale, or a provider (VirusTotal etc.) rate-limited you. Confirm with a second enumerator before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: none to run; you must manually verify each profile hit (handle reuse ≠ same person).
- OpSec: **active** — Find probes 326 sites and Enum hits third-party APIs. Use a proxy/VPN; expect rate-limits.
- Small, lightly-audited project: adapters bit-rot; treat negatives cautiously and keep it updated.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`, `[[namechk]]`, and `[[osrframework-jaykali-fork]]` — each enumerator covers a different site set; running several catches what any one misses.

## Trust & verifiability
`trust: community` — a functional but niche community tool. Verify every hit on the live profile; assume some site checks are outdated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pyosint |
| category | username |
| selectorsIn → selectorsOut | username, domain → social-profile, username, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
