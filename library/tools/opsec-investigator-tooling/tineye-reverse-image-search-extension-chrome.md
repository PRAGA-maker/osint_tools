---
id: tineye-reverse-image-search-extension-chrome
name: TinEye Reverse Image Search (Chrome extension)
description: Use when you have an `image` in your browser and want to right-click it into TinEye's reverse image search in one step — returns image matches, social-profile and domain leads.
url: https://chromewebstore.google.com/detail/tineye-reverse-image-sear/haebnnbpedcbhciplfhjjkbafijpncjl
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: One-click, in-browser reverse image search on any image via TinEye's official extension.
selectorsIn:
- image
selectorsOut:
- social-profile
- domain
- name
status: live
pricing: free
costNote: Free official TinEye browser extension. Basic TinEye search is free; TinEye's paid API/bulk plans aren't needed for this.
opsec: passive
opsecNote: Right-clicking an image sends its URL to TinEye's servers — you don't contact the site hosting the image, so it's passive against your subject. The image URL and your query go to TinEye (a third party); run from a sock-puppet browser profile to keep case activity out of your personal history.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Official extension from TinEye (Idée Inc.), a reputable reverse-image-search provider. TinEye finds exact/edited copies (not visually-similar faces), so it complements rather than replaces face-search engines.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- tineye
- tineye-reverse-image-search
- google-reverse-image-search
tags:
- toddington
- reverse-image-search
- browser-extension
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# TinEye Reverse Image Search (Chrome extension)

> TinEye's official right-click extension — turns "reverse-search this image" into a single context-menu click while you browse, powered by TinEye's exact/edited-copy matching.

## When to use
You're looking at an `image` in the browser — a profile photo, a listing picture, a suspected stolen/reused image — and want to find where else it appears (to trace its origin, spot a catfish reusing a stock photo, or find the earliest posting). The extension skips the upload step: right-click → search TinEye.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the official TinEye extension from the Chrome Web Store (ideally in a sock-puppet profile).
2. Right-click any image on a page → "Search image on TinEye."
3. Review TinEye's matches, which you can sort by **oldest** (find the original) or **most changed** (find edits/derivatives).
4. Open matching pages to extract context: the `domain`/`social-profile` hosting the image, captions, and names.
5. Pivot: an oldest-match page → the image's true origin; a reused stock photo → evidence of a fake persona; a real profile → the person behind the image.

## Inputs → Outputs
- **In:** `image` (any in-browser image, via right-click)
- **Out:** pages hosting matching images → `domain`, `social-profile`, `name` leads
- **Empty/negative result looks like:** "0 results" — TinEye indexes exact/edited copies, so an unindexed or heavily-transformed image (or a genuinely novel photo) returns nothing. That is NOT proof the image is original; try Google/Yandex and face-search engines too.

## Gotchas & OpSec
- TinEye matches **copies of the same image**, not similar-looking faces — it won't find other photos of the same person. Use face-search engines for that.
- Sort by oldest to trace origin; "0 results" just means TinEye hasn't indexed a copy.
- The image URL goes to TinEye; keep case browsing in a clean profile.

## Overlaps ("do both")
- Always pair with `[[google-reverse-image-search]]` and Yandex, plus face-search engines — each indexes different sources, so run several. See `[[tineye]]` for the full web tool and API.

## Trust & verifiability
`trust: trusted` — the genuine TinEye extension from a reputable provider; matches are real hosted copies. Confirm a "match" is truly the same image (not a coincidental crop) before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tineye-reverse-image-search-extension-chrome |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | image → social-profile, domain, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
