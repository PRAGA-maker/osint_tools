---
id: gist-github-com
name: gist.github.com
description: Use as a reference list of known free/webmail and disposable email-provider domains to classify an address by provider type.
url: https://gist.github.com/ammarshah/f5c2624d767f91a7cbdc4e54db8dd0bf
category: email
path:
- email
bestFor: A static GitHub Gist listing free email-provider (and disposable) domains for classifying addresses.
selectorsIn:
- email
- domain
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free public GitHub Gist.
opsec: passive
opsecNote: It is a static reference file; you check a domain against the list locally — nothing about your subject is transmitted to the gist.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely referenced community Gist (ammarshah) of free/webmail email-provider domains; it is a static data file, accurate as a snapshot but not actively guaranteed to be exhaustive or current.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- Email Related Sites
relatedTools:
- free-email-address-validator
source: uk-osint
lastVerified: ''
enrichment: full
---

# gist.github.com — Free email-provider domain list

> A static community Gist listing free/webmail (and disposable) email-provider domains; used to classify an address by provider type.

## When to use
You have an `email` or `domain` and want to know whether it belongs to a free/webmail provider (gmail.com, outlook.com, etc.) or a disposable service versus a corporate/custom domain. That classification tells you whether email-finder and corporate-pivot techniques are viable, or whether you are dealing with an anonymous webmail account.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Gist URL (or download the raw text for offline matching).
2. Search the list for the address's `domain`.
3. Interpret: a match means free/disposable webmail (treat as low-attribution); no match suggests a custom/corporate domain worth a WHOIS and email-finder pivot.

## Inputs → Outputs
- **In:** `email` / `domain`
- **Out:** classification (`metadata-exif`: is-free-provider / not-listed)
- **Empty/negative result looks like:** the domain is absent from the list — either it is a custom domain or simply not yet catalogued (the list is not exhaustive).

## Gotchas & OpSec
- Snapshot data: the list is a point-in-time export and may miss newer providers; absence is not proof a domain is corporate.
- This is a data file, not a live tool — no queries leave your machine if you download it.

## Overlaps ("do both")
- Pairs with `[[free-email-address-validator]]`, which independently flags disposable/role/catch-all addresses.

## Trust & verifiability
`trust: community` — popular, openly inspectable Gist; the data is verifiable by reading it, but completeness/currency are not guaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gist-github-com |
| category | email |
| selectorsIn → selectorsOut | email, domain → metadata-exif (provider classification) |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
