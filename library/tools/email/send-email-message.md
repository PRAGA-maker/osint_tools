---
id: send-email-message
name: Send Email Message
description: Use when you have an `email` and want to validate that it's real/deliverable (or send bulk mail) — its email-verifier component returns a validity signal on the address.
url: http://send-email.org
category: email
path:
- email
bestFor: Desktop bulk-email software whose email-verifier can check whether an address is valid and deliverable.
selectorsIn:
- email
selectorsOut:
- email
status: live
pricing: freemium
costNote: Desktop Windows software (an Email Sender plus an Email Verifier). Typically a free/trial tier with paid licensing for full/bulk use; mailing lists stay local on your machine rather than in a cloud service.
opsec: passive
opsecNote: Email *verification* is passive-ish — SMTP validation pings the mail server, not the person, and a well-behaved verifier need not actually deliver a message. Do NOT use the bulk-*sender* against a target: sending mail is active, contacts the subject, and is unsolicited. Only ever use the verifier side for OSINT, from a controlled sending identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: unverified
trustNote: Third-party desktop email-marketing product of unclear provenance (harvested from a curated directory, not independently vetted); trustworthy enough as a local verifier, but scrutinise any downloaded installer.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- send-email.org
- Email Verifier / Email Sender
tags:
- toddington
- curated-directory
- email-addresses
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# Send Email Message

> Desktop bulk-email software (send-email.org); the piece with OSINT value is its **email verifier**, which flags whether an address is real and deliverable.

## When to use
You have a candidate `email` and want to know if it's a live, deliverable address before you build on it. The email-verifier component validates addresses (syntax, domain/MX, mailbox existence via SMTP checks) — a cheap way to confirm an address exists without emailing the person. The product's other half is a bulk *sender*; that is a marketing tool and is **not** an OSINT/investigation use — don't send unsolicited mail to a subject.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install the Windows software from http://send-email.org (scan the installer; it's a local desktop app, so lists/data stay on your machine).
2. Open the **Email Verifier** tool (ignore the bulk-sender for OSINT).
3. Enter the target `email` (or a small list) and run validation.
4. Read the result: valid/deliverable vs invalid/undeliverable/catch-all.
5. Pivot: a confirmed-valid address is worth enriching via account-existence checks (e.g. `[[account-live-com]]`) and breach lookups; an invalid one saves you chasing a dead lead.

## Inputs → Outputs
- **In:** `email`
- **Out:** deliverability/validity signal on the `email`
- **Empty/negative result looks like:** "invalid," "undeliverable," or "catch-all/unknown" — a catch-all domain returns ambiguous results (server accepts anything), so don't over-read a "valid" on such domains.

## Gotchas & OpSec
- Only the verifier is investigative; the bulk sender is off-limits for OSINT (sending mail is active contact with the target).
- SMTP verification can be blocked/greylisted by some mail servers, yielding "unknown" rather than a clean yes/no.
- OpSec: keep verification passive and low-volume; never let it tip into actually messaging the subject. Vet the installer before running it.

## Overlaps ("do both")
- Pair with `[[account-live-com]]` and breach-lookup tools — this confirms the address is *deliverable*, those confirm it's *tied to real accounts/leaks*; together you know both that mail would land and who's behind it.

## Trust & verifiability
`trust: unverified` — a third-party desktop product from a curated directory, not independently vetted. The verification logic is standard SMTP validation (reliable in principle), but treat "valid" as "deliverable," not as proof of the person's identity, and be cautious with the downloaded binary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | send-email-message |
| category | email |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
