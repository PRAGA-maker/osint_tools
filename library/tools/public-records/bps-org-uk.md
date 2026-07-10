---
id: bps-org-uk
name: bps.org.uk (Directory of Chartered Psychologists)
description: Use when you have a `name` of someone claiming to be a UK psychologist and want to verify BPS membership/chartered status — returns the practitioner's `name`, chartered status, and location/`employer-org` area.
url: https://www.bps.org.uk/lists/DIR
category: public-records
path:
- public-records
bestFor: Verifying whether someone is a British Psychological Society member / Chartered Psychologist, and finding chartered psychologists by area.
selectorsIn:
- name
- address
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free public directory lookup; no account needed.
opsec: passive
opsecNote: A public professional-directory search — you query the register, nothing reaches the subject. No login; standard browser hygiene only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The British Psychological Society is the UK professional body for psychology; its directory of Chartered Psychologists is authoritative for membership/chartered status (though statutory practice regulation is via the HCPC).
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- British Psychological Society
- BPS Directory of Chartered Psychologists
tags:
- professionlicensing
- Profession & Licensing Sites
- uk-professional-register
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# bps.org.uk (Directory of Chartered Psychologists)

> The British Psychological Society's public directory — verify that a person is a BPS member / Chartered Psychologist, or find chartered psychologists in an area.

## When to use
You have a `name` of someone presenting as a psychologist and need to verify their BPS membership / Chartered Psychologist status — checking a claimed professional credential, tying a person to a practice/`employer-org`, or finding chartered psychologists near a location. A credential-verification tool rather than a person-locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bps.org.uk/lists/DIR.
2. Search by practitioner `name` (or browse by area/specialism).
3. Read the entry: `name`, chartered/membership status, specialism, and location/practice area.
4. Cross-check regulated practice: "Chartered Psychologist" is a BPS status, but statutory practitioner-psychologist titles are regulated by the **HCPC** — verify there too for clinical/practising roles.
5. Pivot: confirmed practice/area → `employer-org` and location leads; a mismatch (claims the title but isn't listed) is itself a finding.

## Inputs → Outputs
- **In:** `name` (or area/specialism)
- **Out:** `name`, chartered/BPS-membership status, specialism, practice `address`/area, `employer-org` context
- **Empty/negative result looks like:** no listing — the person may not be a BPS member/Chartered Psychologist (they might be HCPC-registered under a different title, or making an unverified claim). Absence is meaningful for credential-checking.

## Gotchas & OpSec
- BPS ≠ HCPC: chartered status is BPS; the legally protected practitioner titles are HCPC-registered — check both.
- UK-only, psychology only.
- Directory listing depends on the member opting in; some legitimate members may not appear.

## Overlaps ("do both")
- Pairs with the **HCPC register** (statutory regulation of practitioner psychologists) and `[[gassaferegister-co-uk]]`/`[[labcfrontdoor-co-uk]]` for other UK professional checks — BPS confirms chartered status, HCPC confirms legal registration to practise.

## Trust & verifiability
`trust: trusted` — the official professional-body directory; authoritative for BPS/chartered status. For "can they legally practise," corroborate with the HCPC register.
