---
id: handspeak-english-sign-language
name: HandSpeak (ASL Dictionary)
description: Use when you have footage of someone signing and want to identify the signs — a video ASL dictionary to look up American Sign Language signs, fingerspelling and phrases.
url: https://www.handspeak.com/
category: translation-language
path:
- translation-language
bestFor: Looking up American Sign Language signs/fingerspelling from video to interpret a signer.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Dictionary and most materials are free; an optional ad-free Patron subscription exists.
opsec: passive
opsecNote: You browse a public reference site — nothing touches any subject. Fully passive; do not upload your case footage anywhere, just compare signs by eye.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: A comprehensive ASL resource maintained since 1995 by a native signer/instructor (Jolanta Lapiak); reputable within the Deaf-education community.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- handspeak.com
- ASL dictionary
tags:
- toddington
- sign-language
- asl
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# HandSpeak (ASL Dictionary)

> A long-running video dictionary of American Sign Language — search signs, fingerspelling, numbers and phrases with demonstration clips, useful for interpreting a signer in footage.

## When to use
Your evidence includes someone communicating in sign language (a video, a witness who signs) and you need to work out what's being signed. HandSpeak lets you look up individual ASL signs and fingerspelling with video demonstrations, so you can match handshapes/movements in your footage against the dictionary. It's an interpretation aid for ASL specifically — treat serious analysis as a job for a qualified interpreter.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.handspeak.com/.
2. Use the dictionary search for an English word to see its ASL sign, or browse fingerspelling/alphabet and number references.
3. Compare the demonstration video against the handshapes/movements in your footage, sign by sign.
4. Assemble likely meaning, remembering ASL grammar differs from English word order.
5. Pivot: fingerspelled names/letters can yield a `name` lead; for anything consequential, hand the footage to a certified ASL interpreter to confirm.

## Inputs → Outputs
- **In:** an English word to look up, or observed signs to match (no OSINT selector query)
- **Out:** the corresponding ASL sign videos / fingerspelling reference (an interpretation aid)
- **Empty/negative result looks like:** no clear dictionary match for an observed sign — expected for regional variants, name signs or non-ASL sign languages; don't force a match.

## Gotchas & OpSec
- Human-in-the-loop: yes — you (or ideally an interpreter) do the visual matching and interpretation.
- OpSec: **passive** — a public reference; keep your footage local and just compare by eye.
- It's **ASL** — other countries use different sign languages (BSL, LSF, etc.); confirm the language before assuming ASL, and defer to a professional for evidentiary interpretation.

## Overlaps ("do both")
- Pair with a professional ASL interpreter and regional sign-language dictionaries — HandSpeak is the quick self-serve lookup; those are authoritative for dialect, name signs and courtroom-grade interpretation.

## Trust & verifiability
`trust: trusted` — an established, expert-maintained ASL resource; reliable for standard ASL, but interpretation of real footage still needs human/professional judgement.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | handspeak-english-sign-language |
| category | translation-language |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
