---
id: vivaldi
name: Vivaldi
description: Use when you need a compartmentalized investigation browser — returns isolated, tab-tiled sock-puppet sessions for viewing target `social-profile`s and `domain`s.
url: https://vivaldi.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A Chromium-based browser whose profiles and tab tiling make it a tidy home for separate sock-puppet identities.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to download and use on Windows, macOS, Linux, and Android; no account required to browse.
opsec: passive
opsecNote: "Vivaldi is a browsing platform, not an anonymizer — it does not hide your IP or defeat fingerprinting on its own. Its value for OpSec is compartmentalization: use a dedicated Profile per sock-puppet, disable sync/telemetry, and pair it with a VPN/Tor. Signing into a Vivaldi account for sync leaks your identity across profiles, so keep investigative profiles account-less."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Made by Vivaldi Technologies (founded by ex-Opera staff); Chromium-based, closed-source UI over an open engine, with a long-standing pro-privacy stance and no ad/data-broker business model.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Vivaldi browser
tags:
- browsers
- sock-puppet
- opsec
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Vivaldi

> A highly configurable Chromium browser whose per-identity Profiles and split-screen tab tiling make it a practical workbench for running sock-puppet accounts side by side.

## When to use
You need a browser to conduct investigations and want clean separation between identities — one Vivaldi Profile per sock puppet, each with its own cookies, history, and logins — plus the ability to tile several target pages at once (e.g. compare two `social-profile`s or watch a live feed while taking notes). It is infrastructure for OSINT work, not a data source, so it produces no selectors and rates low for missing-persons relevance directly.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install Vivaldi from https://vivaldi.com for your OS.
2. Create a separate **Profile** for each investigation identity (User menu → add profile) so cookies/sessions never cross-contaminate.
3. In each investigative profile, skip signing into a Vivaldi account, turn off sync and telemetry, and route traffic through your VPN/Tor before logging into any sock-puppet account.
4. Use tab tiling (select tabs → Tile) to view multiple target pages simultaneously, and Web Panels to keep a reference (map, notes) docked.
5. Treat each profile as one persona; never reuse it across cases.

## Inputs → Outputs
- **In:** — (a browsing environment, not a query tool)
- **Out:** — (renders whatever sites you visit; produces no selectors itself)
- **Empty/negative result looks like:** n/a — Vivaldi is the vehicle, not the source. "Nothing found" is a property of the site you're viewing.

## Gotchas & OpSec
- It is not anonymity software: your real IP and browser fingerprint still apply unless you add a VPN/Tor and harden the profile. Do not mistake per-profile separation for anonymity.
- Signing into Vivaldi Sync links your profiles/devices — keep investigative profiles account-less.
- Chromium base means the same fingerprinting exposure as Chrome; consider anti-detect measures for high-risk work.

## Overlaps ("do both")
- Complements dedicated anonymity and anti-detect tooling — Vivaldi organizes the personas and windows, while a VPN/Tor and fingerprint hardening provide the actual concealment. Use them together, not one instead of the other.

## Trust & verifiability
`trust: trusted` — a reputable independent browser vendor with a privacy-respecting model; the caveat is scope, not integrity: it compartmentalizes identities but does not by itself make you anonymous.
