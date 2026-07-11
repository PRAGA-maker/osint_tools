---
id: leakey
name: LEAKEY
description: Use when you have a leaked API key/token/credential (e.g. found in a breach or paste) and want to validate whether it is still live and which service it belongs to — returns an active/revoked status and the owning service/employer-org.
url: https://github.com/rohsec/LEAKEY/
category: people-search
path:
- people-search
bestFor: Validating leaked credentials/API tokens (45+ signature types) to see if they are still active during an assessment.
selectorsIn:
- document-id
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free and open source (GitHub); install and run locally. No paid tier.
opsec: active
opsecNote: LEAKEY actively sends authenticated requests to each service's API to test whether a credential is live — that touches the third-party service (and, implicitly, the credential owner's account infrastructure), and can be logged or alert the owner. Only run it against credentials you are legally authorised to test (e.g. your own assessment scope); testing someone else's live keys may be unlawful.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An open-source security utility (rohsec/LEAKEY); code and signatures are auditable. It is a pentest/credential-validation tool, not a person-finder — its people-OSINT relevance is indirect (validating creds found in a subject's breached data).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- leakey
- leaky
tags:
- Universal Contact Search and Leaks Search
- credential-validation
- breach
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# LEAKEY

> A bash utility that takes a leaked API key or token and checks whether it's still live — matching it against 45+ service signatures and calling the real API to confirm validity. A credential-validation tool, not a person-finder.

## When to use
You have a credential — an API key, token, or secret — surfaced from a breach, paste, exposed repo, or a subject's leaked data, and you need to know (a) which service it belongs to and (b) whether it still works. In a people-OSINT context this is a secondary, technical step: confirming that infrastructure/accounts tied to a subject are live. It does not search for people by name/email/phone.

## How to use it (`bestInteractionPattern`: cli)
1. Install locally: `curl https://raw.githubusercontent.com/rohsec/LEAKEY/master/install.sh -o leaky_install.sh && chmod +x leaky_install.sh && bash leaky_install.sh` (requires `jq`).
2. Run `leaky` in the terminal; it loads validation checks from `~/.leakey/signatures.json`.
3. Provide the credential to test; LEAKEY matches its signature and calls the service's auth endpoint to check validity.
4. Extend coverage by adding new service signatures to the JSON config.
5. Pivot: a live key identifies the owning service (`employer-org`/platform) and confirms an active account tied to the subject's infrastructure — a lead for further, authorised investigation.

## Inputs → Outputs
- **In:** a leaked credential/API token (`document-id`-style secret)
- **Out:** the owning service (`employer-org`) and a live/revoked validity status
- **Empty/negative result looks like:** no signature match (unknown credential type) or a "revoked/invalid" response — the key is dead, rotated, or not a recognised type. It never returns personal contact details.

## Gotchas & OpSec
- **Not a people-search tool:** despite its seeded category, LEAKEY validates machine credentials — it will not turn a name/email into a person. Set expectations accordingly.
- **Active and legally sensitive:** testing a live key contacts the real service and may alert the owner or breach terms of use/law. Only test credentials within your authorised scope.
- Requires local install and `jq`; signature coverage is whatever's in the config.

## Overlaps ("do both")
- Pairs with breach/leak discovery tools (`[[personal-data-leak-checker]]`, secret scanners) — those surface that a credential leaked; LEAKEY tells you if it still works.

## Trust & verifiability
`trust: community` — an auditable open-source utility. Its validity checks are authoritative (it calls the real API), but its OSINT role is narrow and technical; treat it as an infrastructure-validation step, not identity discovery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leakey |
| category | people-search |
| selectorsIn → selectorsOut | document-id → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
