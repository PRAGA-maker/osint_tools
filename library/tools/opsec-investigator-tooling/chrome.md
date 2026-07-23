---
id: chrome
name: Chrome
description: Use when you need a hardened, disposable browsing environment for OSINT — Chrome profiles, incognito, DevTools, and extensions form the base platform for sock-puppet research (no subject selectors in or out).
url: https://www.google.com/chrome
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Running compartmentalised sock-puppet browser profiles with DevTools and OSINT extensions as the foundation for online investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free download for all major desktop and mobile platforms; no account required (though signing into a Google profile syncs data — usually undesirable for OSINT).
opsec: active
opsecNote: The browser is your primary attack surface and leak point. A default Chrome signed into your real Google account will tie every search and site visit to your identity and sync history to Google. For investigation use isolated, un-synced profiles (ideally per-case), avoid signing into personal accounts, and remember DevTools/Network tab still originate from your real IP unless you add a VPN/proxy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: First-party Google browser — reliable as software, but its default posture is telemetry-heavy and identity-linked, so trust the tool while distrusting its defaults for OSINT.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- chrome-web-store
aliases:
- Google Chrome
- Chromium
tags:
- browsers
- sock-puppet
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Chrome

> The base browser most OSINT tooling assumes — valuable here as a *platform*: compartmentalised profiles, DevTools, and the extension ecosystem that turn a browser into an investigation workbench.

## When to use
Not a lookup source — it yields no selectors. Reach for Chrome when you need the *environment* to do OSINT safely: a clean, disposable sock-puppet profile separated from your real identity, DevTools for inspecting page source / network requests / hidden metadata, and installed extensions (reverse-image, archiving, EXIF, user-agent switching) that do the actual finding. It is also the runtime for browser-automation approaches like `chrome-mcp`.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Chrome, then create a **dedicated profile per investigation** (People → Add) — do **not** sign it into any personal Google account.
2. Harden the profile: block third-party cookies where possible, disable sync, and pair it with a VPN/proxy so the exit IP isn't your own.
3. Install OSINT extensions from [[chrome-web-store]] (reverse-image search, Wayback/archive savers, EXIF viewers, user-agent spoofers) scoped to that profile only.
4. Use **DevTools** (F12): Elements to read raw HTML/hidden text, Network to capture the real resource URLs and API calls a page makes, Application to inspect cookies/local storage.
5. Tear down or reset the profile between cases so cookies and history don't cross-contaminate identities.

## Inputs → Outputs
- **In:** none (platform/tooling — you bring the investigation to it)
- **Out:** none as subject selectors — provides the environment other tools run in
- **Empty/negative result looks like:** N/A; failure is an *identity leak* (wrong profile, synced account, real IP) rather than an empty query.

## Gotchas & OpSec
- **Default Chrome is not OSINT-safe:** signed into a personal account it links your activity to you and syncs history to Google. Always use isolated, un-synced profiles.
- DevTools and extensions still egress from your real IP unless you add a VPN/proxy — the browser alone does not anonymise you.
- Extensions are powerful but can themselves exfiltrate your browsing; install only trusted ones, scoped per profile.
- For higher assurance, prefer a purpose-built browser VM; Chrome profiles are compartmentalisation, not true isolation.

## Overlaps ("do both")
- Pairs with [[chrome-web-store]] — Chrome is the runtime, the Web Store is where you source the extensions that give it OSINT capabilities. Use both together; neither is useful for investigation alone.

## Trust & verifiability
`trust: trusted` — mainstream, well-maintained first-party software; the reliability caveat is behavioural, not technical: its identity-linked, telemetry-rich defaults must be reconfigured before it's safe for investigative use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chrome |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
