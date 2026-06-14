---
id: reverse-whois
name: Reverse Whois
description: Use when you have a registrant email or name and want every domain they registered — osint.sh reverse-whois returns domains tied to that contact.
url: https://osint.sh/reversewhois/
category: email
path:
- email
bestFor: Pivoting from a person's email or name to the list of domains they registered in WHOIS.
selectorsIn:
- email
- name
selectorsOut:
- domain
- name
- address
status: live
pricing: freemium
costNote: Free web tool on osint.sh; rate-limited / capped results. No login for basic use.
opsec: passive
opsecNote: Queries historical/aggregated WHOIS data — no contact with the subject. You do send the query to osint.sh, so use a VPN if sensitive.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Part of the well-known free osint.sh toolset. WHOIS-privacy redaction (post-GDPR) means many recent domains hide registrant email/name, so coverage is partial and skews to older/un-redacted records.
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
- whois
- reverse-whois
- domain
source: osint4all
lastVerified: ''
enrichment: full
---

# Reverse Whois

> osint.sh Reverse Whois maps a registrant `email` or `name` to every domain registered under it — turning one contact detail into a person's whole web footprint.

## When to use
You have a subject's `email` (or full `name`) and want to discover domains they own — personal sites, businesses, or aliases. Strong for a missing person who ran websites or a small business: their registrant email can reveal additional domains, and those domains' WHOIS can reveal an `address`/phone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to osint.sh/reversewhois/.
2. Enter the registrant email or name.
3. Read the returned list of matching `domain`s.
4. Pivot each domain to a full WHOIS / DNS lookup (e.g. `[[robtex-com]]`) to recover registrant `address`, phone, and hosting.

## Inputs → Outputs
- **In:** `email` or `name`
- **Out:** list of `domain`s registered with that contact; sometimes registrant `name`/`address`.
- **Empty/negative result looks like:** "no domains found" — common when the registrant only ever used WHOIS-privacy/proxy registration.

## Gotchas & OpSec
- Human-in-the-loop: free tool is rate-limited; large queries may be capped.
- OpSec: passive — uses aggregated WHOIS, no subject contact. Post-GDPR redaction hides most EU registrant emails, so absence of results is NOT proof the person owns no domains.

## Overlaps ("do both")
- Pairs with `[[robtex-com]]` (DNS/IP/WHOIS on each discovered domain) to turn a domain list into registrant identity and infrastructure.

## Trust & verifiability
`trust: community` — reputable free osint.sh tool drawing on aggregated WHOIS databases; coverage is inherently partial due to privacy redaction. Confirm ownership before asserting it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reverse-whois |
| category | email |
| selectorsIn → selectorsOut | email, name → domain, name, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
