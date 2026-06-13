# Taxonomy & Controlled Vocabulary

This file is the single source of truth for the enums used across both trees. Schemas reference these lists; harvest agents MUST use these exact values. When a value is genuinely missing, add it here first (and note it in `ledger/go-beyond.md`), then use it.

## Selectors (the pivot vocabulary)

A *selector* is an entity you can start from or pivot to. Tools declare `selectorsIn` / `selectorsOut`; strategies declare `pivotFrom` / `pivotTo`. Shared vocabulary = the two trees form one graph.

| selector | meaning |
|---|---|
| `name` | real legal / given name |
| `username` | handle / screen name reused across sites |
| `email` | email address |
| `phone` | phone number |
| `image` | a photo (not yet face-isolated) |
| `face` | an isolated face for face search |
| `geolocation` | coordinates / a place |
| `address` | postal / street address |
| `ip-address` | IPv4 / IPv6 |
| `mac-address` | hardware MAC |
| `domain` | domain / website |
| `social-profile` | a specific profile URL on a platform |
| `vehicle-plate` | license plate |
| `vin` | vehicle identification number |
| `employer-org` | employer, school, or organization |
| `associate` | a connected person (family, friend, follower) |
| `dob` | date of birth / age |
| `physical-description` | height, tattoos, clothing, distinguishing marks |
| `document-id` | passport / license / case number |
| `crypto-wallet` | blockchain address |
| `device-id` | IMEI / advertising ID / device fingerprint |
| `metadata-exif` | embedded file metadata |

## Trust rubric (`trust`)

Quick verifiability gauge — set it fast, note why in `trustNote`.

| value | assign when |
|---|---|
| `trusted` | official body, well-known vendor, or long-standing widely-cited project (e.g., NamUs, Bellingcat tools, IntelligenceX, Sherlock) |
| `community` | popular open-source repo / community-maintained list with many contributors or stars |
| `personal` | one-person hobby project, personal start.me, or solo dev tool — useful but unaudited |
| `unverified` | found but not yet assessed; default for fresh harvest |
| `untrustworthy` | known to be misleading, a honeypot, malware-adjacent, or a scraper that exfiltrates your query — flag loudly in `trustNote` and set low MP-relevance |

## Missing-persons relevance (`missingPersonsRelevance`)

| value | meaning |
|---|---|
| `high` | directly advances a MP case (people search, social, face/image, geo, phone, MP databases) |
| `medium` | situationally useful (public records, archives, translation, vehicle) |
| `low` | rarely relevant to MP (malware analysis, exploit DBs, infra recon) — kept for completeness, deprioritized |

## Best interaction pattern (`bestInteractionPattern`)

How a Claude agent should actually operate the tool. One primary value.

`cli` · `chrome-mcp` (drive via browser automation) · `web-manual` (human opens it) · `api` · `python-lib` · `desktop-app` · `docker` · `mobile-app` · `browser-extension`

## Human-in-the-loop reasons (`humanInLoopReason[]`)

`captcha` · `account-login` · `manual-review` (results need human judgment) · `api-key` · `payment-wall-partial` (free tier behind a wall) · `rate-limit` · `legal-gate` (jurisdictional access). Empty when `humanInLoop: false`.

## Phases (`phase`)

