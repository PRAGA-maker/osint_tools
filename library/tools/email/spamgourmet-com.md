---
id: spamgourmet-com
name: spamgourmet.com
description: Use when you need disposable, self-destructing email addresses for sock-puppet sign-ups — it forwards a limited number of messages then dies, not a lookup tool.
url: http://spamgourmet.com/
category: email
path:
- email
bestFor: Generating throwaway forwarding addresses to register sock-puppet accounts without exposing a real inbox.
selectorsIn: []
selectorsOut:
- email
status: unknown
pricing: free
costNote: Free disposable-email forwarding service.
opsec: passive
opsecNote: An OpSec-enabling utility for the investigator, not a tool used against a subject. Lets you receive verification mail at a burner address tied to your sock-puppet rather than real infrastructure.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing free disposable-email service; reliability adequate but it is third-party infrastructure you do not control, so treat forwarded mail as non-private.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases: []
tags:
- email
- disposable
- opsec
- Email Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# spamgourmet.com

> A disposable, self-destructing email forwarder — an investigator OpSec utility, not a target-lookup tool.

## When to use
You are building or maintaining a sock-puppet and need a throwaway `email` to register on a platform (people-search site, social network, forum) without linking your real address. Spamgourmet generates addresses that forward a set number of messages to your real inbox, then stop.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a spamgourmet account and set your protected forwarding (real) address.
2. When a site asks for an email, invent an address on the fly: `someword.N.youruser@spamgourmet.com`, where `N` is how many messages to forward before it self-destructs.
3. The verification/confirmation mail is forwarded to your real inbox; after `N` messages the alias dies, limiting spam and traceability.
4. Use only for your own sock-puppet sign-ups — there is no "search" output.

## Inputs → Outputs
- **In:** none (you generate addresses)
- **Out:** a disposable forwarding `email`
- **Empty/negative result looks like:** N/A — it is a utility, not a search; failure mode is a non-delivered/blocked forward (some sites reject disposable domains).

## Gotchas & OpSec
- Many sites blocklist known disposable-email domains, so it may be rejected at signup.
- Human-in-the-loop: requires creating and logging into a spamgourmet account.
- OpSec: keeps your real inbox off third-party sites, but spamgourmet itself can read forwarded mail — never use it for anything sensitive or for the real case email.

## Overlaps ("do both")
- Complements every passive lookup tool that requires registration; pair with a sock-puppet identity kit.

## Trust & verifiability
`trust: community` — established free disposable-mail service; functional but third-party, so assume forwarded content is not private.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spamgourmet-com |
| category | email |
| selectorsIn → selectorsOut | (none) → email (disposable) |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
