---
id: encrypt-gmail-ciphermail-addons-mozilla-org
name: encrypt gmail ciphermail (addons.mozilla.org)
description: Use when you want to encrypt/decrypt Gmail messages in Firefox (operational email security for the investigator) — not an OSINT lookup; it returns nothing about a target.
url: https://addons.mozilla.org/en-US/firefox/addon/encrypt-gmail-ciphermail/?src=search
category: email
path:
- email
bestFor: Encrypting your own Gmail in-browser (investigator OpSec hygiene).
selectorsIn: []
selectorsOut: []
status: unknown
pricing: free
costNote: Free Firefox add-on (CipherMail).
opsec: passive
opsecNote: A client-side email-encryption add-on for your own account; it does not query or contact any target. Relevant to protecting your communications, not to investigating someone.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: Distributed via Mozilla's add-on store (CipherMail); a utility add-on, not an investigative tool. Add-on maintenance/availability not re-verified.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- CipherMail Gmail encryption
tags:
- email
- encryption
- opsec
- Email - Covert IP Trackers
source: uk-osint
lastVerified: ''
enrichment: full
---

# encrypt gmail ciphermail (addons.mozilla.org)

> A Firefox add-on (CipherMail) for encrypting and decrypting Gmail messages in the browser — an operational-security utility for the investigator, not an OSINT data source.

## When to use
When you, the investigator, need to send/receive encrypted email from a Gmail account — e.g. coordinating sensitive missing-persons details with a partner. It produces no intelligence about a subject; it protects your own correspondence. The uk-osint "Covert IP Trackers" label is a miscategorization; this is an encryption add-on.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the add-on from the Mozilla add-ons page in Firefox.
2. Sign in to your Gmail and grant the add-on the requested permissions.
3. Use its encrypt/decrypt controls when composing or reading messages.
4. There is no investigative "output" to pivot from — this is purely a comms-security control.

## Inputs → Outputs
- **In:** your own email content (not a target selector)
- **Out:** none relevant to investigation
- **Empty/negative result looks like:** N/A — it is a utility, not a query tool.

## Gotchas & OpSec
- Human-in-the-loop: requires logging into your Gmail and granting extension permissions.
- Verify the add-on is still maintained/available before trusting it with sensitive mail; browser add-ons are deprecated frequently.
- It does nothing to a target and gives you no data about anyone — do not list it as a discovery tool.

## Overlaps ("do both")
- Operational-security category only; no investigative overlap with the email-lookup tools in this library.

## Trust & verifiability
`trust: community` — a Mozilla-store add-on (CipherMail) categorized here for completeness; it is a comms-security utility, not an OSINT lookup, and its current availability was not re-verified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | encrypt-gmail-ciphermail-addons-mozilla-org |
| category | email |
| selectorsIn → selectorsOut | (none; investigator OpSec utility) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (account-login) |
