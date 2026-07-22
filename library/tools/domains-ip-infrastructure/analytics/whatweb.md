---
id: whatweb
name: WhatWeb
description: Use when you have a `domain`/URL and want to fingerprint its stack (CMS, server, JS libraries, versions) and surface disclosed emails — returns detected technologies and `email` addresses.
url: https://github.com/urbanadventurer/WhatWeb
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- analytics
bestFor: Identifying what a website is built on (CMS, framework, server, analytics IDs) and pulling emails/versions from a single scan.
selectorsIn:
- domain
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free and open-source (Ruby); install locally, no account.
opsec: active
opsecNote: WhatWeb connects directly to the target's web server; at higher aggression levels (-a 3/4) it makes extra requests that appear in the target's logs. Use aggression 1 (passive/stealthy) and route through a VPN/sock-puppet exit when you don't want to be attributed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely-used open-source project (urbanadventurer, 6.7k+ stars, actively released); results are as reliable as its 1,800+ plugins, occasionally false-positive on versions.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- whatweb
tags:
- web-fingerprinting
- recon
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# WhatWeb

> An open-source web-technology fingerprinter — used in OSINT to profile a subject's website or infrastructure and extract identifiers (tech stack, versions, analytics IDs, emails).

## When to use
You have a `domain`/URL tied to a subject (personal site, small business, blog) and want to know what it's built on and what identifiers it leaks. WhatWeb detects CMS/platform, web server, JS libraries, analytics/tracking IDs and email addresses — the analytics ID especially is a strong pivot to find other sites owned by the same person.

## How to use it (`bestInteractionPattern`: cli)
1. Install (`gem install whatweb`, `apt install whatweb`, or clone the repo — it ships with Kali).
2. Run stealthy first: `whatweb -a 1 example.com` (single passive request).
3. Read the output: detected technologies, versions, HTTP headers, and any emails/analytics IDs. Add `--log-json=out.json` for structured output.
4. Pivot: feed an analytics/AdSense ID into a reverse-analytics tool (e.g. to cluster co-owned domains) and emails into email-OSINT.

## Inputs → Outputs
- **In:** `domain` / URL (single, list, or CIDR)
- **Out:** technology fingerprint, versions, headers, analytics IDs, `email` addresses
- **Empty/negative result looks like:** minimal fingerprint (generic server only) — common for CDN-fronted or static sites; the CDN may be masking the origin stack.

## Gotchas & OpSec
- **Active tool** — even a light scan hits the target's server. Stay at `-a 1` for OSINT and use an anonymising exit if attribution matters; `-a 3/4` is noisy and log-visible.
- Version detection can be spoofed or wrong; corroborate before relying on a "vulnerable version" claim.
- Behind Cloudflare/Akamai you fingerprint the CDN, not the origin.

## Overlaps ("do both")
- Pairs with reverse-analytics and WHOIS/DNS tooling: WhatWeb extracts the tracking IDs and stack, those turn them into a list of co-owned domains and registrant leads.

## Trust & verifiability
`trust: community` — mature, well-maintained open-source scanner; treat detected versions as strong hints to verify, not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatweb |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
