---
id: sn1per
name: Sn1per
description: Use when you have a `domain` or `ip-address` and want automated end-to-end recon + vulnerability scanning that orchestrates 90+ tools — returns domain, ip-address plus open ports and findings.
url: https://github.com/1N3/Sn1per
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- vulnerabilities
- scanners
bestFor: One-command attack-surface recon and vuln scanning that wraps dozens of underlying tools.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Community Edition is free and source-available (this GitHub repo). Professional (~$984/yr per seat) and Enterprise tiers add a web UI, JSON API, unlimited scans, and reporting — not needed for CLI recon.
opsec: active
opsecNote: HIGHLY ACTIVE and noisy — Sn1per runs port scans, service probes, and active vulnerability checks directly against the target, generating significant traffic that IDS/WAF/hosting providers will log and may alert on. Only run against infrastructure you are authorized to test; use `-m stealth`/passive modes for lower-noise recon, and never point it at third-party assets you don't own or have permission for.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Long-running open-source project by 1N3, actively maintained (Sn1per Professional 2026 release). Widely used in offensive security; the free CE is the source in this repo.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- domain-dossier
- theharvester
- dnsdumpster
aliases:
- 1N3/Sn1per
- sniper scanner
tags:
- vulnerability-scanner
- recon-automation
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Sn1per

> An offensive-security automation framework: give it a target and it orchestrates 90+ recon/scan tools into a single workflow — asset discovery, port scanning, and active vulnerability verification.

## When to use
You have a `domain`, `ip-address`, or CIDR range for infrastructure you are **authorized to assess** and want a fast, comprehensive attack-surface map without chaining tools by hand. This is an infrastructure/pentest tool, not a people-finder — low relevance to a missing-person case, but useful when an investigation pivots to an organisation's network you have permission to probe.

## How to use it (`bestInteractionPattern`: cli)
1. Install the free Community Edition from the repo (Docker-first deployment is supported).
2. Run a scan: `sniper -t <target>` for a single host, or `-f <file>` / a CIDR for a range.
3. Choose the mode to match your OpSec need: full/intrusive vs. stealth/passive recon.
4. Read results under `/usr/share/sniper/loot/<workspace>/`: discovered subdomains/hosts, open ports, service banners, and flagged vulnerabilities.
5. Pivot: discovered hosts → deeper manual review; a passive-only pass → cross-check with `[[dnsdumpster]]`; emails/names surfaced → people/breach search.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, CIDR, or a targets file
- **Out:** `domain` (subdomains/hosts), `ip-address` (live hosts, open ports), plus service and vulnerability findings
- **Empty/negative result looks like:** no open ports/hosts discovered (well-firewalled or offline target) — not proof the asset doesn't exist; it may simply be blocking your probes.

## Gotchas & OpSec
- **Authorization required:** active scanning without permission is likely illegal. Only target assets you own or are contracted to test.
- Extremely noisy: full scans trip IDS/WAF and appear in target logs. Use stealth/passive modes when you need to stay quiet, and always run from an appropriate testing host/VPN.
- The free CE is CLI-only; the web UI/API/reporting are paid — you don't need them for recon.

## Overlaps ("do both")
- For purely passive infrastructure mapping, prefer `[[dnsdumpster]]` and `[[domain-dossier]]` first, then use Sn1per only when active verification is authorized.
- Pairs with `[[theharvester]]` for the people/email-facing side of an org's footprint.

## Trust & verifiability
`trust: community` — a mature, actively maintained open-source project. Findings are tool-generated and can include false positives; verify any vulnerability manually before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sn1per |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
