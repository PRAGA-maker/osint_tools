---
id: googler
name: Googler
description: Use when you have a `name`/`username`/`email`/`phone`/`domain` and want to run scriptable Google web/news/site searches from the terminal — returns result URLs (social-profile / domain leads).
url: https://github.com/jarun/googler
category: search-engines
path:
- search-engines
bestFor: Scripting Google dorks and bulk name/username/email searches from the command line without a browser.
selectorsIn:
- name
- username
- email
- phone
- domain
selectorsOut:
- social-profile
- domain
status: degraded
pricing: free
costNote: Free, open-source single Python file; no account or API key. Google itself is queried directly.
opsec: active
opsecNote: Queries go straight to Google from your own IP with no browser fingerprint, so heavy or dorked runs earn a CAPTCHA or temporary IP block quickly. Route through a sock-puppet VPN/Tor and pace requests; never loop large query lists from an attributable IP.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Written by Arun Prakash Jana (jarun), a well-known open-source maintainer; the repo has been archived read-only since March 2022, so it gets no fixes when Google changes its result HTML.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- ddgr
aliases:
- googler cli
- jarun/googler
tags:
- Tools for Google
- cli-search
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Googler

> Terminal front-end to Google Search — turns dorks and repeated name/username lookups into a scriptable, browser-free command.

## When to use
You have a batch of selectors (`name`, `username`, `email`, `phone`, `domain`) to push through Google and want it scripted rather than typed into a browser one at a time — e.g. iterating `site:` dorks across a list of usernames, or piping result URLs into another tool. Best when you already know Google dorking and want automation, not for a single ad-hoc lookup (a browser handles that fine).

## How to use it (`bestInteractionPattern`: cli)
1. Install via package manager (`apt`/`dnf`/`pacman install googler`) or grab the single script: `curl -o /usr/local/bin/googler https://raw.githubusercontent.com/jarun/googler/v4.3.2/googler && chmod +x /usr/local/bin/googler` (needs Python 3.6+).
2. Basic search: `googler "John Smith" Denver`. Site dork: `googler -w linkedin.com "jane doe"`. News: `googler -N <topic>`. Limit/paginate: `googler -n 15 -s 3 <query>`.
3. Read the numbered results (title + URL + snippet), or use `--json` to pipe URLs into a script.
4. Pivot: profile URLs feed username tools; a hosting `domain` feeds infrastructure lookups.

## Inputs → Outputs
- **In:** any query string built from `name` / `username` / `email` / `phone` / `domain`
- **Out:** ranked result URLs → `social-profile`, `domain` leads
- **Empty/negative result looks like:** "No results." — but also watch for a CAPTCHA / HTTP 429 page, which means Google blocked the IP, NOT that the subject has no footprint.

## Gotchas & OpSec
- Archived in 2022: when Google changes result markup, googler can silently return nothing until a community patch lands. If results dry up abruptly, verify in a browser before concluding the subject is absent.
- Rate-limit is the main human-in-the-loop: dorking loops trip Google's bot defenses. Pace requests and rotate egress IPs.
- **Active**: every query reaches Google from your IP — use sock-puppet egress for target work.

## Overlaps ("do both")
- Pairs with `[[ddgr]]` — the same author's DuckDuckGo CLI, which is less aggressively rate-limited and gives a second engine's view of the same selector.

## Trust & verifiability
`trust: community` — reputable open-source author, but unmaintained (archived), so treat breakage as expected and cross-check hits in a normal browser.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | googler |
