---
id: h-i-v-e
name: H.I.V.E
description: Use when you have a `phone`, `email`, `username`, `ip-address`, or a leaked text database and want a single Python multi-tool to run reverse-lookup, breach, geolocation and username modules in one pass — returns social-profile, geolocation, phone.
url: https://github.com/Shad0w-ops/H.I.V.E
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: One-shot automated recon (phone/email/username/IP) from a bundled Python toolkit on Kali/BlackArch.
selectorsIn:
- username
- email
- phone
- ip-address
selectorsOut:
- social-profile
- geolocation
- phone
status: live
pricing: free
costNote: Free, open-source; Python 3.10+. Some modules need API keys (Shodan, IntelX, Hunter.io); others (Truecaller-style lookup, username finder) work with less setup.
opsec: active
opsecNote: Modules like Shodan/IP scanning and Truecaller-style reverse lookups query third-party services about the target, and the bundle also ships spoofing/credential features that are out of scope for passive OSINT. Use only the intelligence-gathering modules, run from an isolated sock-puppet environment, and treat phone/IP lookups as observable to those upstream providers.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Community Python multi-tool by Shad0w-ops (~306 stars); an aggregator of third-party services, so per-module accuracy varies and its non-OSINT modules warrant caution.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- hive
tags:
- automation
- multi-tool
- recon
source: gh-topic-osint-framework
lastVerified: '2026-07-22'
enrichment: full
---

# H.I.V.E

> A Python OSINT multi-tool for Kali/BlackArch that bundles eight modules — phone reverse-lookup, Shodan, IP geolocation, breach/database search, email verification, and cross-network username finding — behind one launcher.

## When to use
You hold a `phone`, `email`, `username`, `ip-address`, or a leaked text `database` and want a quick automated sweep across several sources at once. Best as a triage/first-pass tool on a Linux OSINT box; confirm anything useful in a dedicated, authoritative tool afterward.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `github.com/Shad0w-ops/H.I.V.E` and install on Python 3.10+ (built/tested on Kali and BlackArch).
2. Configure API keys for the modules you'll use (Shodan, IntelX, Hunter.io); some modules run with minimal setup.
3. Launch and pick a module: phone reverse-lookup, Shodan scan, IP geolocation, database/breach search, email verification, or username finder.
4. Read the per-module report written to the output directory (organised by module).
5. Pivot: a phone reverse-lookup name feeds people-search; a Shodan/IP result feeds infrastructure mapping; a username hit feeds account enumeration.

## Inputs → Outputs
- **In:** `username`, `email`, `phone`, `ip-address`, or a text `database` file
- **Out:** `social-profile` (username finder, breach hits), `geolocation` (IP), `phone` (reverse-lookup identity)
- **Empty/negative result looks like:** a module returning no rows — commonly a missing/expired API key or upstream change rather than a true negative; verify config first.

## Gotchas & OpSec
- The repo bundles spoofing and credential-extraction features alongside OSINT — those are outside passive intelligence work; stick to the lookup modules.
- Several modules depend on paid/keyed APIs (Shodan/IntelX/Hunter.io); without keys they're inert.
- OpSec: **active** — phone and IP lookups disclose the target to third-party providers; run from an isolated sock-puppet environment and only probe what you're authorised to.

## Overlaps ("do both")
- Pairs with focused tools (dedicated Shodan queries, standalone breach-search, phone-OSINT): H.I.V.E is fast breadth, while the specialists give complete, authoritative results for whichever selector lit up.

## Trust & verifiability
`trust: community` — open-source but an aggregator of third-party services; each result is only as reliable as its upstream API, and the tool's non-OSINT modules mean you should use it selectively.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | h-i-v-e |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email, phone, ip-address → social-profile, geolocation, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
