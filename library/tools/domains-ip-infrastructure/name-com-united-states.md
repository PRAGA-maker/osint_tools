---
id: name-com-united-states
name: Name.com (United States)
description: Use when you have a `domain` and want registration/availability and WHOIS basics — returns registrar/availability data and (redacted) WHOIS via a major US registrar's lookup.
url: https://www.name.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking a domain's availability/registration status and basic WHOIS through a major registrar, plus bulk domain-name searching.
selectorsIn:
- domain
selectorsOut:
- domain
- document-id
status: live
pricing: freemium
costNote: WHOIS/availability lookups are free; registering domains costs money. No account needed to run a lookup.
opsec: passive
opsecNote: A WHOIS/availability lookup is passive and doesn't touch the site owner. It queries registry data through name.com — use a sock-puppet session if you'd rather the lookup not be tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, established ICANN-accredited US registrar; availability/registration data is authoritative, but post-GDPR WHOIS is heavily redacted, so registrant personal details are usually hidden.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- name-com-bulk-search
aliases:
- Name.com
- name.com WHOIS
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- registrar
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Name.com (United States)

> A major US domain registrar whose free WHOIS/availability lookup tells you whether a `domain` is registered, when, and by which registrar — a quick registration-status check, though registrant identities are mostly redacted now.

## When to use
You have a `domain` and want to know its registration status: is it taken or available, when was it created/expires, and which registrar/nameservers it uses. Useful for confirming a domain is active, spotting registration dates that anchor a timeline, and enumerating related names via bulk search. Post-GDPR, don't expect a registrant name/email here — those are usually masked.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.name.com and use its WHOIS/domain-search (or the availability checker).
2. Enter the target `domain`; read registration status, creation/expiry dates, registrar, and nameservers.
3. For related domains, use bulk search (`[[name-com-bulk-search]]`) to test many name variants at once.
4. Because personal WHOIS fields are redacted, treat registration dates/nameservers as the actionable data.
5. Pivot: creation dates → timeline; nameservers/hosting → infrastructure clustering; feed the domain to a full WHOIS-history tool for pre-redaction records.

## Inputs → Outputs
- **In:** `domain`
- **Out:** registration status, dates, registrar/nameservers (`document-id`-style registry facts), and available related `domain`s
- **Empty/negative result looks like:** "available" (unregistered) or a bare record with all personal fields redacted — normal today. For registrant identity, you'll need historical-WHOIS or reverse-WHOIS tools, not a live registrar lookup.

## Gotchas & OpSec
- Modern WHOIS is redacted — this rarely yields a registrant `name`/`email`; use it for status/dates, not identity.
- It's a registrar (its business is selling domains); the lookup is a convenience feature, not a deep intelligence tool.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with `[[name-com-bulk-search]]` and dedicated WHOIS-history/reverse-WHOIS services — this gives current status, while history/reverse tools recover the registrant data redaction now hides.

## Trust & verifiability
`trust: community` — an accredited registrar with authoritative registration data; status/dates are reliable, but the absence of registrant details is a redaction limit, not a data gap you can resolve here.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | name-com-united-states |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
