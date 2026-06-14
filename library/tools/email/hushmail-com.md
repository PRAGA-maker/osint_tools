---
id: hushmail-com
name: hushmail.com
description: Use to recognise hushmail.com, the signup site for the Hushmail encrypted-email provider — a mail service, not an OSINT lookup tool.
url: https://www.hushmail.com/start
category: email
path:
- email
bestFor: Recognising hushmail.com as a privacy-focused email provider (a service a target may use).
selectorsIn:
- email
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Hushmail is a paid encrypted-email provider; this URL is its signup/start page.
opsec: passive
opsecNote: This is an account-signup page for an email service, not a lookup. Nothing about a third party can be queried here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legitimate encrypted-email provider's signup page; duplicate of `[[hushmail]]`. No search/enrichment capability — harvested name/social-profile/username outputs are incorrect.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Hushmail
tags:
- email
- Email Related Sites
relatedTools:
- hushmail
source: uk-osint
lastVerified: ''
enrichment: full
---

# hushmail.com

> The signup/start page for Hushmail, a privacy-focused encrypted email provider — a mail *service*, not an OSINT tool. Duplicate of `[[hushmail]]`.

## When to use
Only to recognise that a subject uses a @hushmail.com `email` (a privacy-conscious behavioural signal). This URL lets you *create* a Hushmail account; it provides no way to look up information about another person.

## How to use it (`bestInteractionPattern`: web-manual)
1. https://www.hushmail.com/start is an account-signup page.
2. There is no public search of Hushmail users.
3. To act on a Hushmail address, run the *email* through breach/account-enumeration tools instead.

## Inputs → Outputs
- **In:** `email` (recognised by @hushmail.com domain)
- **Out:** only the inference of a privacy-oriented provider (`metadata-exif`-style signal)
- **Empty/negative result looks like:** n/a — no lookup exists.

## Gotchas & OpSec
- NOT a search tool; the stub's `name`/`social-profile`/`username` outputs are incorrect.
- Effectively the same as `[[hushmail]]`; consolidate.

## Overlaps ("do both")
- Same provider as `[[hushmail]]`. Pivot any Hushmail address into `[[holehe]]` / `[[have-i-been-pwned]]`.

## Trust & verifiability
`trust: unverified` — legitimate provider, but no verifiable OSINT lookup function; reference/context only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hushmail-com |
| category | email |
| selectorsIn → selectorsOut | email → metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
