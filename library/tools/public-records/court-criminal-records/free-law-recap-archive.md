---
id: free-law-recap-archive
name: Free Law RECAP Archive
description: Use when you have a `name`/case tied to US federal litigation and want the actual court filings — returns dockets and PACER documents naming parties, addresses, and associates.
url: https://www.courtlistener.com/recap/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Free full-text search of US federal court dockets and filings crowdsourced from PACER via CourtListener.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- address
- employer-org
status: live
pricing: free
costNote: Free and public (Free Law Project nonprofit). No PACER account or per-page fee for documents already in the RECAP archive; a free CourtListener account unlocks alerts and the API.
opsec: passive
opsecNote: Searching RECAP queries CourtListener's own archive, not PACER live — so the court/party is not alerted and no PACER charges accrue. Passive. Only documents contributed by RECAP users are present; pulling a brand-new doc from PACER itself (separate flow) is logged by the courts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Free Law Project; RECAP mirrors authentic PACER filings, so documents are genuine court records (though a docket may be incomplete vs. live PACER).
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- courtlistener
- recap-court-doc-repo
- courtlistener-recap
aliases:
- RECAP
- CourtListener RECAP
tags:
- court-records
- pacer
- federal
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# Free Law RECAP Archive

> A free mirror of US federal court filings (PACER documents crowdsourced by RECAP users) inside CourtListener — search a person's name to pull the actual dockets and PDFs they appear in.

## When to use
You have a `name`, business, or case connected to US federal litigation (civil, criminal, or bankruptcy) and want the primary documents: who sued whom, party addresses, attorneys, and named associates. RECAP surfaces filings that PACER normally charges for, so it's the free first stop before paying PACER.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to CourtListener's RECAP search and enter a party `name`, company, docket number, or keyword.
2. Filter by court, date, or document type; open a docket to see the timeline of filings.
3. Read document PDFs already in the archive for free — complaints and filings routinely list home/business `address`es, employers, and co-parties (`associate`s).
4. If a needed document isn't yet in RECAP, note the docket and (separately) fetch it from PACER, or set a CourtListener alert.
5. Pivot: party addresses feed people-search; named co-defendants/attorneys feed link analysis; case dates anchor a timeline.

## Inputs → Outputs
- **In:** party `name` / `employer-org` / docket number / keyword
- **Out:** court documents exposing `associate`s (co-parties, counsel), `address`es, `employer-org` details
- **Empty/negative result looks like:** no matching dockets, or a docket exists but its documents aren't in RECAP yet (you'll see the entry but "Buy on PACER" instead of a free PDF).

## Gotchas & OpSec
- Coverage is US federal only — no state courts; use state portals for those.
- RECAP is crowdsourced, so a docket may be partial; absence of a document ≠ it doesn't exist.
- OpSec: RECAP search is passive; pulling fresh docs from PACER directly is logged and billed by the courts.

## Overlaps ("do both")
- Pairs with `[[courtlistener]]` (opinions/case law on the same platform) and state court record tools — RECAP covers federal filings; run state searches separately for a full picture.

## Trust & verifiability
`trust: trusted` — Free Law Project nonprofit mirroring authentic PACER records; documents are genuine, but confirm a docket is complete against PACER for anything decisive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-law-recap-archive |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → associate, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
