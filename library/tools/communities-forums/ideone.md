---
id: ideone
name: ideone
description: Use when you have an Ideone paste/snippet URL or are dorking for shared code — returns the pasted source and its output; a code-paste host where leaks may appear.
url: https://ideone.com
category: communities-forums
path:
- communities-forums
bestFor: Reading an Ideone code snippet you've been pointed to, and treating it as a code-paste host where credentials or notes may leak.
selectorsIn:
- username
selectorsOut:
- email
- password
status: live
pricing: free
costNote: Free online compiler/paste service; no account needed to view public snippets.
opsec: passive
opsecNote: Viewing a public snippet by link is passive and anonymous; the author isn't notified. Snippets can be public or private — you only reach public ones via URL or a search-engine hit. Don't paste your own case data into it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established online compiler/paste service (Sphere Research); shared code is arbitrary user content with no verification.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- pastebin
- bpaste
- katbin
aliases:
- ideone.com
tags:
- pastebins
- code-paste
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# ideone

> An online compiler and code-paste service — OSINT-relevant because developers paste snippets here that can leak hardcoded credentials, API keys, endpoints, or personal notes.

## When to use
You're pointed to an `ideone.com` snippet, or you're sweeping paste/code sites for leaks tied to a subject. Ideone runs and shares code; public snippets are indexed and sometimes contain hardcoded secrets (passwords, API keys, DB strings, internal hostnames) or comments that reveal identity. Use it to read a referenced snippet and to include `ideone.com` in leak-hunting dorks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open a known snippet directly by URL (e.g. `https://ideone.com/<id>`).
2. To find relevant snippets, dork a search engine: `site:ideone.com "target@email.com"`, a username, or key strings like `password=`.
3. Read the source and its output for hardcoded secrets, endpoints, and identifying comments.
4. Extract selectors: emails, usernames, passwords, hostnames.
5. Pivot: leaked `email`/`password`/host → breach-check, account, and infrastructure tools; author handle → cross-platform search. Never reuse a credential.

## Inputs → Outputs
- **In:** an Ideone snippet URL/ID, or a dork term (`username`, `email`, secret string)
- **Out:** source code + output → possible `email`/`password`/host/key leaks
- **Empty/negative result looks like:** no indexed public snippets for your dork — the snippet was private or never indexed; most Ideone content isn't reachable this way, so absence means little.

## Gotchas & OpSec
- Only *public* snippets are discoverable; private ones aren't indexed — you can't browse the full corpus.
- Content is unverified and may be fabricated, stale, or bait; corroborate before acting.
- Don't paste your own investigation code/notes here; never reuse leaked credentials.

## Overlaps ("do both")
- Pairs with `[[pastebin]]`, `[[bpaste]]`, and `[[katbin]]` — run the same leak dorks across multiple paste/code hosts, since developers scatter snippets across them.

## Trust & verifiability
`trust: community` — an established but unvetted code-paste host. Any find is unverified user content; verify leaked hosts/accounts independently and treat secrets only as attribution signal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ideone |
| category | communities-forums |
| selectorsIn → selectorsOut | username → email, password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
