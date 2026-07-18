---
id: githubrecon
name: GitHub Recon (kriztalz)
description: Use when you have a GitHub `username` or `email` and want the account's exposed data — a free browser tool returning associated `email`s (incl. historical commit emails), account dates and public SSH keys.
url: https://kriztalz.sh/github-recon/
category: social-networks
path:
- social-networks
bestFor: Pulling a GitHub user's leaked/committed email addresses and account metadata from a username or email.
selectorsIn:
- username
- email
selectorsOut:
- email
- social-profile
status: live
pricing: free
costNote: Free and browser-based; no account or install. Queries GitHub's public API/data.
opsec: passive
opsecNote: It reads GitHub's public data — the target isn't notified. The lookup runs from your browser against GitHub; the site states it doesn't store queries, but treat any third-party tool cautiously and use a research browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of a community OSINT toolkit (kriztalz.sh); it surfaces genuinely public GitHub data — verify the emails it returns are actually the target's.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- github-search
- gravatar
- domainrecon
- faviconhash
- metadata-viewer
- pgpkeyanalyser
- searchdorks
- traceroutevisualizer
aliases:
- github-recon
- kriztalz github recon
tags:
- github
- email-discovery
- developer-osint
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# GitHub Recon (kriztalz)

> A one-box GitHub reconnaissance tool: give it a username or email and it returns the account's public emails — including addresses leaked in old commits — plus account dates and public SSH keys.

## When to use
Your subject is (or might be) a developer with a GitHub presence, and you have a `username` or an `email` to test. Developers routinely leak their real email in git commit metadata even when it's hidden on the profile, so a GitHub account is a strong pivot from a handle to a real email (and back). This tool automates the common recon: username → associated emails/account age/SSH keys, or email → which GitHub account it belongs to. Great for tying a coding handle to a real identity or confirming an email is in active use.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://kriztalz.sh/github-recon/.
2. Enter the target GitHub `username` (or an `email` to reverse-lookup the account).
3. Read the results: account creation/last-activity dates, associated `email` addresses (including ones recovered from public commit history), and public SSH keys.
4. Treat surfaced emails as *candidates* — confirm they're the target's (e.g. cross-reference with commits, other breaches, or an email-verification tool) before relying on them.
5. Pivot: a recovered email feeds account-existence/breach tools; the handle feeds cross-platform username search; SSH keys can corroborate device/identity linkage. Combine with `[[github-search]]` for content dorking.

## Inputs → Outputs
- **In:** GitHub `username` or `email`
- **Out:** associated `email`s (profile + historical commit emails), account age/dates, public SSH keys, the `social-profile` (GitHub account)
- **Empty/negative result looks like:** no emails found — the user may have used GitHub's `noreply` commit privacy from the start, or have no public commits. Absence of a leaked email isn't proof none exists; check their repos' commit history manually.

## Gotchas & OpSec
- Emails recovered from old commits may be stale or a throwaway — verify before treating as the subject's primary address.
- Only sees *public* data; private repos and privacy-enabled commits won't leak.
- Third-party tool: it exposes GitHub's public data, but run it from a research browser and don't feed it anything sensitive beyond the target selector.

## Overlaps ("do both")
- Pairs with `[[github-search]]` (dorking repos/code for a subject's mentions and secrets) and `[[gravatar]]` (an email → avatar/profile pivot). Use GitHub Recon to get the email, then Gravatar/breach tools to expand it.

## Trust & verifiability
`trust: community` — a community OSINT toolkit tool. It surfaces genuinely public GitHub data (so nothing fabricated), but attribution is on you: confirm a recovered email actually belongs to your subject before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | githubrecon |
| category | social-networks |
| selectorsIn → selectorsOut | username, email → email, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
