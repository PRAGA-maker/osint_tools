---
id: spy
name: Spy
description: Use when you have a `username` and want a fast presence check across ~210 sites — returns the `social-profile`s where that handle is registered.
url: https://github.com/CYB3R-G0D/SPY
category: username
path:
- username
bestFor: A lightweight Python CLI that checks a single username across ~210 social/web platforms.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open-source (GitHub); no account or API key. Requires local Python install.
opsec: active
opsecNote: The tool requests each candidate profile URL directly from your machine, so all ~210 target sites see your IP. Run it through a VPN/proxy or from a sock-puppet VPS so the sweep isn't attributed to you; consider throttling threads to avoid rate-limit flags.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community GitHub username checker in the Sherlock/WhatsMyName family; simple and unmaintained-risk, with the usual false-positive/negative caveats of presence checkers.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- SPY
- CYB3R-G0D SPY
tags:
- Nicknames
- username-enumeration
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Spy

> A quick Python CLI that checks one username against ~210 sites — a fast first pass to find where a handle is registered.

## When to use
You have a `username` and want a rapid enumeration of which of ~210 platforms have an account under that handle, as an early step before deeper per-site investigation. Best when you want something scriptable and offline-runnable rather than a web form.

## How to use it (`bestInteractionPattern`: cli)
1. Clone/download from https://github.com/CYB3R-G0D/SPY and install its Python requirements.
2. Run `python spy.py <username>` (e.g. `python spy.py alex`).
3. Options: `-l sitelist.txt` for a custom site list, `-t <n>` to set thread count, `-o out.txt` to save results, `-h` for help.
4. Read the terminal/output file for the list of sites where the handle exists.
5. Pivot: open each hit to confirm it's the same person; feed confirmed handles into `[[memory-lol-github-com]]` (for Twitter history) and reverse-image/face search on profile pics.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` URLs (per site) where the handle is registered, plus the confirmed `username`
- **Empty/negative result looks like:** all sites report "not found." Because presence checkers rely on each site's response patterns, expect both false negatives (site changed its markup) and false positives (placeholder/parked pages) — always verify each hit manually.

## Gotchas & OpSec
- Active: every checked site sees your IP; route through a proxy/VPN and throttle threads.
- Community project — its ~210-site list can rot as platforms change; results may drift over time.
- Same handle ≠ same person; confirm identity before pivoting.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-python]]`, `[[spy]]`-class tools, and Sherlock/Maigret — each ships a different site list, so run more than one to widen coverage and cross-check hits.

## Trust & verifiability
`trust: community` — an open-source checker with no authority behind its data. Treat every match as an unverified lead to confirm on the live profile.
