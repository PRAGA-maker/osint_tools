---
id: icann-whois-lookup
name: ICANN Whois Lookup
description: Use when you have a `domain` and want its registration record — returns registrar, registration/expiry dates, name servers, and any public registrant contact via ICANN's official lookup.
url: https://lookup.icann.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Authoritative WHOIS/RDAP registration lookup for a domain via ICANN's own portal.
selectorsIn:
- domain
selectorsOut:
- domain
- email
- name
status: live
pricing: free
costNote: Free official lookup run by ICANN; no account needed.
opsec: passive
opsecNote: You query registry/registrar WHOIS data, not the domain's server, so the site owner isn't contacted. ICANN logs queries. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: ICANN is the body that oversees domain registration; its lookup returns authoritative registry/registrar data, subject to privacy redaction rules.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- icann-lookup
- lookup-icann-org
- rdrs-icann-org
- icann-org
aliases:
- ICANN WHOIS
- lookup.icann.org
- whois.icann.org
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# ICANN Whois Lookup

> ICANN's official WHOIS/RDAP portal — the authoritative starting point for who registered a domain, when, through which registrar, and (where not redacted) their contact details.

## When to use
You have a `domain` (from a subject's website, email address, a link in their content) and want its registration record: the registrar, creation/expiry/update dates, name servers, registration status, and any public registrant/admin/tech contact. This anchors a domain in time (how old it is, when it changed) and, when contacts aren't privacy-protected, can expose a registrant `name`, `email`, organization, or address — a direct pivot from a website to a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://lookup.icann.org/ and enter the `domain`.
2. Read the record: registrar, creation/updated/expiry dates, status codes, and name servers.
3. Check the registrant/admin/tech contact fields — post-GDPR these are often **redacted** ("REDACTED FOR PRIVACY" / privacy-service placeholders), but many domains still leak a name, org, email, or country.
4. If contacts are redacted, note the registrar and use its abuse/RDRS channel, or pivot to historical WHOIS (which may predate redaction).
5. Pivot: an exposed `email`/`name` → email/people tools; creation date + name servers → hosting/infrastructure mapping; registrar → further requests.

## Inputs → Outputs
- **In:** `domain`
- **Out:** registrar, dates, name servers, status, and any public registrant `name`/`email`/org
- **Empty/negative result looks like:** contact fields all "REDACTED FOR PRIVACY" or behind a privacy service (very common now) — you still get registrar/dates/name servers. A truly not-found domain means it's unregistered or a non-standard TLD not in the lookup.

## Gotchas & OpSec
- **Privacy redaction is the norm** post-GDPR; expect contacts to be hidden. Value increasingly comes from dates, registrar, and name servers, plus historical WHOIS snapshots taken before redaction.
- ccTLDs vary — some run their own WHOIS the ICANN portal doesn't fully cover; go to the ccTLD registry directly.
- OpSec: **passive** — registry data query; the domain owner isn't contacted.

## Overlaps ("do both")
- Pairs with historical-WHOIS services (WhoisXML/DomainTools/[[archive-org]] of whois pages) that may show pre-redaction registrant data, and with reverse-WHOIS to find other domains by the same registrant.

## Trust & verifiability
`trust: trusted` — ICANN's official lookup returns authoritative registry/registrar data; the limitation is privacy redaction, not accuracy, so what it shows is reliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | icann-whois-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, email, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
