---
id: xingdumper
name: XingDumper
description: Use when you have an `employer-org` (a XING company page) and want to enumerate its employees — returns `name`, `social-profile`, and optionally `email`/`phone`.
url: https://github.com/l4rm4nd/XingDumper
category: social-networks
path:
- social-networks
bestFor: Bulk-extracting the employee roster of a company from XING (the DACH-region professional network) in two API calls.
selectorsIn:
- employer-org
selectorsOut:
- name
- social-profile
- email
- phone
status: live
pricing: free
costNote: Free, open-source (Python/Docker). No cost beyond needing a valid XING account for the login cookie.
opsec: active
opsecNote: The script authenticates with YOUR XING login cookie and queries the target company via XING's API — XING can attribute the scraping to that account. Use a dedicated sock-puppet XING account, never a personal one; running at scale risks that account being flagged/banned.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Maintained open-source tool by researcher l4rm4nd (active releases through 2026); code is auditable on GitHub, but output is only as accurate as the self-reported XING profiles it scrapes.
missingPersonsRelevance: medium
coverage:
- de
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- linkedindumper
aliases:
- Xing Dumper
tags:
- Social Media
- Xing
- employee-enumeration
- cli
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# XingDumper

> A CLI scraper that turns a XING company page into a full employee list — the DACH-region counterpart to LinkedIn people-enumeration.

## When to use
You have an `employer-org` linked to a subject and want the roster of people who list that company on XING (Germany/Austria/Switzerland's dominant professional network). Useful for finding colleagues/associates of a missing person, confirming an employer, or building a contact map when the subject or their circle is DACH-based.

## How to use it (`bestInteractionPattern`: cli)
1. Create/log into a sock-puppet XING account and copy its `login` session cookie from the browser.
2. Install: `pip install -r requirements.txt` (or use the Docker image `l4rm4nd/xingdumper`).
3. Run against the company URL, e.g. `python xingdumper.py --url https://www.xing.com/pages/<company> --cookie <login-cookie>` (add `--full` to attempt `email`/`phone`).
4. Read the output (CSV/JSON/SSV): firstname, lastname, position, location, and profile link per employee.
5. Pivot: take each `name`/`social-profile` into cross-platform username/people search; `--full` emails feed email-OSINT.

## Inputs → Outputs
- **In:** `employer-org` (a XING company page URL)
- **Out:** per-employee `name`, position, location, `social-profile`; with `--full`, generated `email`/`phone`
- **Empty/negative result looks like:** an empty roster or auth error — the company has no/hidden XING page, or the login cookie is invalid/expired.

## Gotchas & OpSec
- Human-in-the-loop: needs a valid XING account cookie (account-login); use a sock puppet.
- **Active** and against XING's ToS — scraping is attributable to your account and can get it banned; keep volume low.
- `--full` emails are often *pattern-generated*, not verified — treat them as guesses to confirm, not facts.
- XING coverage is DACH-centric; thin outside German-speaking Europe.

## Overlaps ("do both")
- Pairs with `[[linkedindumper]]` — same technique on LinkedIn; run both to cover a company's staff across both networks (many people are on only one).

## Trust & verifiability
`trust: community` — an auditable, actively-maintained open-source tool; reliability of the *data* depends on self-reported XING profiles, so corroborate names/roles before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xingdumper |
| category | social-networks |
| selectorsIn → selectorsOut | employer-org → name, social-profile, email, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
