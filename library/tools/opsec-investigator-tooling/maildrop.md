---
id: maildrop
name: MailDrop
description: Use when you need a throwaway `email` inbox to register sock-puppet accounts without exposing your own address — returns a disposable @maildrop.cc address and its inbox.
url: https://maildrop.cc/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Free disposable email for receiving verification links during sock-puppet account creation.
selectorsIn: []
selectorsOut:
- email
status: live
pricing: free
costNote: Free, no signup; a GraphQL API is available for automated retrieval.
opsec: passive
opsecNote: OpSec plumbing — it keeps your real address out of sock-puppet registrations. But maildrop inboxes are PUBLIC to anyone who knows the address and are not secure: never use it for anything sensitive, for accounts you need to keep, or where inbox exposure would burn the persona.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running free disposable-mail service with spam filtering (Heluna); reliable for its purpose but explicitly non-private and ephemeral.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Maildrop
- maildrop.cc
tags:
- opsec-investigator-tooling
- disposable-email
- sock-puppet
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# MailDrop

> A free, no-signup disposable inbox — a burner `email` for receiving verification mail when standing up sock-puppet accounts.

## When to use
You are creating a throwaway persona and a site needs a working email for the confirmation link, but you don't want to expose your real (or reusable) address. MailDrop gives you an instant @maildrop.cc inbox you can check in the browser or via API — good for one-off, low-value registrations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://maildrop.cc/ and pick/generate an address like `something@maildrop.cc`.
2. Use that address in the sign-up form of the target service.
3. Return to MailDrop and open the inbox for that alias to read the verification email and click the link.
4. Pivot: the confirmed sock-puppet account is now usable for OSINT collection. For personas you must keep, use a dedicated real mailbox instead.

## Inputs → Outputs
- **In:** none (you invent an address)
- **Out:** a disposable `email` address and its received-mail inbox
- **Empty/negative result looks like:** an empty inbox — the site never sent (check spam-filtering/blocklists) or the alias was mistyped; some services block known disposable domains.

## Gotchas & OpSec
- Inboxes are PUBLIC — anyone who guesses/knows the alias can read it. Never receive password resets or anything sensitive.
- Ephemeral: messages are auto-purged; don't rely on it for anything you must retain.
- Many services blacklist maildrop.cc — have a fallback disposable/real provider.

## Overlaps ("do both")
- Pairs with sock-puppet browser setups (`[[librewolf]]`) and phone-verification workarounds — MailDrop covers the email step; you still need identity separation and sometimes a burner number.

## Trust & verifiability
`trust: community` — a dependable, long-lived free service for exactly one job; by design it is neither private nor durable, so use it only for disposable registrations.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maildrop |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
