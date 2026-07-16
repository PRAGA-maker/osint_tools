---
id: new-jersey-voter-records
name: New Jersey Voter Records
description: Use when you have a `name` and want to confirm a New Jersey address, birth year, and party from voter-registration data — returns residential address and household-level leads.
url: https://stevemorse.org/njvoters/njvoters.html
category: public-records
path:
- public-records
bestFor: Looking up a New Jersey voter's registered residential address, approximate age, and party via Steve Morse's One-Step search.
selectorsIn:
- name
- address
selectorsOut:
- address
- dob
- associate
status: live
pricing: free
costNote: Free One-Step search hosted on stevemorse.org; no account or payment.
opsec: passive
opsecNote: Queries a static voter-data set hosted for research/genealogy; nothing is sent to the subject and no login is required. It reflects a snapshot of NJ voter registration data, which is public in New Jersey. Use a clean browser; treat as one dated snapshot, not live.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Steve Morse's One-Step tools are a well-known, reputable genealogy/records resource; the NJ voter data is a public dataset snapshot, so coverage is bounded to that vintage and to registered voters.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Steve Morse NJ Voters
- One-Step NJ voter search
tags:
- voter-records
- new-jersey
- genealogy
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- brooklyn-genealogy
- chicago-cook-county-genealogy
- decoding-social-security-numbers
- encoding-and-decoding-driver-s-license-numbers
- familysearch-s-united-states-record-collections
- new-york-state-prison-records
- new-york-state-voter-records
- social-security-death-index
- street-name-changes
---

# New Jersey Voter Records

> A free Steve Morse "One-Step" search over New Jersey voter-registration data — enter a name and get the registered residential address, approximate age, and party for NJ voters.

## When to use
You have a `name` and think the subject is (or was) a registered voter in New Jersey, and you want to confirm a residential `address` and approximate age/DOB year. Voter registration is a strong address anchor and identity corroborator; because it lists everyone registered at an address, it can also surface household members (`associate`s). Reach for it in NJ locate work, or to disambiguate namesakes by address/age.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stevemorse.org/njvoters/njvoters.html.
2. Enter the subject's name (and optionally narrow by town/county); Steve Morse forms allow partial and phonetic matching.
3. Submit and read results: registered name, residential address, party, and birth-year/age field.
4. Look for others registered at the same address as household `associate`s.
5. Pivot: the `address` feeds reverse-address and people-search; birth year disambiguates identity; household members become new subjects.

## Inputs → Outputs
- **In:** `name` (optionally `address`/town to narrow)
- **Out:** `address` (registered residence), `dob` (birth year/age), `associate` (same-address registrants)
- **Empty/negative result looks like:** no match — the subject isn't a registered NJ voter in this dataset, registered under a variant name, or moved after the snapshot. Not proof of no NJ ties; try name variants and other state voter tools.

## Gotchas & OpSec
- Human-in-the-loop: none.
- The dataset is a **dated snapshot** and covers **registered voters in New Jersey only** — addresses can be stale and non-voters are absent.
- OpSec: passive; the subject is not notified.

## Overlaps ("do both")
- Pairs with other state voter-record One-Step tools and general people-search — voter data gives an authoritative-ish address+age anchor; people-search adds phones/relatives and cross-state coverage.

## Trust & verifiability
`trust: community` — a reputable hosted search over a public NJ voter dataset; reliable for the snapshot's vintage, with recency and coverage limited to registered voters at capture time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-jersey-voter-records |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, dob, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
