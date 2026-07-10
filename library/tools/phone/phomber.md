---
id: phomber
name: Phomber
description: Use when you have a `phone` (or IP/domain/username) and want CLI reconnaissance — returns carrier/line metadata and OSINT footprints, no API keys required.
url: https://github.com/s41r4j/phomber
category: phone
path:
- phone
bestFor: A one-stop command-line OSINT framework for reverse-looking-up a phone number (plus IP, domain, username) without needing API keys.
selectorsIn:
- phone
- ip-address
- domain
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free and open-source; installable via git, pip, or Docker. v3 explicitly requires no API keys for its OSINT modules.
opsec: passive
opsecNote: Runs locally and reverse-looks-up the number/selector rather than contacting the subject. Its recon may query third-party sources/search engines from your IP — use a proxy/sock-puppet context for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Community open-source OSINT framework (s41r4j). Handy and dependency-light, but a smaller project than PhoneInfoga; verify its outputs against a second tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- phoneinfoga-demo
aliases:
- phomber
tags:
- Phone numbers
- phone-recon
- cli
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Phomber

> A dependency-light CLI OSINT framework: reverse-lookup a phone number (or IP, domain, username) from the terminal with no API keys to configure.

## When to use
You have a `phone` (or an `ip-address`, `domain`, or `username`) and want quick command-line reconnaissance without signing up for API keys. Phomber bundles reverse-lookup modules into one tool: for a number it reports carrier/line metadata and hunts for OSINT footprints; it also handles IP/domain/username lookups, making it a convenient all-in-one for scripted or terminal-based investigation.

## How to use it (`bestInteractionPattern`: cli)
1. Install one of: `pip install phomber`; or `git clone https://github.com/s41r4j/phomber && pip3 install -r pyproject.toml`; or `docker pull sinawic/phomber:latest`.
2. Run `phomber` (or `python3 phomber.py`).
3. Use the `number` command for a reverse phone lookup; other commands cover IP/domain/username.
4. Read the results: carrier/line metadata and any OSINT footprints found. No API keys needed in v3.
5. Pivot: discovered `social-profile`s/`geolocation` context feed account and people-search tools.

## Inputs → Outputs
- **In:** `phone` (or `ip-address`, `domain`, `username`)
- **Out:** carrier/line metadata, `geolocation` (region), and `social-profile` footprints
- **Empty/negative result looks like:** carrier data but no footprints, or a module error. Coverage depends on the free sources it queries; an empty footprint result means "nothing found via those sources," not that the owner has no presence — corroborate with another tool.

## Gotchas & OpSec
- Requires local install (pip/git/Docker) and a terminal.
- Smaller/less battle-tested than PhoneInfoga; module reliability varies and can break as sources change.
- It does NOT geolocate a live phone — carrier/region metadata only.
- OpSec: local and passive toward the subject, but recon queries leave your IP — proxy for sensitive cases.

## Overlaps ("do both")
- Pairs with `[[phoneinfoga-demo]]` — both do CLI phone recon; PhoneInfoga has a larger scanner ecosystem, Phomber is simpler and no-API-key. Run both and reconcile — agreement raises confidence, divergence flags a source gap.

## Trust & verifiability
`trust: unverified` — a useful community open-source framework, but smaller and less audited than the mainstream tools. Treat its footprint findings as leads and confirm carrier/identity signals against a second tool before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phomber |
</content>
