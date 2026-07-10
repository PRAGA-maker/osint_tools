---
id: familysearch-s-united-states-record-collections
name: FamilySearch's United States Record Collections
description: Use when you have a `name` and want a one-page portal into FamilySearch's US genealogy record collections (census, vital, immigration) via Steve Morse's One-Step tools — returns links/forms into `dob`, `address`, `associate` records.
url: https://stevemorse.org/fhl/websitesunitedstates.html
category: public-records
path:
- public-records
bestFor: A single indexed gateway (Steve Morse "One-Step") into FamilySearch's US record collections for genealogy/identity research.
selectorsIn:
- name
selectorsOut:
- name
- dob
- address
- associate
status: live
pricing: freemium
costNote: The One-Step portal is free; it links into FamilySearch, which is also free but requires a free FamilySearch account to view many record images.
opsec: passive
opsecNote: A directory of search links plus the FamilySearch archive — you query records, nothing reaches any subject. A free FamilySearch login is needed for some images; use a research account, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Steve Morse's One-Step pages are a long-respected genealogy resource; they front FamilySearch (run by the LDS Church), whose record collections are authoritative primary sources.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Steve Morse One-Step FamilySearch US
- One-Step US record collections
tags:
- genealogy
- familysearch
- one-step
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# FamilySearch's United States Record Collections

> A Steve Morse "One-Step" gateway that indexes FamilySearch's US record collections in one place — census, vital, immigration, and more — with streamlined search forms.

## When to use
You have a `name` and need to work US genealogy/vital records to confirm identity, establish `dob`, or map family — and want a single organized entry point into FamilySearch's large but sprawling US collections rather than hunting through its catalog. Steve Morse's One-Step pages present these collections with direct, simplified search links.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stevemorse.org/fhl/websitesunitedstates.html.
2. Scan the indexed list of FamilySearch US collections (federal/state census, births/marriages/deaths, immigration/naturalization, etc.).
3. Click through to the relevant collection and search by `name` + year/place.
4. Sign into a free FamilySearch account when prompted to view record images.
5. Pivot: extract `dob`, `address`, and family members (`associate`) from each record; feed names into further collections or `[[freecen-org-uk]]`/`[[scotlandspeople-gov-uk-2]]` for non-US branches.

## Inputs → Outputs
- **In:** `name` (+ approximate year/place)
- **Out:** links into FamilySearch records yielding `name`, `dob`, `address`, `associate` (household/family)
- **Empty/negative result looks like:** a collection returns no matching record — try spelling variants, adjacent years, and other collections; absence in one collection isn't absence in all.

## Gotchas & OpSec
- It's a portal, not a database — the actual records live on FamilySearch, which needs a free login for many images.
- US-focused; use other One-Step pages / national archives for other countries.
- Passive; only the FamilySearch login is attributable — use a research account.

## Overlaps ("do both")
- Pairs with `[[freecen-org-uk]]` and `[[scotlandspeople-gov-uk-2]]` (UK records) and paid aggregators (Ancestry) — One-Step/FamilySearch is strong and free for US collections; the others cover other regions or fill US gaps.

## Trust & verifiability
`trust: trusted` — a respected genealogy gateway fronting FamilySearch's authoritative primary-source collections; verify each hit against the actual record image.
