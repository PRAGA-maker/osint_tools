---
id: mailcat
name: Mailcat
description: Use when you have a `username` and want to find which email providers it has accounts on — returns existing email addresses via API and SMTP verification across providers.
url: https://github.com/sharsil/mailcat
category: email
path:
- email
bestFor: Enumerating a username into likely existing email addresses across many providers at once.
selectorsIn:
- username
selectorsOut:
- email
status: live
pricing: free
costNote: Free and open-source (GitHub); no account or payment. Run locally in Python.
opsec: active
opsecNote: Mailcat verifies addresses by touching mail-provider APIs and SMTP servers — an ACTIVE probe. Providers may rate-limit, block, or log your IP, and SMTP checks are increasingly unreliable as providers harden against them. The mailbox owner is not notified, but your infrastructure is querying theirs — route through a sock-puppet IP and don't hammer.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A popular open-source email-discovery tool; effective but SMTP-based verification is inherently noisy (false positives/negatives) as major providers block or fake responses.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- mailcat
- sharsil/mailcat
tags:
- email-enumeration
- smtp
- python
- cli
source: gh-topic-osint-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Mailcat

> A username-to-email enumerator: run one handle and it checks, via API and SMTP, which providers have a `<username>@provider` mailbox that actually exists.

## When to use
You have a `username` and want to find the subject's likely email addresses — the `<username>@gmail.com` / `@yahoo.com` / `@outlook.com` style permutations that actually exist. Discovered emails are high-value pivots: they feed breach checks, account-existence oracles, and further OSINT. Reach for it when a handle needs to become a set of real email addresses.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/sharsil/mailcat and install (Python).
2. Run it against a handle, e.g. `python mailcat.py <username>`.
3. Route through a sock-puppet VPN/proxy — checks hit provider servers from your IP.
4. Read the output: providers where `<username>@provider` appears to exist (via API/SMTP verification).
5. Verify and pivot: confirm each candidate with an account-existence oracle (`[[account-live-com]]`) or a different verifier before trusting it; then feed confirmed emails into breach checks and email-OSINT.

## Inputs → Outputs
- **In:** `username`
- **Out:** existing `email` addresses across the checked providers
- **Empty/negative result looks like:** no verified addresses — the handle isn't used as an email local-part, or (very commonly) providers blocked/faked the SMTP responses so nothing could be confirmed. Absence here is weak evidence given SMTP hardening.

## Gotchas & OpSec
- **SMTP verification is unreliable now** — Gmail/Outlook and others block or return non-committal responses, causing false positives and negatives. Treat results as candidates, not confirmations.
- Active probing can get your IP rate-limited or blocked; go slow and use a sock-puppet IP.
- OpSec: **active** — you're querying mail infrastructure; the owner isn't alerted but your requests are logged.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` (Microsoft existence oracle) and holehe-style email-account checkers — Mailcat guesses which addresses exist; those confirm existence and enrich a known address. Guess here, verify there.

## Trust & verifiability
`trust: community` — a capable open-source tool, but its verification method is degraded by modern provider defenses. Confirm every candidate email through an independent oracle before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mailcat |
| category | email |
| selectorsIn → selectorsOut | username → email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
