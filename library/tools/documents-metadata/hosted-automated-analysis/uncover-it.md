---
id: uncover-it
name: Uncover It
description: Use when you have a malware sample/executable and want fast static config extraction (C2 servers, keys, indicators) without detonating it — returns ip-address, domain, document-id.
url: https://www.uncoverit.org/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
bestFor: Static extraction of malware configuration (C2, keys, IOCs) from a sample without running it.
selectorsIn:
- document-id
selectorsOut:
- ip-address
- domain
- crypto-wallet
status: live
pricing: free
costNote: Free hosted analysis service; no account required for basic use.
opsec: active
opsecNote: Uploading a sample sends the file to a third-party service where it (and any embedded indicators/victim data) is processed and may be retained or shared with the security community. Only submit samples you're authorised to share; never upload a file containing a victim's private data or a sample tied to a sensitive live investigation. Analysis is static (no execution), so the malware's C2 is not contacted by the tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A hosted malware-config extraction service (arf-seed listing). Automated static parsers can misparse packed/novel samples; treat extracted config as a lead and confirm in a controlled environment.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- virustotal
- malware-bazaar
- any-run
tags:
- malware-analysis
- config-extraction
- threat-intel
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Uncover It

> A hosted static malware-config extractor: upload a sample and it pulls out the embedded C2 servers, keys, and indicators — fast, and without ever executing the code.

## When to use
Your investigation reached a malicious binary/document (from a phishing email, a compromised device, a threat-intel lead) and you need its network indicators — C2 `domain`s/`ip-address`es, campaign identifiers, sometimes `crypto-wallet` addresses — to pivot on the infrastructure or actor. Static, so it's faster and quieter than a sandbox detonation. Infrastructure/CTI-oriented; low relevance to a person-centric case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.uncoverit.org/.
2. Upload the malware sample / executable (only if you're cleared to share it).
3. Let it statically parse the sample — no detonation occurs.
4. Read the extracted configuration: C2 endpoints, encryption keys, mutexes, and other IOCs.
5. Pivot: a C2 `domain`/`ip-address` → `[[virustotal]]`/passive DNS and reverse-IP to map the campaign; a hash → `[[malware-bazaar]]` for related samples.

## Inputs → Outputs
- **In:** a malware sample / file (referenced by hash, a `document-id`)
- **Out:** `domain` & `ip-address` C2 endpoints, keys/indicators, sometimes `crypto-wallet` addresses
- **Empty/negative result looks like:** no config extracted — the sample may be packed, a family the parser doesn't support, or benign. A null result isn't proof the file is clean; escalate to a sandbox.

## Gotchas & OpSec
- **Uploading shares the file:** assume submitted samples may be retained/shared with the community. Never upload files containing victim PII or tied to a sensitive investigation.
- Static parsers miss packed/obfuscated or novel families — pair with dynamic analysis when it comes up empty.
- Extracted IOCs are leads; validate before acting (e.g. before attributing infrastructure).

## Overlaps ("do both")
- Pairs with `[[any-run]]` (dynamic sandbox) when static extraction fails, and with `[[virustotal]]` / `[[malware-bazaar]]` to correlate the hash and indicators across the wider corpus.

## Trust & verifiability
`trust: unverified` — a hosted automated parser with no transparency on its config coverage. Good for a fast first pass; confirm extracted indicators in a controlled analysis before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uncover-it |
| category | documents-metadata |
| selectorsIn → selectorsOut | document-id → ip-address, domain, crypto-wallet |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
