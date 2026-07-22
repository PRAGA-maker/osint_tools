---
id: malpedia
name: Malpedia
description: Use when you have a malware family name or sample and want authoritative family context, references and YARA rules — returns malware family analysis and threat-actor links.
url: https://malpedia.caad.fkie.fraunhofer.de/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Identifying and getting reference context on a malware family (aliases, references, YARA, actor associations).
selectorsIn: []
selectorsOut:
- associate
status: live
pricing: free
costNote: Free to use; the public inventory and statistics are open, but full sample/YARA access is gated behind an invite-only trust-group account.
opsec: passive
opsecNote: Browsing the public inventory is passive research against a reference DB, not the target. Uploading a sample or querying via an authenticated account ties activity to your identity — use an appropriate research account for anything beyond public browsing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Fraunhofer FKIE (a German research institute); a well-curated, citation-grade malware reference used across the threat-intel community.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: true
deprecated: false
relatedTools: []
aliases:
- Fraunhofer Malpedia
tags:
- malware
- threat-intel
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Malpedia

> A curated, research-grade malware encyclopedia from Fraunhofer FKIE — family identification, aliases, references and YARA rules, with a public browse layer over an invite-only sample store.

## When to use
An investigation surfaces a malware family name, a hash, or an indicator, and you need authoritative context: what the family actually is, its aliases across vendors, which threat actors use it, published analyses, and YARA rules to hunt for it. Malpedia is the reference you cite when you need to disambiguate the many vendor names for the same malware.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://malpedia.caad.fkie.fraunhofer.de/.
2. Browse or search the public **inventory** by family name or alias.
3. Read the family page: description, aliases, external references, associated actors, and available YARA rules.
4. For sample downloads and non-public YARA, you need an invite-only account — request access if your work justifies it.
5. Pivot: associated-actor names and referenced reports (`associate`) feed threat-actor and campaign research; use the ApiVector/API for programmatic lookups once authenticated.

## Inputs → Outputs
- **In:** a malware family name / alias (or, with an account, a sample)
- **Out:** family analysis, alias mapping, references, `associate` (threat-actor) links, YARA rules
- **Empty/negative result looks like:** an unindexed or brand-new family returns no match — absence means Malpedia hasn't catalogued it, not that the family is fake; check vendor reporting.

## Gotchas & OpSec
- Two tiers: public inventory/stats are open; samples and some YARA require an invite-only trust-group account.
- Aliases are the point — one family has many vendor names; use Malpedia to normalise them before correlating across sources.
- OpSec: passive for public browsing; authenticated actions are attributable to your account.

## Overlaps ("do both")
- Complements sample sandboxes and hash-lookup services — those tell you *what a specific file does*, Malpedia tells you *which known family and actor* it belongs to and gives citations.

## Trust & verifiability
`trust: trusted` — curated by Fraunhofer FKIE with references on each entry, making it a citable, authoritative malware reference rather than a crowd list.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | malpedia |
