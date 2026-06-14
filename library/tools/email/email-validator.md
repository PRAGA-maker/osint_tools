---
id: email-validator
name: Email Validator
description: Use when you want a quick syntax/MX/deliverability check on a single email address via a lightweight web form — returns validity/metadata only (no profile data).
url: https://chema.ga/emailvalidator/index.php
category: email
path:
- email
bestFor: Lightweight syntax/MX validity check of an email address.
selectorsIn:
- email
selectorsOut:
- metadata
status: unknown
pricing: free
costNote: Free hobby-hosted web form.
opsec: passive
opsecNote: Validation-style lookup (syntax/MX, possibly SMTP probe). An SMTP-handshake check can touch the recipient mail server; the address owner is not directly notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Hobby tool on a free .ga host with no clear ownership or stability; could not confirm behavior or that it is still online without fetching.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- validation
source: metaosint
lastVerified: ''
enrichment: full
---

# Email Validator

> A minimal hobby-hosted web form that, by name, checks whether an email address is syntactically and (likely) MX-valid — not an investigative pivot tool.

## When to use
You only need to know whether an `email` is well-formed and points to a real mail domain before spending effort on it. It does not return profiles, names, or accounts, so it is a hygiene step, not a discovery step.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the page and enter the `email` in the form.
2. Submit and read the validity verdict (expected: syntax OK, domain/MX present, possibly a deliverability guess).
3. Pivot: if valid, hand the address to a real lookup (`[[email-reputation]]`, `[[epieos-email-tool]]`); if invalid, discard or correct it.

## Inputs → Outputs
- **In:** `email`
- **Out:** `metadata` (validity / MX / deliverability indication)
- **Empty/negative result looks like:** an "invalid" verdict, or the page failing to load (free-host tools often go offline).

## Gotchas & OpSec
- Hosted on a free `.ga` domain — likely unstable or already dead; verify it loads before relying on it.
- A deliverability check may perform an SMTP probe that touches the destination mail server; avoid for OpSec-sensitive targets.
- No profile output — do not expect identity data.

## Overlaps ("do both")
- Superseded for verification by `[[emailhippo]]` and for investigation by `[[email-reputation]]`; use those instead when available.

## Trust & verifiability
`trust: unverified` — anonymous hobby tool on a throwaway host; behavior described from name/URL only, not confirmed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-validator |
| category | email |
| selectorsIn → selectorsOut | email → metadata |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
