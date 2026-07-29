---
id: abine
name: Abine (DeleteMe)
description: Use when you need to remove a person's info from data-broker/people-search sites (your own or a client's, with consent) — a subscription opt-out service, and a checklist of which brokers hold data.
url: https://www.abine.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Counter-OSINT / privacy hardening — Abine's DeleteMe subscription removes personal listings from data brokers; also a reference to which people-search sites carry a subject's data.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: freemium
costNote: The company (Abine) offers IronVest (a freemium account/payment protector) and DeleteMe (a paid annual subscription, ~$129+/yr, that does the data-broker opt-outs). The removal service itself is paid; the broker list it targets is informative for free.
opsec: passive
opsecNote: This is a defensive/counter-OSINT tool. Only run removals for yourself or with explicit authorization — submitting someone's opt-outs means handing their data to Abine and the brokers. As an investigator, its main OSINT value is the reverse: the roster of data brokers it targets tells you where a subject's info likely lives.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established US privacy company (since 2010, "100M+ listings removed"). Legitimate; effectiveness is inherently partial since brokers re-list data over time.
missingPersonsRelevance: low
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- deleteme
- whitepages
- spokeo
aliases:
- Abine
- DeleteMe
- IronVest
tags:
- privacy
- counter-osint
- data-broker-removal
source: metaosint
lastVerified: '2026-07-29'
enrichment: full
---

# Abine (DeleteMe)

> A US privacy company whose flagship, DeleteMe, subscription-removes your personal listings from data-broker/people-search sites — a counter-OSINT service, and (read in reverse) a map of where a subject's data is exposed.

## When to use
Two angles. (1) **Privacy hardening (defensive):** you or a consenting client want personal info pulled from data brokers (Whitepages, Spokeo, and dozens more) — DeleteMe automates the opt-outs and re-checks periodically. (2) **Investigative, in reverse:** the list of brokers Abine targets is effectively a checklist of where a subject's `name`/`address`/`phone` likely appears, pointing you to the people-search sites worth querying directly. It is not itself a person-lookup that returns data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.abine.com and choose the product: **DeleteMe** (data-broker removals) or **IronVest** (account/payment protection).
2. For DeleteMe: create an account, subscribe, and provide the identity details to opt out (name, addresses, etc.). Abine's team files removals across supported brokers and reports back.
3. Track the periodic reports — brokers re-list, so removal is ongoing, not one-and-done.
4. Investigative use: don't buy it — read which brokers it covers, then query those `[[whitepages]]`/`[[spokeo]]`-type sites yourself to find (rather than remove) a subject's exposure.
5. Pivot: use the broker list to drive your people-search enumeration; use the service to reduce a protected person's footprint.

## Inputs → Outputs
- **In:** `name` (plus identity details) for removals — or just the broker roster as reference.
- **Out:** none returned as investigative data — removal reports for the subscriber; indirectly, a list of relevant brokers.
- **Empty/negative result looks like:** a broker outside Abine's coverage, or data that reappears after removal — expected, since brokers continuously re-aggregate.

## Gotchas & OpSec
- Human-in-the-loop: account + paid subscription for DeleteMe (partial paywall).
- OpSec: **defensive** — run removals only for yourself or with authorization; submitting a third party's data to Abine is itself a disclosure. Its clean OSINT use is the broker list, not the service.
- Removal is partial and perpetual: brokers re-list, coverage is US-centric, and no service catches every source.

## Overlaps ("do both")
- Inverts `[[whitepages]]` / `[[spokeo]]` — those are the people-search sites Abine opts you out of; as an investigator you query them, as a subject you remove from them.
- Overlaps with `[[deleteme]]` (its own flagship product entry) as the removal service.

## Trust & verifiability
`trust: trusted` — a legitimate, long-running privacy company. Its removals are real but inherently incomplete (data re-aggregates), so treat "removed" as "reduced," and treat its broker coverage as a useful, not exhaustive, map of exposure.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | abine |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name → — |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
