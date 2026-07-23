---
id: id-ransomware
name: ID Ransomware
description: Use when you have a ransom note or encrypted file and want to identify the ransomware — returns the family/variant plus decryptor and reference info.
url: https://id-ransomware.malwarehunterteam.com/
category: documents-metadata
path:
- documents-metadata
- search
bestFor: Identifying which ransomware family hit a victim, from a ransom note, encrypted sample, or ransom contact details.
selectorsIn:
- crypto-wallet
- email
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free service by MalwareHunterTeam. No account.
opsec: active
opsecNote: You upload a ransom note and/or a (usually small, encrypted) sample file to a third-party service. Encrypted victim files may still carry a filename or path revealing PII — review before uploading, and use the identify-only path rather than sharing more than needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by MalwareHunterTeam and endorsed within the community (linked from Bleeping Computer / No More Ransom workflows); the de-facto first-stop for ransomware identification.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ID-Ransomware
- MalwareHunterTeam ID Ransomware
tags:
- ransomware
- malware-identification
- incident-response
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# ID Ransomware

> Paste the ransom note (or upload an encrypted file) and it tells you which ransomware family you're dealing with — and whether a free decryptor exists.

## When to use
A device in a case has been hit by ransomware and you need to identify the exact family/variant — to find a decryptor, understand the actor, or extract IOCs. ID Ransomware matches against 1000+ known families using the ransom note text, an encrypted file sample, or the attacker's contact details (email, `crypto-wallet`, onion URL). It's incident-response/identification; missing-persons relevance is low (its investigative value is attribution and extracting the attacker's payment `crypto-wallet`/`email` to pivot on).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://id-ransomware.malwarehunterteam.com/.
2. Provide identifiers: upload the ransom note file and/or a sample encrypted file, and paste the attacker's contact info (email, Bitcoin address, onion site) into the fields.
3. Submit — it reports the matched family/variant (or "no match / multiple matches"), with links to relevant decryptors and write-ups.
4. Pivot: the attacker's payment `crypto-wallet` feeds blockchain tracing; their `email`/onion feeds infrastructure/actor research; the family name feeds No More Ransom for a decryptor and threat-intel for TTPs.

## Inputs → Outputs
- **In:** ransom note text/file, encrypted sample, and/or attacker `email`/`crypto-wallet`/onion
- **Out:** ransomware family/variant identification, decryptor availability, reference links, and (echoed) attacker `crypto-wallet`/`email` to pivot on
- **Empty/negative result looks like:** "no match found" or several possible families — a new/rare variant or too-little signal; provide more of the note/sample or check back as signatures update.

## Gotchas & OpSec
- **Privacy:** encrypted files can still expose PII via filenames/paths; review before uploading and share the minimum needed for identification.
- A "no match" doesn't mean the file is safe — it may be a novel variant.
- Identification ≠ decryption; a matched family may have no free decryptor.
- OpSec: active (you upload to a third party) — but that's inherent to identification; avoid uploading sensitive documents beyond the note/sample.

## Overlaps ("do both")
- Feeds No More Ransom (decryptor lookup) and threat-intel/sandbox tools like `[[hybrid-analysis]]`; the extracted `crypto-wallet` feeds blockchain-analysis tools. ID Ransomware *names* the threat; those *act* on it.

## Trust & verifiability
`trust: trusted` — the community-standard identification service run by MalwareHunterTeam; matches are reliable, though a negative/ambiguous result reflects signature coverage, not a verdict on the file's safety.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | id-ransomware |
| category | documents-metadata |
| selectorsIn → selectorsOut | crypto-wallet, email → crypto-wallet |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
