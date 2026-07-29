---
id: git-hound
name: git-hound
description: Use when you have a keyword, `domain`, `employer-org`, or username and want secrets/credentials leaked across public GitHub — returns matching code, API keys, and exposed `password`s.
url: https://github.com/tillson/git-hound
category: documents-metadata
path:
- documents-metadata
bestFor: Hunting exposed API keys, credentials, and secrets across all of public GitHub via keyword + regex, with entropy/dictionary false-positive filtering.
selectorsIn:
- domain
- employer-org
- username
selectorsOut:
- password
- email
status: live
pricing: free
costNote: Free and open-source (MIT). CLI. Needs a (free) GitHub account/session to use GitHub's code search; heavy use is subject to GitHub rate limits.
opsec: active
opsecNote: Searching is passive toward the secret's owner, but you authenticate to GitHub, so your account is tied to the queries — use a sock-puppet GitHub account. Finding a live credential doesn't authorise using it; validating a key against the real service is intrusive and often illegal. Report, don't exploit.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Popular, actively maintained OSS by tillson (v3.0, dashboard); reliable tool. Output needs triage — even with entropy/dictionary filters, expect false positives and revoked/dummy keys.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- trufflehog
- gitleaks
- github-search
aliases:
- git-hound
- githound
- tillson git-hound
tags:
- github
- secret-scanning
- credential-leak
- Dorks/Pentest/Vulnerabilities
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# git-hound

> A GitHub secret-hunter: feed it a keyword/domain/org and it sweeps all of public GitHub — code, commits, and history — for exposed API keys, credentials, and secrets, filtering out the noise.

## When to use
You want to know whether a target organisation, domain, or developer has leaked credentials into public GitHub. git-hound queries GitHub's code search with dorks + regex, digs commit history and files, and uses Shannon entropy/dictionary checks to weed false positives. Point it at an `employer-org` name, a `domain` (for internal hostnames/emails in code), or a `username`, and it surfaces exposed secrets. Infrastructure/breach recon; missing-persons relevance is indirect.

## How to use it (`bestInteractionPattern`: cli)
1. Install (Go): `go install github.com/tillson/git-hound@latest`, and configure a (sock-puppet) GitHub account/session it can search with.
2. Run a query: `git-hound --query "acme.com"` or pipe a term: `echo "AKIA" | git-hound`.
3. Add depth with `--dig-commits` / `--dig-files`; use `--rules` for custom regex and `--json` for machine-readable output.
4. Triage results: entropy/dictionary filters help, but confirm each hit is a real, current secret vs a dummy/revoked/example value. Do **not** test keys against live services.
5. Pivot: extract leaked `email`s/usernames/hostnames into your enrichment chain; responsibly report exposed live credentials to the owner.

## Inputs → Outputs
- **In:** keyword / `domain` / `employer-org` / `username`.
- **Out:** matching code and, potentially, `password`/API keys and `email`s exposed in public repos.
- **Empty/negative result looks like:** no matches — nothing public under that term, or GitHub rate-limited/blocked the search. Absence isn't proof nothing leaked (private repos and past-deleted code aren't covered).

## Gotchas & OpSec
- Human-in-the-loop: needs a GitHub login; results require manual triage.
- OpSec: queries are tied to your GitHub account — use a sock puppet. Interception of the *secret* is passive; **using** a found credential is not — that's unauthorised access. Report to the owner; never exploit.
- False positives and stale/revoked keys are common; a match is a lead, not a confirmed live secret.
- Respect GitHub's terms and rate limits; aggressive scanning can get an account throttled/banned.

## Overlaps ("do both")
- Overlaps with `[[trufflehog]]` / `[[gitleaks]]` — those scan specific repos/history you clone (deeper per-repo, incl. private with access); git-hound scans *all public* GitHub broadly. Use git-hound to discover, TruffleHog/Gitleaks to deep-scan a found repo.
- Complements `[[github-search]]` for manual dorking.

## Trust & verifiability
`trust: community` — well-maintained, widely used OSS. The tool is reliable; its findings are raw and need verification (real vs dummy, current vs revoked) before you act — and acting on a live credential is a legal line, not just a technical one.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | git-hound |
| category | documents-metadata |
| selectorsIn → selectorsOut | domain, employer-org, username → password, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
