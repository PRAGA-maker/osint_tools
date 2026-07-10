---
id: planning-org-uk
name: planning.org.uk (Planning Alerts)
description: Use when you have a UK `address`/postcode and want planning-application activity there — returns `address` (application sites), `associate` (applicant/agent names), and `employer-org` (developers/architects).
url: https://planning.org.uk/
category: public-records
path:
- public-records
bestFor: Surfacing UK planning applications near a postcode to reveal property works, owners, applicants, and agents.
selectorsIn:
- address
selectorsOut:
- address
- associate
- employer-org
status: live
pricing: freemium
costNote: Free email alerts and searches for applications within a ¼-mile radius of a chosen postcode; larger alert areas carry a small monthly charge. Underlying application data is public.
opsec: passive
opsecNote: Searching planning applications is passive and touches only the alerts service / council data — nothing reaches the property owner. Signing up for alerts requires an email; use a research address, not a personal one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates official Local Planning Authority application data (241 UK authorities); the notices themselves are public-record council submissions.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Planning Alerts
- planning.org.uk
tags:
- propertysites
- Property Related Sites
- planning-applications
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# planning.org.uk (Planning Alerts)

> "Planning Alerts" — aggregates UK Local Planning Authority applications so you can see (or get emailed) what's being built or altered near any postcode, and who applied.

## When to use
You have a UK `address`/postcode tied to a subject and want to know what planning activity is attached to it or its neighbourhood — extensions, developments, change-of-use. Planning applications publicly name the applicant and agent and describe the works, so they can confirm a person's connection to a property, reveal a home renovation (occupancy signal), or surface a developer/architect (`employer-org`) linked to the subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://planning.org.uk/.
2. Enter the target postcode; the free tier covers applications within a ¼-mile radius (larger radii are a small paid add-on).
3. Optionally register a research email for daily alerts of new applications in that area.
4. Read each application: site `address`, description of works, applicant and agent names, dates, and status.
5. Pivot: applicant/agent names become `associate`/`employer-org` leads; the works description and dates give a property/occupancy timeline; cross-check with Land Registry for ownership.

## Inputs → Outputs
- **In:** `address` (UK postcode)
- **Out:** `address` (application sites), `associate` (applicant/agent names), `employer-org` (developers/architects), works description, dates/status
- **Empty/negative result looks like:** no applications near the postcode — meaning no recent planning activity there (or the council isn't among the 241 covered authorities). Absence isn't proof; check the council's own planning portal directly too.

## Gotchas & OpSec
- Free radius is small (¼ mile); wider coverage costs a little.
- Covers 241 of the UK's ~400 planning authorities — a gap may mean "authority not indexed," not "no application."
- Names come from the applications; verify the applicant is actually your subject, not a namesake/agent.

## Overlaps ("do both")
- Pairs with `[[planit-org-uk]]`-style planning search, the council's own planning portal, and HM Land Registry — planning shows *works and applicants*, Land Registry shows *ownership*; combine for a full property picture.

## Trust & verifiability
`trust: trusted` — aggregates official council planning data; the applications are primary public records. Confirm any name-to-subject link against ownership/other sources.
