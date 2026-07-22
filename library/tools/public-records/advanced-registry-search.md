---
id: advanced-registry-search
name: Registry of Lobbyists — Advanced Search (Canada)
description: Use when you have a `name` or `employer-org` and want to see federal lobbying registrations, clients, and lobbied officials in Canada — returns `name`, `employer-org`, `associate` links.
url: https://lobbycanada.gc.ca/app/secure/ocl/lrs/do/advSrch?lang=eng
category: public-records
path:
- public-records
bestFor: Searching Canada's federal Registry of Lobbyists by lobbyist, firm, client, or subject matter.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Free public government registry operated by the Office of the Commissioner of Lobbying of Canada; no account required.
opsec: passive
opsecNote: Querying a public federal registry is passive and leaves no trace with the subject. It reflects official filings, not your interest.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Government of Canada registry (Office of the Commissioner of Lobbying); filings are legally required and authoritative.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Registry of Lobbyists Canada
- lobbycanada.gc.ca advanced search
- OCL registry
tags:
- public-records
- government
- lobbying
- canada
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Registry of Lobbyists — Advanced Search (Canada)

> Canada's official federal lobbying registry — ties a name or organisation to who they lobbied, for whom, and on what.

## When to use
You have a `name` or an `employer-org` with a Canadian public-affairs angle and want to establish their lobbying activity: which firm/organisation a person lobbies for, which clients they represent, which government institutions and officials they contacted, and the subject matter. In an investigation this maps professional associations, employers, and networks of a subject active in Canadian government relations, and corroborates claimed roles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the advanced search at https://lobbycanada.gc.ca (Registry of Lobbyists → Advanced Search).
2. Search by lobbyist `name`, firm/organisation, client, or subject-matter keyword.
3. Open a registration to read the registrant, the client/employer, listed lobbyists, targeted institutions, and communication reports (monthly meeting logs naming officials).
4. Pivot: the client `employer-org`, co-registered lobbyists (`associate`), and named officials feed company-registry, LinkedIn (`[[linkedin]]`), and news searches.

## Inputs → Outputs
- **In:** `name` / `employer-org` / subject keyword
- **Out:** `name` (registered lobbyists), `employer-org` (firms/clients), `associate` (co-lobbyists and lobbied officials), subject matter, meeting dates
- **Empty/negative result looks like:** no registration — the person/org is not a registered federal lobbyist (most people aren't). It says nothing about provincial lobbying or non-lobbying activity.

## Gotchas & OpSec
- Federal only; provinces (Ontario, Quebec, BC, etc.) run separate registries — check those too for a full picture.
- Only registrable lobbying appears; informal influence isn't captured.
- OpSec: passive public-record lookup; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with `[[linkedin]]` and company-registry tools to corroborate employers and roles, and with provincial lobbyist registries for coverage the federal registry omits.

## Trust & verifiability
`trust: trusted` — an official Government of Canada registry backed by mandatory legal filings; the data is authoritative, though limited to what the law requires to be registered.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | advanced-registry-search |
| category | public-records |
