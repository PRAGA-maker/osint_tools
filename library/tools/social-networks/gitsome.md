---
id: gitsome
name: gitSome
description: Use when you have an `email`, `username`/org, or `domain` and want to pivot through GitHub — extracts commit emails, maps emails to GitHub accounts, and finds org members — returns email, username, and employer-org links.
url: https://github.com/chm0dx/gitSome
category: social-networks
path:
- social-networks
bestFor: Extracting email addresses from a GitHub user/org's commits and mapping an email back to the GitHub account that authored it.
selectorsIn:
- email
- username
- domain
selectorsOut:
- email
- username
- employer-org
status: live
pricing: free
costNote: Free and open-source Python CLI. A (free) GitHub personal access token is recommended for rate limits and the email→account feature.
opsec: active
opsecNote: Queries the GitHub API, which is logged by GitHub against your token/IP; it does not alert the subject. The tool bundles FireProx to rotate source IPs during recon — only use IP rotation within authorized engagements. Use a dedicated (sock-puppet) GitHub token, never your real identity.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source OSINT tool by chm0dx; it reads public GitHub data via the official API, so results are as authoritative as GitHub's own records.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- gitSome
- chm0dx gitSome
tags:
- Social Media
- Github
- cli
- email-enumeration
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# gitSome

> A GitHub-focused OSINT CLI that harvests commit emails, maps an email to the account that authored it, and enumerates org members and domain-related addresses.

## When to use
You have a GitHub-adjacent selector and want to pivot: a `username`/org whose contributors' `email` addresses you want, an `email` you want to resolve to the GitHub account that used it in a commit, or a `domain` whose employees may have committed with corporate addresses. Strong for connecting a developer persona to a real email (commit author metadata is public), and for tying people to an employer via their org memberships.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/chm0dx/gitSome`, then `pip install -r requirements.txt`.
2. Add a GitHub personal access token (from a sock-puppet account) for higher rate limits and the email→account feature; the email extraction path also needs local `git` + SSH access.
3. Run the relevant mode: search a **domain** for related emails from commits/issues; profile a **user/org** to pull emails and org memberships; scan a **repo's** commits; or convert an **email** to its GitHub account(s).
4. Pivot: a recovered `email` feeds email-OSINT (breach/account-existence checks); an `employer-org` membership corroborates employment; a resolved `username` links the persona across platforms.

## Inputs → Outputs
- **In:** `email`, `username`/org, or `domain`
- **Out:** `email` (commit-author addresses), `username` (GitHub accounts), `employer-org` (org memberships), repo relationships
- **Empty/negative result looks like:** no emails/accounts returned — the user committed only with GitHub's `noreply` address, has no public commits, or the token lacks scope. Absence isn't proof; try other repos the person contributed to.

## Gotchas & OpSec
- Human-in-the-loop: supply a GitHub API token (api-key); without it, rate limits and the email→account mapping are constrained.
- Only public commit metadata is exposed; developers who enable GitHub's email privacy (`noreply`) won't leak a real address.
- OpSec: **active** against GitHub's API (logged to your token). FireProx IP rotation is bundled — reserve it for authorized work; use sock-puppet credentials throughout.

## Overlaps ("do both")
- Complements other GitHub email-harvesters and username enumerators — run gitSome to get the `email`↔`username`↔org links, then hand the recovered email to breach/account-existence tools to widen the identity graph.

## Trust & verifiability
`trust: community` — an open-source tool reading the official GitHub API, so its outputs are grounded in GitHub's real public records. Reliability depends on your token's scope and the target's privacy settings, not on any third-party data broker.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gitsome |
| category | social-networks |
| selectorsIn → selectorsOut | email, username, domain → email, username, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
