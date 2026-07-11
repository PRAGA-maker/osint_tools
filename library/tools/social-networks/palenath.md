---
id: palenath
name: Palenath (megadose toolset)
description: Use when you have an `email`, `phone` or `username` and want to enumerate which sites and social accounts it is registered on — returns social profiles, names, phones and emails via megadose's open-source tools.
url: https://github.com/megadose
category: social-networks
path:
- social-networks
bestFor: One selector (email/phone/username) fanned out across dozens of sites to find where the subject holds accounts, plus scraping public Instagram/LinkedIn data.
selectorsIn:
- email
- phone
- username
selectorsOut:
- social-profile
- name
- email
- phone
status: live
pricing: free
costNote: Free and fully open-source (GPL); you run the Python tools yourself, no account or key for the core account-enumeration functions.
opsec: active
opsecNote: Holehe/Ignorant trigger real password-reset or registration-check requests against each target site, so the LOOKUP touches those platforms with the subject's address/number — some may log or rate-limit it. Run from a VPN/throwaway IP; never point it at your own infrastructure. Toutatis needs an Instagram session cookie — use a sock-puppet account, never a real one.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: python-lib
trust: community
trustNote: Widely used, well-starred tools by researcher "megadose" (Palenath); open-source and auditable, but community-maintained and dependent on target-site behaviour that changes often.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- megadose
- Holehe
- Toutatis
- Ignorant
tags:
- instagram
- Instagram Related Sites
- account-enumeration
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Palenath (megadose toolset)

> The GitHub home of "Palenath"/megadose — a suite of account-enumeration and social-scraping tools (Holehe, Ignorant, Toutatis, Nqntnqnqmb) that turn one selector into a map of where a subject is registered.

## When to use
You have a single strong selector — an `email`, a `phone` number, or an Instagram `username` — and want to know which platforms it belongs to. Holehe checks an email against 120+ sites via their forgotten-password endpoints; Ignorant does the same for phone numbers (Snapchat, Instagram, Amazon); Toutatis pulls public data (obfuscated email/phone, IDs) from an Instagram account; Nqntnqnqmb scrapes LinkedIn profiles/companies. Reach for this when you need to expand a lone identifier into a footprint.

## How to use it (`bestInteractionPattern`: python-lib)
1. Open https://github.com/megadose and pick the tool matching your selector: `holehe` (email), `ignorant` (phone), `toutatis` (Instagram username), `nqntnqnqmb` (LinkedIn).
2. Install it, e.g. `pip3 install holehe`, then run `holehe target@example.com`.
3. For email/phone: read the table of sites, each flagged as account-exists / not-found / rate-limited.
4. For Toutatis: supply a valid Instagram session cookie plus the target username to retrieve public profile metadata (obfuscated email/phone, account id, linked info).
5. Pivot: a confirmed account on a new platform becomes a fresh `social-profile` to enrich; a leaked partial phone/email feeds `[[account-live-com]]`-style existence checks or phone OSINT.

## Inputs → Outputs
- **In:** `email` / `phone` / `username`
- **Out:** `social-profile` (sites where the selector is registered), plus `name`, partial `email`, partial `phone` from Instagram scraping
- **Empty/negative result looks like:** every site returns "not found" (selector genuinely unused, or the tool's checks are stale/blocked), or rows show "rate limited" — meaning inconclusive, not negative.

## Gotchas & OpSec
- Human-in-the-loop: target sites impose rate limits and CAPTCHAs; large runs need pacing or throwaway IPs.
- Maintenance drift: these tools break when a target site changes its reset flow — check the repo's issues/last-commit before trusting a clean "not found".
- OpSec: **active** — Holehe/Ignorant send real reset/registration probes carrying the subject's address/number. Toutatis' cookie must come from a sock-puppet Instagram account.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` — Holehe covers many sites; account.live.com is the authoritative Microsoft check the enumeration may miss.
- Pairs with `[[sherlock]]`-style username hunters — megadose keys off email/phone, username hunters key off the handle, so together they cover more of the footprint.

## Trust & verifiability
`trust: community` — open-source, auditable, and heavily used in the OSINT community, but results depend on each target site's current behaviour, so treat a single clean run as a lead, not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | palenath |
