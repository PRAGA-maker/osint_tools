---
id: daprofiler
name: DaProfiler
description: Use when you have a `name` (best for a French subject) and want to auto-aggregate emails, phones, addresses, and social profiles via scraping and Google dorking — returns contact details and linked profiles.
url: https://github.com/TheRealDalunacrobate/DaProfiler
category: people-search
path:
- people-search
bestFor: Automated aggregation of a person's emails, phones, addresses and socials from a name, with French-specific email guessing.
selectorsIn:
- name
- email
selectorsOut:
- email
- phone
- address
- social-profile
- image
status: degraded
pricing: free
costNote: Free and open-source (self-hosted). No fees, but you supply your own environment and, for some modules, API keys.
opsec: active
opsecNote: DaProfiler drives a real browser (Firefox), scrapes third-party sites, and runs Google dorks from your machine — that traffic hits target and intermediary services from your IP. Run it from a VM behind a VPN/sock-puppet identity; some scraping may breach site terms of service. Facial-recognition matching of profile photos is intrusive and legally sensitive.
humanInLoop: true
humanInLoopReason:
- rate-limit
- captcha
bestInteractionPattern: python-lib
trust: community
trustNote: Community open-source project (~200 stars) by a single maintainer; unaudited scraper whose accuracy depends on volatile third-party sites. Read the code before running.
missingPersonsRelevance: high
coverage:
- fr
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- DaProfiler OSINT
tags:
- Universal Contact Search and Leaks Search
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# DaProfiler

> A self-hosted Python OSINT profiler that fans a person's name out across scrapers, Google dorks, and (for French targets) email-pattern guessing to assemble contact details and social profiles.

## When to use
You have a subject's first + last `name` and want an automated first pass that collects candidate `email`s, `phone`s, `address`es, and `social-profile`s in one run, rather than querying each source by hand. Its email-guessing and coverage are strongest for **French** subjects, but the scraping/social modules work more broadly. Treat output as leads to verify, not confirmed facts.

## How to use it (`bestInteractionPattern`: python-lib)
1. Clone and install locally (requires Python 3.8 and Firefox):
   ```
   git clone https://github.com/TheRealDalunacrobate/DaProfiler.git
   cd DaProfiler
   pip install -r requirements.txt
   ```
2. Run the tool and supply the target's first and last name (and any known `email`) as input.
3. Let the modules run — web scraping, Google dorking, and email-permutation guessing; a Firefox instance is driven automatically.
4. Read the aggregated report: discovered emails, landline/mobile numbers, addresses, social profiles, employment hints, and any matched photos.
5. Pivot: emails feed `[[account-live-com]]`/breach checks; social profiles feed username tools; addresses feed public-records lookups.

## Inputs → Outputs
- **In:** `name` (first + last), optionally a known `email`
- **Out:** `email`, `phone`, `address`, `social-profile`, `image` (profile photos), employment hints
- **Empty/negative result looks like:** modules return nothing or error out (dead scrapers / CAPTCHAs / changed site HTML). Because it depends on volatile third-party pages, an empty run is often tooling breakage, not a genuine absence — spot-check manually before concluding.

## Gotchas & OpSec
- Human-in-the-loop: scrapers hit rate limits and CAPTCHAs; expect to babysit runs and re-try modules.
- Maintenance risk: `status: degraded` — scraper-heavy projects rot fast as target sites change; verify it still runs against a known control before trusting a live case.
- OpSec: **active** — all traffic originates from your host; isolate in a VM behind a VPN/sock puppet. Facial recognition and aggressive scraping carry legal/ToS exposure — know your authorization.

## Overlaps ("do both")
- Pairs with `[[blackbird]]` — DaProfiler focuses on contact-detail aggregation and French email guessing, while Blackbird sweeps 600+ sites for username/email account presence; together they cover contacts and account footprint.

## Trust & verifiability
`trust: community` — an unaudited single-maintainer scraper. Read the source, run it isolated, and corroborate every emitted selector against an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | daprofiler |
| category | people-search |
| selectorsIn → selectorsOut | name → address, email, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | active |
| human-in-loop | yes |
