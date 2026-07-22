---
id: where-does-this-link-go
name: Where Does This Link Go?
description: Use when you have a shortened or suspicious URL (`domain`) and want to see the full redirect chain and final destination without clicking it — returns hops and the final `domain`.
url: https://wheregoes.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- url-expanders
bestFor: Expanding a short link and tracing every redirect hop to its final landing page from the safety of a server.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free web tool; an optional newsletter/account is teased for future extras (API, history) but the core tracer needs nothing.
opsec: passive
opsecNote: WhereGoes fetches the URL from its own servers, so your IP never touches the target link — this is the safe way to expand a link a subject sent without tipping them off or landing on malware.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent redirect-checker; results are directly verifiable (the hops it lists are reproducible), so trust rests on the observable chain rather than the operator.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- WhereGoes
- wheregoes.com
tags:
- url-expander
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Where Does This Link Go?

> A server-side redirect tracer: paste a short or sketchy link and see every hop and the real destination without your browser ever loading it.

## When to use
You have a shortened link (bit.ly, t.co, a tracking redirect) or a suspicious URL a subject shared, and you need to know where it actually leads before touching it. Expanding it here reveals the final `domain` (and often intermediate tracking domains) so you can decide whether it is a social profile, a phishing page, or a benign redirect.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wheregoes.com/.
2. Paste the URL into the tracer box and submit.
3. Read the ordered list of hops — each row shows the redirect method (301/302, meta-refresh, JavaScript) and the URL it forwards to.
4. Note the final destination row: that is where a real click would land.
5. Pivot: take the final `domain` into a domain/WHOIS or reputation lookup; note any tracking-parameter or affiliate domains in the chain as leads.

## Inputs → Outputs
- **In:** a `domain`/URL (typically a shortener or redirect)
- **Out:** ordered redirect hops, HTTP response codes, and the final `domain` (sometimes resolving `ip-address`)
- **Empty/negative result looks like:** a direct link with no redirects returns a single hop equal to the input — that means the URL is already its own destination, not that the tool failed.

## Gotchas & OpSec
- Some links cloak based on user-agent or geo, so a server-side trace may differ from what a real browser in the target's region would see.
- No login or CAPTCHA for normal use.
- OpSec: passive and safe — the fetch happens on WhereGoes' infrastructure, keeping your IP and browser out of contact with the target link.

## Overlaps ("do both")
- Complements any WHOIS/hosting lookup: this tool tells you *where* a link ends up; a WHOIS tool then tells you *who* owns that final domain.

## Trust & verifiability
`trust: community` — an independent tool, but its output is self-verifying: the redirect chain it reports is reproducible by anyone, so you are trusting observable HTTP behaviour, not the operator's word.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | where-does-this-link-go |
