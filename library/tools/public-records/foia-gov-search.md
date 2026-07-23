---
id: foia-gov-search
name: FOIA.gov Search
description: Use when you have a topic, agency, or `name` and want US federal records — returns previously-released FOIA documents and the path to file your own request.
url: https://search.foia.gov/
category: public-records
path:
- public-records
bestFor: Searching already-released federal FOIA records and finding the right agency to file a new request with.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free federal portal; filing a FOIA request is free to submit, though some agencies charge search/copy fees for large fulfillments.
opsec: passive
opsecNote: "Searching the FOIA library and reading released records is passive and anonymous. Filing an actual request is different — it is a formal, identity-attached legal action on the record with a federal agency, and the subject of the request is not notified but the request itself may later be released. Treat searching (passive) and requesting (attributable) as separate steps."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US government FOIA portal operated by the Department of Justice / OIP; it indexes agencies' own FOIA reading rooms and request pipelines.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- FOIA.gov
- search.foia.gov
tags:
- foia
- government
- records
source: inteltechniques-tools
lastVerified: '2026-07-23'
enrichment: full
---

# FOIA.gov Search

> The US government's central FOIA hub: search records federal agencies have already released, and — when the record you need isn't public — find and file with the right agency.

## When to use
You want federal government records tied to a topic, program, agency, or a public figure's `name` — inspection reports, correspondence, contracts, policy documents — either to read what's already been disclosed or to lodge a Freedom of Information Act request. In a missing-persons context this is a slow, indirect avenue (records mentioning a subject, or agency actions involving them), so relevance is low and the fulfillment timeline is long.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://search.foia.gov/ and enter keywords, an agency, or a `name` into the FOIA library search.
2. Review released documents in the results — many agencies post frequently-requested records here.
3. If the record isn't already public, use FOIA.gov's agency finder to identify which of the 100+ federal agencies holds it, then follow its request wizard.
4. Submit the request (passive search ends here; filing is an attributable action) and track the case number the agency issues.
5. Cite any released `document-id` and pivot facts (dates, orgs, names) into other record searches.

## Inputs → Outputs
- **In:** `name` / keyword / agency
- **Out:** released FOIA documents and their `document-id`/case references; a filed request pathway
- **Empty/negative result looks like:** no released records in the library — that only means nothing has been *proactively* posted, not that no records exist; a fresh request may still surface them (with a wait of weeks to months).

## Gotchas & OpSec
- Searching is passive and anonymous; **filing** a request is a formal, identity-attached action — plan accordingly.
- FOIA covers federal records only; state/local records use separate state public-records laws, not this portal.
- Fulfillment is slow and subject to exemptions (privacy, law-enforcement) — expect redactions and delays, and note personal records about a living third party are often exempt.

## Overlaps ("do both")
- Complements state/local public-records and government-directory tools — FOIA.gov is the federal lane; jurisdiction-specific records require the relevant state/agency portal. Use both to cover all levels of government.

## Trust & verifiability
`trust: trusted` — the official DOJ-operated FOIA portal indexing agencies' own releases; documents it returns are authoritative government records (read redactions and cover letters for context).
