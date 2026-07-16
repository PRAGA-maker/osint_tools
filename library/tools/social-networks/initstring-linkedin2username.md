---
id: initstring-linkedin2username
name: linkedin2username
description: Use when you have an `employer-org` (company LinkedIn page) and want a generated list of likely employee usernames/emails and real names — returns username, email and name.
url: https://github.com/initstring/linkedin2username
category: social-networks
path:
- social-networks
bestFor: Enumerating a company's employees from LinkedIn and generating username/email permutations for them.
selectorsIn:
- employer-org
selectorsOut:
- username
- email
- name
status: live
pricing: free
costNote: Free, open-source Python CLI. No cost beyond needing a valid LinkedIn account to authenticate the scrape.
opsec: active
opsecNote: This logs into LinkedIn with YOUR account and scrapes company employees via automation — LinkedIn actively detects scraping and can restrict or ban the account used. Always use a dedicated sock-puppet LinkedIn account, throttle with the sleep options, and consider a proxy. Targets/employees are not directly notified, but the account you use is at risk.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: A widely-referenced open-source recon tool (initstring); reliability shifts with LinkedIn's anti-automation changes, so check the repo's issues for current working status before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- linkedin2username
- l2u
tags:
- linkedin
- open-source
- cli
- username-generation
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- cloud-enum
---

# linkedin2username

> A Python CLI that scrapes a company's LinkedIn employees and mints username/email permutations — the classic bridge from an organisation to its people.

## When to use
You have an `employer-org` and want to enumerate the individuals working there and predict their usernames/email addresses. Given a company's LinkedIn URL name, it harvests employee full names and titles, then generates common formats (`first.last`, `flast`, `firstl`, raw names) — useful for building a people list around an organisation, guessing a specific person's work email, or seeding username sweeps. Primarily a red-team/recon tool, equally useful for investigative enumeration.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install requirements: `git clone https://github.com/initstring/linkedin2username && cd linkedin2username && pip install -r requirements.txt`.
2. Prepare a **sock-puppet** LinkedIn account (do not use your real one).
3. Run: `python linkedin2username.py -c <company-as-in-linkedin-url> -d <domain.com>` (add `-s` sleep, proxy, keyword, and geo options to stay under the radar).
4. Authenticate when prompted; it drives a browser session to scrape employees.
5. Read the output files: `first.last.txt`, `flast.txt`, `rawnames.txt`, `metadata.txt` (names + titles), plus other format variants.
6. Pivot: feed generated emails into `[[phonebook-cz]]`/verification; feed real names into people-search; feed usernames into cross-site sweeps.

## Inputs → Outputs
- **In:** `employer-org` (company LinkedIn identifier) + optional email domain
- **Out:** `username` lists (multiple formats), predicted `email`s, employee `name`s and titles
- **Empty/negative result looks like:** few/no employees scraped — LinkedIn may have throttled the account, the company slug is wrong, or the org has little LinkedIn presence; check repo issues for auth breakage.

## Gotchas & OpSec
- **Active and account-risking:** LinkedIn detects automation; the sock-puppet account can be limited/banned. Throttle and proxy.
- Generated emails are *predictions* — verify before trusting a specific address maps to a specific person.
- The tool breaks periodically when LinkedIn changes its site; confirm it still works before depending on it.

## Overlaps ("do both")
- Pairs with `[[phonebook-cz]]` — l2u predicts the org's email formats from names; Phonebook shows which addresses IntelX has actually seen, letting you confirm the real convention.

## Trust & verifiability
`trust: community` — a well-known open-source recon tool. Employee names it scrapes are real LinkedIn data; the emails/usernames are algorithmic guesses that must be verified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | initstring-linkedin2username |
| category | social-networks |
| selectorsIn → selectorsOut | employer-org → username, email, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
