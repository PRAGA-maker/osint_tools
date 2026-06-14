---
id: reacher-github
name: Reacher Github
description: Use when you need to verify email deliverability at scale or privately — the open-source check-if-email-exists CLI/library that probes SMTP without sending mail.
url: https://github.com/reacherhq/check-if-email-exists
category: email
path:
- email
- email-verification
bestFor: Self-hosted, scriptable, bulk email verification with full control and no third-party logging.
selectorsIn:
- email
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Open source (free, AGPL/commercial dual-licensed). Self-host the binary/Docker; the hosted SaaS API is paid.
opsec: passive
opsecNote: Connects to the target's MX server and runs an SMTP handshake without delivering a message, so the subject is not notified. Run from a clean IP — repeated probes can get an IP greylisted/blacklisted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular, actively maintained Rust project (reacherhq) with thousands of GitHub stars. Verdicts are SMTP-heuristic; Gmail/Yahoo greylisting and catch-all domains yield "unknown."
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- reacher-demo
aliases:
- check-if-email-exists
tags:
- email
- email-verification
- cli
- open-source
source: arf-seed
lastVerified: ''
enrichment: full
---

# Reacher Github

> `check-if-email-exists` (Reacher) — the open-source SMTP email verifier you run yourself, so deliverability checks stay private and scale to lists.

## When to use
You have one or many candidate `email` addresses for a subject and want to confirm which mailboxes actually exist, without handing your query list to a third-party SaaS. Prefer this over the hosted demo when you need bulk throughput, scripting, or no external logging.

## How to use it (`bestInteractionPattern`: cli)
1. Install via Docker (`docker run -p 8080:8080 reacherhq/backend`) or build the Rust binary from the repo.
2. CLI check: `check_if_email_exists someone@example.com`, or POST to the local HTTP API for batches.
3. Parse the JSON: `is_reachable` (`safe`/`invalid`/`risky`/`unknown`) plus `mx`, `smtp`, `misc` (disposable, role-account) sub-objects.
4. Feed confirmed-valid addresses into breach search and social-profile pivots.

## Inputs → Outputs
- **In:** `email`
- **Out:** reachability verdict + MX records, SMTP response, disposable/role flags (`metadata-exif` technical metadata).
- **Empty/negative result looks like:** `invalid` = no mailbox; `unknown` = server blocked the probe (typical for Gmail). Catch-all domains report `risky`.

## Gotchas & OpSec
- Human-in-the-loop: none once installed; needs a host that can make outbound port-25 connections (many cloud/residential ISPs block 25, forcing a proxy).
- OpSec: passive toward the subject, but your IP makes the SMTP connection — use a dedicated/rotating IP; aggressive probing risks blacklisting.

## Overlaps ("do both")
- Same engine as the hosted `[[reacher-demo]]`; overlaps `[[proofy]]`. Self-host this when privacy/scale matter; use the demo for a quick one-off.

## Trust & verifiability
`trust: community` — well-known, actively maintained open-source project; you can read the source. Results remain SMTP-heuristic and bounded by mail-server behavior.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reacher-github |
| category | email |
| selectorsIn → selectorsOut | email → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
