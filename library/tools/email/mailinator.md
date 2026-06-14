---
id: mailinator
name: Mailinator
description: Use when you have (or suspect) a @mailinator.com disposable address and want to read its PUBLIC inbox, or need a throwaway public inbox to receive a one-time signup code.
url: https://www.mailinator.com
category: email
path:
- email
bestFor: Reading public disposable inboxes and receiving throwaway signup mail.
selectorsIn:
- email
- username
selectorsOut:
- email
- metadata-exif
status: live
pricing: freemium
costNote: Public inboxes are free; private domains, retention, and API are paid.
opsec: passive
opsecNote: Reading a public Mailinator inbox is passive — anyone can open any inbox with no login. But remember the inverse: any mail YOU send to a mailinator address is world-readable, so never send sensitive content there.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Mailinator is a long-running, widely documented public disposable-email service. Behavior (public, password-less, auto-expiring inboxes) is well established.
missingPersonsRelevance: high
coverage: []
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases: []
tags:
- email
- disposable-email
source: metaosint
lastVerified: ''
enrichment: full
---

# Mailinator

> Public, password-less disposable-inbox service — every @mailinator.com address has an open inbox anyone can read, and it doubles as a throwaway receiver for signup codes.

## When to use
- You have a subject's `email` or a guessed `username` and suspect they used a `*@mailinator.com` address; you can open that inbox directly to see what mail (signup confirmations, services used) landed there.
- You are building a sock puppet and need a quick, no-signup inbox to catch a one-time verification code.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to mailinator.com and type the inbox name (the part before @mailinator.com) — or just visit and enter any `username`.
2. The inbox loads with no password; read messages and headers (`metadata-exif`-style mail headers can reveal sending services/IPs).
3. To receive: have a site send a code to `anything@mailinator.com`, then open that inbox to read it.
4. Pivot: services that emailed the inbox reveal where the subject registered; sender headers can pivot to domains/IPs.

## Inputs → Outputs
- **In:** `email` or `username` (the inbox name)
- **Out:** message contents + mail headers (`email`, `metadata-exif`)
- **Empty/negative result looks like:** empty inbox (never used, already auto-expired — public mail is purged quickly, often within hours).

## Gotchas & OpSec
- Everything in a public inbox is world-readable; do not route anything confidential through Mailinator and assume the subject knew it was public too.
- Public inboxes auto-delete fast, so evidence is ephemeral — screenshot/preserve immediately.
- Private/custom domains and longer retention require a paid plan and login.

## Trust & verifiability
`trust: trusted` — established, openly documented service with stable, well-understood behavior. Capability verified by common knowledge.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mailinator |
| category | email |
| selectorsIn → selectorsOut | email, username → email, metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
