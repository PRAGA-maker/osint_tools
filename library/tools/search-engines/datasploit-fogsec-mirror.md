---
id: datasploit-fogsec-mirror
name: datasploit (FOGSEC mirror)
description: Use when you have a `name`, `email`, `domain`, `username`, or `phone` and want to run automated multi-source recon that aggregates raw findings — returns emails, social profiles, and domain/subdomain data in HTML/JSON.
url: https://github.com/FOGSEC/datasploit
category: search-engines
path:
- search-engines
bestFor: Automated enrichment across people/email/domain/phone selectors via a scriptable Python framework (reference/legacy).
selectorsIn:
- name
- email
- domain
- username
- phone
selectorsOut:
- email
- social-profile
- domain
status: degraded
pricing: free
costNote: Free and open-source (GPL-3.0). No cost, but many modules require your own third-party API keys to return results.
opsec: passive
opsecNote: Runs locally on your machine and queries public/API sources server-to-server, so it is not attributed to the subject. Beware that some modules hit paid/rate-limited APIs under your keys, and active submodules (subdomain brute force, port/active scans) DO touch target infrastructure — disable those if you need to stay passive.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Community fork/mirror of the original (now largely unmaintained) DataSploit framework; Python 2.7-era code with stale modules — useful as a reference and for still-working sources, not a turnkey pipeline.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- datasploit
- DataSploit
tags:
- framework
- enrichment
- python
source: gh-topic-osint-resources
lastVerified: '2026-07-19'
enrichment: full
---

# datasploit (FOGSEC mirror)

> A legacy Python OSINT automation framework that fans a single selector out across many recon modules and aggregates the raw results — valuable as a reference and for its still-live modules, but dated (Python 2.7, many stale/keyed modules).

## When to use
You have a starting selector — a `name`, `email`, `domain`, `username`, or `phone` — and want to automate the first sweep across many public sources at once (breach/email checks, social-handle discovery, subdomain and DNS enumeration, credential/API-key leakage) rather than querying each by hand, then get the aggregate as HTML/JSON to triage. Best treated as a scaffold you cherry-pick working modules from, and as a menu of source ideas, rather than a run-and-trust pipeline.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the mirror: `git clone https://github.com/FOGSEC/datasploit`.
2. Install dependencies (Python 2.7-era; use a matching virtualenv or container) and copy the API-key config template, filling in keys for the sources you have (many modules do nothing without them).
3. Run a selector module, e.g. `python emailOsint.py target@example.com`, `python domainOsint.py example.com`, or `python usernameOsint.py handle`.
4. Read the aggregated HTML/JSON report; treat each module's output independently and re-verify hits in a live tool, since some modules are stale or point at dead endpoints.
5. Pivot: discovered `email`/`social-profile`/`domain` values feed dedicated, currently-maintained tools for confirmation and deeper enrichment.

## Inputs → Outputs
- **In:** `name`, `email`, `domain`, `username`, or `phone`
- **Out:** aggregated `email`, `social-profile`, and `domain`/subdomain findings (HTML/JSON)
- **Empty/negative result looks like:** a module returning nothing usually means a missing/expired API key or a dead upstream source, not that the subject is absent — check the module's config and status before concluding.

## Gotchas & OpSec
- Human-in-the-loop: you must supply **API keys** for many modules; without them large parts of the framework are silent.
- OpSec: mostly **passive** (local, server-to-server queries under your keys), but subdomain brute-forcing and any active-scan modules send traffic to the target's infrastructure — turn those off for a passive posture. Route through appropriate egress; don't leak your real API accounts against a sensitive target.
- Maintenance: this is a mirror of an unmaintained project on Python 2.7; expect broken modules and plan to verify everything downstream.

## Overlaps ("do both")
- Pairs with modern maintained enrichment suites (SpiderFoot, theHarvester, Recon-ng) — those cover the same selector-to-sources idea with current modules; use datasploit to cross-reference sources or when a specific still-working module gives something the others miss.

## Trust & verifiability
`trust: community` — an open-source community fork of a legacy tool; its code is inspectable but its modules are dated and partly broken, so every finding should be re-confirmed in a live, maintained source before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | datasploit-fogsec-mirror |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, domain, username, phone → email, social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
