---
id: duke-reporters-lab
name: Duke Reporters' Lab Fact-Checking Database
description: Use when you have a claim, story or region and want a vetted fact-checking outlet to consult — returns a searchable global map/list of active fact-checking organizations by country.
url: https://reporterslab.org/
category: image-video-face
path:
- image-video-face
- fact-checking-tools
bestFor: Finding a reputable fact-checking organization in a given country to verify a claim or media item.
selectorsIn:
- name
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free academic resource from Duke University's Sanford School; no account or payment.
opsec: passive
opsecNote: Browsing the fact-checker directory is passive and anonymous; you are reading a public database of organizations, not querying anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the Duke Reporters' Lab, a journalism research center at Duke University; its fact-checking census is a widely-cited authoritative directory.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fact-checking
aliases:
- Reporters' Lab
- Duke fact-checking database
- Duke Reporters Lab
tags:
- fact-checking
- verification
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Duke Reporters' Lab Fact-Checking Database

> A Duke University-maintained global census of fact-checking organizations, browsable as a map or list — the canonical place to find a credible fact-checker in any country.

## When to use
You are verifying a claim, a viral story, or a piece of media and want a reputable, independent fact-checking outlet — ideally one operating in the relevant country or language — to see whether it has already been debunked or covered. The Reporters' Lab database catalogs active (and defunct) fact-checkers worldwide with their country, organization name (`employer-org`) and website, so you can route a verification task to the right local source rather than guessing. It finds organizations, not individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://reporterslab.org/fact-checking/ and open the database (map view or list view).
2. Filter/browse by country or region relevant to your claim to find active fact-checking organizations.
3. Open an organization's entry for its name, country and link, then go to that outlet to search whether the specific claim has been checked.
4. Pivot: the chosen fact-checker's site may already carry a debunk of your claim; its byline authors and cited sources feed further verification and people/org research.

## Inputs → Outputs
- **In:** a claim/topic plus a target country or language (as `name`/keywords)
- **Out:** `employer-org` — matching fact-checking organizations with country and website
- **Empty/negative result looks like:** no active fact-checker listed for a country/region — coverage is thin in some areas; that means route to an international fact-checker, not that no verification is possible.

## Gotchas & OpSec
- Human-in-the-loop: none; fully public.
- This is a directory of organizations — it does not itself fact-check your claim; you still have to visit the listed outlet and search there.
- Entries include inactive/defunct outlets flagged as such; confirm an organization is still active before relying on it.

## Overlaps ("do both")
- Pairs with `[[fact-checking]]` and reverse-image/media-verification tools — the Reporters' Lab points you to the right human fact-checkers, while image/video verification tools let you check the media yourself; use both on a suspect item.

## Trust & verifiability
`trust: trusted` — it is maintained by Duke University's Reporters' Lab and its annual fact-checking census is widely cited; the directory itself is authoritative, though each listed outlet's individual reporting should still be judged on its merits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | duke-reporters-lab |
| category | image-video-face |
| selectorsIn → selectorsOut | name → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
