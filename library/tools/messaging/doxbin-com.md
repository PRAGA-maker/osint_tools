---
id: doxbin-com
name: doxbin.com
description: Use when you have a `name`, `username` or `phone` and want to check whether the subject has been doxed — returns any leaked personal dossier (address, phone, email, associates) posted about them.
url: https://doxbin.com/
category: messaging
path:
- messaging
bestFor: Checking whether a subject already has a publicly-posted "dox" (leaked personal dossier) and reading what identifiers it exposes.
selectorsIn:
- name
- username
- phone
selectorsOut:
- address
- phone
- email
- social-profile
- associate
status: live
pricing: free
costNote: Free to search and read public pastes; some content and posting may require an account.
opsec: active
opsecNote: Highly sensitive. Doxbin is Cloudflare-gated and hostile; browsing is technically passive but you are visiting a site that logs traffic and is itself a target of law enforcement. Never log in with, post, or search personal identifiers tied to you. Use an isolated VM + sock-puppet routing. Reading is a defensive check on what is exposed about your subject; do NOT create, add to, or amplify a dox.
humanInLoop: true
humanInLoopReason:
- legal-gate
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous, unmoderated doxing paste site; entries are attacker-submitted, frequently false, malicious, or mixing multiple people. Nothing here is verified — treat as unsourced accusation.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- doxbin
- doxbin.com
tags:
- telegram
- Telegram
- doxing
- leaked-data
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# doxbin.com

> A notorious anonymous "dox" paste site: search a subject to see whether someone has already published a dossier of their personal info — read defensively, never contribute.

## When to use
Reach for this only as a defensive/awareness check: you have a `name`, `username`, or `phone` and want to know whether the subject has been doxed — i.e. whether an attacker has already published their home `address`, phones, emails, family and other identifiers. Knowing a dox exists (and what it leaks) matters in threat-assessment and some missing-person/stalking contexts. It is never a source of *verified* facts — entries are attacker-authored and often wrong or malicious.

## How to use it (`bestInteractionPattern`: web-manual)
1. Treat this as a hostile environment before you connect: use an isolated VM and sock-puppet routing, and clear any identifiers of your own from the browser session. Get a legal/authorization sign-off first — accessing and handling this material can carry legal and ethical exposure.
2. The site sits behind Cloudflare (expect challenge pages). Reach https://doxbin.com/ and use its search to look up the subject's `name`/`username`/`phone`.
3. If a paste exists, read it strictly to inventory what identifiers are exposed about your subject and to gauge threat — do not treat any field as confirmed.
4. Do NOT create an account tied to you, do NOT post, add, comment, or "claim" anything, and do NOT re-share the dossier. Your role is to observe exposure, not to extend it.
5. Pivot: exposed identifiers become things to *protect* or corroborate elsewhere; a confirmed dox feeds a safety/threat report and, where appropriate, takedown or law-enforcement referral.

## Inputs → Outputs
- **In:** `name`, `username`, or `phone`
- **Out:** (if a dox exists) `address`, `phone`, `email`, `social-profile`, `associate`s — all attacker-asserted
- **Empty/negative result looks like:** no matching paste — meaning no dox is indexed here, NOT that the person is safe or that no dox exists elsewhere.

## Gotchas & OpSec
- Human-in-the-loop: mandatory legal/authorization gate before use, plus Cloudflare challenges; only log in from a fully compartmentalized identity, if at all.
- OpSec: classed **active** because it is a monitored, adversarial site under law-enforcement scrutiny — your visit is logged. Isolate everything.
- Data is unverified and frequently defamatory or conflated across people. Never republish, and never present a doxbin field as fact.
- Ethics/legal: this tool is for defensive assessment of exposure only. Do not use it to locate, harass, or contribute to harming anyone.

## Overlaps ("do both")
- Pairs with breach/leaked-credential checkers like `[[haveibeenpwned]]`-style tools — those tell you what data leaked from breaches, while doxbin tells you whether someone deliberately assembled and published a targeted dossier.

## Trust & verifiability
`trust: unverified` — content is anonymous, unmoderated, attacker-submitted, and routinely false or malicious; its only evidentiary value is "a dossier claiming X has been published," never that X is true.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | doxbin-com |
| category | messaging |
| selectorsIn → selectorsOut | name, username, phone → address, phone, email, social-profile, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (legal-gate, account-login) |
