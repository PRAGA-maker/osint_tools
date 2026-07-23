---
id: guerrilla-mail
name: Guerrilla Mail
description: Use when an investigation step needs a throwaway inbox — sign up to a target's site/service, receive a verification code, or test a flow without exposing your real email.
url: https://www.guerrillamail.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Instant disposable email inbox for sock-puppet signups and receiving verification codes without an account.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Core disposable inbox is free with no registration; an optional "scramble address" and custom-domain forwarding plan costs ~$9.99/yr. Free tier is fully sufficient for OSINT signups.
opsec: active
opsecNote: This is investigator-side opsec, not a query about a target. Disposable addresses keep your real identity out of a service you're registering with, but Guerrilla inboxes are PUBLIC to anyone who knows/guesses the address — never receive anything sensitive. Many sites block known disposable domains, so signups may be rejected.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, widely-used disposable-mail service; a utility for your own opsec, not a data source about subjects.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- guerrillamail.com
- sharklasers.com
tags:
- disposable-email
- sock-puppet
- privacy-tools
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Guerrilla Mail

> A free, no-signup disposable inbox — spin up a throwaway address to register with a target's service and catch the verification email, keeping your real identity out of it.

## When to use
Not a lookup tool — an opsec utility. Reach for it when a downstream step requires you to *sign up* somewhere (a forum, an app, a service the subject uses) and you don't want that registration tied to a real address. Guerrilla Mail gives you an instant inbox to receive the confirmation/verification code, then discard.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.guerrillamail.com — an inbox and random address are created immediately (no login).
2. Optionally pick a different domain (sharklasers.com, etc.) or set a custom local part; copy the address.
3. Use that address to register on the target service.
4. Watch the inbox for the incoming verification email/code (it appears in seconds). Read it, act, and let the address expire.

## Inputs → Outputs
- **In:** none (you generate an address; no OSINT selector)
- **Out:** a disposable inbox that receives mail — no subject data returned
- **Empty/negative result looks like:** no email arrives — often because the target site blocks disposable-email domains; switch to a different provider or a longer-lived sock-puppet mailbox.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **active** in that you're creating an account somewhere — the disposable address protects your identity, but the signup itself is an action the service logs. Inboxes are public/guessable, so never route password resets for real accounts through it.
- Widely blocklisted: expect some sites to reject `guerrillamail.com`/`sharklasers.com` addresses.

## Overlaps ("do both")
- Complements longer-lived sock-puppet mail and account-existence tools like [[account-live-com]] — Guerrilla Mail is for one-shot receives, while a persistent puppet mailbox is needed when a service requires ongoing access.

## Trust & verifiability
`trust: community` — an established utility judged on reliability, not data quality. It returns your own mail, not investigative data, so there's nothing to corroborate — just don't trust its inboxes with anything private.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | guerrilla-mail |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
