---
id: openpgp-org
name: openpgp.org
description: Use when you have an email address and want to check public PGP keyservers for a key tied to it — returns confirmed email use, a name/identity string, and key metadata.
url: https://www.openpgp.org
category: email
path:
- email
bestFor: Confirming an email is in use and tied to an identity via public PGP key lookups.
selectorsIn:
- email
selectorsOut:
- name
- email
- metadata-exif
status: live
pricing: free
costNote: Free. OpenPGP and public keyservers (keys.openpgp.org, keyserver.ubuntu.com) are free.
opsec: passive
opsecNote: Keyserver lookups query public infrastructure; no contact with the subject. Lookups may be logged by the keyserver.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: openpgp.org is the official informational site for the OpenPGP standard. It is not a search engine itself; the value is the surrounding ecosystem of public keyservers it points to (keys.openpgp.org etc.).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OpenPGP
- PGP keyserver
tags:
- email
source: metaosint
lastVerified: ''
enrichment: full
---

# openpgp.org

> The official home of the OpenPGP standard — your gateway to public PGP keyservers, where an email can be confirmed and tied to a named identity and key history.

## When to use
You have an `email` for a technical or privacy-conscious subject and want to confirm it is real and learn the `name`/identity string and key timestamps the owner published. PGP keys often carry a real or chosen name and creation dates useful for timeline-building.

## How to use it (`bestInteractionPattern`: web-manual)
1. Start at https://www.openpgp.org to find recommended keyservers/software.
2. Search the email on a public keyserver — e.g. keys.openpgp.org or keyserver.ubuntu.com.
3. If a key exists, read the User ID (name + email), key creation/expiry dates, and any linked identities.
4. Pivot the confirmed `name`/`email` to people-search (`[[pipl]]`) and account checks (`[[osint-rocks]]`).

## Inputs → Outputs
- **In:** `email`
- **Out:** `name` (User ID string), `email` (confirmed), `metadata-exif` (key creation date, fingerprint, key history)
- **Empty/negative result looks like:** "No keys found" — the subject likely never published a PGP key (true for most people).

## Gotchas & OpSec
- Most people have no PGP key; expect empty results outside technical/privacy/journalist communities.
- The User ID name can be a pseudonym — treat as a lead.
- OpSec: passive; keyserver operators may log lookups, but nothing reaches the subject.

## Overlaps ("do both")
- Pairs with `[[osint-rocks]]` (account discovery) and `[[pipl]]` (identity resolution) to corroborate a name found on a key.

## Trust & verifiability
`trust: trusted` — openpgp.org is the authoritative standard site; the data lives on public keyservers run by reputable operators. A key proves email control at upload time, not present-day identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openpgp-org |
| category | email |
| selectorsIn → selectorsOut | email → name, email, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
