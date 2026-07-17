---
id: gitxray
name: gitxray
description: Use when you have a GitHub `username` or repo and want deep recon on the account — returns contributor emails, leaked keys, activity-timing patterns, and signs of tampering/fake accounts.
url: https://github.com/kulkansecurity/gitxray
category: social-networks
path:
- social-networks
bestFor: X-raying a GitHub user or repository via the public API to surface identity leaks, activity patterns, and tampering.
selectorsIn:
- username
selectorsOut:
- email
- name
- associate
status: live
pricing: free
costNote: Free, open-source (AGPL-3.0). Runs unauthenticated, but a free GitHub API token is strongly recommended to avoid rate limits.
opsec: passive
opsecNote: It reads only public GitHub REST API data, so the target user is not notified and nothing is posted. Passive. Use a dedicated (sock-puppet) GitHub token for the rate limit, not your real account, to avoid tying the recon to you.
humanInLoop: false
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Actively maintained open-source tool by Kulkan Security (v1.0.20, Jan 2026); it surfaces genuinely public GitHub metadata, so findings are verifiable against GitHub itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
aliases:
- gitxray GitHub OSINT
- kulkansecurity/gitxray
tags:
- github
- osint-cli
- forensics
source: gh-topic-osint-resources
lastVerified: '2026-07-17'
enrichment: full
---

# gitxray

> A command-line "X-ray" of GitHub users and repositories using only public REST APIs — it pulls out contributor emails, leaked keys, activity-timing patterns, and signals of fake or tampered accounts.

## When to use
You have a subject's GitHub `username` (or a repo they contribute to) and want more than the profile page shows. gitxray aggregates public API data to reveal the emails and names embedded in a user's commits and PGP keys, when they're active (timezone/behaviour inference), which accounts and repos they touch (`associate`s), and anomalies like tampered commits or fake accounts. It's ideal for attributing a coder identity, deriving a real email/name from a handle, or vetting an account's authenticity.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install gitxray --upgrade` (needs Python + `requests`).
2. Set a GitHub token in the environment (a sock-puppet account's token) to lift rate limits.
3. Run against a user: `gitxray -o https://github.com/<username>` — or a repo: `gitxray -r https://github.com/<owner>/<repo>`.
4. Read the report (text/JSON/HTML): exposed emails/PGP key names, contributor list, activity timeline, and flagged anomalies. Filter by date for forensic correlation.
5. Pivot: a recovered `email`/`name` feeds email/people OSINT; co-contributors and cross-repo activity map `associate`s; activity timing narrows timezone/geography.

## Inputs → Outputs
- **In:** GitHub `username` (or repository/org URL).
- **Out:** contributor `email`s and `name`s, leaked key identifiers, activity-timing patterns, co-contributors (`associate`), tampering/fake-account flags.
- **Empty/negative result looks like:** a sparse account with no commits/keys yields little — a fresh or privacy-hardened profile leaks nothing. Absence of leaks ≠ absence of the person.

## Gotchas & OpSec
- Human-in-the-loop: supply a GitHub API token (sock-puppet), or you'll hit rate limits fast on any real target.
- It only sees public data — emails come from public commits/keys, so a user who scrubbed those won't expose them.
- Anomaly flags (tampering, fake account) are heuristics — investigate the underlying evidence before concluding.

## Overlaps ("do both")
- Pair with generic username-enumeration and with commit-email tools; feed recovered emails into breach/email OSINT to widen identity.

## Trust & verifiability
`trust: community` — a maintained security-vendor open-source tool over public GitHub APIs. Findings are checkable directly against GitHub, so treat them as verifiable leads and confirm any recovered identifier at source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gitxray |
| category | social-networks |
| selectorsIn → selectorsOut | username → email, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
