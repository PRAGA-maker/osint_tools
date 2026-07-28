---
id: idn-checker
name: IDN Checker
description: Use when you have a `domain` and want to find visually-similar (homograph) lookalike domains — returns registered impersonating `domain`s and their WHOIS.
url: https://holdintegrity.com/checker
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Spotting IDN/homograph lookalikes of a domain used for phishing or impersonation.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: The one-off checker is free to use; ongoing automated monitoring is sold as the paid "Domains Integrity Service."
opsec: passive
opsecNote: Passive — you query HoldIntegrity's checker about a domain string; the lookalike domains and their owners are not contacted. Only the checker's operator sees your query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by HoldIntegrity (a brand-protection vendor); the checker surfaces WHOIS/registration data for lookalikes, which is verifiable independently.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- central-ops
aliases:
- HoldIntegrity IDN checker
- homograph checker
tags:
- bellingcat-toolkit
- homograph
- phishing
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# IDN Checker

> A homograph/lookalike-domain checker: enter a domain and it finds internationalised (IDN) or otherwise visually-similar domains that could be impersonating it.

## When to use
You have a `domain` and want to know whether someone has registered a confusable version — using non-Latin characters that look like Latin ones (e.g. Cyrillic "а" for Latin "a"), or common typos — typically to phish or impersonate. In a missing-person or fraud context, a scam message or fake profile often links to such a lookalike domain; this tool tells you which impersonating domains exist and who registered them, giving a lead on the actor behind the scam.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://holdintegrity.com/checker.
2. Enter the legitimate `domain` and its TLD (in English/Latin).
3. Submit; it lists existing or possible homograph impersonations and, where a lookalike is registered, may show WHOIS/registration details.
4. For each registered lookalike, note the registrant, name servers, and hosting `ip-address`.
5. Pivot: run the lookalike through a full WHOIS/DNS report (e.g. `[[central-ops]]`) to get registrant and infrastructure, then correlate with the scam message.

## Inputs → Outputs
- **In:** `domain`
- **Out:** impersonating/lookalike `domain`s, plus (when registered) WHOIS and hosting `ip-address`
- **Empty/negative result looks like:** no registered lookalikes found — only theoretical variants exist, meaning no active impersonation is detected for that name.

## Gotchas & OpSec
- Passive and safe; no contact with the lookalike domains or their owners.
- The free checker is a point-in-time query — new lookalikes can be registered later (that's what the paid monitoring upsell covers).
- A "possible" variant that isn't registered is just a candidate, not evidence of impersonation.

## Overlaps ("do both")
- Pairs with `[[central-ops]]` — IDN Checker finds the lookalike, CentralOps' Domain Dossier resolves who owns and hosts it.

## Trust & verifiability
`trust: community` — a vendor tool, but its output (which lookalike domains exist and their WHOIS) is independently verifiable through any registrar/WHOIS lookup.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | idn-checker |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
