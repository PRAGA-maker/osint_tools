---
id: easy-disposable-email-address-extension-chrome
name: Easy Disposable Email Address Extension (Chrome)
description: Use when a sock-puppet registration or verification needs a throwaway inbox on the spot — opens a disposable email address/inbox in a new tab; no real address exposed.
url: https://chromewebstore.google.com/detail/easy-disposable-email-add/mkpfodpjhekjdhkchalfflggeoamfajh
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: One-click throwaway email inbox for sock-puppet sign-ups and one-time verification codes.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free Chrome extension. Note it is old (last updated 2017) and simply front-ends a disposable-email provider — modern services often work as well or better.
opsec: passive
opsecNote: The point is OpSec — keep your real address out of sock-puppet registrations. But disposable inboxes are public/guessable and unencrypted: never use them for anything you must keep private, for account-recovery emails, or for a persona you need to keep long-term (they expire). Treat everything sent there as readable by others.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A small, abandoned-looking third-party extension (unchanged since 2017) that relies on external disposable-email sites; convenient but not something to trust with anything sensitive.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- disposable email Chrome extension
- temporary email extension
tags:
- opsec
- disposable-email
- sock-puppet
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Easy Disposable Email Address Extension (Chrome)

> A one-click throwaway-inbox button for your investigation browser — grab a disposable email for a sock-puppet sign-up without ever exposing a real address.

## When to use
You're building or operating a sock puppet and a site demands an email to register or send a verification code you just need to read once. This extension spins up a disposable inbox in a new tab so your real (or persona-critical) address never touches the site.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension into your dedicated sock-puppet browser profile.
2. When a form asks for an email, right-click where you need it (or use the toolbar action) to open a disposable inbox in the next tab.
3. Paste the throwaway address into the sign-up, then watch the disposable inbox for the confirmation/verification message.
4. Read the code/link and move on — assume the inbox will vanish and that anyone could read it.

## Inputs → Outputs
- **In:** none — it generates an address on demand
- **Out:** none as a selector — a temporary email address and its public inbox
- **Empty/negative result looks like:** no message arriving usually means the target blocks known disposable-email domains — fall back to a different disposable provider or a dedicated persona mailbox.

## Gotchas & OpSec
- Many sites block disposable-email domains outright — keep a real persona mailbox as backup for personas you need to persist.
- Disposable inboxes are public and ephemeral: never route password resets, sensitive codes, or anything you must keep private through them.
- Dated extension (2017) and unverified maintainer — vet it, or just use a reputable disposable-mail website directly.

## Overlaps ("do both")
- Same function as web services like 10MinuteMail / temp-mail and persona-mailbox setups; use the extension for speed, a real persona inbox when the account must last.

## Trust & verifiability
`trust: unverified` — a small, stale third-party extension fronting external services; fine for throwaway sign-ups, but keep anything sensitive far away from it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | easy-disposable-email-address-extension-chrome |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
