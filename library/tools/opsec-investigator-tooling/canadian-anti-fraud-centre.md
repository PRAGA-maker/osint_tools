---
id: canadian-anti-fraud-centre
name: Canadian Anti-Fraud Centre
description: Use when you have a suspected scam/fraud pattern in Canada and want to identify the fraud type or report it — an official reference/reporting portal, returns fraud classifications, not personal selectors.
url: https://www.antifraudcentre-centreantifraude.ca/index-eng.htm
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Identifying a Canadian fraud/scam type and filing an official fraud report.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free official Canadian government service (RCMP partnership); no account for browsing, reporting is free.
opsec: passive
opsecNote: Browsing the fraud A–Z is passive and anonymous. Filing a report submits information to a Canadian law-enforcement body — do so deliberately and only with the reporter's consent, since it enters an official system.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Government of Canada / RCMP-partnered central agency for fraud and identity-theft reporting; authoritative for Canadian scam typologies and reporting procedure.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CAFC
- Centre antifraude du Canada
tags:
- opsec
- fraud
- reference
- canada
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# Canadian Anti-Fraud Centre

> Canada's official central fraud-reporting agency — a reference for identifying scam/fraud types and the channel for filing a fraud report.

## When to use
You're dealing with a suspected scam or fraud with a Canadian nexus and need to (a) classify what kind of fraud it is, or (b) report it through the proper official channel. The CAFC maintains an A–Z index of scam, phishing, hoax and identity-theft types with descriptions and current alerts, and provides the national fraud-reporting mechanism. It's a reference and reporting tool, not a lookup that returns data about an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.antifraudcentre-centreantifraude.ca/index-eng.htm.
2. To identify a scam: browse the A–Z index / "frauds by medium" / audience categories and match the observed pattern to a documented type.
3. Read the type's description and any active alerts to understand the modus operandi and red flags.
4. To report: use the "Report fraud" section and follow the official process (this submits to law enforcement — see OpSec).
5. Pivot: use the identified fraud type to guide the technical investigation (e.g. a phishing typology tells you what infrastructure/selectors to chase in domain/email tools).

## Inputs → Outputs
- **In:** none (a fraud pattern/behaviour you're trying to classify) — no personal selector
- **Out:** fraud-type classification, modus-operandi descriptions, current alerts; a reporting channel (no data about a specific person is returned)
- **Empty/negative result looks like:** no listed type cleanly matches your scenario — the scam may be novel, non-Canadian, or a hybrid. The site classifies and receives reports; it does not look up perpetrators for you.

## Gotchas & OpSec
- Human-in-the-loop: filing a report is a deliberate legal action (legal-gate) — it goes into an official law-enforcement system, so only report with the affected person's consent.
- OpSec: browsing is **passive** and anonymous; reporting is not anonymous in effect and shouldn't be done casually.
- Canada-focused. For frauds tied to other jurisdictions, use the equivalent national body (e.g. IC3 in the US, Action Fraud in the UK).

## Overlaps ("do both")
- Complements technical investigation tools — CAFC tells you *what kind* of fraud you're looking at and where to report it; domain/email/phone tools tell you *who and how*. Pair the typology with the equivalent agency in the relevant country.

## Trust & verifiability
`trust: trusted` — the official Government of Canada / RCMP-partnered anti-fraud centre, authoritative for Canadian fraud typologies and the national reporting process.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-anti-fraud-centre |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
