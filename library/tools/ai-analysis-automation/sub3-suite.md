---
id: sub3-suite
name: Sub3 Suite
description: Use when you have a `domain`, `ip-address`, or `email` and want a GUI framework to enumerate and correlate infrastructure — returns subdomains, IPs, certs, ASNs, and related records.
url: https://github.com/3nock/sub3suite
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: GUI-driven subdomain and infrastructure enumeration with cross-correlation across many OSINT sources.
selectorsIn:
- domain
- ip-address
- email
selectorsOut:
- domain
- ip-address
status: live
pricing: free
opsec: passive
opsecNote: Sub3 Suite is primarily passive — it queries third-party OSINT sources and APIs (cert transparency, passive DNS, WHOIS, search engines) rather than probing the target, so the subject isn't touched. Active brute/resolve modes exist; know which you enable. Add API keys via a dedicated account and run behind controlled infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Open-source Qt GUI OSINT framework by 3nock; capable and actively developed community tool, results inherit their source's quality.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- ote-osint-template-engine
- spidersuite
aliases:
- Sub3 Suite
- sub3suite
- 3nock/sub3suite
tags:
- subdomain-enumeration
- infrastructure-mapping
- osint-framework
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Sub3 Suite

> A cross-platform Qt GUI OSINT framework for infrastructure recon — enumerate subdomains, IPs, certificates, and ASNs from many sources and correlate them visually, no command line required.

## When to use
You have a `domain`, `ip-address`, or `email` and want broad infrastructure enumeration with a graphical interface rather than stitching CLI tools together. Sub3 Suite bundles subdomain discovery, DNS/IP resolution, certificate and ASN lookups, WHOIS, and "raw" API access to dozens of sources, then lets you pivot and correlate results in one workspace — handy for mapping an organization's or person's web footprint.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download a Sub3 Suite release (Windows/Linux/macOS) from https://github.com/3nock/sub3suite, or build it.
2. Add API keys for the sources you have under settings (many modules work without, more with).
3. Use the relevant tab — subdomain enumeration, IP/host, SSL cert, ASN, raw — and enter your seed (`selectorsIn`).
4. Read and correlate the results across tabs (`selectorsOut`); export or pivot discovered domains/IPs into deeper tools.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or `email`
- **Out:** `domain` (subdomains), `ip-address`es, TLS certificates, ASN/netblock and WHOIS data — correlated in the GUI
- **Empty/negative result looks like:** thin results — usually few API keys configured or little public exposure; add sources rather than concluding nothing exists.

## Gotchas & OpSec
- Human-in-the-loop: none to run; coverage scales with your own API keys.
- OpSec: mostly passive (third-party sources); active resolve/brute modes exist — know which you enable before running.
- Community tool: capable but its findings inherit each source's reliability; verify important results.

## Overlaps ("do both")
- Overlaps with CLI enumerators [[subfinder]] and frameworks [[spiderfoot]]/[[sn0int]], and pairs with [[ote-osint-template-engine]] (same author's ecosystem) — use Sub3 Suite when you want a GUI and cross-source correlation, the CLIs for scripting/scale.

## Trust & verifiability
`trust: community` — an actively-developed open-source GUI framework. The tool is solid; because it aggregates many third-party sources, attribute each finding to its source and confirm the ones that matter.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sub3-suite |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, ip-address, email → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
