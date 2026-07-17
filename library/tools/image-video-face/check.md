---
id: check
name: Check (Meedan)
description: Use when you (as a newsroom/CSO team) have a claim, image, or video to verify collaboratively at scale — returns a shared workspace with tiplines, claim-matching, and media analysis; not a one-off lookup.
url: https://meedan.org/check
category: image-video-face
path:
- image-video-face
bestFor: Team-based, at-scale verification of claims and media via tiplines, claim matching, and collaborative annotation.
selectorsIn:
- social-profile
- image
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Open-source software from Meedan (a nonprofit); the hosted platform is provided to qualifying newsrooms, fact-checkers, and civil-society organisations, often free or low-cost. Requires an organisational account.
opsec: passive
opsecNote: Content you upload for verification is processed on Meedan's platform and shared within your workspace/team — treat it as leaving your machine. Suited to collaborative newsroom work, not covert single-analyst OSINT; don't load sensitive case material you can't share.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Meedan, an established nonprofit in the fact-checking/verification space; used by major fact-checkers (AFP, Rappler, India Today). It's a workflow platform, not an automated identifier of people.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- montage-meedan-com
- invid-verification-plugin
aliases:
- Meedan Check
- Check by Meedan
tags:
- fact-checking
- verification
- collaborative
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Check (Meedan)

> Meedan's collaborative verification platform: a team workspace for triaging, claim-matching, and analysing at scale — built for fact-checking newsrooms, not for one-off face/image identification.

## When to use
You are working in (or with) a newsroom, fact-checking outfit, or civil-society team that needs to verify a high volume of claims, images, and videos collaboratively. Check ingests submissions via tiplines (WhatsApp, Messenger, Telegram, LINE, Viber), matches new items against previously-checked claims to avoid duplicate work, runs multilingual media analysis, and lets a team annotate and resolve items together. It is a *workflow and triage* tool — reach for it when the problem is scale and collaboration, not when you need a single quick lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Obtain an organisational account (Meedan onboards qualifying newsrooms/CSOs; the software is also open source and self-hostable).
2. Set up or join a workspace; connect tiplines if you collect public submissions.
3. Submit or receive items (claims, images, videos); Check clusters them and surfaces prior matching checks.
4. Use the media-analysis tools and team annotation to reach and publish a verification verdict.
5. Pivot: for the actual forensic image/video steps, pair with dedicated tools — Check organises the workflow around them rather than replacing them.

## Inputs → Outputs
- **In:** claims, `image`/video, or `social-profile` content submitted for verification
- **Out:** a shared verification record — status, prior-match links, annotations (`social-profile` context around a claim)
- **Empty/negative result looks like:** no prior match and no team verdict yet — the item is novel and needs original verification work; Check tells you it's unseen, it doesn't decide truth for you.

## Gotchas & OpSec
- Not a person-finder: it does no face recognition or reverse-image identification itself — misfiled here as a lookup; it's a collaboration layer. Low direct missing-persons relevance.
- Access gate: the hosted platform needs an organisational account; it's aimed at teams, not individual investigators.
- Shared data: uploads live in a team workspace — don't load material you can't share with collaborators or Meedan.
- OpSec: passive on content, but account-gated and collaborative by design, so not for covert solo work.

## Overlaps ("do both")
- Pairs with `[[invid-verification-plugin]]` (frame/metadata forensics) and `[[montage-meedan-com]]` — Check runs the team workflow while those do the actual media forensics; use them together in a newsroom pipeline.

## Trust & verifiability
`trust: trusted` — a reputable nonprofit tool widely used by professional fact-checkers; reliable as a verification workflow platform, with the caveat that verdicts come from the humans using it, not from the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | check |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile, image → social-profile |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
