---
id: protonmail-users
name: ProtonMail User Enumeration (PGP key server)
description: Use when you have a candidate Proton (ProtonMail) `email`/`username` and want to confirm it exists — query Proton's public PGP key server and get back a key with a creation timestamp hinting at account age.
url: https://api.protonmail.ch/pks/lookup?op=index&search=<username>@protonmail.com
category: username
path:
- username
- specific-sites
bestFor: Confirming a Proton/ProtonMail address exists and reading its PGP key creation date as an account-age signal.
selectorsIn:
- email
- username
selectorsOut:
- email
- metadata-exif
status: live
pricing: free
costNote: Free, unauthenticated HKP key-server query; no account or payment needed.
opsec: passive
opsecNote: An unauthenticated GET to Proton's public key server. The target is not notified, and you're not logging into anything. Still route through a sock-puppet browser/VPN; the query goes to Proton's infrastructure and could be logged on their side.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: This is Proton's own first-party public key server (HKP), so an existence/keys answer is authoritative — the account has a published key iff it exists and hasn't disabled key publication.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- ProtonMail PKS lookup
- Proton key server enumeration
tags:
- email
- account-existence
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# ProtonMail User Enumeration (PGP key server)

> A first-party existence oracle for Proton addresses: query Proton's public PGP key server and, if a key comes back, the account exists — with a creation timestamp that hints at how old it is.

## When to use
You have a candidate Proton address (`@protonmail.com`, `@protonmail.ch`, `@proton.me`, `@pm.me`) or a `username` you want to test, and you need to confirm whether it's a real Proton account. Because encrypted-mail users are otherwise hard to verify, this is a valuable existence check — and the key's creation date is a rough proxy for account age, useful for triaging leads in a missing-person or identity case.

## How to use it (`bestInteractionPattern`: api)
1. Build the URL, substituting the address: `https://api.protonmail.ch/pks/lookup?op=index&search=<username>@protonmail.com` (swap the domain for `@proton.me` etc. as needed).
2. Open it in a sock-puppet browser or `curl` it.
3. Read the HKP response:
   - A `pub:` line with a key fingerprint, algorithm, and creation timestamp + a `uid:` line = the account EXISTS, and the timestamp is the key's creation date.
   - An empty index / "No results" = no published key for that address (likely doesn't exist, or key publication disabled).
4. Convert the Unix timestamp to a date to estimate account age.
5. Pivot: a confirmed address feeds breach/email-OSINT checks and correlation with other identifiers; account age helps rank multiple candidate addresses.

## Inputs → Outputs
- **In:** Proton `email` / `username`
- **Out:** existence boolean, PGP key fingerprint + algorithm, key creation timestamp (`metadata-exif`-style metadata), email UID
- **Empty/negative result looks like:** an empty HKP index — treat as "no published Proton key," which usually means the address doesn't exist (but a user could have disabled key publishing), not proof of absence across other providers.

## Gotchas & OpSec
- Endpoint drift: Proton has multiple domains (`.ch`, `.com`, `proton.me`); if one host stops responding, try the equivalent on another Proton domain.
- Interpretation: a missing key is strong but not absolute evidence of non-existence; some accounts may not publish keys.
- OpSec: passive and unauthenticated, but still query from a sock-puppet network — Proton can log requests.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` (Microsoft existence oracle) and email-breach tools — each provider needs its own existence check; use this specifically to validate Proton addresses others can't confirm.

## Trust & verifiability
`trust: trusted` — it's Proton's own key server, so the existence/key answer is first-party authoritative; only the "account definitely doesn't exist" inference carries the caveat that a user might not publish a key.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | protonmail-users |
| category | username |
| selectorsIn → selectorsOut | email → email, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
