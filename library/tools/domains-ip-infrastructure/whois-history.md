---
id: whois-history
name: Whois History (osint.sh)
description: Use when you have a `domain` and want its historical WHOIS records to recover a registrant name/email/address hidden by today's privacy redaction — returns name, email, address.
url: https://osint.sh/whoishistory/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: Recovering past registrant details (pre-redaction) from a domain's historical WHOIS.
selectorsIn:
- domain
selectorsOut:
- name
- email
- address
- phone
status: live
pricing: freemium
costNote: Free to use on osint.sh (a free OSINT toolkit); generous but rate-limited. No account for basic lookups.
opsec: passive
opsecNote: osint.sh queries historical WHOIS databases on its servers — you never contact the target domain, so it's passive and invisible to the registrant. Your query is processed by a third-party service; avoid submitting anything beyond the domain itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: osint.sh is a widely-used free OSINT tool aggregator; the WHOIS-history data is sourced from historical WHOIS providers. Historical records can be incomplete or contain transcription artefacts — corroborate before relying on a name.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- domain-dossier
- viewdns-info
- whoxy
tags:
- whois
- whois-history
- domain-and-ip-research
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Whois History (osint.sh)

> A free historical-WHOIS lookup: shows who registered a domain *before* privacy redaction — often the single best way to unmask the person behind a now-private domain.

## When to use
You have a `domain` whose current WHOIS is redacted (privacy proxy / GDPR) but you need the real registrant. Historical WHOIS frequently captures the original registration — a real `name`, `email`, `address`, and `phone` from before the owner enabled privacy. High-value pivot when a subject's site or a scam domain is the lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.sh/whoishistory/.
2. Enter the `domain` and submit.
3. Read the timeline of historical WHOIS snapshots; look at the earliest records where privacy was often not yet enabled.
4. Extract registrant name/org, email, phone, and postal address from any pre-redaction snapshot.
5. Pivot: a registrant email → email/breach search and reverse-WHOIS (other domains by the same email); a name/address → people search.

## Inputs → Outputs
- **In:** `domain`
- **Out:** historical `name`, `email`, `address`, `phone` (registrant details over time)
- **Empty/negative result looks like:** only redacted/privacy-proxy snapshots across the whole history, or no records — meaning the domain was privacy-protected from the start or isn't in the historical dataset. Not proof no owner exists.

## Gotchas & OpSec
- Data quality varies: older snapshots can be sparse or contain artefacts; treat a single hit as a lead and corroborate.
- Coverage is provider-dependent; a miss here doesn't mean other WHOIS-history sources (`[[whoxy]]`) won't have it.
- Passive and target-invisible; just don't over-share in the query.

## Overlaps ("do both")
- Pairs with `[[viewdns-info]]` and `[[whoxy]]` for reverse-WHOIS (find all domains tied to a discovered name/email) and with `[[domain-dossier]]` for current DNS/network context.

## Trust & verifiability
`trust: community` — a free aggregator over third-party historical WHOIS. The signal is often decisive for de-anonymising domains, but verify recovered identities across sources before asserting them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whois-history |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → name, email, address, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
