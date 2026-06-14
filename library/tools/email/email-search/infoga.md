---
id: infoga
name: Infoga
description: Use when you want quick email reconnaissance from search engines / public APIs — but note the project is old and largely unmaintained.
url: https://github.com/m4ll0k/infoga
category: email
path:
- email
- email-search
bestFor: Lightweight email harvesting/recon from search engines and public sources via CLI.
selectorsIn:
- email
- domain
selectorsOut:
- email
- ip-address
- domain
status: degraded
pricing: free
costNote: Free and open-source. Some sources (e.g. Shodan, HIBP) need API keys; several scrapers have broken with provider changes over the years.
opsec: passive
opsecNote: Pulls from search engines and public APIs without contacting the target. Your queries hit those providers from your IP.
humanInLoop: true
humanInLoopReason:
- api-key
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Recognised older OSINT tool by m4ll0k, but the repo is largely unmaintained and several modules break against modern search engines. Verify it still runs before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- holehe
- have-i-been-pwned
- hunter
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# Infoga

> A lightweight Python CLI that gathers email-related info (which domains/hosts, IPs, breach status) by scraping search engines and querying public APIs. Capable but aging and partly broken.

## When to use
Early-stage recon when you have an `email` or `domain` for a missing person/associate and want a quick sweep for where the address appears, related hosts/IPs, and breach status — as a fast first pass before more reliable, targeted tools.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/m4ll0k/infoga && cd infoga && pip install -r requirements.txt`.
2. Run by domain: `python infoga.py --domain example.com --source all --breach -v`.
3. Run by email: `python infoga.py --info target@example.com`.
4. Add keys (Shodan/HIBP) where prompted for richer output.
5. Read stdout: emails found, source, related IPs/hosts, breach flag.

## Inputs → Outputs
- **In:** `email`, `domain`
- **Out:** discovered `email`s, related `ip-address`/host (`domain`), breach status
- **Empty/negative result looks like:** few/no rows — often because a scraper module is broken or the search engine blocked it, not necessarily a true negative.

## Gotchas & OpSec
- Unmaintained: expect broken modules and rate-limiting/CAPTCHA from search engines — confirm it runs first.
- Human-in-the-loop: some sources need API keys; search scraping gets rate-limited.
- OpSec: passive toward the target, but your IP queries the providers — use a research network.

## Overlaps ("do both")
- Pair with maintained tools: `[[holehe]]` (registered services), `[[have-i-been-pwned]]` (breaches), `[[hunter]]` (work emails) — these are more reliable than Infoga's aging scrapers.

## Trust & verifiability
`trust: community` — a known OSINT project, but its unmaintained state means outputs are unreliable; cross-check anything it returns.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infoga |
| category | email |
| selectorsIn → selectorsOut | email, domain → email, ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key, rate-limit) |
