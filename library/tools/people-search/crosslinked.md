---
id: crosslinked
name: CrossLinked
description: Use when you have an `employer-org` and want to enumerate its employees' names and likely emails from LinkedIn — returns names and format-generated email addresses without touching LinkedIn directly.
url: https://github.com/m8sec/CrossLinked
category: people-search
path:
- people-search
bestFor: Harvesting an org's employee names and email addresses from LinkedIn via search-engine scraping.
selectorsIn:
- employer-org
selectorsOut:
- name
- email
status: live
pricing: free
costNote: Free, open-source Python tool (MIT). Only cost is your own compute; no account or key.
opsec: passive
opsecNote: Scrapes Google/Bing result snippets rather than logging into LinkedIn, so LinkedIn never sees you and the targets are not notified. Search engines see the queries from your IP; use a VPN/proxy and throttle to avoid CAPTCHA/blocks. Generated emails are inferred, not confirmed — do NOT send to them as part of recon.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known open-source recon tool by m8sec, widely used in pentest/OSINT; output quality depends on current search-engine indexing of LinkedIn.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- pymeta
- linkedin2username
- theharvester
aliases:
- m8sec/CrossLinked
tags:
- linkedin
- enumeration
- python
- email-format
source: osintambition-social
lastVerified: '2026-07-17'
enrichment: full
---

# CrossLinked

> An open-source LinkedIn name/email enumerator that scrapes search-engine results — no LinkedIn login — then applies an email format to turn discovered names into likely addresses.

## When to use
You have an `employer-org` (a company name and its email domain) and want the roster of employees and their probable email addresses — for mapping an organization, finding a specific person tied to a company, or seeding people/breach lookups. Because it works from Google/Bing snippets instead of the LinkedIn UI, it needs no LinkedIn account and leaves no trace on the platform.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install crosslinked` (or clone `https://github.com/m8sec/CrossLinked`).
2. Run with the target company name and a name format, e.g. `crosslinked -f '{first}.{last}@corp.com' "Target Company Inc"`.
3. CrossLinked queries Google and Bing for `site:linkedin.com/in "Target Company"`, parses the names from result titles/snippets, and writes `names.txt` plus formatted emails.
4. Choose the `-f` format to match the org's real convention (confirm the pattern separately, e.g. from a known employee address).
5. Pivot: feed the `name` list into people-search and the `email` list into breach-check tools; verify emails with an SMTP/validation tool before trusting them.

## Inputs → Outputs
- **In:** `employer-org` (company name + email domain/format)
- **Out:** `name` (employees), `email` (format-inferred addresses)
- **Empty/negative result looks like:** few or no names — search engines are rate-limiting/CAPTCHA-ing you, the company name is too generic, or LinkedIn profiles for that org aren't indexed. Retry from a different IP or refine the company string.

## Gotchas & OpSec
- Emails are **generated from a format, not verified** — a name in the list only means a LinkedIn profile matched; the address may be wrong or the person may have left. Never treat generated emails as confirmed contacts.
- Search engines throttle scraping aggressively; run behind a proxy, add delays, and expect intermittent CAPTCHA gaps in results.
- OpSec: **passive** toward LinkedIn (no login, no view on the target's profile); your exposure is only to the search engines you query.

## Overlaps ("do both")
- Pairs with `[[theharvester]]` (multi-source name/email harvesting) and `[[linkedin2username]]` — different collection methods surface different employees, so union the results and dedupe.

## Trust & verifiability
`trust: community` — a well-established open-source recon tool; results are only as good as current search-engine indexing, so validate names against live LinkedIn and validate emails before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crosslinked |
| category | people-search |
| selectorsIn → selectorsOut | employer-org → name, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
