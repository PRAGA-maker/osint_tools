---
id: prnewswire
name: PR Newswire (for Journalists)
description: Use when you have a company `employer-org` or person `name` and want press releases naming executives, spokespeople and media contacts — returns names, roles, organizations and often a PR contact `email`/phone.
url: https://prnmedia.prnewswire.com
category: people-search
path:
- people-search
bestFor: Mining corporate press releases for named executives, spokespeople and PR-contact details, plus expert sourcing via ProfNet.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- email
status: live
pricing: free
costNote: Free for content creators (journalists, freelancers, bloggers); a free registration unlocks profile customization and full downloads, but releases are publicly readable.
opsec: passive
opsecNote: Reading and searching press releases is passive and anonymous. If you register or use ProfNet to contact a source, you reveal an identity — use a sock-puppet journalist profile, not your real one, and never contact a subject's associates from a traceable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Cision; PR Newswire is a major official press-release distributor, so releases are authentic primary documents (though written by the issuing organization, i.e. promotional).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
relatedTools:
- pr-newswire
aliases:
- PRNewswire
- PR Newswire for Journalists
- prnmedia
- ProfNet
tags:
- expert-search
- press-releases
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# PR Newswire (for Journalists)

> A searchable archive of corporate press releases — a fast way to tie a `name` to a company and role, and to pull the PR contacts, executives and spokespeople an organization names publicly.

## When to use
You want to connect a person to an organization, or find the humans behind a company. Press releases routinely name executives (with titles), spokespeople, and a "media contact" with an `email` and phone. Search by `employer-org` to enumerate a company's named people and announcements, or by `name` to find where someone has been quoted or announced. ProfNet additionally connects you to experts/sources by field.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://prnmedia.prnewswire.com (register a free journalist/creator profile for full access and downloads; browsing releases works without it).
2. Search or browse "All News Releases" by company name, person, topic, or keyword.
3. Open matching releases and read for OSINT signals: named executives and titles, quoted spokespeople, and the "Media Contact" block (name, `email`, phone).
4. For sourcing, use **ProfNet** to find experts/spokespeople by expertise and organization.
5. Pivot: a media-contact `email`/phone feeds email/phone-OSINT; a named executive feeds LinkedIn/people-search; the company link maps the org around your subject.

## Inputs → Outputs
- **In:** `employer-org` (company) or `name`
- **Out:** `name`s + roles, `employer-org` links, and PR-contact `email`/phone from release footers
- **Empty/negative result looks like:** no releases for the company/person — the organization doesn't distribute via PR Newswire, or the individual has never been named in a release here. Try a competing wire (Business Wire, GlobeNewswire) before concluding nothing exists.

## Gotchas & OpSec
- Releases are **written by the issuing org** — treat claims as promotional, but the names, titles and contact details are usually accurate and directly usable.
- Coverage skews toward companies that pay to distribute; small/private entities may be absent.
- OpSec: **passive** to read; **active** if you register or contact a source — use a sock-puppet identity.

## Overlaps ("do both")
- Pairs with `[[pr-newswire]]` (same provider, public newsroom) and competing wires (Business Wire, GlobeNewswire) — running the same company across wires catches releases each one misses.

## Trust & verifiability
`trust: trusted` — a Cision-operated, established press-release distributor. Releases are authentic primary sources; just remember they are self-published by the subject organization, so cross-check factual claims independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | prnewswire |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
