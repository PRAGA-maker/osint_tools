---
id: sourcegraph
name: Sourcegraph (Public Code Search)
description: Use when you have a `username`, `email`, key, or code string and want to search across public open-source repositories at scale — returns email, social-profile, domain leads from code.
url: https://sourcegraph.com/search
category: documents-metadata
path:
- documents-metadata
bestFor: Powerful regex/structural search across millions of public repos for a person's code, commit emails, or leaked secrets.
selectorsIn:
- username
- email
- domain
selectorsOut:
- email
- social-profile
- domain
status: live
pricing: freemium
costNote: Public code search on sourcegraph.com is free to use; a free account unlocks higher limits and features. Sourcegraph's paid product is for enterprise/private-code deployments (not needed for public OSINT search).
opsec: passive
opsecNote: You search an index of already-public code — you don't clone or contact the target's repos, so it's passive against the subject. Queries are tied to your Sourcegraph session/account; use a sock-puppet account if you'd rather not attach the searches to you.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Sourcegraph is a well-established code-search company; results come directly from public repository contents. Access terms to the public index have shifted over time — confirm current sign-in requirements when you use it.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- github-search
- grep-app
- gh-archive
tags:
- code-search
- github
- secrets
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Sourcegraph (Public Code Search)

> A fast, regex- and structural-search engine over millions of public repositories — go beyond GitHub's own search to find a developer's code, the emails in their commits, and secrets they leaked.

## When to use
You have a developer `username`, a commit `email`, an API key, a distinctive code string, or a `domain` and want to find it across open-source code at large — to map a person's projects, recover an identity from a commit email, spot leaked credentials/config referencing your target, or trace where a code snippet originated. Cross-host (not just GitHub), with more powerful query operators than native code search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to sourcegraph.com/search (sign in for higher limits).
2. Enter a query — plain terms, `regex:` patterns, or structural search; filter with `repo:`, `file:`, `lang:`, `author:`.
3. Search for the target selector: a username/email, a key pattern, or a unique string.
4. Open matches to read the surrounding code and repo — extract emails, handles, referenced domains, and author identities.
5. Pivot: a commit `email` → email/breach search; a repo owner → their `social-profile`; a referenced `domain`/endpoint → infrastructure research.

## Inputs → Outputs
- **In:** `username`, `email`, key, code string, or `domain`
- **Out:** code matches revealing `email`s, `social-profile` (repo owners/authors), and referenced `domain`s
- **Empty/negative result looks like:** no matches — meaning the string isn't in the indexed public corpus (private repos and unindexed hosts won't appear), not that it exists nowhere. Cross-check GitHub search and other code-search tools.

## Gotchas & OpSec
- Indexes **public** code only; private/enterprise repos are invisible here.
- Access requirements to the public index have changed over time — you may need a free account; confirm at use.
- Handle discovered secrets ethically and lawfully — finding a leaked key doesn't authorise using it.

## Overlaps ("do both")
- Pairs with `[[github-search]]` and `[[grep-app]]` (different indexes/operators — run all three), and with `[[gh-archive]]` for historical GitHub *activity* rather than current code contents.

## Trust & verifiability
`trust: trusted` — an established provider searching real public repository contents. Matches are verifiable by opening the source file; confirm a code-derived identity across commits before attributing it to a person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sourcegraph |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, email, domain → email, social-profile, domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
