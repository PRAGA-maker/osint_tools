---
id: yaraif
name: YARAify
description: Use when you have a suspicious file or hash (`document-id`) and want to know what malware it is and what infrastructure it links to — returns domain and associate (sample/campaign) leads.
url: https://yaraify.abuse.ch/scan/
category: search-engines
path:
- search-engines
bestFor: Scanning a file or looking up a hash against a large YARA-rule and sample database to identify malware family and pivot to related samples and C2 infrastructure.
selectorsIn:
- document-id
selectorsOut:
- domain
- associate
status: live
pricing: free
costNote: Free community service run by abuse.ch (Spamhaus). No payment; an optional free API key (Auth-Key) enables programmatic scanning and lookups.
opsec: passive
opsecNote: Scanning uploads the file to abuse.ch, which shares malware intelligence with the community — do NOT upload files that contain victim/target PII or that would tip off an adversary, as submissions can become searchable. For a passive check, look up the file's hash rather than uploading the file itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by abuse.ch (now part of Spamhaus), a well-established, widely-cited threat-intelligence provider; its data underpins many commercial and open feeds.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- abusech
- malwarebazaar
- urlhaus
- zeus-c2-tracker
- zeus-tracker
aliases:
- yaraify.abuse.ch
- abuse.ch YARAify
tags:
- speciality-search-engines
- threat-intel
- malware
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# YARAify

> abuse.ch's file-scanning and YARA-hunting service — hand it a suspicious file or hash and it identifies the malware and links you to related samples and command-and-control infrastructure.

## When to use
You have a suspicious file, attachment, or a hash (`document-id` — MD5/SHA256) tied to a device, an email, or a seized artefact in an investigation, and you need to know what it is and what it connects to. YARAify matches the file against a large corpus of YARA rules (plus optional ClamAV and PE unpacking) and lets you search its database of prior submissions, pivoting a single sample into a malware family, related samples, and associated domains/C2.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://yaraify.abuse.ch/scan/.
2. To identify a file, upload it for scanning against the YARA-rule set (optionally enable ClamAV / PE unpacking). To stay passive, instead paste the file's **hash** into the database search.
3. Read the result: matched YARA rules and malware family, ClamAV verdict, and links from the sample to related submissions.
4. Use the database/hunting search to pivot on the hash, rule, or imphash to find sibling samples and the infrastructure they use.
5. Pivot: linked `domain`s/C2 feed URL/domain-OSINT tools; related samples/actors are `associate` leads; cross into abuse.ch's `[[malwarebazaar]]` and `[[urlhaus]]` for the full campaign picture.

## Inputs → Outputs
- **In:** a file, or a `document-id` (MD5/SHA256/imphash) to look up
- **Out:** malware family/rule matches, `domain`/infrastructure links, `associate` (related samples, campaigns)
- **Empty/negative result looks like:** "no matches" — the file matched no YARA rule and isn't in the database; that means unknown/clean-to-this-corpus, not proven safe. Corroborate with other multiscanners.

## Gotchas & OpSec
- Uploading shares the file with the community and it can become searchable — never upload files carrying victim PII or that would alert an adversary; look up the hash instead.
- A "no match" is not a clean bill of health; YARAify covers known rules/samples, not everything.
- Rate limits apply to anonymous use; grab a free API key for bulk/automated lookups.

## Overlaps ("do both")
- Pairs with `[[malwarebazaar]]` and `[[urlhaus]]` (same provider) — YARAify identifies and rule-matches the sample, MalwareBazaar holds the sample corpus, and URLhaus maps the malware-distribution URLs.

## Trust & verifiability
`trust: trusted` — abuse.ch/Spamhaus is a long-standing, widely-relied-upon threat-intel source; matches cite specific YARA rules and hashes you can re-verify against other multiscanners and the linked abuse.ch feeds.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yaraif |
| category | search-engines |
| selectorsIn → selectorsOut | document-id → domain, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
