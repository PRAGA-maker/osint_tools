---
id: phonebook-cz
name: Phonebook.cz
description: Use when you have a `domain` and want to enumerate every email address, subdomain, and URL Intelligence X has indexed for it — returns email and domain.
url: https://phonebook.cz/
category: email
path:
- email
bestFor: Bulk-enumerating email addresses and subdomains associated with a domain via Intelligence X's index.
selectorsIn:
- domain
- email
selectorsOut:
- email
- domain
status: live
pricing: freemium
costNote: Free to query with a capped number of returned results per search; the full result set and API require an Intelligence X account (paid tiers). The free web tier is enough for most enumeration.
opsec: passive
opsecNote: Queries Intelligence X's own index — it does not touch the target's mail server or website, so nothing is sent to the target's infrastructure. Only your query and IP reach IntelX.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A front-end to Intelligence X, a reputable data-search company. Results are as complete as IntelX's crawl; a null result means "not in their index", not "does not exist".
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Phonebook
- IntelX Phonebook
- phonebook.cz
tags:
- email-enumeration
- domain-recon
- intelligence-x
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Phonebook.cz

> Intelligence X's Phonebook — point it at a domain and it lists every email address, subdomain, and URL that IntelX has indexed for it.

## When to use
You have a `domain` (a company, organisation, or an email's domain part) and want to enumerate the email addresses that exist under it — for finding an individual's likely work address, mapping an organisation's people, or expanding from one known email to the naming pattern (`first.last@`, `flast@`) that reveals others. Also enumerates subdomains and URLs for infrastructure recon.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://phonebook.cz/.
2. Enter the `domain` (e.g. `example.com`) and choose the result type: **Email addresses**, **Domains/subdomains**, or **URLs**.
3. Run the search and read the list. For emails you get every indexed `first.last@domain`-style address, which reveals the org's address convention.
4. If results are truncated by the free cap, refine (search a subdomain) or use an IntelX account for the full set.
5. Pivot: a discovered email convention lets you predict a named person's address; individual emails feed breach-checkers and email-to-profile tools; subdomains feed infrastructure recon.

## Inputs → Outputs
- **In:** `domain` (or a partial `email`/pattern)
- **Out:** `email` addresses, `domain`/subdomains, URLs under the target domain
- **Empty/negative result looks like:** an empty list — the domain simply isn't well-represented in IntelX's index; try the apex vs. a subdomain, and treat absence as "not indexed", not "no such emails".

## Gotchas & OpSec
- Free tier caps the number of returned results; the tail may be hidden without an IntelX account.
- Data reflects IntelX's crawl date — addresses can be stale, and freshly-created ones absent.
- Passive: nothing is sent to the target's mail server or site; you query IntelX only.

## Overlaps ("do both")
- Pairs with an email-permutation/verification tool — Phonebook gives you the real naming convention and known addresses; a verifier confirms whether a predicted address for a specific person actually exists.

## Trust & verifiability
`trust: community` — backed by Intelligence X, a well-known data-search firm. The addresses it returns were really seen by their crawler; completeness is bounded by their index and the free-tier cap.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phonebook-cz |
| category | email |
| selectorsIn → selectorsOut | domain, email → email, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
