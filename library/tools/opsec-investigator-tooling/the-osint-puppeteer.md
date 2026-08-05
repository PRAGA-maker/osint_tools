---
id: the-osint-puppeteer
name: The OSINT Puppeteer
description: Use when you need to build a durable sock-puppet identity for investigation — returns a step-by-step tradecraft guide for creating and maintaining research personas.
url: https://osintcurio.us/2018/12/27/the-puppeteer/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Learning how to design, provision, and maintain a believable sock-puppet account without burning your real identity.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free article on the OSINT Curious blog; no account required to read.
opsec: passive
opsecNote: This is the OpSec guidance itself — reading it is passive. Its whole purpose is to keep your investigative persona separated from your real identity; follow it before you interact with any target, because a leaky sock puppet can expose you and tip off the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by OSINT Curious (osintcurio.us), a respected practitioner community; widely cited tradecraft guidance authored by experienced investigators.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osintcurious
- cosint-osint-on-cars
aliases:
- The Puppeteer
- OSINT Curious sock puppet guide
tags:
- sockpuppet
- tradecraft
- opsec
source: metaosint
lastVerified: '2026-08-05'
enrichment: full
---

# The OSINT Puppeteer

> A practitioner guide to building and running sock-puppet accounts — the tradecraft layer you set up before touching any platform, so your research never traces back to you.

## When to use
Before you create or use any investigative persona — to view a private profile, join a group, or interact where a real account would expose you. This is a methodology resource, not a lookup tool: it tells you how to construct a believable persona (name, backstory, photos, phone/verification) and maintain it so platforms don't flag it and targets can't unmask you. Read it early; a poorly built puppet is an OpSec failure waiting to happen.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the article at https://osintcurio.us/2018/12/27/the-puppeteer/.
2. Design the persona: pick a culturally/geographically appropriate name and write a full backstory (gender, DOB, residence, employer, interests) — document it so you answer security questions consistently.
3. Provision infrastructure: a dedicated prepaid SIM/VoIP number for verification, a separated browser/identity, and a password manager + tracking spreadsheet for multiple personas.
4. Handle photos carefully: avoid reverse-image-searchable stock photos — the guide's tactics (alteration, morphing) reduce, but don't eliminate, that risk (see gotchas).
5. Maintain the account with ordinary activity over time and plan a burn/contingency procedure in case it's exposed.

## Inputs → Outputs
- **In:** none — it's a methodology/reading resource
- **Out:** a repeatable process for creating and sustaining sock-puppet identities
- **Empty/negative result looks like:** n/a — this is guidance, not a query; "failure" is a persona that gets flagged or unmasked because a step was skipped.

## Gotchas & OpSec
- Human-in-the-loop: all of it — building a credible persona is manual, ongoing work.
- Photo risk: never use real people's photos or plain stock images; even altered stock can be reverse-image-searched, and AI-generated faces have their own tells — treat the article's 2018 photo advice as a floor, not the current state of the art.
- Legal/ToS: sock puppets violate many platforms' terms; ensure your use is lawful and authorized for your engagement.
- The article dates to 2018 — the principles hold, but verification/detection has tightened, so pair it with current persona-OpSec practice.

## Overlaps ("do both")
- Pairs with [[osintcurious]] and other persona/OpSec resources, plus AI-face-detection tools — this teaches persona construction; the detectors help you check your own puppet the way a target would.

## Trust & verifiability
`trust: trusted` — authoritative community tradecraft from OSINT Curious; the guidance is sound, though technical specifics (phone verification, photo evasion) should be updated against today's platform defenses.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-osint-puppeteer |
