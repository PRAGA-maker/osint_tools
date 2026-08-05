---
id: printwhatyoulike
name: PrintWhatYouLike
description: Use when you want to keep or print only selected parts of a web page — strip and edit a page to the content you care about, then save it as a clean PDF/print.
url: https://www.printwhatyoulike.com
category: documents-metadata
path:
- documents-metadata
bestFor: Trimming a web page to just the relevant content and saving/printing it cleanly for records.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: passive
opsecNote: It loads the page in your own browser and lets you edit what to keep, so the target site sees your normal visit and the trimming happens client-side. Sock-puppet the browser if the visit must be non-attributable; for evidentiary use, also record the original URL and a hash.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running web utility; because you hand-edit what to keep, the output is a curated excerpt — note that when preserving it as a record.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- pagezipper
aliases:
- printwhatyoulike.com
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- print
- readability
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# PrintWhatYouLike

> A page-trimming tool: load any URL and interactively remove the clutter — ads, sidebars, navigation — keeping only the content you want, then save or print it as a clean document.

## When to use
You want a tidy record of a web page's *relevant* portion — an article, a listing, a profile section — without the surrounding noise, and you want control over exactly what is kept. PrintWhatYouLike lets you delete elements, resize, and remove images/backgrounds before saving to PDF/print. It curates a page; it returns no subject lookup data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.printwhatyoulike.com and enter the target page URL (or use its bookmarklet).
2. The page loads in an editable view; click to remove unwanted blocks (ads, menus), hide images/backgrounds, and adjust widths/fonts.
3. Save as PDF or print the trimmed result.
4. For records, note the original URL, date, and a hash alongside the saved file.
5. Pivot: file the excerpt with case notes; pair with a full capture if you also need the untrimmed original.

## Inputs → Outputs
- **In:** a web page URL (you then choose what to keep)
- **Out:** a cleaned, user-edited PDF/print of the selected content
- **Empty/negative result looks like:** JS-heavy or login-gated pages that won't load or edit cleanly — fall back to a full-page screenshot tool for those.

## Gotchas & OpSec
- Human-in-the-loop: yes in spirit — you manually choose what to keep, which is the point but also means the output is a **curated excerpt**, not the whole page.
- OpSec: passive — trimming is client-side; the site sees a normal visit. Sock-puppet the browser for sensitive URLs.
- Because it produces an edited version, always keep the original URL (and ideally a full capture) so the excerpt can't be mistaken for the complete page.

## Overlaps ("do both")
- Pairs with [[fireshot]] (full-page capture) and [[textise-net]] (plain text) — FireShot preserves the whole page, Textise gives raw text, PrintWhatYouLike gives a clean curated excerpt; choose by whether you need the whole, the words, or the relevant part.

## Trust & verifiability
`trust: unverified` — a durable convenience utility. Its output is a user-edited excerpt, so for evidence keep the source URL plus an unedited capture; use PrintWhatYouLike for readable, shareable records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | printwhatyoulike |
| category | documents-metadata |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
