---
id: spamhaus
name: Spamhaus
description: Use when you have a domain or IP from an email header and want its spam/abuse reputation — returns blocklist status for that domain/IP.
url: https://check.spamhaus.org/
category: email
path:
- email
bestFor: Checking whether a domain or IP (e.g. from an email's headers) is listed on Spamhaus abuse blocklists.
selectorsIn:
- domain
- ip-address
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free single-lookup reputation check; bulk/API access (Spamhaus datasets) is a paid product.
opsec: passive
opsecNote: You query Spamhaus's blocklist database, not the subject; the domain/IP owner is not notified. Fully passive.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Spamhaus is a long-established, authoritative anti-abuse organization; its blocklist data is industry-standard and reliable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases: []
tags:
- email
- reputation
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Spamhaus

> Authoritative domain/IP reputation lookup — tells you if an address or mail server is flagged for abuse.

## When to use
You have a `domain` or `ip-address` (often pulled from an email's `Received:` headers, or a domain a subject used) and want to judge its legitimacy — is it a known spam/abuse source, a throwaway, or clean infrastructure? This is a corroboration/triage check, not a person-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://check.spamhaus.org/.
2. Enter the `domain` or `ip-address` and solve the captcha.
3. Read the result: which Spamhaus lists (SBL, XBL, PBL, DBL, etc.) the entry appears on, or "not listed."
4. Pivot: a listed/dynamic IP suggests the sender used disposable or compromised infrastructure; a clean record supports legitimacy and points to a real owner to research further.

## Inputs → Outputs
- **In:** `domain`, `ip-address`
- **Out:** blocklist status / reputation `metadata-exif`
- **Empty/negative result looks like:** "not listed" — the address is not flagged (does not by itself prove legitimacy).

## Gotchas & OpSec
- It judges reputation, not identity — it will not return a name or email for a person.
- Human-in-the-loop: a captcha gates the web check.
- OpSec: fully passive; the queried party is never notified.

## Overlaps ("do both")
- Pairs with email-header analysis (e.g. `[[support-google-com]]` for reading headers) — extract the IP/domain from headers, then reputation-check it here.

## Trust & verifiability
`trust: trusted` — Spamhaus is the de-facto industry authority on email/IP abuse reputation; data is authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spamhaus |
| category | email |
| selectorsIn → selectorsOut | domain, ip-address → metadata-exif (reputation) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
