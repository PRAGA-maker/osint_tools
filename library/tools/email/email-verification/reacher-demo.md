---
id: reacher-demo
name: Reacher Demo
description: Use when you want to quickly check if a single email is real/deliverable in-browser — the hosted demo of the open-source Reacher SMTP verifier.
url: https://reacher.email
category: email
path:
- email
- email-verification
bestFor: One-off, no-install email deliverability checks via the hosted Reacher service.
selectorsIn:
- email
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Hosted demo/free checks are rate-limited; the full Reacher SaaS/API is paid. Self-hosting is free (see reacher-github).
opsec: passive
opsecNote: Verifies via MX/SMTP probing without sending an email to the target, so the subject is not alerted.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Front end for the well-known open-source reacherhq verifier; verdicts are SMTP-heuristic (Gmail/Yahoo greylisting and catch-all domains return "unknown"/"risky").
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- reacher-github
aliases: []
tags:
- email
- email-verification
source: arf-seed
lastVerified: ''
enrichment: full
---

# Reacher Demo

> The hosted, click-and-go front end of Reacher — paste an email and get a deliverability verdict without sending mail or installing anything.

## When to use
You have a candidate `email` for a subject and want a fast, in-browser yes/no on whether the mailbox exists before enriching it. Best for single checks; for bulk or repeated use, self-host `[[reacher-github]]`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to reacher.email.
2. Enter the target email and run the check.
3. Read the verdict: `safe` (deliverable), `invalid`, `risky` (catch-all/disposable/full mailbox), or `unknown`.
4. Pivot a confirmed-valid address to breach search and social-profile lookups.

## Inputs → Outputs
- **In:** `email`
- **Out:** deliverability classification plus SMTP/MX signals, disposable & catch-all flags (`metadata-exif`-style technical metadata).
- **Empty/negative result looks like:** `invalid` = mailbox does not exist; `unknown`/`risky` = inconclusive (common for Gmail/Yahoo), do not treat as proof.

## Gotchas & OpSec
- Human-in-the-loop: the public demo is rate-limited; heavy use needs the paid API or self-hosting.
- OpSec: passive — probes the mail server, not the user; no email reaches the subject. Major providers greylist SMTP probes, yielding "unknown."

## Overlaps ("do both")
- Same engine as `[[reacher-github]]` (self-hostable) and overlaps `[[proofy]]` — cross-check "unknown"/"risky" verdicts between them.

## Trust & verifiability
`trust: community` — the open-source Reacher project is well regarded; the demo is the canonical hosted instance. Verdicts are heuristic and limited by SMTP server behavior.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reacher-demo |
| category | email |
| selectorsIn → selectorsOut | email → metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
