---
id: theharvester
name: theHarvester
description: Use when you have a domain or company and want to enumerate associated emails, subdomains, hosts, and IPs from public sources — returns emails, subdomains, IPs, and URLs.
url: https://github.com/laramies/theHarvester
category: email
path:
- email
- email-search
bestFor: Passive footprinting of a domain to harvest emails and infrastructure from search engines and OSINT APIs.
selectorsIn:
- domain
- employer-org
selectorsOut:
- email
- domain
- ip-address
- name
status: live
pricing: free
costNote: Open source (MIT). Free; some data sources need free or paid API keys for full results.
opsec: passive
opsecNote: Queries third-party engines/APIs (Bing, DuckDuckGo, crt.sh, Shodan, etc.), not the target's own servers, so the target domain is not directly contacted in default passive modes. Active DNS brute-forcing options exist and do touch target infrastructure.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: trusted
trustNote: Mature, widely used recon tool by Christian Martorella (laramies); standard component of OSINT/pentest distros like Kali.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
relatedTools:
- toofr
aliases:
- theHarvester
- the-harvester
tags:
- email
- recon
- domain
- subdomain-enumeration
source: arf-seed
lastVerified: ''
enrichment: full
---

# theHarvester

> A command-line passive-recon tool that mines public search engines and OSINT APIs to map a domain's emails and exposed infrastructure.

## When to use
You have a `domain` or `employer-org` tied to a subject (their employer, business, or personal domain) and want to surface associated `email` addresses, `subdomains`, `ip-address`es, and host `URLs`. In a missing-persons context it is most useful when the subject is linked to an organization or self-hosted domain — it harvests the org's email patterns, which you can then match against a likely personal address.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pipx install theHarvester` (or clone the GitHub repo and `pip install -r requirements.txt`).
2. Add free/paid API keys in `api-keys.yaml` for richer sources (Shodan, Hunter, etc.) — optional.
3. Run: `theHarvester -d targetdomain.com -b bing,duckduckgo,crtsh -l 500`.
4. Read output (terminal + optional HTML/XML report): lists of emails, hosts, subdomains, IPs.
5. Pivot: take a harvested `email` into reverse-lookup tools ([[thatsthem]], [[venacus]]); take subdomains/IPs into infrastructure tools.

## Inputs → Outputs
- **In:** `domain`, `employer-org`
- **Out:** `email`, `domain` (subdomains/hosts), `ip-address`, occasionally `name` (from email local-parts)
- **Empty/negative result looks like:** few or zero results — common when sources lack indexed data, keys are missing, or rate limits truncate the run.

## Gotchas & OpSec
- Human-in-the-loop: best results need API keys for several sources; keyless runs are thinner.
- Some engines rate-limit or block; rotate sources/keys and lower `-l` limits.
- OpSec: passive by default (third parties do the querying). Avoid the active DNS-bruteforce flags if you must stay off the target's logs.

## Overlaps ("do both")
- Pairs with [[toofr]] — theHarvester finds the org's real email patterns, Toofr predicts/verifies a specific person's address from name + that domain.

## Trust & verifiability
`trust: trusted` — long-maintained, well-known open-source recon tool shipped in mainstream security distros; results still need corroboration since sources vary in freshness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | theharvester |
| category | email |
| selectorsIn → selectorsOut | domain, employer-org → email, domain, ip-address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes |
