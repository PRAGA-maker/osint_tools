---
id: fakemailgenerator-com
name: fakemailgenerator.com
description: Use when you need a disposable inbox to register sock-puppet accounts during an investigation (investigator OpSec) — it creates throwaway email; it does not look anyone up.
url: http://www.fakemailgenerator.com/
category: email
path:
- email
bestFor: Spinning up disposable/throwaway inboxes for sock-puppet account creation.
selectorsIn: []
selectorsOut:
- email
status: live
pricing: free
costNote: Free disposable-email service.
opsec: passive
opsecNote: A temp-mailbox provider for your own use; it does not contact or reveal any target. Note these inboxes are public/insecure — anyone with the address can read them; never use for real accounts you own.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-known free disposable-email site; works as advertised but inboxes are public and ephemeral.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- fake mail generator
- temp mail
tags:
- email
- disposable
- sockpuppet
- Email Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# fakemailgenerator.com

> A free disposable-email service that hands you a throwaway inbox on the spot — an investigator OpSec utility for creating sock-puppet accounts, not a lookup tool.

## When to use
When you need a burner `email` to register an OSINT sock-puppet account (e.g. to view a gated social profile) without exposing your real address. It returns no intelligence about a subject — it is a means to operate safely.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site; it auto-generates a temporary address (pick a domain/alias if desired).
2. Use that address to sign up for the target service.
3. Refresh the public inbox to read the verification/confirmation email.
4. There is no investigative output; the value is the burner identity, not data about a person.

## Inputs → Outputs
- **In:** none (you request an address)
- **Out:** `email` (a disposable address you control temporarily)
- **Empty/negative result looks like:** N/A — it always issues an address; "failure" is a verification mail never arriving (some services block disposable domains).

## Gotchas & OpSec
- Inboxes are PUBLIC and shared — anyone can read mail to a given address; never use for anything you need to keep private or own long-term.
- Many platforms blocklist known disposable domains, so sign-ups may be rejected.
- OpSec: this is *your* hygiene tool; it does nothing to a target and leaks nothing about your case.

## Overlaps ("do both")
- Operational tooling for sock-puppet creation; pairs conceptually with any gated lookup where you need a throwaway account.

## Trust & verifiability
`trust: community` — a well-known free disposable-email service that works as described; treat its inboxes as public and ephemeral.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fakemailgenerator-com |
| category | email |
| selectorsIn → selectorsOut | (none) → email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
