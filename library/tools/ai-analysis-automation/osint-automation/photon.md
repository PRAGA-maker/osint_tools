---
id: photon
name: Photon
description: Use when you have a `domain`/URL and want to crawl it fast for emails, social links, files, subdomains, and keys — returns harvested `email`s, `social-profile`s, and endpoints.
url: https://github.com/s0md3v/Photon
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: Fast recon crawl of a website to extract emails, social accounts, files, endpoints, and secrets.
selectorsIn:
- domain
selectorsOut:
- email
- social-profile
- domain
status: live
pricing: free
costNote: Free and open-source (s0md3v/Photon, GPL); install and run locally.
opsec: active
opsecNote: Crawling a live site is ACTIVE — Photon fetches many pages fast and is easily seen in the target's server logs (and can trip WAF/rate limits). Only crawl sites you're authorised to, throttle with delays, and route through a VPN/sock-puppet. To stay passive, point it at the Wayback Machine instead of the live host.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A popular open-source crawler by s0md3v (author of many well-known security tools); code is auditable, results depend on what the target exposes.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- orbit
- striker
- theharvester
- zen
- zen-github-com
aliases:
- Photon crawler
- s0md3v Photon
tags:
- web-crawler
- recon
- osint-automation
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Photon

> A fast, scriptable OSINT web crawler — point it at a site and it harvests the emails, social links, files, subdomains, and secrets scattered across its pages.

## When to use
You have a `domain`/URL and want to mine everything it leaks: contact `email`s, linked `social-profile`s, document/file URLs, in-scope subdomains and endpoints, and accidentally-exposed API keys. Photon crawls quickly, categorises what it finds into folders, and can pull from the Wayback Machine so you can enumerate a site's historical URLs without touching it live.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/s0md3v/Photon && cd Photon && pip install -r requirements.txt`.
2. Basic crawl: `python photon.py -u https://target.tld -l 2 -t 10` (`-l` depth, `-t` threads). Add `--wayback` to seed URLs from archives (passive), `-d N` to delay/throttle.
3. Photon writes organised output (urls, emails, social accounts, files, external links, intel like keys/DNS) to a results folder.
4. Review the harvested selectors and prioritise leads (a contact `email` → email-OSINT; a `social-profile` → username-search).
5. Pivot: feed emails into breach lookups, social links into profile enrichment, and subdomains into infra tools.

## Inputs → Outputs
- **In:** `domain`/URL (optionally Wayback-seeded)
- **Out:** harvested `email`s, `social-profile` links, file URLs, subdomains/endpoints, exposed keys
- **Empty/negative result looks like:** near-empty output folders — the site is small/static, blocks crawling, or exposes nothing; try more depth or the Wayback mode.

## Gotchas & OpSec
- **Active and loud** against a live host — highly detectable and potentially disruptive. Crawl only with authorisation; throttle and proxy. Use `--wayback` for a passive alternative.
- Respect scope: aggressive depth can wander off-target or hammer a server.
- Exposed keys/secrets it surfaces are sensitive — handle responsibly and don't act beyond your authority.

## Overlaps ("do both")
- Pairs with `[[theharvester]]` (emails/subdomains from search engines/passive sources — no crawling) and `[[striker]]`/`[[orbit]]` — use passive tools first, then Photon for a deep on-site crawl when you're cleared to.

## Trust & verifiability
`trust: community` — a widely-used open-source crawler; the code is auditable, and it only reports what the target site actually exposes (verify surfaced secrets/links before acting).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | photon |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → email, social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
