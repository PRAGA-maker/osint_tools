---
id: redirectdetective
name: RedirectDetective
description: Use when you have a shortened or suspicious URL/`domain` and want to reveal its full redirect chain and final destination without visiting it yourself — returns the destination domain.
url: http://redirectdetective.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Unmasking where a short/redirecting link actually leads, step by step, before you click it.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: passive
opsecNote: RedirectDetective fetches the URL from its own servers, so the destination sees the tool's IP, not yours — a safety benefit for probing hostile links. But the service itself sees the URL you submit; don't submit links that themselves contain private tokens/session data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing third-party redirect tracer; it reports the hops it observes, but cannot always follow JavaScript/meta-refresh or cloaked redirects that behave differently per client.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- redirect-detective
aliases:
- Redirect Detective
tags:
- url-analysis
- redirects
- domain-research
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# RedirectDetective

> A redirect tracer: paste a short or suspicious link and it walks the chain of hops to reveal the true final destination — without you having to load it.

## When to use
You have a shortened link (bit.ly, t.co, tracking links) or a suspicious URL and need to know where it actually goes before clicking — the real destination `domain`, and every intermediate hop (which often exposes trackers, affiliate networks, or a cloaked landing page). Use it to safely unmask links in messages, ads, phishing, or a subject's posts, and to see the redirect infrastructure behind a campaign.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://redirectdetective.com and paste the URL.
2. Run the trace; read the ordered list of redirect hops and the final destination.
3. Note intermediate hosts — URL shorteners, ad/tracking domains, cloaking layers — as infrastructure leads.
4. Take the final `domain` into WHOIS/hosting/`[[hurricane-electric-bgp-toolkit]]` for attribution.
5. Pivot: repeat for other links in the same campaign to map shared redirect infrastructure.

## Inputs → Outputs
- **In:** a URL/`domain` (often a shortened or redirecting link)
- **Out:** the ordered redirect chain and the final destination `domain` (plus intermediate tracker/cloak hosts)
- **Empty/negative result looks like:** the tool shows a single hop / can't resolve — the link may use JavaScript/meta-refresh or client-specific cloaking it can't follow; try a sandboxed browser or urlscan-style tool.

## Gotchas & OpSec
- OpSec: it fetches server-side, shielding your IP from the destination — good for hostile links; but the tool sees your submitted URL, so avoid links embedding private tokens.
- It follows HTTP redirects best; JavaScript, meta-refresh, and client-conditional (cloaked) redirects may not be fully traced — a "clean" single hop isn't a guarantee.
- Cloakers can serve different destinations by geo/user-agent; corroborate with a tool that lets you vary those.

## Overlaps ("do both")
- Do both with urlscan/sandbox tools and `[[hurricane-electric-bgp-toolkit]]` — RedirectDetective reveals the hop chain, a sandbox renders JS-based redirects, and infrastructure tools attribute the final host.

## Trust & verifiability
`trust: community` — a third-party tracer; reliable for standard HTTP redirect chains, but verify with a second method when cloaking or JavaScript redirection is suspected.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | redirectdetective |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
