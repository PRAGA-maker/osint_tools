---
id: castrick
name: Castrick
description: Use when you have an `email`, `username` or `phone` and want a trace-free reverse lookup into linked accounts — Castrick returned `social-profile` links from real-time sources, but the service shut down in February 2026.
url: https://castrickclues.com
category: social-networks
path:
- social-networks
bestFor: (Historical) Trace-free reverse email / username / phone lookup returning linked social profiles.
selectorsIn:
- email
- username
- phone
selectorsOut:
- social-profile
- name
status: down
pricing: freemium
costNote: When live, Castrick was freemium — a limited free tier plus subscriptions roughly $12–$100/month. It is no longer purchasable; the service closed on 7 February 2026 and unused credits were refunded/contacted by email.
opsec: passive
opsecNote: Castrick advertised trace-free lookups — it claimed not to log/store searches and that its modules did not alert the target, aggregating only real-time public sources (no breach/data-broker databases). Since the service is now down, this is moot; do not rely on the domain, and treat any site now answering on it as unaffiliated.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Was a known, community-referenced OSINT platform (listed on awesome-osint) with a stated no-log / no-broker-data policy. As of 2026 it is defunct, so the entry is retained for historical reference only.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- account-live-com
aliases:
- Castrick Clues
- castrickclues.com
- castrick.com
tags:
- real-time-search-social-media-search-and-general-social-media-tools
- reverse-lookup
- defunct
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Castrick

> A trace-free reverse email/username/phone-to-social-profile lookup — now defunct (shut down February 2026), retained so investigators don't waste time chasing a dead service.

## When to use
Historically: you had an `email`, `username`, or `phone` and wanted linked `social-profile` accounts without leaving a trace on the target, drawing only from real-time public sources rather than breach dumps. **As of 2026 this no longer applies** — Castrick closed on 7 February 2026 and the domain no longer resolves as the service. This entry exists to tell you to route around it, not to use it.

## How to use it (`bestInteractionPattern`: web-manual)
1. **Do not** attempt to sign up — the service is down; `castrickclues.com` no longer serves the platform.
2. If a page now answers on that domain, treat it as unaffiliated/parked and do not enter target selectors into it.
3. Substitute a live equivalent: use a maintained reverse email/username tool for account discovery.
4. Pivot: for the "does this email map to an account" question, use first-party existence oracles like `[[account-live-com]]`, plus current username-enumeration tools.

## Inputs → Outputs
- **In (historical):** `email`, `username`, or `phone`
- **Out (historical):** linked `social-profile` accounts and associated `name`
- **Empty/negative result looks like:** the whole service is now an empty/negative result — expect DNS failure or a parked page. Any "result" from the bare domain today should be treated as untrustworthy.

## Gotchas & OpSec
- **Defunct.** Closed 7 Feb 2026; do not budget it into a workflow.
- Beware domain reuse — a shuttered OSINT brand's domain can be re-registered by third parties; never feed selectors into whatever now sits there.
- OpSec (historical): it marketed trace-free, no-log lookups; irrelevant now that it is offline.

## Overlaps ("do both")
- Replace with `[[account-live-com]]` and current reverse-email/username services — those cover the account-existence and profile-linking jobs Castrick used to do.

## Trust & verifiability
`trust: community` — it was a genuine, community-listed OSINT platform with a stated no-broker-data policy, but it is now **down**. The rating reflects its historical standing; operationally, treat it as unavailable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | castrick |
| category | social-networks |
| selectorsIn → selectorsOut | email, username, phone → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
