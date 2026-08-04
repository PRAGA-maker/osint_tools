---
id: reconftw
name: ReconFTW
description: Use when you have a `domain` or `employer-org` and want an automated end-to-end recon pipeline — returns subdomains, resolved hosts, emails, leaks, screenshots and OSINT findings in a structured report.
url: https://github.com/six2dez/reconftw
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: One-command, comprehensive recon automation over a domain: subdomains, OSINT, web analysis and reporting.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- email
status: live
pricing: free
costNote: Free and open-source (MIT). Optional third-party API keys (Shodan, GitHub, WHOISXML) improve coverage.
opsec: active
opsecNote: Runs both passive OSINT and active scanning (DNS brute-force, web probing, screenshots, optional vuln checks) that directly touch the target's infrastructure and are logged by it. The project's own disclaimer stresses it is illegal to use against targets without consent — restrict to authorised engagements from a controlled IP.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: trusted
trustNote: Very widely used, actively maintained framework (six2dez, ~8k stars, thousands of commits).
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- dorks-hunter
aliases:
- recon-ftw
- reconftw.sh
tags:
- recon-automation
- subdomains
- osint-pipeline
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# ReconFTW

> A one-command reconnaissance orchestrator that chains dozens of best-in-class tools to fully map a domain — subdomains, hosts, OSINT, web surface and (optionally) vulnerabilities.

## When to use
You have a `domain` (or an org's domain / IP range you are authorised to assess) and want a thorough, repeatable recon sweep without wiring up 40 separate tools. It combines passive subdomain discovery, DNS resolution, email/leak/GitHub OSINT, metadata extraction, Google dorking and web analysis into one structured output tree.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/six2dez/reconftw && cd reconftw && ./install.sh` (or use the Docker image).
2. Add API keys in `reconftw.cfg` / `secrets.cfg` (Shodan, GitHub token, WHOISXML, etc.) for richer OSINT.
3. Run a recon-only pass: `./reconftw.sh -d example.com -r` (use `-l` for a list, or profile flags for passive-only vs. full).
4. Review the `Recon/` output: subdomain lists, resolved hosts, screenshots, harvested emails/leaks, and an HTML/JSON report.
5. Pivot: harvested `email`s feed email-OSINT; `domain`/`ip-address` assets feed infrastructure clustering.

## Inputs → Outputs
- **In:** `domain` (single or list), `ip-address`/CIDR.
- **Out:** subdomains and resolved `ip-address`es, harvested `email`s, leak/GitHub findings, screenshots, and structured reports.
- **Empty/negative result looks like:** thin output directories — usually a low-footprint target or missing API keys, not a definitive negative.

## Gotchas & OpSec
- **Active by default:** the full profile scans and probes the target; only the passive profile stays hands-off. Choose the profile deliberately and only run active modes with authorisation.
- Heavy: installs many binaries and can run for a long time; run on a dedicated Linux VPS.
- Coverage and quality scale with the API keys you provide.

## Overlaps ("do both")
- Bundles what standalone tools do individually — its dorking overlaps `[[pydork]]`, its host data overlaps `[[hostintel-keithjjones-github]]`; use reconFTW for breadth, the standalone tool when you need to control one step precisely. Pairs with `[[dorks-hunter]]`.

## Trust & verifiability
`trust: trusted` — a heavily-used, actively maintained open-source framework; because it wraps well-known tools, individual findings are traceable back to the underlying tool that produced them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reconftw |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
