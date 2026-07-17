---
id: pubpeer
name: PubPeer
description: Use when you have a `name`, DOI, or paper title and want post-publication peer critique — returns comment threads flagging errors, image manipulation, corrections, and retractions on that author's work.
url: https://pubpeer.com/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Checking whether a researcher's or paper's credibility has been publicly challenged — flags, corrections, retractions.
selectorsIn:
- name
- document-id
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free to search and read; no account needed. An account (and often verified authorship) is required only to post comments.
opsec: passive
opsecNote: Searching and reading PubPeer is passive and not disclosed to paper authors. The browser extension, if installed, sends the DOIs of pages you visit to PubPeer to check for comments — use the website directly if you don't want that.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by the non-profit PubPeer Foundation; comments are crowd-sourced (often anonymous) critique, so individual claims range from rigorous to speculative — read the evidence, not just the flag.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- PubPeer post-publication review
- pubpeer.com
tags:
- academic
- publication-verification
- credibility
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# PubPeer

> The "journal club of the internet": post-publication comment threads attached to scientific papers, flagging errors, image manipulation, corrections, and retractions.

## When to use
You are vetting a researcher, an academic claim, or a specific paper — checking a subject's scientific credibility, or verifying a study before you rely on it. Search a `name`, DOI, or title and PubPeer shows any public critique attached to that author's or paper's work: statistical problems, duplicated/manipulated figures, undisclosed conflicts, and links to formal corrections or retractions. It's a fast way to see whether a publication has been contested.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://pubpeer.com/ and search by author `name`, DOI, or paper title.
2. Open matching entries and read the comment threads — note the specific evidence raised (e.g. figure overlays, source-data discrepancies) rather than just the existence of comments.
3. Check whether the journal has issued a correction/retraction (often linked in the thread).
4. Pivot: an author's PubPeer profile lists their commented-on papers and affiliation (`employer-org`); follow the DOIs to primary sources and the author's institutional page (`social-profile`).

## Inputs → Outputs
- **In:** author `name`, DOI/title (`document-id`).
- **Out:** critique threads, flags, correction/retraction links, author affiliation and profile leads.
- **Empty/negative result looks like:** no comments — most papers are never discussed on PubPeer, so absence is NOT a clean bill of health, just no flagged critique.

## Gotchas & OpSec
- Comments are crowd-sourced and often anonymous: some are decisive, some are wrong or malicious. Weigh the evidence presented, not the flag alone.
- No comments ≠ credible; presence of comments ≠ fraud. It's a lead, corroborate with the journal's official notices.
- If you install the browser extension, it phones DOIs of pages you view to PubPeer — prefer the site for a sensitive investigation.

## Overlaps ("do both")
- Pair with Retraction Watch and the journal/publisher's own correction notices, and with academic databases (Google Scholar/ORCID) to build a full picture of an author's record.

## Trust & verifiability
`trust: community` — a respected non-profit platform, but the content is user-contributed critique. Treat threads as leads backed by inspectable evidence; confirm any correction/retraction against the publisher's official record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pubpeer |
| category | search-engines |
| selectorsIn → selectorsOut | name, document-id → social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
