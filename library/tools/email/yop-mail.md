---
id: yop-mail
name: YOPmail
description: Use when you have a `email` that looks like a YOPmail disposable address and want to read its public inbox, or when you need a throwaway inbox for a sock puppet — returns inbox contents / registration signals.
url: http://www.yopmail.com
category: email
path:
- email
bestFor: Reading the (password-less, public) inbox of any YOPmail disposable address, and generating throwaway inboxes for investigator OpSec.
selectorsIn:
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Completely free; no account or payment. It is a disposable-email service.
opsec: passive
opsecNote: Reading a YOPmail inbox is passive — no login, no notification to anyone. But note YOPmail inboxes are PUBLIC and unauthenticated: anyone who knows the address can read them, and there is zero privacy. For your own OpSec, YOPmail is useful to create burner inboxes for puppet-account signups; never route anything sensitive or real through it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Well-known disposable-email provider; legitimate for its purpose, but inboxes are public and content is ephemeral, so treat anything read there as unverified and transient.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- YOPmail
- yopmail.com
- disposable email
tags:
- toddington
- curated-directory
- email-addresses
- disposable-email
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# YOPmail

> A disposable-email service whose inboxes are public and password-less — useful both to read any YOPmail address's inbox and to spin up burner inboxes for sock-puppet accounts.

## When to use
Two cases. (1) **Investigation:** your subject used a YOPmail address (e.g. to sign up somewhere) — because YOPmail inboxes require no password, you can open that inbox and read whatever landed in it, including registration/confirmation emails that reveal which services the address registered on (`social-profile` leads). (2) **Your OpSec:** you need a throwaway inbox to receive verification emails for a puppet account without exposing a real address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to yopmail.com.
2. **To read an address:** enter the YOPmail username (the part before `@yopmail.com`) — the inbox opens with no password, showing whatever emails it currently holds.
3. Scan for signup/confirmation emails that name the services the address registered with, and any embedded personal details.
4. **To create a burner:** just choose any `name@yopmail.com` and use it at signup; return to yopmail.com to read the incoming mail.
5. Pivot: registration emails reveal accounts (`social-profile`) to investigate; a shared burner address across services can link a subject's accounts.

## Inputs → Outputs
- **In:** `email` (a `@yopmail.com` address / username)
- **Out:** `social-profile` (services revealed by confirmation/registration emails in the inbox)
- **Empty/negative result looks like:** an empty inbox — likely because YOPmail auto-purges mail after a short retention window, or nothing was recently sent there; not proof the address was never used.

## Gotchas & OpSec
- **No privacy by design:** every YOPmail inbox is world-readable; useful to you, but also means anything there is transient and unauthenticated.
- Mail is auto-deleted after a short period — you only see recent messages.
- Only works for YOPmail (and its alias domains) — other disposable providers need their own viewers.

## Overlaps ("do both")
- Pairs with disposable-email detectors and `[[account-live-com]]`-style existence checks — YOPmail confirms an address is disposable and lets you read it; existence tools confirm which mainstream services an address is tied to.

## Trust & verifiability
`trust: unverified` — a legitimate disposable service, but inbox contents are public, ephemeral and easily spoofed; treat anything read there as an unverified lead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yop-mail |
| category | email |
| selectorsIn → selectorsOut | email → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
