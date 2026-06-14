---
id: mailaccess
name: MailAccess
description: Use when you want to run an open-source email checker locally — likely tests whether an email address exists / is accessible; confirm exact behavior from the repo README before relying on it.
url: https://github.com/KatrielMoses/MailAccess
category: email
path:
- email
bestFor: Self-hosted email existence / access checking from a GitHub script.
selectorsIn:
- email
selectorsOut:
- email
status: unknown
pricing: free
costNote: Open-source on GitHub; free to clone and run.
opsec: unknown
opsecNote: Depends on implementation. Email "access"/validation scripts may attempt SMTP probes or login attempts against the target provider, which can be active and may violate terms of service. Read the source before running.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: unverified
trustNote: Personal GitHub repo (KatrielMoses/MailAccess) with no independent reputation signal. Exact functionality not verified — inferred from the name and the "email-search/email-check" listing. Audit the code before use.
missingPersonsRelevance: medium
coverage: []
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases: []
tags:
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# MailAccess

> An open-source GitHub utility apparently aimed at checking email addresses — treat as unverified until you read the README and source.

## When to use
You have an `email` and want a local, scriptable way to test whether it exists / is reachable, and you prefer running your own code over a hosted checker. Because the exact behavior is unconfirmed, use it only after auditing the repository.

## How to use it (`bestInteractionPattern`: cli)
1. Open the GitHub repo and read the README to confirm what it actually does and what credentials/inputs it needs.
2. Clone it: `git clone https://github.com/KatrielMoses/MailAccess`.
3. Install dependencies as documented, then run the script with the target `email`.
4. Pivot: a "valid/exists" result corroborates an address; pair with a hosted verifier like `[[mailtester]]` or `[[mxtoolbox]]` to cross-check.

## Inputs → Outputs
- **In:** `email`
- **Out:** existence/access status for that `email` (best guess from naming)
- **Empty/negative result looks like:** script errors or "not found"; without a verified spec, do not over-trust either outcome.

## Gotchas & OpSec
- Unknown whether it performs passive SMTP RCPT checks or active login attempts; active attempts can be intrusive, logged, or against ToS. **Read the code first.**
- No release reputation; pin a commit and review before executing.
- Treat any result as a weak signal until corroborated.

## Trust & verifiability
`trust: unverified` — single-author GitHub project with no independent corroboration; functionality inferred, not tested. Counted as an unidentified tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mailaccess |
| category | email |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | cli |
| opsec | unknown |
| human-in-loop | yes |
