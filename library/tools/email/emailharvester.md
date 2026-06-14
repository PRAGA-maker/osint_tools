---
id: emailharvester
name: EmailHarvester
description: Use when you have a target domain and want to scrape associated email addresses from search engines and public sources — returns email addresses tied to that domain.
url: https://pypi.org/project/EmailHarvester/
category: email
path:
- email
bestFor: Harvesting email addresses for a given domain from public search sources.
input: Domain name
output: List of email addresses found for that domain
selectorsIn:
- domain
selectorsOut:
- email
status: live
pricing: free
costNote: Free, open-source (MIT); no account needed, but underlying search engines may rate-limit or require API keys for some plugins.
opsec: passive
opsecNote: Passively scrapes public search-engine and web results; does not contact the target domain's owner. Heavy use can trip search-engine rate limits/CAPTCHAs against your IP.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by maldevel on PyPI/GitHub; inspectable code, modest but real user base.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- email-harvester
tags:
- email
- domain
- harvesting
source: osint4all
lastVerified: ''
enrichment: full
---

# EmailHarvester

> A Python CLI that scrapes email addresses associated with a domain from search engines and public sources — domain-to-emails enumeration.

## When to use
You have a `domain` (a person's employer, small business, club, or personal site) and want every email address publicly associated with it. In missing-persons work this turns a known affiliation into contactable/identifying addresses to pivot on.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install EmailHarvester`.
2. Run against a domain: `EmailHarvester -d example.com` (use `-e <engine>` to pick a source plugin, `-s`/`-l` for save/limit options; `--help` lists plugins).
3. Read the deduplicated list of harvested addresses.
4. Pivot: each `email` feeds verification (`[[emailhippo]]`, `[[email-reputation]]`) and account enumeration (`[[holehe]]`, `[[epieos-email-tool]]`).

## Inputs → Outputs
- **In:** `domain`
- **Out:** `email` (addresses found referencing that domain)
- **Empty/negative result looks like:** zero addresses returned — the domain has no indexed public emails, or your queries were rate-limited/blocked.

## Gotchas & OpSec
- Search-engine plugins get rate-limited or CAPTCHA-walled with volume; rotate sources/IPs and pace requests.
- Some plugins need their own API keys; results vary by engine.
- OpSec: passive toward the target, but your IP hits the search engines — use a clean egress for sensitive work.

## Overlaps ("do both")
- Sibling to broader recon like theHarvester; EmailHarvester is email-focused. Run alongside `[[epieos-email-tool]]` to then expand each harvested address into accounts.

## Trust & verifiability
`trust: community` — open-source (maldevel), code on GitHub/PyPI and fully auditable; results quality depends on upstream search engines.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | emailharvester |
| category | email |
| selectorsIn → selectorsOut | domain → email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
