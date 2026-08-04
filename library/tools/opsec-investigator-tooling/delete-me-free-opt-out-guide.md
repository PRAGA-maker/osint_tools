---
id: delete-me-free-opt-out-guide
name: DeleteMe Free Opt-Out Guide
description: Use when you have a `name` exposed on data-broker/people-search sites and want to remove it — returns step-by-step opt-out instructions per broker (defensive/OpSec).
url: https://joindeleteme.com/help/diy-free-opt-out-guide/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A maintained directory of free, per-broker DIY opt-out instructions for scrubbing your own (or a subject's) exposure from people-search sites.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
costNote: The DIY guides are free; DeleteMe also sells a paid managed-removal service, but every opt-out walkthrough is available at no cost.
opsec: passive
opsecNote: Reading the guides is passive. Executing an opt-out is active against each broker — you submit the subject's details (and sometimes verify by email/phone) to the very sites that hold the data, which confirms the identity to them. Do it only for accounts you are authorised to scrub, and read each broker's own removal form carefully.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by DeleteMe (Abine), an established privacy-removal company; the guides are actively maintained with dated updates, though brokers change their forms so steps can drift.
missingPersonsRelevance: low
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- DeleteMe DIY opt-out
- Abine opt-out guide
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# DeleteMe Free Opt-Out Guide

> A living, per-broker cookbook for removing a person's records from data-broker and people-search sites — the defensive counterpart to the people-search tools in this library.

## When to use
This is an OpSec / subject-protection resource, not a discovery tool. Reach for it when you (or a person you are authorised to protect) are exposed on data brokers — Whitepages, Spokeo, BeenVerified, Radaris, TruePeopleSearch and dozens more — and you need the exact opt-out procedure for each. Investigators also use it in reverse: the broker list itself is a checklist of where a `name` is likely to surface.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://joindeleteme.com/help/diy-free-opt-out-guide/.
2. Browse or search the index of data brokers; each entry links to a step-by-step removal walkthrough.
3. For each broker: follow the steps — usually find your listing, submit the opt-out/suppression form, and complete any email/phone verification.
4. Track completion per broker (they must be repeated periodically — records reappear).
5. Pivot (investigative use): treat the broker index as a coverage map of people-search sites to check for the subject before scrubbing.

## Inputs → Outputs
- **In:** `name` (the exposed identity to remove or audit)
- **Out:** procedural removal instructions per broker (no data returned about the person)
- **Empty/negative result looks like:** a broker not covered by the guide, or a listing you can't locate on the broker itself — meaning either no record there or it's indexed under a variant name.

## Gotchas & OpSec
- Removals are not permanent — brokers re-scrape; re-run periodically.
- Submitting an opt-out often requires handing the broker verification details (email/phone), which confirms the identity to them; weigh that before starting.
- Broker forms change; a step in the guide may be stale — follow the broker's current form, not the screenshot.
- Only scrub identities you are authorised to act for.

## Overlaps ("do both")
- The mirror image of the people-search tools in this library — where those enumerate a `name` into `address`/`associate`, this enumerates the same brokers to suppress those records. Run a people-search first to see what's exposed, then work the guide to remove it.

## Trust & verifiability
`trust: trusted` — first-party, dated, actively maintained content from an established privacy vendor (Abine/DeleteMe); the free DIY guidance is genuine, with a paid managed service offered alongside it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | delete-me-free-opt-out-guide |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
