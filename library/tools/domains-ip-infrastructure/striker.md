---
id: striker
name: Striker
description: Use when you have a `domain` and want fast offensive recon — subdomains, tech fingerprint, header/misconfig and sensitive-file checks — returns discovered `domain`s and findings.
url: https://github.com/s0md3v/Striker
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-shot recon sweep of a domain (attack surface, subdomains, tech, misconfigurations) from the command line.
selectorsIn:
- domain
selectorsOut:
- domain
status: degraded
pricing: free
costNote: Free and open-source (Python); no account. Striker 2.0 is explicitly a prototype, not production-ready.
opsec: active
opsecNote: Striker actively probes the target — subdomain enumeration, port scan of the top 1000 TCP ports, header/sensitive-file requests. All of this is logged by the target and any IDS. Only run against infrastructure you're authorised to test, and always via an anonymising exit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source project by s0md3v; leverages retire.js/Wappalyzer/sqlmap, but the current 2.0 line is a stated prototype, so expect rough edges.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- orbit
- photon
- zen
- zen-github-com
aliases:
- Striker recon
tags:
- Domain/IP/Links
- Domain/IP investigation
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Striker

> An open-source offensive recon scanner — used in OSINT/infrastructure work to sweep a single `domain` for its attack surface, subdomains, tech stack and obvious misconfigurations in one run.

## When to use
You have a `domain` tied to a subject or organisation and want a quick, consolidated recon pass rather than running five separate tools. Striker enumerates subdomains, fingerprints technologies (via Wappalyzer/retire.js), scans common ports, and flags misconfigured headers, sensitive files and outdated JS. Use it for scoping; hand serious findings to dedicated tools.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install requirements (`pip install -r requirements.txt`).
2. Run against the target: `python striker.py` and enter the `domain` when prompted (see repo README for the current 2.0 invocation).
3. Read the output: discovered subdomains (`domain`s), tech fingerprint, open ports, header/file findings.
4. Pivot: take live subdomains into screenshotting (`[[gowitness]]`) and tech findings into targeted verification.

## Inputs → Outputs
- **In:** `domain`
- **Out:** discovered `domain`s (subdomains), technology fingerprint, open ports, misconfiguration/sensitive-file flags
- **Empty/negative result looks like:** few subdomains and a thin fingerprint — common behind a CDN or for a small site; not proof the surface is small.

## Gotchas & OpSec
- **Active and intrusive** — port scans and file probes are unambiguously offensive traffic. Only use with authorisation; this is not a passive OSINT lookup.
- Striker 2.0 is a stated prototype ("not intended to be used by regular users"), so expect breakage — hence `status: degraded`. Prefer mature tools for anything you must rely on.
- Anonymise your exit; the target will see the scan.

## Overlaps ("do both")
- Pairs with `[[photon]]` (crawling) and `[[gowitness]]` (screenshotting): Striker scopes the surface, those crawl and visually capture it.

## Trust & verifiability
`trust: community` — a known open-source recon script, but its prototype status means results should be re-verified with a dedicated scanner before you act on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | striker |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
