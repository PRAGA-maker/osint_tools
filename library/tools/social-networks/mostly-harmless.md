---
id: mostly-harmless
name: Mostly Harmless
description: Use when you have a URL/`domain` or image and want to find where it's been posted on Reddit and who submitted it — a browser extension returning social-profile (Reddit) leads.
url: http://kerrick.github.io/Mostly-Harmless/#features
category: social-networks
path:
- social-networks
bestFor: While browsing any page, instantly seeing every Reddit thread that submitted that URL and jumping to the submitters and discussions.
selectorsIn:
- domain
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free and open-source (MIT) browser extension; no account or payment.
opsec: passive
opsecNote: The extension queries Reddit's public API about the URL you're viewing — it does not contact any Reddit user, so it's passive. Be aware it sends the URLs you browse to Reddit's API; use its domain-exclusion settings to avoid leaking sensitive/private URLs, and don't run it while browsing case material you want kept off Reddit's servers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Long-standing open-source extension (Kerrick Long, since 2011); reliable in concept, but old — it may lag behind Reddit API/Manifest V3 changes, so verify it still functions in your current browser.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Mostly Harmless
- Mostly Harmless Reddit extension
tags:
- reddit
- browser-extension
- link-discovery
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Mostly Harmless

> A browser extension that, on any page, tells you whether that URL has been posted to Reddit and links you straight to the threads and the accounts that submitted it.

## When to use
You're looking at a webpage, image, video or article tied to your subject and want to know if it's been discussed on Reddit — and by whom. A subject who shared their own content, or content about them, often submitted it to Reddit under an account you can then investigate. Mostly Harmless surfaces every Reddit submission of the current URL, giving you Reddit `social-profile`s and discussion threads to pivot into.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store / its GitHub (verify it still installs on your current browser).
2. Browse to the page/URL of interest (an article, image, or the subject's own content).
3. Click the Mostly Harmless toolbar button — it shows the Reddit submissions of that exact URL, with subreddits, scores and submitters.
4. Open the threads; note the submitting accounts (`social-profile`) and comment participants.
5. Pivot: a submitter's Reddit account feeds Reddit-user OSINT (post history, other subreddits); the discussion may name the subject or add context.

## Inputs → Outputs
- **In:** the URL/`domain` of the page you're viewing (article, image, etc.)
- **Out:** `social-profile` (Reddit submitters/threads where the URL appears)
- **Empty/negative result looks like:** "not posted to Reddit" — meaning that exact URL wasn't submitted (a slightly different URL/CDN link may have been), NOT that the topic is absent from Reddit.

## Gotchas & OpSec
- **Aging tool:** built in 2011; confirm it still works with current Reddit API and browser extension rules, and have a manual fallback (search `site:reddit.com <url>`).
- Matches exact URLs — reposts under different links won't all show; try canonical and CDN variants.
- It sends browsed URLs to Reddit's API — exclude sensitive domains in settings.

## Overlaps ("do both")
- Pairs with Reddit user-analysis tools and a manual `site:reddit.com` search — the extension finds the submissions passively while you browse; Reddit-user tools then profile whoever posted.

## Trust & verifiability
`trust: community` — open-source and long-lived, but dated; verify it functions and cross-check with a manual Reddit URL search before relying on a "not found".

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mostly-harmless |
| category | social-networks |
| selectorsIn → selectorsOut | domain → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
