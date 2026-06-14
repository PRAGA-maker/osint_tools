---
id: h8mail
name: h8mail
description: Use when you have an email (or list) and want to find breach hits and exposed passwords from public/leak sources.
url: https://github.com/khast3x/h8mail
category: email
path:
- email
bestFor: Bulk email breach hunting and password/credential lookup from a CLI.
selectorsIn:
- email
selectorsOut:
- email
- metadata-exif
status: live
pricing: free
costNote: Free and open-source. Some integrated sources (e.g. HIBP, Hunter, Snusbase) require your own paid API keys for full results.
opsec: passive
opsecNote: Queries breach databases and third-party APIs; never contacts the target. Your API keys and source IP are exposed to the providers you configure.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Mature, widely-used open-source tool (khast3x); 4k+ GitHub stars. Output quality depends entirely on which breach sources/keys you configure.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
aliases: []
tags:
- email-search-email-check
relatedTools:
- have-i-been-pwned
- holehe
source: awesome-osint
lastVerified: ''
enrichment: full
---

# h8mail

> CLI breach hunter: feed it an email (or a file of them) and it pulls breach hits and, where available, plaintext/hashed passwords from leak databases.

## When to use
You have an `email` for a missing person (or an associate) and want to know which breaches it appears in, plus any exposed credentials that might reveal reused usernames, passwords, or recovery clues. Best for batch work — checking a whole list of emails at once.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install h8mail`.
2. Single target: `h8mail -t target@example.com`.
3. Bulk: `h8mail -t emails.txt -o results.csv`.
4. Add power sources by creating a config with API keys (HIBP, Hunter.io, Snusbase, Leak-Lookup, etc.): `h8mail -t target@example.com -c h8mail_config.ini`.
5. Chase local breach dumps ("BreachCompilation"): `h8mail -t target@example.com -bc /path/to/BreachCompilation/`.
6. Read the CSV: each row is a source + the data it returned (password, hash, related email).

## Inputs → Outputs
- **In:** `email` (single or file)
- **Out:** breach source names, exposed passwords/hashes, related `email`/`metadata-exif` fragments
- **Empty/negative result looks like:** all configured sources return zero rows; means no public leak hits (or you have no keys configured for the sources that would hit).

## Gotchas & OpSec
- Human-in-the-loop: most valuable sources need **your own API keys**; without them you get thin results.
- OpSec: passive toward the target, but you reveal your keys/IP to each provider; use a dedicated research key.
- Exposed passwords are sensitive — handle per legal/ethical rules; never attempt to log into the target's accounts.

## Overlaps ("do both")
- Pairs with `[[have-i-been-pwned]]` (authoritative breach index) and `[[holehe]]` (which *services* an email is registered on) — h8mail adds the credential contents HIBP won't show.

## Trust & verifiability
`trust: community` — established open-source project with broad use in the OSINT community; results are only as good as the sources you wire in.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | h8mail |
| category | email |
| selectorsIn → selectorsOut | email → email, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
