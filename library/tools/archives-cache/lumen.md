---
id: lumen
name: Lumen Database
description: Use when you have a `domain`, URL, or company/person `name` and want to find legal takedown notices (DMCA, court orders) filed against online content — returns the notices, who complained, and what URLs were targeted.
url: https://lumendatabase.org/
category: archives-cache
path:
- archives-cache
bestFor: Discovering what content someone tried to remove from the internet (and who filed the request) via published takedown notices.
selectorsIn:
- domain
- name
selectorsOut:
- domain
- name
status: live
pricing: free
costNote: Free public research database (Harvard Berkman Klein Center); a free API/registration is available for bulk access.
opsec: passive
opsecNote: Fully passive — searching an archive of already-published legal notices. Nothing touches your subject and no one is notified. Some personal details in notices are redacted by Lumen; treat what remains as public record.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running academic transparency project (Harvard's Berkman Klein Center, formerly Chilling Effects); notices are primary-source documents submitted by platforms.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- copyright-search
aliases:
- Lumen
- Chilling Effects
- lumendatabase.org
tags:
- takedown
- dmca
- transparency
- archive
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Lumen Database

> A searchable archive of legal takedown notices (DMCA, court orders, right-to-be-forgotten) that platforms like Google and Twitter forward for transparency.

## When to use
You want to know what content connected to a `domain`, URL, person or company `name` someone has tried to suppress — and who filed the complaint. Takedown notices reveal removed URLs, the complaining party, and the legal basis. This can surface deleted pages worth chasing in archives, expose reputation-management campaigns, and link a complainant to the content they wanted gone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://lumendatabase.org/ and use the search box.
2. Query by `domain`/URL, complainant or target `name`, or keyword.
3. Open a notice to see the targeted URLs, the sender/principal, the recipient platform, and the date.
4. Take removed URLs into a web archive (Wayback) to recover the content that was taken down.
5. Pivot: a repeat complainant name can reveal a coordinated cleanup effort; targeted URLs map what someone wanted hidden.

## Inputs → Outputs
- **In:** `domain`/URL, or a complainant/target `name`
- **Out:** takedown notices — targeted URLs (`domain`s), sender/principal `name`, platform, date, legal basis
- **Empty/negative result looks like:** no notices found — nothing has been reported to Lumen for that term; it doesn't mean no takedowns ever happened (not every platform submits).

## Gotchas & OpSec
- Coverage depends on which platforms submit notices; absence isn't proof.
- Lumen redacts some personal info from notices; you'll see partial data by design.
- Targeted URLs may now be dead — pair with an archive to recover the content.

## Overlaps ("do both")
- Pairs with the Wayback Machine / archive tools — Lumen tells you *what* was removed and *by whom*; the archive recovers the actual content that was taken down.

## Trust & verifiability
`trust: trusted` — an established Harvard academic transparency archive of primary-source legal notices; entries are the actual documents platforms submitted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lumen |
