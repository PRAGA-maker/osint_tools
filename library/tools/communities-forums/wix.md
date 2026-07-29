---
id: wix
name: Wix (username site check)
description: Use when you have a `username` and want to check whether it owns a Wix-hosted site — returns a `social-profile`/personal site at that handle.
url: https://wix.com
category: communities-forums
path:
- communities-forums
bestFor: Confirming whether a username maps to a Wix-hosted site and mining that site for identity details.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse any public Wix site; a Wix account is only needed to build one, not to view.
opsec: passive
opsecNote: Visiting a public `username.wixsite.com` page is an ordinary web request, but Wix pages embed heavy analytics and the site owner may see referrer/visit data — browse from sock-puppet egress and avoid contact forms, which reach the owner directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Wix is a major first-party site-builder; the platform is real and reliable, but "presence of a site at a handle" is only a lead — handles are not reserved uniquely to one person.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- wixsite
- wix.com
tags:
- forums
- username-presence
source: metaosint
lastVerified: '2026-07-29'
enrichment: full
---

# Wix (username site check)

> A username-enumeration angle on the Wix site-builder: does `username.wixsite.com` exist, and what does that personal site reveal?

## When to use
You have a `username` and are enumerating where it has a presence. Wix hosts free sites under `username.wixsite.com/<sitename>`, so a hit both confirms the handle is in use and often surfaces a personal/business page rich in identity data (real name, contact, portfolio, location). Use it as one node in a broader username sweep, not a standalone finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try `https://<username>.wixsite.com/` in a sock-puppet browser, and also run a `site:wixsite.com "<username>"` / `site:wix.com "<name>"` Google dork to catch custom-domain and sub-path variants.
2. If a site loads, read it for name, contact details, social links, portfolio, and location cues.
3. Note the custom domain if the owner attached one — that feeds WHOIS/infrastructure lookups.
4. Pivot: extracted `name`/contact feeds people-search; a linked social handle feeds profile correlation.

## Inputs → Outputs
- **In:** `username`
- **Out:** a `social-profile`/personal Wix site → name, contact, links harvested from it
- **Empty/negative result looks like:** the subdomain 404s or shows a Wix "site not found"/parked page — meaning no free Wix site at that exact handle (they may still have one under a custom domain, so try the dork).

## Gotchas & OpSec
- Handle collision: a Wix site at a handle isn't proof it's *your* subject — corroborate the content against known facts.
- Owners often move to a custom domain, detaching the `wixsite.com` subdomain — a dork across content is more reliable than guessing the subdomain.
- **Passive**, but don't submit the site's contact form (that alerts the owner).

## Overlaps ("do both")
- Pairs with multi-platform username tools (Sherlock/WhatsMyName-style) and a `site:` search via `[[googler]]` — the username tools flag the Wix hit, a content dork confirms identity and catches custom domains.

## Trust & verifiability
`trust: unverified` — the platform is legitimate, but a handle-to-site match is a lead requiring content corroboration, not identity proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wix |
