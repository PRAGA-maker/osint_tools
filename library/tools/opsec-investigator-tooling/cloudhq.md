---
id: cloudhq
name: CloudHQ
description: Use when you need Gmail-workflow add-ons for an investigation inbox — export/preserve emails as PDF, block or (actively) plant read-tracking, returning open-time `ip-address`/`geolocation` signals.
url: https://www.cloudhq.net/apps
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A suite of free/freemium Gmail & Chrome extensions for email export/preservation, tracking, and inbox automation on an investigator sock-puppet account.
selectorsIn:
- email
selectorsOut:
- ip-address
- geolocation
status: live
pricing: freemium
costNote: Many individual extensions have a free tier; advanced/bulk features and some apps require a paid CloudHQ subscription. A CloudHQ/Google account is needed to install.
opsec: active
opsecNote: Most features (Save-as-PDF export, tracking blocker) are passive and defensive. But the "Email Tracker" plants a tracking pixel — if you send a tracked message to a subject, opening it reports their `ip-address`, approximate `geolocation`, device and open-time back to you. That is an ACTIVE, intrusive touch on the target; only do it with authorisation, and use the tracking BLOCKER on your own inbound mail.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: unverified
trustNote: CloudHQ is an established SaaS vendor, but these are third-party Gmail add-ons that request broad mailbox permissions — install only on a dedicated sock-puppet Google account, never a real one.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- support-cloudhq-net
aliases:
- cloudHQ Gmail apps
- CloudHQ extensions
tags:
- gmail-tooling
- email-tracking
- workflow-automation
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# CloudHQ

> A large catalog of free/freemium Gmail and Chrome extensions — the investigator-relevant ones are email preservation (Save-as-PDF), a tracking-pixel blocker for your own inbox, and an email tracker that can geolocate a recipient who opens your message.

## When to use
You're running an investigation from a Gmail sock-puppet and want to (a) preserve email evidence cleanly (export threads/attachments to PDF), (b) protect your own OpSec by stripping tracking pixels from mail you receive, or (c) — with authorisation — learn where a subject is by sending a read-tracked email. It's tooling for the analyst's workflow, not a lookup: on its own it produces no records, but the tracking feature can yield an `ip-address`/`geolocation` from a live target.

## How to use it (`bestInteractionPattern`: browser-extension)
1. On a dedicated sock-puppet Google account, go to https://www.cloudhq.net/apps and pick an app.
2. **Save Emails to PDF** — install, then one-click export a thread (with attachments) to PDF/HTML/Text for evidence preservation.
3. **Free Email Tracking Blocker** — install to neutralise tracking pixels in mail sent *to* you, protecting your OpSec.
4. **Email Tracker** (active/authorised only) — sends a tracked message; when the recipient opens it you see open time, device, and IP-derived location.
5. Grant the requested Gmail permissions (this is the account-login gate) — only ever on the throwaway account.

## Inputs → Outputs
- **In:** `email` (the sock-puppet inbox / a message you send)
- **Out:** exported PDF evidence; from the tracker, a recipient's `ip-address` and approximate `geolocation` at open time
- **Empty/negative result looks like:** a tracked email that's never opened (no callback), or a recipient whose client blocks remote images — no location signal returned.

## Gotchas & OpSec
- Human-in-the-loop: installation requires OAuth-granting broad Gmail access — a real risk; isolate to a sock-puppet account.
- The tracker is **active and intrusive**: it touches the target and its accuracy is coarse (IP-geolocation, defeated by VPNs/proxied image loaders). Get authorisation before tracking a person.
- Freemium: expect paywalls on bulk export and advanced apps.

## Overlaps ("do both")
- Part of the same vendor family as `[[support-cloudhq-net]]`; for pure evidence capture, pair with a general screenshot/archiving tool rather than relying on a Gmail add-on alone.

## Trust & verifiability
`trust: unverified` — a legitimate vendor, but third-party mailbox add-ons with broad OAuth scope carry inherent risk; the exported PDFs are verifiable evidence, while tracker geolocation is an inexact lead, not a fix.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloudhq |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | email → ip-address, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
