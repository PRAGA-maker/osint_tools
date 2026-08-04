---
id: magnifier
name: Magnifier
description: Use when you have a `domain` and want a one-shot recon sweep — returns subdomains, harvested emails, DNS/WHOIS, GeoIP, reverse-IP and CMS fingerprint in a single toolkit.
url: https://github.com/TheEyeOfCyber/Magnifier
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A bundled command-line recon toolkit that runs 15+ information-gathering modules against a target website.
selectorsIn:
- domain
selectorsOut:
- domain
- email
- ip-address
status: degraded
pricing: free
costNote: Free and open-source (MIT). Caveat: it targets Python 2, which is end-of-life — expect to patch it or run it in a Python 2 environment/Termux.
opsec: active
opsecNote: Several modules (port scan, zone transfer, subdomain probing, email harvesting) connect directly to the target's infrastructure, so this is active reconnaissance the target can log. Run it from disposable/proxied infrastructure and only against targets you're authorised to assess.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community-authored toolkit (TheEyeOfCyber) that wraps common recon techniques; it's a convenience bundle rather than a novel data source, and its Python 2 base means it's under-maintained — verify each module's output independently.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- TheEyeOfCyber Magnifier
tags:
- Tools collections/toolkits
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Magnifier

> An all-in-one recon toolkit: point it at a domain and it runs subdomain discovery, email harvesting, DNS/WHOIS, GeoIP, port scan, reverse-IP and CMS detection back to back — a fast first sweep of a target's web footprint.

## When to use
You have a `domain` and want a broad, quick reconnaissance pass without stringing together a dozen separate tools. Magnifier bundles the usual first-pass modules — subdomain finder, website email collector, zone transfer, reverse-IP lookup, WHOIS, GeoIP, port scan, CMS detection (WordPress/Drupal/Joomla/Magento) — into one CLI run, giving you a starting map of the target's infrastructure and exposed contacts.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/TheEyeOfCyber/Magnifier && cd Magnifier`.
2. Run `python2 magnifier.py` (it targets Python 2 — use a Py2 env or Termux; patch if needed).
3. Provide the target `domain` and choose the module(s) to run.
4. Read the outputs: subdomains, harvested emails, DNS/zone data, reverse-IP neighbours, GeoIP, open ports, CMS fingerprint.
5. Pivot: harvested `email`s feed email-OSINT; subdomains and reverse-IP neighbours expand the infrastructure map; CMS fingerprint informs further recon.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` (subdomains, DNS), `email` (harvested addresses), `ip-address` (resolved/reverse-IP, GeoIP), plus CMS/port findings
- **Empty/negative result looks like:** modules returning nothing — zone transfer refused (normal), no emails on the pages crawled, or reverse-IP empty; a blank module is usually the target being locked down, not a tool error.

## Gotchas & OpSec
- **Python 2 / under-maintained:** it's EOL tech, so expect setup friction and audit the code before running.
- **Active recon:** port scans, zone-transfer attempts and email harvesting hit the target directly — authorised targets only, from proxied infrastructure.
- Bundled convenience means each module is basic; corroborate important findings with a dedicated, current tool.

## Overlaps ("do both")
- Overlaps heavily with purpose-built recon tools (dedicated subdomain finders, WHOIS/DNS, reverse-IP, email harvesters) — use Magnifier for a fast combined first pass, then a maintained single-purpose tool to confirm and go deeper on any hit.

## Trust & verifiability
`trust: community` — an open, inspectable but under-maintained toolkit; treat it as a launcher for standard techniques and verify each result against a current authoritative tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | magnifier |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain, email, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
