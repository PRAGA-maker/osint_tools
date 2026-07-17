---
id: just-delete-me
name: Just Delete Me
description: Use when you have a service `username`/account and want the direct account-deletion link and difficulty rating — supports investigator OpSec and persona cleanup (no target selectors out).
url: https://backgroundchecks.org/justdeleteme/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- privacy-clean-up
bestFor: Finding the direct "delete my account" link and difficulty rating for a given web service, to wind down sock-puppet personas or shrink your own footprint.
selectorsIn:
- username
selectorsOut: []
status: live
pricing: free
costNote: Free directory; open-source community project. No account or payment.
opsec: passive
opsecNote: A reference directory — browsing it reveals nothing to any target. The actual deletion happens on each service and is an active step you take on YOUR OWN persona accounts, not against a subject.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running open-source project (originally by Robb Lewis, now community-maintained); links point to each service's real deletion page.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- backgroundchecks-org
- fake-identity-generator
aliases:
- JustDeleteMe
- Just Delete Me directory
tags: []
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Just Delete Me

> A crowd-maintained directory of direct account-deletion links and difficulty ratings — an OpSec hygiene tool for retiring investigation personas and cleaning up your own digital footprint.

## When to use
This is investigator tradecraft, not a subject lookup. Reach for it when you need to tear down a sock-puppet account after an operation, or help a client/yourself reduce exposure: you know the service (`username`/account there) and want the fastest, verified path to delete it — plus a heads-up on how painful the service makes it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the directory and search or scroll to the service name.
2. Read the entry's colour-coded difficulty: **easy** (self-serve link), **medium** (extra steps), **hard** (must contact support), **impossible** (no deletion offered).
3. Click through to the direct deletion URL and follow that service's flow while logged into the persona/account you are retiring.
4. For "impossible" services, plan accordingly — data can't be removed, only abandoned; avoid seeding those with real details next time.

## Inputs → Outputs
- **In:** `username` / the service where an account exists (you supply which service).
- **Out:** none about a subject — it returns a deletion link, difficulty rating, and instructions for the service.
- **Empty/negative result looks like:** the service isn't catalogued — check the service's own settings/privacy page manually, or its GDPR/CCPA contact.

## Gotchas & OpSec
- Human-in-the-loop: you must review each entry and perform the deletion manually on the correct account — the directory only points the way.
- Ratings can lag reality as services change their flows; treat the link as a strong starting point, not a guarantee.
- OpSec: browsing the directory is passive. Deleting an account is an active step — do it only on YOUR persona accounts, never attempt to delete a subject's account (that's intrusive and likely illegal).

## Overlaps ("do both")
- Pairs with `[[fake-identity-generator]]` — one spins up disposable personas, this one helps you decommission them cleanly. `[[backgroundchecks-org]]` is the parent site's people-search side.

## Trust & verifiability
`trust: trusted` — a well-known open-source project whose links go straight to each service's own deletion page; the difficulty data is community-verified but should be spot-checked as services evolve.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | just-delete-me |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | username → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