`intake` (define the case, collect the seed selectors) · `triage` (assess what's workable, prioritize) · `pivot` (selector → selector expansion) · `enrichment` (deepen a confirmed lead) · `verification` (corroborate / disprove) · `reporting` (package findings) · `opsec` (cross-cutting, protect the investigation and subject).

## Strategy types (`type`)

`pattern` (a reusable good move) · `antipattern` (a tempting bad move + why it fails) · `technique` (a concrete how-to) · `playbook` (an ordered sequence for a situation) · `case-study` (a real solved case + what worked).

## Coverage (`coverage[]`)

`global` · `us` · `eu` · `uk` · `na` · `latam` · `apac` · `africa` · or an ISO country code (`us-ca` for state). Reflects where the tool's data is actually useful.

## Tool tree — top-level categories (MP-first ordering)

The skeleton mirrors and extends the OSINT-Framework, reordered and reweighted for missing-persons work, with MP-specific branches the infosec-oriented original lacks (marked ✚).

1. `people-search` — people-search engines, registries, relatives, obituaries
2. `username` — cross-platform handle enumeration + per-site checkers
3. `email` — search, verification, breach/leak lookup, format inference
4. `phone` — number lookup, carrier, messaging-app presence, voicemail
5. `social-networks` — per-platform (Instagram, TikTok, Reddit, X, Facebook, Snapchat, Discord, Telegram, LinkedIn, Bluesky, Threads, gaming) ✚ deepened
6. `image-video-face` — reverse image, **face search** ✚, EXIF/metadata, video/frame, deepfake detection
7. `geolocation` — geolocation, **chronolocation** ✚, maps/satellite/street-view, coordinate tools
8. `public-records` — court, property, voter, vital (birth/death), licenses
9. `transportation` — vehicle/plate/VIN, flights, marine, rail
10. `communities-forums` — Reddit, niche forums, Discord directories, paste sites
11. `messaging` — Telegram, WhatsApp, Signal, Discord, regional (LINE/WeChat)
12. `dating-classifieds` — dating profiles, marketplaces, escort/adult (trafficking relevance)
13. `archives-cache` — Wayback, cached pages, deleted-content recovery, datasets
14. `documents-metadata` — document search, metadata extraction, file analysis
15. `translation-language` — translation, transliteration, slang/leetspeak
16. `maps-geospatial-data` — gazetteers, OSM, imagery providers (distinct from #7 tools)
17. `dark-web` — directories, search, monitoring (trafficking relevance)
18. `financial-crypto` — wallet tracing, chain analysis, sanctions (trafficking money flows)
19. `domains-ip-infrastructure` — whois, DNS, IP, certs (low MP, kept)
20. `ai-analysis-automation` — OSINT automation frameworks, graph/link analysis, AI assistants
21. `opsec-investigator-tooling` — sock puppets, anonymous browsing, VM/persona, cleanup
22. `evidence-capture` — screen/page capture, chain-of-custody documentation
23. `training-ctf` — practice ranges, CTF, learning resources

> Note: there is **no** `missing-persons-databases` category. In a Trace Labs-style CTF the subject is *given*, so registries like NamUs/NCMEC are case-sources, not investigative pivot tools. If a registry is genuinely useful as a lookup (e.g. matching an unidentified person), file it under `public-records` or `people-search`.

## Strategy tree — top-level structure (pivot graph + phases)

```
strategies/
  00-phases/        intake · triage · pivot · enrichment · verification · reporting · opsec
  pivots/           <from-selector>/<to-selector>/<technique>.md   e.g. username/face/...
  patterns/         reusable good moves (cross-cutting)
  antipatterns/     tempting bad moves + why they fail
  playbooks/        ordered sequences for a situation (e.g. "runaway teen, social-first")
  case-studies/     real solved cases — what actually worked
  platforms/        per-platform technique notes (instagram, tiktok, reddit, telegram, ...)
```

A strategy can live in `pivots/` (primary) and be tagged into `patterns/`, `platforms/`, or a `phase` — folder = primary home, tags = the rest.

## Naming & structure conventions

- **id / filename:** kebab-case slug, unique within its tree. File = `<id>.md`.
- **Depth:** tools tree ≤5 folders deep; aim ~5 leaves per end node. Prefer splitting a 20-child node into sub-nodes over a flat dump.
- **Group index:** every folder has `_index.md` (a group skill) listing each child with a one-line accounting.
- **Cross-links:** use `relatedTools` / `relatedStrategies` / `toolsUsed` (ids), and `[[id]]` inline in prose.
- **Provenance:** `source` = the `sources.json` id where the entry was found, so coverage can be audited.
