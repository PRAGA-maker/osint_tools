---
id: tookie-osint
name: Tookie-OSINT
description: Use when you have a `username` and want to enumerate matching accounts across many sites from the command line — returns social-profile URLs where the handle exists.
url: https://github.com/Alfredredbird/tookie-osint
category: username
path:
- username
bestFor: CLI username enumeration across many social/web platforms (a Sherlock/Maigret-style account finder).
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open-source (GitHub); no account or payment. You run it locally in Python.
opsec: passive
opsecNote: Tookie queries each target site directly from YOUR machine/IP as it checks the handle, so those sites can see your requests — route it through a sock-puppet IP/VPN. It does not contact the subject, and some checks use Selenium (a headless browser) which is heavier and more detectable than plain HTTP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community open-source project (Alfredredbird), actively maintained (v4 rewrite, v4.1 in 2026); like all account-finders it produces false positives, so hits need manual confirmation.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- tookie
- Tookie OSINT
tags:
- username
- social-media
- account-discovery
- cli
source: gh-topic-osint-framework
lastVerified: '2026-07-10'
enrichment: full
---

# Tookie-OSINT

> A locally-run, Sherlock-style username enumerator: feed it a handle and it hunts matching accounts across many sites, returning the URLs where they exist.

## When to use
You have a `username` and want an automated, scriptable sweep across social and web platforms — run from your own machine so you control the site list, output format, and rate. Reach for it over web scanners when you want to pipe results into other tooling, run repeatedly, or customise which sites are checked in a missing-person/identity workflow.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/Alfredredbird/tookie-osint and install (Python; deps like colorama, requests, selenium, webdriver-manager install during setup).
2. Run it against a handle, e.g. `python tookie.py -u <username>` (see `-h` for options).
3. Route through a sock-puppet VPN/proxy — checks hit target sites from your IP.
4. Read the output: a list of sites where the handle resolves, with `social-profile` URLs.
5. Confirm each hit manually (open the profile) — then pivot: a real name/avatar feeds people-search and `[[reverse-image-search]]`.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` URLs across many platforms where the handle exists, plus the `username` per site
- **Empty/negative result looks like:** few/no hits — a rare handle, or sites that changed their detection responses (account-finders drift as sites update). Common handles produce many false positives. Absence is not proof of no accounts.

## Gotchas & OpSec
- **False positives are inherent** — verify every hit by opening the profile; matching handle ≠ same person.
- Selenium-based checks are slower and more detectable; sites may rate-limit or block — expect some checks to fail intermittently.
- OpSec: **passive** to the subject, but checks originate from your IP — always use a sock-puppet VPN/proxy.

## Overlaps ("do both")
- Pairs with `[[user-searcher]]`, `[[usersearch-org]]` and Sherlock/Maigret — site coverage differs between finders, so run more than one and union the confirmed hits.

## Trust & verifiability
`trust: community` — an actively maintained open-source tool; the code is inspectable, but results are heuristic. Confirm accounts individually before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tookie-osint |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
