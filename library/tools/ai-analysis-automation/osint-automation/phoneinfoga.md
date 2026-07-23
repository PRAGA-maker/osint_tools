---
id: phoneinfoga
name: PhoneInfoga
description: Use when you have a `phone` number and want to validate it and gather footprint intelligence (carrier, line type, VoIP flags, and search-engine footprints) — returns carrier/geographic data and pivot leads.
url: https://github.com/sundowndev/PhoneInfoga
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: Scanning an international phone number for carrier/line-type facts and generating footprint/search leads.
input: Phone numbers
output: Country, carrier, line type, reputation status, associated information
selectorsIn:
- phone
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Open source (GPLv3); free to run. Some scanner integrations (e.g. Numverify, third-party APIs) need free API keys to enrich results.
opsec: passive
opsecNote: Local formatting/validation is fully passive. But its footprint scanners issue Google/Bing/DuckDuckGo dork queries and can call third-party APIs — those queries touch search engines and API providers, not the number's owner, and never place a call or SMS to the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely used open-source project by sundowndev; currently stable but flagged unmaintained, so integrations may drift over time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- phoneinfoga
tags:
- phone-osint
- osint-automation
source: arf-seed
lastVerified: '2026-07-23'
---

# PhoneInfoga

> An open-source phone-number reconnaissance CLI: validate an international number, learn its carrier/line type, and generate footprint/search-engine leads toward the owner.

## When to use
You have a `phone` number (E.164 format, e.g. `+14155552671`) tied to a missing person or subject and want to confirm it's valid, learn the country/carrier/line type (mobile, landline, VoIP), and surface where the number appears online. It's a fast automation layer over the manual "Google the number" step.

## How to use it (`bestInteractionPattern`: cli)
1. Install via the release binary, `go install`, or Docker (`docker run --rm sundowndev/phoneinfoga scan -n <number>`).
2. Run a scan: `phoneinfoga scan -n "+14155552671"`.
3. Optionally launch the local web UI (`phoneinfoga serve`) or REST API for a browser workflow.
4. Read the output: validity, country, carrier, line type, and footprint links (search-engine dorks, reputation lookups). Configure API keys (e.g. Numverify) for richer carrier data.
5. Pivot: footprint dorks pointing to a marketplace ad, social post, or business listing feed `name` / `social-profile` discovery and reverse-phone people search.

## Inputs → Outputs
- **In:** `phone` (international format)
- **Out:** carrier/line-type/geographic facts, plus footprint leads that can resolve to `name` / `social-profile`
- **Empty/negative result looks like:** "invalid number" (bad format/nonexistent range) or a scan with carrier facts but zero footprint hits — the latter means the number isn't publicly posted, not that it's unused.

## Gotchas & OpSec
- It explicitly cannot geolocate a phone in real time, name the owner directly, or "hack" anything — treat carrier/line-type as facts and footprints as leads to verify.
- The project is stable-but-unmaintained; scanner modules that depend on third-party sites can break — check output for empty/error scanners.
- OpSec: **passive**, but footprint scanning hits search engines/APIs; run from a sock-puppet environment for sensitive work.

## Overlaps ("do both")
- Pairs with reverse-phone people-search sites and messaging-app account-existence checks — PhoneInfoga classifies and footprints the number; those resolve it to a person or an app account.

## Trust & verifiability
`trust: community` — reputable, transparent open-source tool; verify each footprint lead at its source rather than trusting the aggregated scan.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phoneinfoga |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | phone → name, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
