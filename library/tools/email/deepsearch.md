---
id: deepsearch
name: DeepSearch
description: Use when you want to search Tor hidden-service (.onion) content for a name, username, email, or keyword tied to a subject — returns links to dark-web pages that mention the selector.
url: http://xjypo5vzgmo7jca6b322dnqbsdnp3amd24ybx26x5nxbusccjkm4pwid.onion.pet/
category: email
path:
- email
bestFor: Keyword/selector search across Tor onion-site content.
selectorsIn:
- name
- username
- email
- domain
selectorsOut:
- social-profile
- email
- document-id
status: unknown
pricing: freemium
costNote: Onion search engines are typically free; some gate listings or require Tor for the canonical .onion.
opsec: active
opsecNote: The URL is an .onion.pet clearnet gateway to a Tor hidden service — using the clearnet gateway exposes your IP to the gateway operator. For real OpSec use the Tor Browser .onion directly, never the clearnet proxy, and never from your operational identity.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: A dark-web (Tor) search engine reached via a .onion.pet proxy; its index, operator, and uptime are unverified and onion search engines are notoriously unstable. Results may include illicit content and must be independently verified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- darkweb
- tor
- search-engine
source: osint4all
lastVerified: ''
enrichment: full
---

# DeepSearch

> A Tor hidden-service search engine (reached here via a clearnet .onion.pet gateway) for finding dark-web pages that mention your selector.

## When to use
You have a `name`, `username`, `email`, or `domain` and want to check whether it surfaces in Tor onion-site content — marketplaces, forums, paste/leak sites. Niche and last-resort: useful when a subject or associate may have a dark-web footprint, but expect noise and instability.

## How to use it (`bestInteractionPattern`: web-manual)
1. For OpSec, do **not** use the clearnet .onion.pet link — open the canonical `.onion` in Tor Browser from a non-attributable environment.
2. Enter the selector as a keyword and run the search.
3. Manually review results for relevance; onion indexes are stale and full of dead links and unrelated/illicit hits.
4. Pivot: a relevant page may yield a `social-profile`, an `email`, or a `document-id` to chase elsewhere.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, or `domain` (keyword)
- **Out:** links to onion pages mentioning the selector; possible `social-profile` / `email` / `document-id` leads
- **Empty/negative result looks like:** no results or all-dead links — common; onion search coverage is thin and decays fast.

## Gotchas & OpSec
- OpSec is the headline risk: the `.onion.pet` clearnet gateway routes your real IP through a third-party proxy that can log and tamper. Treat **active**, not passive. Use Tor Browser and the raw .onion, isolated from your real identity.
- Results may surface illegal content; review carefully and stay within legal/authorisation boundaries.
- Human-in-the-loop: manual relevance review is mandatory.

## Trust & verifiability
`trust: unverified` — operator, index quality, and uptime are unknown, and onion search engines change addresses or disappear frequently. Verify every lead against another source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deepsearch |
| category | email |
| selectorsIn → selectorsOut | name, username, email, domain → social-profile, email, document-id |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
