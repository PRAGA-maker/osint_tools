---
id: emailsherlock-caution-alerts-email-account-holder
name: EmailSherlock (Caution – Alerts email account holder)
description: Use when you have an `email` and want a fast reverse lookup for the owner's name, linked social profiles and the address's reputation — returns `name`, `social-profile` and deliverability/blacklist signals.
url: https://www.emailsherlock.com/
category: email
path:
- email
bestFor: Free reverse-email lookup that pairs owner discovery (name + social profiles) with technical reputation signals (SPF/DKIM/DMARC, blacklists).
selectorsIn:
- email
selectorsOut:
- name
- social-profile
status: live
pricing: freemium
costNote: Free unlimited single lookups with no signup; a Premium tier checks 30+ social networks (vs ~8 free), plus batch (up to 100) and API access behind payment/registration.
opsec: active
opsecNote: Treat as ACTIVE. The tool performs live validation against the address's mail host, and per the Toddington caution it can generate a probe that risks alerting the account holder. Never run it against a target's primary address without accepting that risk; query from a sock-puppet context and prefer passive checks first.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Run by a commercial data-lookup operator (the "Sherlock" family, e.g. PeopleSherlock); results aggregate public records and prior lookups and are not independently verified — treat every hit as a lead.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- epieos
- holehe
aliases:
- EmailSherlock
- emailsherlock.com
tags:
- toddington
- curated-directory
- email-addresses
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# EmailSherlock (Caution – Alerts email account holder)

> A free reverse-email lookup that returns a possible owner name, linked social profiles and the address's reputation in one shot — fast, but flagged as potentially *active*, so use it carefully.

## When to use
You have an `email` and want a quick first read on who is behind it and whether it's trustworthy: EmailSherlock checks the address against public records, social networks and its database of prior lookups, then returns a candidate owner `name`, matched `social-profile`s (8 networks free, 30+ premium), and technical signals — SPF/DKIM/DMARC, host reputation, and blacklist/spam history. Handy for triaging a lead address (is it real, whose is it, is it tied to other profiles/a different name — the classic catfish check). Because of the alert caution below, treat it as a *second-pass* enrichment after passive tools, not your opening move on a sensitive target.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.emailsherlock.com/ in a clean/sock-puppet browser.
2. Paste the target `email` into the reverse-search box and submit (no account needed for a single lookup).
3. Read the result card: candidate owner `name`, linked `social-profile`s, host trust score, and SPF/DKIM/DMARC/blacklist status.
4. For deeper coverage (30+ networks, batch, API) you'd need the Premium/registered tier — weigh whether it's worth it over free passive tools.
5. Pivot: matched profiles feed username/social enumeration; a different name tied to the same address is a strong catfish/alias signal; deliverability/blacklist status informs whether the address is live.

## Inputs → Outputs
- **In:** `email`
- **Out:** candidate owner `name`, linked `social-profile`s, host reputation + SPF/DKIM/DMARC/blacklist signals
- **Empty/negative result looks like:** "no owner found" / no social matches and only generic host info — the address may be new, privacy-protected, or simply not in their data; corroborate with dedicated passive tools before concluding.

## Gotchas & OpSec
- OpSec: flagged **active** — the validation step contacts the address's mail host and, per the Toddington caution embedded in this tool's name, may alert the account holder. Do not treat it as safe/passive; run passive email tools first and only use this when you accept the alert risk.
- Trust: a commercial aggregator — owner/profile matches can be stale, wrong, or drawn from thin data; never treat a returned name as confirmed without independent corroboration.
- Free tier is capped to ~8 networks and single lookups; the useful breadth sits behind Premium.

## Overlaps ("do both")
- Pairs with `[[epieos]]` and `[[holehe]]` — those run *passive* account-existence checks across many services for an email; do them first, then use EmailSherlock's owner-name/reputation angle to enrich, accepting its higher OpSec cost.

## Trust & verifiability
`trust: unverified` — a commercial reverse-lookup service with opaque sourcing. Its technical signals (SPF/DKIM/DMARC, blacklists) are checkable and reliable; its *owner/identity* claims are leads to verify, not facts. Corroborate any attributed name against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | emailsherlock-caution-alerts-email-account-holder |
| category | email |
| selectorsIn → selectorsOut | email → name, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
