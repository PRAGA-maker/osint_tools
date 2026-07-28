---
id: anonaddy
name: AnonAddy (addy.io)
description: Use when you have an `email` inbox and want disposable forwarding aliases for sock-puppet accounts — returns new alias `email` addresses that forward to you.
url: https://anonaddy.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Creating throwaway email aliases so investigation sign-ups never expose your real address.
selectorsIn:
- email
selectorsOut:
- email
status: live
pricing: freemium
costNote: Free tier gives unlimited standard aliases (username.addy.io), 1 recipient, 10 shared-domain aliases and 10MB/mo bandwidth; Lite $1/mo and Pro $3/mo (billed yearly) add custom domains, more recipients and unlimited bandwidth. Fully open source and self-hostable at no cost.
opsec: passive
opsecNote: This is investigator-side OpSec, not a lookup on a subject. Aliases forward to a real recipient inbox, so treat that recipient as sensitive — use a dedicated puppet inbox, not your personal address. Deactivate or delete an alias the moment a site starts abusing it; a leaked alias points back to your account, not the wider world.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source (GitHub), self-hostable, actively maintained; rebranded from AnonAddy to addy.io. Community-run rather than an accredited data provider.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- addy.io
- anonaddy
- anonymous email forwarding
tags:
- privacy-and-encryption-tools
- email-aliases
- opsec
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# AnonAddy (addy.io)

> An open-source email-alias/forwarding service — spin up disposable addresses so your real inbox never touches an investigation account.

## When to use
You are about to register a sock-puppet account (a social platform, a data broker, a forum) and do not want that site — or a later breach of it — to hold your real `email`. AnonAddy gives you a unique alias per site that silently forwards to a puppet inbox and can be killed independently.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at https://addy.io (formerly anonaddy.com) with a dedicated puppet recipient address; verify it.
2. Pick a username — your aliases live at `anything@<username>.addy.io`, or generate random `.anonaddy.me` aliases.
3. When a site asks for an email, hand it a fresh alias (create on the fly or via the browser extension / API).
4. Mail sent to the alias forwards to your recipient inbox; replies can be routed back through the alias so your real address never appears.
5. Pivot/cleanup: if a site spams or is breached, **deactivate** (silently drop) or **delete** the alias — the rest of your identity is unaffected.

## Inputs → Outputs
- **In:** `email` (a recipient inbox to forward to)
- **Out:** `email` (unlimited forwarding aliases)
- **Empty/negative result looks like:** free-tier bandwidth cap (10MB/mo) exceeded — new mail to aliases bounces until reset or upgrade; not a lookup, so there is no "no results" state.

## Gotchas & OpSec
- Human-in-the-loop: account registration and email verification required before any alias works.
- The alias is only as anonymous as the recipient inbox behind it — never point aliases at your personal Gmail.
- Some sites block known alias domains (`addy.io`, `anonaddy.me`); a custom domain (paid) evades that.
- Self-host if you need the forwarding logs to stay entirely under your control.

## Overlaps ("do both")
- Pairs with disposable-inbox and puppet-management tooling — AnonAddy handles the forwarding address while a separate puppet inbox holds the mail; use both when standing up a durable investigative identity.

## Trust & verifiability
`trust: community` — reputable open-source project (auditable code, self-hostable), but a volunteer/commercial hybrid rather than a vetted enterprise provider; keep that in mind for high-stakes anonymity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | anonaddy |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
