---
id: domainwatch
name: DomainWatch
description: Use when you have a `domain`, or a registrant `name`/`email`, and want WHOIS plus reverse-WHOIS — returns registration details and other domains sharing the same registrant.
url: https://domainwat.ch/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: WHOIS lookup and reverse-WHOIS — pivoting from a registrant name/email/org to every other domain they registered.
selectorsIn:
- domain
- name
- email
selectorsOut:
- domain
- email
- name
status: degraded
pricing: freemium
costNote: Free web WHOIS and reverse-WHOIS searches with limits; bulk/API access is paid. Availability can be intermittent.
opsec: passive
opsecNote: Passive — you query DomainWatch's stored WHOIS index, not the target's domain, so nothing touches the subject and no one is notified. Registrant data is frequently privacy-masked; treat unmasked historical records as leads to confirm.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party WHOIS/reverse-WHOIS aggregator; useful for pivots, but its historical registrant data can be stale or partial and should be confirmed.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- DomainWatch
- domainwat.ch
tags:
- whois
- reverse-whois
- domain-registrant
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# DomainWatch

> A WHOIS and reverse-WHOIS service: look up a domain's registration, or pivot from a registrant name/email to all the other domains they own.

## When to use
You have a `domain` and want its registration details, or — more powerfully — you have a registrant `name`, `email`, or organization and want every other `domain` registered with those details. Reverse-WHOIS is a strong footprint-mapping pivot: one leaked historical registrant email can expose a whole portfolio of a person's or operator's domains.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://domainwat.ch/ (retry if temporarily unavailable).
2. For WHOIS: enter the `domain` to see registrant, registrar, dates, and nameservers.
3. For reverse-WHOIS: search by registrant `name`, `email`, or organization to list associated domains.
4. Note historical records — pre-privacy registrations often reveal the real registrant.
5. Verify a critical registrant link against a live WHOIS and cross-check with another reverse-WHOIS source.

## Inputs → Outputs
- **In:** `domain`, or registrant `name`/`email`/org
- **Out:** WHOIS registration fields; reverse-WHOIS list of related `domain`s with shared registrant `email`/`name`
- **Empty/negative result looks like:** privacy-masked/"redacted" WHOIS or no reverse matches — modern registrations are usually masked; try historical records or another aggregator before concluding no link exists.

## Gotchas & OpSec
- **Privacy masking:** most current WHOIS is redacted; the value is often in *historical* records.
- Reverse-WHOIS matches can include coincidental shared privacy-service emails — confirm the email is genuinely the registrant's.
- Intermittent availability and stale index — cross-check with another WHOIS-history tool.

## Overlaps ("do both")
- Pairs with other WHOIS-history/reverse-WHOIS tools (WhoisXML, ViewDNS, Whoxy) and `[[website-informer]]` — indexes differ, so run more than one and take the union of registrant-linked domains.

## Trust & verifiability
`trust: community` — a third-party WHOIS aggregator; treat registrant links as leads and confirm against live WHOIS and a second source before asserting common ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | domainwatch |
