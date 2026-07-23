---
id: s
name: S
description: Use when you have a `name`, `username`, or `email` and want to fan the same query across 150+ search sites from your terminal — returns browser tabs of results per provider.
url: https://github.com/zquestz/s
category: search-engines
path:
- search-engines
bestFor: Firing one query at any of 150+ named search engines from the command line without opening each site by hand.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (MIT); install via Go, Homebrew (`s-search`), or AUR.
opsec: passive
opsecNote: "`s` just constructs a search URL and opens it in your default browser (or returns JSON with `-o json`), so the query hits the chosen provider from your real browser/IP unless you point it at a sock-puppet profile. It sends nothing to any zquestz server. Route it through a burner browser + VPN when the query names a live subject."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Long-standing, widely packaged open-source CLI (zquestz) under an MIT license; it only builds and opens URLs, so there is no hidden data collection to trust.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- s-search
- zquestz/s
tags:
- Search engines
- Universal search tools
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# S

> A tiny terminal launcher that turns `s -p <provider> <query>` into the right search URL and opens it — one keystroke to hit any of 150+ engines.

## When to use
You are pivoting a `name`, `username`, or `email` and want to run the identical query across many engines (Google, Bing, Reddit, GitHub, YouTube, StackOverflow, PyPI, …) without hand-typing each site. Also handy for scripting: `-o json` emits the target URL so you can feed a batch of selectors through a shell loop. Convenience tooling rather than a data source, so missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/zquestz/s@latest`, or `brew install s-search`, or `yay -S s`.
2. Default search: `s john doe missing` opens the query in your default provider.
3. Target a specific engine: `s -p reddit "jdoe123"` or `s -p github jdoe123`.
4. Use tags to hit a category: `s -t video "subject name"`; list providers with `s --list-providers`.
5. Script it: `s -o json "jdoe123"` prints the URL instead of opening a browser — pipe into other tools or a curl fetch.
6. Add custom providers by editing `~/.config/s/config` (e.g. an OSINT site not in the defaults).

## Inputs → Outputs
- **In:** `name`, `username`, or `email` (any free-text query)
- **Out:** an opened browser tab of that provider's results (or a JSON URL); surfaced `social-profile`s / mentions depend entirely on the provider
- **Empty/negative result looks like:** the provider's own "no results" page — `s` itself never reports found/not-found, it only routes the query.

## Gotchas & OpSec
- It does not aggregate or dedupe results — each `s` invocation opens one provider; loop over providers yourself.
- Because it opens your real browser, the query and referrer reach the provider from your identity unless you set a sock-puppet default browser.
- Provider list drifts as sites change their query params; a stale provider may build a broken URL — update the package.

## Overlaps ("do both")
- Complements meta/aggregating search tools: `s` is a fast keyboard launcher for known engines, while aggregators fan out and merge results server-side. Use `s` when you already know which engine you want.

## Trust & verifiability
`trust: community` — mature, MIT-licensed, packaged in Homebrew/AUR; its only behavior is URL construction, so it introduces no data-quality or exfiltration risk of its own.
