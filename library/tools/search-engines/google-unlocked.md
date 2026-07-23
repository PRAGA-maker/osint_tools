---
id: google-unlocked
name: Google Unlocked
description: Use when a Google search for a `name`/`domain` looks scrubbed by DMCA removals — returns the hidden/delisted result links re-injected into the page.
url: https://github.com/Ibit-to/google-unlocked
category: search-engines
path:
- search-engines
bestFor: Revealing Google results that were removed/hidden due to DMCA takedown notices.
selectorsIn:
- name
- domain
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free and open-source; but removed from the Chrome Web Store and Firefox Add-ons, so it must be side-loaded manually or run as a userscript.
opsec: passive
opsecNote: "The extension only re-parses Google's own results page you already loaded (it reads the DMCA-removal notices Google appends and pulls the delisted URLs back in), so it issues no extra queries against any target — passive. It runs your normal Google session, so standard search-OpSec applies: use a signed-out/sock-puppet browser and a VPN if the query names a live subject."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source (Ibit-to) but unmaintained (last release v1.6, Jan 2022) and delisted from official stores; it may break as Google changes its results markup, and side-loaded extensions should be reviewed before install.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Google Unlocked
- Ibit-to/google-unlocked
tags:
- Search engines
- dmca
- uncensor
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Google Unlocked

> A browser extension that reads the "results removed due to DMCA" notices on a Google page and re-injects the delisted links — surfacing pages Google hid from the visible results.

## When to use
You're searching a `name`, `domain`, or piece of content and suspect the results were scrubbed by DMCA takedown requests (common around leaked/pirated material, and sometimes used to bury information). Google appends a removal notice with a link to the Lumen database; this tool pulls the affected URLs back into view so you can see what was delisted. Niche and currently degraded, so low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Get the code from https://github.com/Ibit-to/google-unlocked and **side-load** it (it's no longer in the Chrome/Firefox stores) or use its userscript version with a userscript manager.
2. Review the source before installing — it's unmaintained and side-loaded.
3. Run a Google search in a signed-out/sock-puppet session; if results were DMCA-removed, the extension re-injects the hidden links (typically at the bottom).
4. Cross-check the recovered URLs; open via an archive if the live page is down.
5. Also consult Google's own Lumen (chillingeffects) link for the full removal record.

## Inputs → Outputs
- **In:** a Google search for a `name`/`domain`/content
- **Out:** the DMCA-hidden result URLs re-added to the page (`social-profile`s/pages that were delisted)
- **Empty/negative result looks like:** nothing extra appears — either no DMCA removals applied to that query, or (likely) Google changed its markup and the stale extension no longer parses it. Verify via the Lumen notice directly.

## Gotchas & OpSec
- **Degraded:** unmaintained since 2022 and delisted from stores; it may silently fail on current Google. Treat a null result skeptically and fall back to Lumen.
- Side-loading unmaintained extensions is a supply-chain risk — read the code, or use the userscript in an isolated profile.
- It only recovers *DMCA-removed* results, not other kinds of filtering/personalization.

## Overlaps ("do both")
- Complements Google's Lumen/chillingeffects removal records and archive tools like [[resurrect-pages]] — the extension surfaces the hidden URL, Lumen documents the takedown, and an archive recovers the page if it's since gone.

## Trust & verifiability
`trust: community` — open-source but stale and store-delisted; because it may not work on current Google, always corroborate against the first-party Lumen removal notice rather than trusting (or trusting the absence of) its output.
