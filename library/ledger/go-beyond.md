# Go Beyond — Frontier Log

The point of this file: a harvest agent should never *silently* notice a new place to look. Every time you see a new direction — a GitHub topic that links sibling topics, a start.me board that links other boards, an awesome-list with many forks worth diffing, a tool category we don't have, a database referenced in a writeup — **append it here** with enough context for a human to triage it.

Format per entry: `- [STATUS] direction — why it's promising — where noticed (source id)`. STATUS ∈ {NEW, TRIAGED→sources.json, SKIP}.

## How agents must use this
- During any harvest, if you discover a source not already in `sources.json`, add it to BOTH: a `queued` row in `sources.json` (so Go Deep tracks it) and a `TRIAGED` line here (so the human sees the reasoning).
- If you spot a whole *area* (not a single source) — e.g. "facial-recognition search engines are fragmenting into many small services" — log it as `NEW` here even if you can't name a single URL yet.

## Frontier (seed observations)
- [NEW] GitHub topic pages cross-link related topics in the sidebar (e.g. `osint` ↔ `osint-tools` ↔ `social-media-analysis`) — each is a fresh source surface. — github-topic crawl
- [NEW] `awesome-osint` has dozens of forks; diffing popular forks against upstream surfaces tools the canonical list dropped. — awesome-osint
- [NEW] start.me boards almost always embed links to *other* curators' boards — treat each board as a hub, not a leaf. — start.me sources
- [NEW] Missing-persons-specific tooling (NamUs/NCMEC/Doe Network/Charley Project + international equivalents) is under-represented in infosec-origin lists; needs a dedicated harvest pass beyond the seed lists. — taxonomy gap
- [NEW] Face-search services churn fast (PimEyes-likes appear/disappear); maintain a recurring re-check rather than a one-time harvest. — taxonomy gap

## Wave 1 harvest — discovered directions (2026-06-13)
- [TRIAGED] Meta-collections are higher-yield than single tools: ultimate-osint is itself 44 curated boards -> MetaOSINT, Bellingcat Toolkit, cyb_detective, sinwindie/OSINT, IntelTechniques, UK-OSINT, Toddington all added to sources.json (queued). — ultimate-osint
- [TRIAGED] osintambition/Social-Media-OSINT-Tools-Collection (290+ tools, 16 platforms) only partially mined; HowToFind-bot/osint-tools (300+ selector-indexed) not yet mined. — gh-topic-osint-resources
- [TRIAGED] castrickclues is a (now-defunct, shut 2026-02-07) SaaS, not a directory; its real value is the open-source equivalents holehe/whatsmyname/maigret/sherlock. — castrickclues
- [TRIAGED] cupidcr4wl: purpose-built username/phone OSINT for dating/adult/escort platforms — trafficking-case relevant; added (queued). — osinti4l-user
- [NEW] GitHub /topics/ pages are paginated; osint-resources had 7+ pages with a low-value long tail. Decide a star/relevance cutoff rather than exhausting every page. — gh-topic-osint-resources
- [NEW] Many start.me boards 403 WebFetch but have an official GitHub mirror whose raw README is a complete dump (osint4all.github.io). Pattern: look for a repo mirror before giving up on a board. — osint4all
- [NEW] Google CSE (cse.google.com) links rot over time; flag for periodic re-validation. — osint4all
- [RETRY] cybertraining.uk/finding-the-lost (404) and Shandyman 'Leveraging AI in OSINT' (Cloudflare 526) were unreachable; retry later. — searchparty-writeups

## Wave 2 + Kimi + Discord (2026-06-13)
- [DONE] Kimi swarm (4 angles: face-search, TikTok/Snap, Telegram, geo/chronolocation) surfaced 12 net-new CURRENT tools (geospy.ai, picarta.ai, lenso.ai, reversely.ai, epieos, telemetr.io, lyzem, geogramint, telepathy, telerecon, snapintel, whereisthisplace). Kimi free-tier facts captured in skill metadata.
- [PARTIAL] TL Discord: channel map captured; richest channels to scrape next = #tools-n-tech (901641655466197034), #general-osint (896091275097427968), #tl-writeups (1402014518111899688), #library-submissions. Discord SPA froze CDP eval — do per-channel in a fresh tab with scroll-to-load.
- [NEW] Toddington & MetaOSINT are huge directories (1899 + 719 new) — many low-MP long-tail entries; flag for an MP-relevance re-scoring pass.
- [RETRY] cupidcr4wl harvest returned 0 (blocked) — re-fetch raw repo.
