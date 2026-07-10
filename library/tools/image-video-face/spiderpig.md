---
id: spiderpig
name: SpiderPig
description: Use when you have a target `domain`/website and want to spider it, download its documents and extract embedded metadata — returns metadata-exif, geolocation (photo GPS), email and creator names.
url: https://github.com/hatlord/spiderpig
category: image-video-face
path:
- image-video-face
bestFor: Spidering a website, harvesting its documents/images, and mining them for author names, software, GPS geotags, emails and other leaked metadata.
selectorsIn:
- domain
selectorsOut:
- metadata-exif
- geolocation
- email
- name
status: live
pricing: free
costNote: Free and open-source (Ruby) on GitHub; no cost. You run it locally.
opsec: active
opsecNote: SpiderPig actively crawls the target website and downloads its files, so your IP hits the target's server (and optional subdomain brute-forcing generates noticeable DNS/HTTP traffic). This is active reconnaissance — use a VPN/proxy and only run it against domains you are authorised to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source pentest utility by "hatlord" on GitHub; source is inspectable, but the project shows no recent releases, so expect to fix dependencies on a modern Ruby.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- SpiderPig
- hatlord/spiderpig
tags:
- metadata
- document-harvester
- exif
- cli
- open-source
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# SpiderPig

> A document-and-metadata harvester (Ruby CLI) — point it at a website and it spiders the site, pulls down the documents and images, and extracts the author names, software, GPS geotags and emails hiding in their metadata.

## When to use
You have a target `domain` (a person's or organisation's website) and want the intelligence that leaks through *file metadata*: Office/PDF author and "last modified by" names, the software/versions used, EXIF GPS coordinates baked into photos, and emails/IPs/keywords scraped from document text. This is not a reverse-image or face tool despite its category — it's a FOCA/metagoofil-style harvester for finding real names, locations and infrastructure behind a website.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo (`git clone https://github.com/hatlord/spiderpig`) and install the Ruby dependencies.
2. Spider a site: `./spiderpig -u http://targetsite.com` — it crawls, downloads documents/images, and extracts metadata.
3. Optionally brute-force subdomains first: `./spiderpig -d targetsite.com`.
4. Use "dirt mode" to pull emails, IPs and keywords from harvested files; review EXIF GPS geotags mapped from images.
5. Extract: author/creator `name`s, `email`s, photo `geolocation` (GPS EXIF), and software fingerprints (`metadata-exif`).
6. Pivot: creator names and emails feed people/email OSINT; GPS geotags feed mapping; software/versions feed further recon.

## Inputs → Outputs
- **In:** target `domain`/URL
- **Out:** `metadata-exif` (document + image metadata: authors, software, EXIF), `geolocation` (photo GPS), `email`, `name` (document creators)
- **Empty/negative result looks like:** the site hosts few downloadable files, or documents were scrubbed of metadata — a clean/empty harvest means low metadata hygiene payoff, not that the site is inaccessible.

## Gotchas & OpSec
- **Not a reverse-image tool** — it mines metadata from files it downloads; don't reach for it to identify a face.
- Unmaintained: expect to patch Ruby/gem compatibility to run it today.
- **Active recon:** crawling and subdomain brute-forcing are noisy and touch the target's infrastructure — authorise first and route through a VPN/proxy.

## Overlaps ("do both")
- Pairs with metagoofil/FOCA-style harvesters and standalone EXIF tools (ExifTool) — SpiderPig automates the crawl-and-extract; ExifTool digs deeper into a single interesting file it finds.

## Trust & verifiability
`trust: community` — open-source and inspectable, but dated; verify extracted names/geotags directly (open the file in ExifTool) since a harvester can misattribute metadata.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spiderpig |
| category | image-video-face |
| selectorsIn → selectorsOut | domain → metadata-exif, geolocation, email, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
