---
id: phantomtrace
name: PhantomTrace
description: Use when you have a `username`, `email`, `domain` or `image` and want a one-shot recon sweep — account hunting across 35+ sites, breach checks, EXIF and WHOIS — returns `social-profile`, `email`, `metadata-exif`, `geolocation`.
url: https://github.com/nomadrai/osint-PhantomTrace
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Running a fast multi-selector OSINT sweep (username enumeration + breach + EXIF + WHOIS + dorks) and getting a consolidated HTML report.
selectorsIn:
- username
- email
- domain
- image
selectorsOut:
- social-profile
- email
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free and open-source (Python 3); the only cost is a HaveIBeenPwned API key for the breach-check module.
opsec: passive
opsecNote: It queries public profile pages and third-party APIs (HIBP, WHOIS), not the subject directly, so it's passive toward the target — but every lookup goes out from your IP; run it behind a VPN/sock-puppet and expect the usual username-enumeration false positives.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: unverified
trustNote: A small, low-profile GitHub project; treat it as a convenience wrapper over public sources whose logic you should read before trusting, and corroborate every hit at the source.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- osint-PhantomTrace
tags:
- osint
- aggregator
- username-enumeration
- cli
source: gh-topic-footprinting
lastVerified: '2026-07-21'
enrichment: full
---

# PhantomTrace

> A Python recon multi-tool — throw it a username, email, domain or image and it runs account hunting, breach checks, EXIF and WHOIS in one pass, then writes an HTML report.

## When to use
Early in an investigation when you have one or more selectors and want breadth fast. PhantomTrace bundles several common OSINT steps: username enumeration across 35+ platforms, a HaveIBeenPwned breach check on an email, EXIF extraction from an image (GPS/device/timestamps), a WHOIS lookup on a domain, and Google-dork query generation — collating everything into one HTML report. Use it to generate leads to verify, not as an authority.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/nomadrai/osint-PhantomTrace and `pip install -r requirements.txt` (Python 3).
2. Add your HaveIBeenPwned API key where the README specifies (needed for the breach module).
3. Run it with the selector(s) you have — username, email, domain, and/or an image file.
4. Open the generated HTML report: per-platform account hits, breach appearances, EXIF fields, WHOIS data, and dork links.
5. Verify each hit manually (open the profile, confirm it's the same person) before relying on it; pivot confirmed accounts into deeper per-platform tooling.

## Inputs → Outputs
- **In:** `username`, `email`, `domain`, and/or `image`
- **Out:** `social-profile` (candidate accounts), `email` (breach exposure), `metadata-exif` (EXIF incl. GPS), `geolocation` (from EXIF/WHOIS)
- **Empty/negative result looks like:** a report full of "not found" rows, or account hits that turn out to be someone else — username enumeration is noisy, so treat unconfirmed hits as leads only.

## Gotchas & OpSec
- Human-in-the-loop: you need an HIBP API key; without it the breach module is inert.
- OpSec: passive toward the target but your IP makes all the requests — use a VPN/sock puppet.
- It's a thin aggregator: coverage of the "35+ platforms" drifts as sites change, and results include false positives. Read the source, keep dependencies current, and confirm everything downstream.

## Overlaps ("do both")
- Overlaps with dedicated username-search tools (e.g. Sherlock-class enumerators), breach-check services, and EXIF readers — PhantomTrace is the quick combined sweep; use the specialised tools to verify and go deep on each lead it surfaces.

## Trust & verifiability
`trust: unverified` — a small open-source project aggregating public sources; useful for breadth, but every finding must be corroborated at the primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phantomtrace |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email, domain, image → social-profile, email, metadata-exif, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
