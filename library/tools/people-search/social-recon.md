---
id: social-recon
name: Social Recon (osint-scraper)
description: Use when you have a `username` or `email` and want an automated sweep of their online footprint — returns social-profile, associate, and email leads (self-hosted, unmaintained).
url: https://github.com/famavott/osint-scraper
category: people-search
path:
- people-search
bestFor: A self-hosted Python/Flask app that compiles a person's online presence from a username/email.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
- associate
- email
status: degraded
pricing: free
costNote: Free and open-source (MIT-style). Cost is your own time — it's dated (Python 3.5-era) and likely needs dependency fixes to run today.
opsec: passive
opsecNote: Runs locally under your control, so queries originate from your machine/IP — route through a VPN/sock-puppet setup if you don't want your IP hitting the sites it scrapes. It pulls public data only and does not notify the subject.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: python-lib
trust: community
trustNote: A community open-source project (a few hundred GitHub stars) that is no longer actively maintained; audit the code before running and expect breakage against sites that have changed since.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- osint-scraper
- famavott osint-scraper
tags:
- people-search
- open-source
- cli
- self-hosted
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Social Recon (osint-scraper)

> A self-hosted open-source Python/Flask app that takes a username or email and compiles what it can find about that online identity.

## When to use
You have a `username` and/or `email` and want an automated first-pass footprint without paying for a SaaS enumerator — and you're comfortable running a local Python app. Best when you already self-host tooling; for a no-setup equivalent, a maintained web enumerator is usually the better call given this project's age.

## How to use it (`bestInteractionPattern`: python-lib)
1. Clone the repo (github.com/famavott/osint-scraper) and read the code/README.
2. Set up a Python 3 virtualenv and install dependencies — expect to patch a few pinned/legacy packages to get it running.
3. Launch the local Flask web interface and submit a `username`/`email`.
4. Review the compiled output (profiles/mentions across the sites it queries).
5. Pivot: discovered `social-profile`s and `associate`s feed further per-platform lookups; found emails feed breach/email OSINT.

## Inputs → Outputs
- **In:** `username` and/or `email`
- **Out:** compiled `social-profile` hits, related `associate`/mention leads, `email` references
- **Empty/negative result looks like:** sparse or empty output, or errors on run — often because target sites changed their markup/APIs since the tool was last updated. Treat a blank as "tool is stale," not "nothing exists."

## Gotchas & OpSec
- Maintenance: unmaintained (Python 3.5, legacy CI, deprecated helper services) — hence `status: degraded`. Audit and patch before trusting it.
- Rate limits: scraping several sites in sequence can trip throttling/blocks; pace it.
- OpSec: passive to the subject, but queries come from *your* IP — use a VPN/sock-puppet environment.

## Overlaps ("do both")
- Pairs with maintained username enumerators (Sherlock/Maigret-class tools) and email-OSINT — those cover more sites and are kept current; run this only if you want its specific compilation or already self-host it.

## Trust & verifiability
`trust: community` — an open-source hobby project, inspectable but aging and unmaintained. Verify its findings against live sources; don't rely on it as a sole source, and read the code before running it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-recon |
| category | people-search |
| selectorsIn → selectorsOut | username, email → social-profile, associate, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
