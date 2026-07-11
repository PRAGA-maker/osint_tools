---
id: linkedindumper
name: LinkedInDumper
description: Use when you have an `employer-org` and want its staff roster from LinkedIn — a Python tool that dumps employee names, titles, locations, profile links, and generated emails.
url: https://github.com/l4rm4nd/LinkedInDumper
category: social-networks
path:
- social-networks
bestFor: Enumerating a company's employees (names, roles, profile URLs, likely emails) from its LinkedIn page.
selectorsIn:
- employer-org
selectorsOut:
- name
- social-profile
- email
status: live
pricing: free
costNote: Free, open-source (Python; Docker image available). No purchase — but it requires YOUR LinkedIn session cookie to run.
opsec: active
opsecNote: This drives LinkedIn using your li_at session cookie — the activity is attributable to that account and automated scraping violates LinkedIn's ToS, risking rate-limiting or a ban. Use a burner LinkedIn account, not your real one, and throttle. The generated emails are guesses, not verified.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: A known red-team/OSINT enumeration tool (l4rm4nd); it automates LinkedIn's own company-employee listings, so accuracy tracks what LinkedIn shows to your account.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- LinkedIn Dumper
tags:
- linkedin
- employee-enumeration
- red-team
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# LinkedInDumper

> Company-to-people at scale: point it at a firm's LinkedIn and get its employee roster — names, titles, profile links, and guessed emails — in CSV/JSON.

## When to use
You have an `employer-org` and want the people inside it: to find a specific subject known only by their employer, to map colleagues (`associate`s) around a person, or to build an org picture. LinkedInDumper automates LinkedIn's company-employees listing into a structured dump, which is far faster than clicking through profiles by hand.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/l4rm4nd/LinkedInDumper` and `pip install -r requirements.txt` (or use the Docker image).
2. Sign into a **burner** LinkedIn account, grab its `li_at` session cookie from browser dev tools.
3. Run the tool with the target company's LinkedIn URL and your cookie; optionally set an email format and `--output-csv`/`--output-json`.
4. Read the dump: firstname, lastname, title, location, profile URL, and format-generated email per employee.
5. Pivot: a target's confirmed profile/title feeds deeper SOCMINT; colleagues are `associate` leads; generated emails feed email-verification tools before you trust them.

## Inputs → Outputs
- **In:** `employer-org` (its LinkedIn company URL) + your LinkedIn session cookie
- **Out:** employee `name`s, titles, locations, `social-profile` URLs, and *generated* `email` guesses
- **Empty/negative result looks like:** few/no employees — the account's visibility is limited (out-of-network), the company page is small/private, LinkedIn rate-limited you, or the cookie expired. A thin dump often reflects your account's access, not the company's real size.

## Gotchas & OpSec
- Emails are **generated from a pattern**, not verified — validate before using them as fact.
- OpSec: **active** and ToS-violating — the scraping is tied to your LinkedIn account; use a burner, throttle, and expect possible rate-limiting/bans.
- LinkedIn shows different rosters to different accounts; results are account-dependent, not absolute.

## Overlaps ("do both")
- Pairs with `[[linkedin-x-ray-search-tool]]` — the X-ray builder finds specific public profiles via Google with no login footprint, while LinkedInDumper bulk-enumerates a whole company (at higher OpSec cost); use X-ray for a named target, Dumper for org-wide sweeps.

## Trust & verifiability
`trust: community` — a known enumeration tool that surfaces LinkedIn's own data; roster accuracy tracks LinkedIn, but generated emails and out-of-network gaps mean you must verify individual results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkedindumper |
| category | social-networks |
| selectorsIn → selectorsOut | employer-org → name, social-profile, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
