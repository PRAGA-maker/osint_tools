---
id: ahmia
name: Ahmia
description: Use when you have a `name`, `username`, `email` or keyword and want to find it on the dark web — returns indexed Tor onion services and pages matching your search, from the clearnet.
url: https://ahmia.fi/
category: dark-web
path:
- dark-web
- tor-search
bestFor: Searching indexed Tor onion services by keyword from a normal browser.
selectorsIn:
- username
- email
- name
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free and open-source; no account, with a public search API.
opsec: passive
opsecNote: Searching Ahmia's clearnet site queries its own index, not each onion directly, so you don't touch hidden services yet. Do the searching on ahmia.fi (or its .onion) via Tor, and NEVER open a resulting onion outside the Tor Browser. Ahmia filters CSAM but results are otherwise unvetted — expect illegal/hostile content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running project by Juha Nurmi developed with Tor Project support; open-source and the standard clearnet gateway for onion search, though it indexes only what it can crawl.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- ahmia-link-graph
- ahmia-list-of-onion-domains
aliases:
- Ahmia.fi
- Ahmia search
tags:
- dark-web
- tor
- onion-search
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Ahmia

> The standard clearnet search engine for Tor hidden services — search onion sites by keyword from an ordinary browser, then open hits safely in Tor.

## When to use
You're checking whether a subject's identifiers — a `username`, `email`, `name`, wallet, or a distinctive keyword — surface on the dark web: leak markets, forums, paste sites, or onion services. Ahmia indexes crawlable onion sites and lets you search them from the clearnet, so you can triage dark-web exposure without first knowing any onion addresses.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the Tor Browser, go to https://ahmia.fi/ (or its onion mirror).
2. Search the identifier or keyword; Ahmia returns matching onion services/pages with titles and descriptions.
3. Review the result snippets first; only open an onion link inside the Tor Browser, never in a normal browser.
4. Pivot: a hit tying a `username`/`email` to a forum or market feeds breach/leak analysis and further onion recon; use `[[ahmia-list-of-onion-domains]]` / `[[ahmia-link-graph]]` to expand from a found service.

## Inputs → Outputs
- **In:** `username`, `email`, `name`, or keyword
- **Out:** matching onion `domain`s/services and `social-profile`-style pages (forum/market presences)
- **Empty/negative result looks like:** no results — the term isn't in Ahmia's crawl; the dark web is largely uncrawlable, so absence here is weak evidence and you should try other onion indexes.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must operate through Tor and exercise extreme caution.
- **Safety/legal:** results are unvetted (Ahmia filters CSAM and, since 2023, sexual content, but not other illegal material); opening onions can expose you to malware and illegal content — use Tor Browser in a hardened/VM environment and follow your engagement's legal rules.
- Coverage is partial: Ahmia only indexes onions it can reach and that allow crawling; many services are invisible to it.

## Overlaps ("do both")
- Pairs with `[[ahmia-list-of-onion-domains]]` and other Tor search engines — different onion crawlers index different services, so run more than one; Ahmia is the reliable clearnet starting point.

## Trust & verifiability
`trust: trusted` — an open-source, Tor-Project-supported project and the de-facto onion search gateway; the index is authoritative for what it crawls, but always verify a hit by (carefully) visiting the source onion in Tor.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ahmia |
| category | dark-web |
| selectorsIn → selectorsOut | username, email, name → social-profile, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
