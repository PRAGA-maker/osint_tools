---
id: hushmail-canada
name: Hushmail (Canada)
description: Use when you have an `email` on a Hush domain and want to understand what that provider choice implies — returns provider/domain context, not a lookup result.
url: https://www.hushmail.com
category: email
path:
- email
bestFor: Recognising a Hush-family email domain and reading the privacy/behavioural signal it carries.
selectorsIn:
- email
selectorsOut:
- domain
- metadata-exif
status: live
pricing: freemium
costNote: Hushmail is a paid encrypted-email provider (with a limited free tier historically); there is no free public lookup API here. For OSINT this entry is about recognising the domain, not querying a service.
opsec: passive
opsecNote: Simply noting that an address ends in a Hush domain is passive and leaks nothing. Do NOT attempt to log into secure.hushmail.com with the target's address or trigger a password-reset against it — that touches the provider's auth and could alert the owner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hushmail is a long-running (since 1999), reputable Canadian encrypted-email company; the domain signal is authoritative even though there is no investigative API.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- hushmail.com
- hush.com
- encrypted email provider
tags:
- toddington
- curated-directory
- email-addresses
- privacy-provider
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- hushmail
- hushmail-com
---

# Hushmail (Canada)

> A Canadian end-to-end encrypted email provider — for OSINT it is a *domain signal*, not a search tool: an address on a Hush domain tells you the subject chose privacy-first email.

## When to use
You have an `email` and notice it ends in a Hush-family domain (`hushmail.com`, `hush.com`, `hush.ai`, `hushmail.me`, `mac.hush.com`, and a handful of vanity domains Hushmail hosts). That choice is itself intelligence: Hushmail markets heavily to therapists, healthcare and legal practices, and to privacy-conscious individuals. It does not offer a public "is this a real account" oracle, so treat this as an interpretation aid rather than a lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Inspect the domain part of the `email` you already have.
2. If it is a Hush-family domain, record the behavioural signal: the subject deliberately uses an encrypted provider often tied to a profession (health/therapy/legal) or to a privacy motive.
3. Do NOT probe the account. There is no benign existence check here — the login/reset flow at `secure.hushmail.com` is authenticated and any reset attempt notifies the owner.
4. Pivot: run the full address through breach/existence tooling that is designed for it, e.g. `[[account-live-com]]` (only if it is also a Microsoft alias) or a breach-search source, and treat the provider choice as context for the person's threat-awareness.

## Inputs → Outputs
- **In:** `email` (specifically the domain component)
- **Out:** `domain` classification (Hush provider) and the behavioural `metadata-exif`-style inference (privacy-focused / likely professional use)
- **Empty/negative result looks like:** the domain is not a Hush domain — this entry then tells you nothing; move on.

## Gotchas & OpSec
- Human-in-the-loop: none for the passive domain read.
- OpSec: passive so long as you only classify the domain. Actively touching Hushmail's login/reset for the target's address is intrusive and can alert them — don't.
- Don't over-read: plenty of ordinary users pick Hushmail; the signal is "privacy-aware," not "hiding something."

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` and breach-search tooling — those probe existence/exposure of the address, while this only explains what the *provider* choice implies.

## Trust & verifiability
`trust: trusted` — Hushmail is an established provider, so the domain-to-provider mapping is reliable; the caveat is that there is no first-party investigative endpoint to verify a specific account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hushmail-canada |
| category | email |
| selectorsIn → selectorsOut | email → domain, metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
</invoke>
