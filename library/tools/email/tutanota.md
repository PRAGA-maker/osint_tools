---
id: tutanota
name: Tutanota
description: Use when you need a privacy-focused encrypted mailbox for sock-puppet accounts, or to recognize a subject's address is a privacy-provider domain — it is an email service (now rebranded Tuta), not a lookup tool.
url: https://tutanota.com
category: email
path:
- email
bestFor: Anonymous/encrypted email provider (now Tuta) usable for investigator sock-puppet inboxes.
selectorsIn:
- email
selectorsOut:
- domain
- metadata
status: live
pricing: freemium
costNote: Free encrypted mailbox with limited storage; paid tiers add storage, custom domains, and aliases. Now branded as Tuta (tuta.com).
opsec: passive
opsecNote: As a provider it is an OpSec asset — create disposable/sock-puppet inboxes for registrations on other OSINT tools. Seeing a @tutanota.com / @tuta.com address on a subject signals a privacy-conscious user, but reveals no identity by itself.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Tutanota is the legacy brand of Tuta, a well-established German end-to-end-encrypted email provider. It is a mail service, not an OSINT identity source — the seed's name/phone/social-profile outputs are incorrect.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- tuta-com
aliases:
- Tuta
- tuta.com
tags:
- email
- encrypted-email
- sock-puppet
source: metaosint
lastVerified: ''
enrichment: full
---

# Tutanota

> The encrypted email provider Tutanota (now rebranded Tuta) — primarily an OpSec asset for sock-puppet mailboxes, and a behavioral signal when a subject uses it. Not a lookup tool.

## When to use
Two honest uses: (1) create a free encrypted, sock-puppet `email` here to register accounts on other OSINT tools without exposing your real identity; (2) recognize that a subject's address is on a privacy-focused provider — a weak behavioral signal, not identifying data. It cannot take an email and return a `name`, `phone`, or `social-profile`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://tutanota.com` (redirects toward `tuta.com`) and sign up for a free encrypted mailbox as a dedicated sock puppet.
2. Use that inbox for registrations/verifications on people-search and breach tools.
3. If investigating: simply note when a target's address is a tutanota/tuta domain.
4. Pivot: run the subject's actual address through reverse-lookup/breach tools ([[venacus]], [[thatsthem]]) regardless of provider.

## Inputs → Outputs
- **In:** `email` (your own, when creating an account)
- **Out:** `domain` (provider recognition), `metadata` (privacy-provider signal)
- **Empty/negative result looks like:** there is no lookup; do not expect identity output from this service.

## Gotchas & OpSec
- Human-in-the-loop: account creation and login required.
- Do not treat a tutanota address as identifying — it is by design hard to attribute.
- OpSec: strong investigator-side OpSec when used for sock-puppet inboxes.

## Overlaps ("do both")
- Same provider as [[tuta-com]] (the current brand/domain); maintain one sock-puppet account, not two.

## Trust & verifiability
`trust: trusted` — a reputable, established encrypted-mail provider; categorized correctly here as a mail service and OpSec asset, not an identity lookup.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tutanota |
| category | email |
| selectorsIn → selectorsOut | email → domain, metadata |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
