---
id: state-public-records-laws
name: State Public Records Laws
description: Use when you need to obtain a US public record about a person and want to know each state's records-law rules and file the request — returns the pathway to documents (name, dob, document-id).
url: https://www.muckrock.com/place
category: public-records
path:
- public-records
bestFor: Understanding each US jurisdiction's public-records (FOIA) law and filing a request to obtain documents.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: MuckRock's place/records-law data and guidance are free to browse. Filing requests via MuckRock is free to start, though agencies may charge copy/processing fees and MuckRock has paid plans for heavy filers.
opsec: active
opsecNote: Filing a public-records request is an overt, named, on-the-record action — the agency (and sometimes the subject, via notice provisions) learns a request was made. This is not covert research; use it only when an official paper request is appropriate and consider that some states notify third parties.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: MuckRock is a well-established nonprofit transparency/journalism platform; its records-law data is professionally researched and its filing tooling is genuine.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: true
aliases:
- MuckRock place
- MuckRock public records
tags:
- court
- inmate
- foia
- public-records
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# State Public Records Laws

> MuckRock's jurisdiction guide and filing tool: learn each US state's public-records law, then file the request that actually pulls the document.

## When to use
You have identified a record that should exist about a subject (court, agency, inmate, licensing, correspondence) and need the *procedural* path to obtain it: which law applies in that state, response deadlines, exemptions, whether out-of-state requesters are allowed, and how to appeal a denial. Then use MuckRock to file and track the request. This is the bridge from "the record exists somewhere" to "I have the document."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.muckrock.com/place and pick the US state/jurisdiction.
2. Read its profile: applicable records law, average response time, deadlines, exemptions, branch coverage, out-of-state rules, and appeal process.
3. Draft and file a request through MuckRock (free account to file/track); scope it precisely to the record and subject.
4. Track responses and appeals in-platform; expect agency copy/processing fees and manual back-and-forth.
5. Pivot: an obtained document yields the authoritative `name`/`dob`/`document-id` that anchors the rest of your profile.

## Inputs → Outputs
- **In:** `name` / a specific record you're targeting, plus the correct jurisdiction
- **Out:** the procedural pathway and, once fulfilled, primary documents containing `name`, `dob`, `document-id`
- **Empty/negative result looks like:** an exemption or "no responsive records" reply — meaning the record is withheld or doesn't exist under that request's scope, not that no record exists anywhere; refine scope or jurisdiction and consider an appeal.

## Gotchas & OpSec
- This is overt and on-the-record: a records request is a named legal action, not covert OSINT. Some jurisdictions notify affected third parties.
- Slow: responses take days to months; not a quick-lookup tool.
- Fees and exemptions vary sharply by state — read the profile before filing.

## Overlaps ("do both")
- Complements directory tools like `[[os-divorce-records]]`: those point you to which office holds a record, while MuckRock tells you the law and files the formal request to actually extract it.

## Trust & verifiability
`trust: trusted` — MuckRock is a reputable nonprofit transparency platform; its records-law research is authoritative and any document you obtain is a primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | state-public-records-laws |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (manual-review) |
