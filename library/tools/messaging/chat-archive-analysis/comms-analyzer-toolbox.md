---
id: comms-analyzer-toolbox
name: Comms Analyzer Toolbox
description: Use when you have an exported `email` (MBOX) or SMS/iMessage (CSV) archive and want to index, search and timeline it — returns searchable records, `associate` contact graphs and activity timelines.
url: https://github.com/bitsofinfo/comms-analyzer-toolbox
category: messaging
path:
- messaging
- chat-archive-analysis
bestFor: Turning a raw MBOX email dump or CSV message export into a searchable Elasticsearch/Kibana index for timeline and contact-pattern analysis.
selectorsIn:
- email
- phone
- name
selectorsOut:
- associate
- email
- phone
status: live
pricing: free
costNote: Free and open source (MIT). Runs locally in Docker; no paid tier or cloud dependency.
opsec: passive
opsecNote: Purely local analysis — the toolbox spins up Elasticsearch/Kibana in Docker and ingests files you already hold; nothing is uploaded and no target is contacted. OpSec risk is data-handling: you are indexing someone's private messages, so run it on an encrypted, access-controlled machine and destroy the index afterwards.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: docker
trust: community
trustNote: Open-source project by bitsofinfo on GitHub; code is auditable but community-maintained, not a vetted commercial forensics suite.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- aleph
aliases:
- comms-analyzer-toolbox
- bitsofinfo comms analyzer
tags:
- chat-archive-analysis
- email-forensics
- timeline-analysis
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Comms Analyzer Toolbox

> A Dockerised Elasticsearch + Kibana stack that ingests an MBOX/CSV comms dump and makes it searchable and timelineable — forensic triage of someone's own message history when you lawfully hold the export.

## When to use
You have possession of a communications archive — a Gmail/Outlook **MBOX** export, or a **CSV** of iPhone SMS/iMessages (e.g. pulled with iMessage/text-export tools) — and you need to go from a flat file to answers: who did they talk to most, when did contact with a person start or stop, what was said around a key date. In a missing-person context this is for the subject's own recovered devices/accounts (with proper authority/consent): it surfaces `associate` contacts, last-activity `email`/`phone` endpoints, and a timeline that can bracket disappearance or reveal a plan.

## How to use it (`bestInteractionPattern`: docker)
1. Install Docker on your (offline/isolated) analysis machine and clone/pull the toolbox image per the GitHub README.
2. Prepare your input: an `.mbox` email archive, and/or a `.csv` message export with a datetime column.
3. Run the container, mounting your data file and passing the import parameters (file path, type, index name). The container boots Elasticsearch + Kibana and imports each message as a searchable document (sender, recipient, subject, body for email; all columns for CSV).
4. Open Kibana in your browser and analyse: full-text search the body, aggregate by sender/recipient to rank `associate` contacts, and build a Discover/visualisation timeline to see activity over dates.
5. Pivot: top contacts become `associate`/`email`/`phone` leads for other tools; a specific address or number feeds email/phone OSINT; the timeline scopes where to look next.

## Inputs → Outputs
- **In:** `email` archive (MBOX), SMS/iMessage export (CSV) — optionally seeded by a known `name`/`phone` to search for
- **Out:** searchable message records, ranked `associate`/contact graph, `email`/`phone` endpoints, activity timeline
- **Empty/negative result looks like:** import completes but the index is empty or fields are unparsed — usually a malformed MBOX, wrong CSV delimiter, or a missing datetime column; fix the export format and re-import.

## Gotchas & OpSec
- Human-in-the-loop: results are raw records — you must manually read, correlate and interpret; it does no entity resolution or judgement for you.
- OpSec: **passive** and fully local — no upload, no target contact. The real exposure is legal/ethical: you are indexing private communications, so ensure lawful authority, run on an encrypted host, and delete the Elasticsearch index when done.
- Elasticsearch is memory-hungry; a large MBOX needs adequate RAM/disk or the import stalls.

## Overlaps ("do both")
- Pairs with `[[aleph]]` — Aleph is better for cross-referencing an archive against other datasets and entities, while this toolbox is the fast local option for full-text search and timelining a single message dump.

## Trust & verifiability
`trust: community` — open-source and code-auditable on GitHub, but maintained by an individual rather than a certified forensics vendor. Fine for investigative triage; for evidentiary work, corroborate findings and preserve original files with a proper chain of custody.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | comms-analyzer-toolbox |
| category | messaging |
| selectorsIn → selectorsOut | email, phone, name → associate, email, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | docker |
| opsec | passive |
| human-in-loop | yes (manual-review) |
