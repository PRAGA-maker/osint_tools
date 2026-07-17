---
id: copyscape-plagiarism-checker
name: Copyscape
description: Use when you have a block of text (a bio, listing, message, or `domain` page) and want to find where else it appears online — returns matching pages / `social-profile`/`domain` leads.
url: https://www.copyscape.com/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Tracing where a specific passage of text has been copied or republished across the web — catching duplicated bios, recycled scam text, or the same listing under different names.
selectorsIn:
- domain
selectorsOut:
- domain
- social-profile
status: live
pricing: freemium
costNote: Free basic search by URL (finds copies of a page); pasting large custom text or batch checks uses the paid Premium tier.
opsec: passive
opsecNote: Submitted text/URLs are sent to Copyscape's servers for comparison — passive toward any subject, but don't paste truly sensitive case text into a third-party service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established commercial plagiarism/duplicate-content service; matches are real web hits, though its index and free-tier limits shape what you find.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Copyscape
- copyscape.com
tags: []
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Copyscape

> A duplicate-content finder that locates every place a passage of text has been copied online — a lateral OSINT trick for linking profiles, listings, and scams that reuse the same words.

## When to use
You have a distinctive block of text — a dating/social bio, a rental or job listing, a company "About" paragraph, a scam email, a review — and want to find every other page carrying the same words. Fraudsters and sock-puppet operators reuse copy across many personas and sites; matching that text links otherwise-separate profiles, exposes a template, or reveals the original source. Also confirms whether a subject's "original" content was lifted from elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.copyscape.com/.
2. Free path: paste the URL of a page whose text you want to trace — Copyscape returns other pages containing matching text.
3. For arbitrary pasted text (not on a public URL), use Copyscape Premium (paid) or fall back to exact-phrase quotes in Google/Bing (`"unusual sentence from the bio"`).
4. Read the match list — each result is a page reusing the text; note the domains and any names/handles on them.
5. Pivot: a matched `domain`/`social-profile` is a linked persona or the source — feed it into domain/profile search and compare identities.

## Inputs → Outputs
- **In:** a `domain`/URL (free) or a text passage (premium)
- **Out:** `domain`/`social-profile` pages containing the same text, with match indicators.
- **Empty/negative result looks like:** no matches — the text is unique/original, too short, or behind logins Copyscape can't index; try shorter distinctive phrases in a general search engine.

## Gotchas & OpSec
- The free tier searches by URL; tracing pasted (non-URL) text needs Premium — a quoted exact-phrase search in Google/Bing is a free substitute.
- Very short or generic text yields noise; pick an unusual full sentence.
- OpSec: text is sent to a third party — don't submit sensitive case material.

## Overlaps ("do both")
- Complements exact-phrase search-engine queries and reverse-image tools — text reuse links personas the way a reused avatar does; run a phrase search and an image search together to catch both.

## Trust & verifiability
`trust: community` — a commercial service returning genuine web matches; confirm each match by opening the page, and remember free-tier/index limits mean absence isn't proof of uniqueness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | copyscape-plagiarism-checker |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
