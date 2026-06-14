---
id: proofy
name: Proofy
description: Use when you have an email address and need to confirm it is real/deliverable before investing in it — returns a validity/deliverability verdict without sending mail.
url: https://proofy.io/
category: email
path:
- email
bestFor: Bulk or single email validation — checking whether an address is real, deliverable, disposable, or a catch-all.
selectorsIn:
- email
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free tier with a small number of verification credits on sign-up; paid credit packs for bulk lists.
opsec: passive
opsecNote: Validates via MX/SMTP probing without sending an actual email to the target, so the subject is not notified.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial email-verification SaaS; verdicts are heuristic (SMTP catch-alls and greylisting cause "unknown"/"accept-all" results).
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases: []
tags:
- email
- email-verification
source: osint4all
lastVerified: ''
enrichment: full
---

# Proofy

> Proofy is a commercial email-verification service that tells you whether an address is real and deliverable, without tipping off the owner.

## When to use
You have a candidate `email` for a subject (from a breach, a profile, or a guessed pattern) and need to know it actually exists before spending effort enriching it or attempting outreach. Use it to filter dead/disposable addresses out of a list of guesses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at proofy.io to get free verification credits.
2. Enter a single email or upload a list.
3. Read the per-address verdict: valid / invalid / accept-all (catch-all) / disposable / unknown.
4. Pivot confirmed-valid addresses to breach search, social-profile lookups, or pattern-expansion across the same domain.

## Inputs → Outputs
- **In:** `email`
- **Out:** deliverability verdict, MX/SMTP signals, disposable flag (`metadata-exif`-style technical metadata).
- **Empty/negative result looks like:** "invalid" = mailbox does not exist; "accept-all/unknown" = server can't confirm, so do NOT treat as proof either way.

## Gotchas & OpSec
- Human-in-the-loop: account-login required; free credits are limited.
- OpSec: passive — it probes the mail server, not the user, so no email reaches the subject. Catch-all domains return "accept-all" for everything, which is a false-positive trap.

## Overlaps ("do both")
- Pairs with `[[reacher-github]]` / `[[reacher-demo]]` (open-source SMTP verification) — cross-check when Proofy returns "unknown" or "accept-all."

## Trust & verifiability
`trust: community` — widely used commercial verifier; results are heuristic and limited by SMTP server behavior, so confirm important hits with a second tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | proofy |
| category | email |
| selectorsIn → selectorsOut | email → metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
