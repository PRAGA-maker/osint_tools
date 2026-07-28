---
id: simplelogin
name: SimpleLogin
description: Use when you need a disposable, forwarding `email` alias to register accounts or contact sources without exposing your real inbox — an investigator OpSec tool, not a lookup.
url: https://simplelogin.io/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Creating burner/alias email addresses that forward to your inbox, for sock-puppet registrations and safe contact.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier gives up to 10 aliases and unlimited forwarding; unlimited aliases, custom domains and more mailboxes are paid (Proton-bundled). Open-source, self-hostable for free.
opsec: passive
opsecNote: This protects YOUR identity — it does not touch any target. Aliases hide your real address from services you sign up to and from people you email. Register the SimpleLogin account itself on a clean, non-attributable identity; a subpoena to SimpleLogin/Proton can still unmask the forwarding inbox, so it is privacy, not anonymity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source, acquired by Proton (2022); widely used and audited. Trust the software; remember the provider can be legally compelled.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools: []
aliases:
- simplelogin.io
- SimpleLogin alias
tags:
- opsec
- email-alias
- sock-puppet
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# SimpleLogin

> An email-aliasing service (now part of Proton) that mints forwarding burner addresses — infrastructure for your sock-puppet accounts, not a way to find data on a subject.

## When to use
You are building or maintaining a research/sock-puppet identity and need an `email` you can hand to a site, a data broker, or a source without revealing your real inbox. Each SimpleLogin alias forwards to (and can send from) your true mailbox, so you keep control while compartmentalising per-account. Use it whenever registering for a platform to view a target's content, or when contacting a tipster who should not see your primary address.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Create a SimpleLogin account (free tier) on a clean identity, or self-host the open-source server.
2. Install the browser extension (Chrome/Firefox/Safari) or mobile app, or use the web dashboard at https://app.simplelogin.io/.
3. On any signup form, click the extension to generate a fresh alias (e.g. `random.word@simplelogin.co` or `anything@yourdomain`) and paste it into the email field.
4. Mail sent to that alias forwards to your real inbox; reply from your client and SimpleLogin rewrites the sender so the alias — not your address — is what the other party sees.
5. Disable or delete an alias when a sock-puppet account is retired, cutting that channel without affecting others.

## Inputs → Outputs
- **In:** none (you supply nothing about a target — you generate aliases for yourself)
- **Out:** a working, forwarding `email` alias for operational use (not a selector harvested from a subject)
- **Empty/negative result looks like:** free-tier alias cap (10) reached — you must delete an old alias or upgrade before generating another.

## Gotchas & OpSec
- Human-in-the-loop: creating and managing aliases requires a logged-in SimpleLogin/Proton account.
- This is **your** OpSec, not a lookup: it hides your identity from services and correspondents but is not untraceable — the provider holds the forwarding link and can be legally compelled.
- Register the underlying account and mailbox on a non-attributable identity; don't forward aliases into your personal Gmail if the case is sensitive.

## Overlaps ("do both")
- Pairs with any sock-puppet / burner-phone tooling in this category: SimpleLogin covers the email leg of a research identity while a separate burner number and clean browser profile cover the rest.

## Trust & verifiability
`trust: community` — mature open-source project, acquired by and integrated with Proton, and self-hostable if you want to remove the third-party provider entirely. The code is auditable; the operational caveat is legal compulsion of the provider, not software risk.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | simplelogin |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (account-login) |
