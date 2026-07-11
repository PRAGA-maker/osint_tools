---
id: solicitorstribunal-org-uk
name: Solicitors Disciplinary Tribunal — Judgment Search
description: Use when you have a `name` of a solicitor in England & Wales and want to check for published disciplinary judgments against them — returns case document-id, findings/outcome and employer-org (firm) context.
url: https://www.solicitorstribunal.org.uk/judgment-search-results#search
category: public-records
path:
- public-records
bestFor: Checking whether a solicitor in England & Wales has faced disciplinary proceedings and the outcome.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- document-id
- employer-org
status: live
pricing: free
costNote: Free public search of published disciplinary judgments; no account or payment.
opsec: passive
opsecNote: A public tribunal record; searching is passive and the subject is not notified. No login required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Solicitors Disciplinary Tribunal (SDT) is the statutory disciplinary body for solicitors in England & Wales; published judgments are authoritative first-party records.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- SDT judgment search
- Solicitors Disciplinary Tribunal
tags:
- professionlicensing
- disciplinary-records
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Solicitors Disciplinary Tribunal — Judgment Search

> The statutory record of disciplinary proceedings against solicitors in England & Wales — search a solicitor's name to see whether they've been struck off, suspended, fined, or cleared.

## When to use
You have a `name` (and possibly a firm) of a solicitor in England & Wales and want to assess integrity/background: has this person faced disciplinary action, and what was the outcome? Useful for due diligence, corroborating or challenging a professional's standing, and adding adverse-record context to a subject profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.solicitorstribunal.org.uk/judgment-search-results#search.
2. Search by respondent name; optionally filter by case number, allegation/breach type, or outcome.
3. Read the results: case number, respondent name, outcome (e.g. "Strike off", "Suspend – Fixed Period", "Not Proved/Dismissed"), and the full judgment document.
4. If the solicitor isn't in the published judgments, that generally means no published SDT finding (the tribunal notes staff can assist for older/archived matters).
5. Pivot: a judgment names the firm(s) and often other parties (`employer-org`, `associate`), and the full text can corroborate dates, roles and conduct; combine with the SRA register for current practising status.

## Inputs → Outputs
- **In:** solicitor `name` (optionally firm/`employer-org`)
- **Out:** case `document-id`, respondent `name`, disciplinary outcome, firm/`employer-org` context, and full judgment text
- **Empty/negative result looks like:** no published judgment for that name — means no SDT disciplinary finding is published (a good sign), not proof of a spotless record; recent hearings can take up to ~7 weeks to publish.

## Gotchas & OpSec
- Publication lag: judgments typically appear within ~7 weeks of a hearing; very recent matters may not yet show.
- Scope: England & Wales solicitors only — not barristers (BSB), not Scotland/NI. For current practising status use the SRA register instead.
- OpSec: passive, authoritative public record; no subject notification.

## Overlaps ("do both")
- Pairs with the SRA (Solicitors Regulation Authority) register — the SDT shows disciplinary history; the SRA register shows current practising status and firm.

## Trust & verifiability
`trust: trusted` — first-party statutory tribunal; published judgments are authoritative. The full judgment PDF is the primary source — read it rather than relying on the summary outcome alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | solicitorstribunal-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
