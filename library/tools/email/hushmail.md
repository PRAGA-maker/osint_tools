---
id: hushmail
name: Hushmail
description: Use to understand/recognise Hushmail, an encrypted email provider a subject might use — it is a mail service, not an OSINT lookup tool.
url: http://hushmail.com
category: email
path:
- email
bestFor: Recognising Hushmail as a privacy-focused email provider (a service a target may use, not a search engine).
selectorsIn:
- email
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Hushmail is a paid encrypted-email provider (small free/trial tiers historically; now mostly paid plans).
opsec: passive
opsecNote: Hushmail is an email service, not a lookup. There is nothing to query about a third party; you can only recognise a @hushmail.com address as a privacy-conscious signal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Hushmail is a legitimate, long-running encrypted-email provider, but it offers NO search/enrichment capability. Harvested selectors (name/social-profile/phone out) are incorrect — it cannot return those about a target.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- hushmail.com
tags:
- email
relatedTools:
- hushmail-com
source: metaosint
lastVerified: ''
enrichment: full
---

# Hushmail

> A privacy-focused, OpenPGP-capable encrypted email provider — a mail *service*, not an OSINT tool. Relevant only as context when a subject uses a @hushmail.com address.

## When to use
You encounter an `email` on the @hushmail.com domain and want to understand what that implies: the person chose a privacy/encryption-oriented provider, which is a behavioural signal (privacy-conscious, possibly intentionally hard to trace). You cannot search Hushmail for information about a third party.

## How to use it (`bestInteractionPattern`: web-manual)
1. Recognise the domain: a @hushmail.com address signals use of an encrypted-mail provider.
2. There is no public lookup — you cannot query Hushmail for a user's name, phone, or profiles.
3. Investigative value comes from running the *email itself* through breach/account-enumeration tools, not through Hushmail.

## Inputs → Outputs
- **In:** `email` (recognised by domain)
- **Out:** only the inference that the subject uses a privacy-oriented provider (`metadata-exif`-style behavioural signal)
- **Empty/negative result looks like:** n/a — there is no search to run here.

## Gotchas & OpSec
- This is NOT a search tool; the original stub's `name`/`social-profile`/`phone` outputs are wrong and were not fabricated here.
- To make use of a Hushmail address, pivot the email into `[[holehe]]` / `[[have-i-been-pwned]]`, not into Hushmail.

## Overlaps ("do both")
- Duplicate context entry `[[hushmail-com]]` points at the same provider's signup page.

## Trust & verifiability
`trust: unverified` — the provider is legitimate, but as an OSINT resource it has no verifiable lookup function; rating reflects "not an investigative tool," not "untrustworthy company."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hushmail |
| category | email |
| selectorsIn → selectorsOut | email → metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
