---
id: cewl
name: CeWL
description: Use when you have a `domain` and want a target-specific wordlist (and any emails) built from its site content — returns a custom wordlist plus scraped `email`s and metadata.
url: https://github.com/digininja/CeWL
category: ai-analysis-automation
path:
- ai-analysis-automation
- wordlist
bestFor: Spidering a website to generate a bespoke wordlist for password-guessing and to harvest emails/metadata.
selectorsIn:
- domain
selectorsOut:
- password
- email
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (Ruby); ships with Kali.
opsec: active
opsecNote: CeWL actively crawls the target site from your machine, generating traffic in the target's logs. Route through a proxy/VPN and mind the crawl depth so you don't hammer the site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known tool by Robin Wood (digininja), a standard in the Kali toolset. It reports words/emails/metadata it finds; relevance of the wordlist depends on the site.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- sitediff
aliases:
- Custom Word List generator
tags:
- wordlist
- web-recon
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# CeWL

> A Custom Word List generator — spider a target's website and turn its own vocabulary into a bespoke password wordlist, while also scraping emails and document metadata along the way.

## When to use
You have a `domain` and want two things: (1) a wordlist tuned to that target's own language (names, jargon, product terms) for authorised password-guessing, and (2) the `email`s and author `metadata-exif` CeWL harvests while crawling. The metadata/email harvest is the more OSINT-relevant output — document authors and contact addresses tied to a site. Infrastructure/pentest tool; low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: cli)
1. Install (or use Kali): `gem install cewl` or `apt install cewl`.
2. Basic crawl: `cewl -d 2 -m 5 -w words.txt https://example.com` (depth 2, min word length 5).
3. Harvest emails: add `-e` (writes found `email`s); metadata: add `-a`/`--meta` (author/creator from docs).
4. Route via a proxy for OpSec: `--proxy_host`/`--proxy_port`.
5. Pivot: emails → email-OSINT; document author names → `name` searches; the wordlist → authorised credential testing.

## Inputs → Outputs
- **In:** `domain`/site URL (+ depth/length options)
- **Out:** a custom wordlist (`password` candidates), scraped `email`s, and document `metadata-exif` (authors/creators)
- **Empty/negative result looks like:** a thin wordlist and no emails/metadata for a small, JS-heavy, or login-walled site — CeWL only sees server-rendered content it can crawl. Increase depth or seed specific pages.

## Gotchas & OpSec
- Human-in-the-loop: none, but deep crawls are slow and noisy.
- OpSec: **active** — the crawl hits the target from your IP and appears in their logs. Proxy/VPN it and keep depth modest.
- Only crawl and only build wordlists for targets you're authorised to test.

## Overlaps ("do both")
- Pairs with `[[sitediff]]` for tracking site changes; combine CeWL's email/metadata harvest with dedicated email-OSINT tools to enrich the contacts it finds.

## Trust & verifiability
`trust: community` — a standard, well-maintained open-source tool; the emails and metadata it reports come straight from the crawled pages, so verify them at source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cewl |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → password, email, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
