---
id: odbparser
name: ODBParser
description: Use when you have a `name`/`email`/keyword and want to find it inside exposed public databases — returns leaked PII (`email`, `phone`, `address`) from misconfigured Elasticsearch/MongoDB.
url: https://github.com/citcheese/ODBParser
category: search-engines
path:
- search-engines
bestFor: Searching and dumping PII from open (unauthenticated) Elasticsearch/MongoDB servers discovered via Shodan/BinaryEdge.
selectorsIn:
- name
- email
- username
selectorsOut:
- email
- phone
- address
status: live
pricing: free
costNote: Free, open-source Python tool. Requires your own (free-tier) Shodan and/or BinaryEdge API key to discover the exposed servers.
opsec: active
opsecNote: LEGALLY SENSITIVE and active. ODBParser connects to and dumps data from exposed third-party databases; accessing data on a server you do not own can be unlawful in many jurisdictions even when it is unauthenticated. The tool's own README restricts it to identifying exposed PII to warn owners, or querying databases you are authorised to access. Run only within a lawful mandate, from research infrastructure, and record your authorisation. Your Shodan/BinaryEdge queries and the connections to target hosts are logged.
humanInLoop: true
humanInLoopReason:
- api-key
- legal-gate
bestInteractionPattern: cli
trust: community
trustNote: Community open-source OSINT tool (citcheese/ODBParser); the data it returns is raw, unverified, and often stale breach/exposure content — treat every record as an unconfirmed lead.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- citcheese ODBParser
- Open Database Parser
tags:
- toddington
- curated-directory
- specialty-search
- exposed-databases
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# ODBParser

> A Python tool that finds exposed, unauthenticated Elasticsearch/MongoDB servers (via Shodan/BinaryEdge) and searches/dumps the PII inside them — powerful and legally fraught, for authorised use only.

## When to use
You have a selector — a `name`, `email`, `username`, or keyword — and want to check whether it appears in the vast pool of misconfigured, publicly exposed databases, which can contain names, emails, phones, addresses, and more. Use it when you have a lawful basis (authorised investigation, or notifying an owner of an exposure), not to trawl strangers' data on a whim.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `citcheese/ODBParser`, install Python 3.7.3+ and `requirements.txt`.
2. Add your Shodan and/or BinaryEdge API keys in `ODBconfig.py`.
3. Run with filters, e.g. `python ODBParser.py -cn US -p 8080 -t users --elastic --shodan --csv` (country, port, search term, engine, output format). Also accepts single IPs, a file of IPs, or clipboard input.
4. Review the parsed output (JSON/CSV) for records matching your selector.
5. Pivot: a hit gives contact fields to corroborate elsewhere — but confirm against a primary source before relying on any of it.

## Inputs → Outputs
- **In:** a search term / `name` / `email` / `username` (plus country/port filters)
- **Out:** matching records dumped from exposed databases — `email`, `phone`, `address`, and other PII fields present
- **Empty/negative result looks like:** no matching servers/records (nothing currently exposed with your term) — common and expected; absence is not proof the person isn't in some other (non-exposed) dataset.

## Gotchas & OpSec
- **Human-in-the-loop: api-key + legal-gate.** Needs Shodan/BinaryEdge keys, and lawful authority to access exposed data — do not run against arbitrary targets.
- Data is raw, unverified, often duplicated or stale from old exposures; heavy false-positive/outdated-record risk.
- Connecting to and dumping third-party servers is active and attributable — isolate your infrastructure.

## Overlaps ("do both")
- Complements Shodan itself — Shodan finds the exposed hosts, ODBParser automates searching and extracting the PII within them; and breach-lookup services cover leaked data ODBParser's live-exposure scan won't.

## Trust & verifiability
`trust: community` — a maintained open-source tool, but the *content* it surfaces is unverified exposure data; every field must be independently confirmed, and use must stay within legal authorisation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | odbparser |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, username → email, phone, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key, legal-gate) |
