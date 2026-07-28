---
id: webcopilot
name: WEBCOPILOT
description: Use when you have a `domain` and want an automated recon chain — returns subdomains, live hosts, endpoints, and screenshots as `domain`/`ip-address` leads.
url: https://github.com/h4r5h1t/webcopilot
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-command subdomain enumeration, endpoint crawling, screenshotting, and vulnerability triage for a target domain.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (MIT). Runs locally; wraps other free CLI recon tools it installs for you.
opsec: active
opsecNote: This is active recon — it resolves subdomains, crawls endpoints, screenshots live hosts, and probes for vulnerabilities, all of which send traffic to the target's servers and can be logged/WAF-flagged. Run from an attribution-safe host; do not point the vuln-scan (`-a`) at systems you're not authorised to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source project by GitHub user h4r5h1t; auditable but single-maintainer, and it orchestrates several third-party tools under the hood.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- amass
- dork-dump
aliases:
- webcopilot recon
tags:
- subdomain-enumeration
- recon-automation
- attack-surface
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# WEBCOPILOT

> A bash automation wrapper that chains popular recon tools: give it a domain and it enumerates subdomains, finds live hosts, crawls endpoints, grabs screenshots, and flags likely vulnerabilities.

## When to use
You have a `domain` linked to your subject and want a fast, all-in-one reconnaissance pass rather than running each tool by hand. WebCopilot is the "one command" option when you need breadth quickly — the subdomain list, live-host screenshots, and crawled endpoints can surface a personal blog, a login portal, or a forgotten service that then leaks names, emails, or handles. Infrastructure-first, so direct missing-person value is low, but the screenshots and endpoints often reveal human-facing content worth pivoting on.

## How to use it (`bestInteractionPattern`: cli)
1. Install (Linux): `git clone https://github.com/h4r5h1t/webcopilot && cd webcopilot && chmod +x webcopilot install.sh && sudo mv webcopilot /usr/bin/ && ./install.sh` (pulls in its dependency tools).
2. Subdomains only (lighter): `webcopilot -d example.com`.
3. Full run (enumerate + crawl + screenshot + vuln checks): `webcopilot -d example.com -a`.
4. Review the output directory: subdomain list, live hosts, endpoint URLs, screenshots, and any flagged issues.
5. Pivot: open screenshotted human-facing pages; feed discovered subdomains/`ip-address` to WHOIS/reverse-IP and any leaked contact into people/username search.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` (subdomains, live hosts), `ip-address` (resolved), plus endpoint URLs and screenshots
- **Empty/negative result looks like:** no subdomains beyond the apex and no live extra hosts — typical for a single-page site or one fully behind a CDN.

## Gotchas & OpSec
- OpSec: fully **active** — endpoint crawling and the `-a` vulnerability checks are intrusive and can trip WAFs/IDS. Only scan targets you're authorised to test.
- It installs and runs several third-party binaries; review what it pulls in before running on a work machine.
- Heavy runs are slow and noisy; scope and pace them.

## Overlaps ("do both")
- Overlaps `[[amass]]` for subdomain discovery (Amass is quieter/passive-capable; WebCopilot adds crawling + screenshots) and pairs with `[[dork-dump]]` to then harvest indexed documents from the hosts it finds.

## Trust & verifiability
`trust: community` — open-source and inspectable, but a single-maintainer orchestrator of other tools; verify results against the underlying tools' raw output rather than trusting the summary blindly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webcopilot |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
