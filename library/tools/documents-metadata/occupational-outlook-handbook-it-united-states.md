---
id: occupational-outlook-handbook-it-united-states
name: Occupational Outlook Handbook – IT (United States)
description: Use when you have a claimed US IT job title or salary and want to sanity-check it against official occupation data — a reference source, returns `employer-org`/role context, not people.
url: http://www.bls.gov/ooh/computer-and-information-technology/home.htm
category: documents-metadata
path:
- documents-metadata
bestFor: Verifying that a claimed IT job title, duties, credentials and pay band are plausible against official US labor-statistics data.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free official US government (Bureau of Labor Statistics) reference; no account.
opsec: passive
opsecNote: You are reading published government reference material — no subject interaction, no login. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party US Bureau of Labor Statistics publication; authoritative reference for occupational descriptions and pay in the United States.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- BLS OOH Computer and Information Technology
- Occupational Outlook Handbook IT
tags:
- reference
- labor-statistics
- documents-metadata
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Occupational Outlook Handbook – IT (United States)

> The US Bureau of Labor Statistics' reference on computer & IT occupations — a plausibility check for job-title, duties and salary claims, not a source on any individual.

## When to use
This is a reference document, useful for *verification by context* rather than finding people. When a subject or a document claims a specific US IT role — "senior network architect," a stated salary, particular duties or entry requirements — the OOH lets you confirm whether the title, typical responsibilities, required education, and pay band are realistic. It's handy for spotting résumé embellishment, vetting a claimed profession in due diligence, or grounding an interview/profile in what the role actually entails.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the BLS OOH Computer and Information Technology hub (link above; if BLS has reorganized, search "BLS OOH" plus the occupation).
2. Pick the occupation that matches the claim (e.g. "Computer Network Architects," "Information Security Analysts").
3. Read the standardized fields: duties, work environment, education/credentials required, median pay, and job outlook.
4. Compare against the subject's claim — mismatches (e.g. a title requiring a degree the subject lacks, or a salary far outside the band) are flags to probe.
5. Pivot: use confirmed role/credential expectations to frame further checks (licensing bodies, professional registries, `employer-org` records).

## Inputs → Outputs
- **In:** an `employer-org`/occupation context (a claimed US IT job title or role)
- **Out:** standardized occupation data — duties, required education, median pay, outlook (role/`employer-org` context, never an individual)
- **Empty/negative result looks like:** the claimed title isn't a recognized BLS occupation (possibly an internal/marketing title rather than a standard one) — informative in itself, not a dead end.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully **passive**; reading public reference data.
- US-only and national-median: it describes occupations in aggregate, not a specific employer's titles or a person's actual pay. Use it to test plausibility, not to assert facts about an individual.

## Overlaps ("do both")
- Pairs with professional-licensing registries and company-records tools — the OOH tells you what a role *should* involve; those confirm whether a specific person actually holds the credential or job.

## Trust & verifiability
`trust: trusted` — a first-party US Bureau of Labor Statistics publication, authoritative and methodologically documented for US occupational data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | occupational-outlook-handbook-it-united-states |
| category | documents-metadata |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
