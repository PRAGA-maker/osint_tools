---
id: build-clean-sock-puppet-accounts-that-look-normal
name: Build clean sock-puppet accounts that look normal
description: Use when When you need research accounts to view platforms that require login (e.g., Instagram, Facebook, TikTok).
type: technique
summary: 'TOFM''s sock-puppet guidance is counterintuitive: blend in rather than over-engineer. Create accounts via the mobile app (more forgiving signup), from your residential IP without a VPN on a vanilla Chrome browser so you look like an ordinary user, and don''t put in more effort than needed. Never reuse other people''s headshots/profile photos from around the internet — that will get you flagged. The cleanest method is a disposable phone set up over your home internet.'
missingPersonsRelevance: medium
phase: opsec
pivotFrom: []
steps:
- Prefer the platform's mobile app for signup (more forgiving than web).
- Sign up from your residential IP, no VPN, vanilla Chrome — appear 'normal'.
- Keep the persona minimal; don't over-build it.
- Never use other people's headshots/profile pics scraped from the internet.
- For the cleanest setup, use a disposable mobile phone provisioned over your home connection.
signals:
- The account survives signup and routine use without verification challenges or bans
pitfalls:
- Using a VPN/exotic browser that makes the new account look suspicious and gets it flagged
- Reusing someone's real photo as the profile pic (gets you 'in trouble')
- Over-investing effort that increases exposure
tags:
- sock-puppet
- opsec
- account-creation
- tracelabs
evidence:
- type: doc
  url: https://raw.githubusercontent.com/tracelabs/tofm/main/tofm.md
  note: 'TOFM sock-puppet advice: mobile signup, residential IP without VPN, vanilla Chrome, no scraped headshots, disposable phone is cleanest.'
trust: community
source: tofm
---

# Build clean sock-puppet accounts that look normal

> TOFM's sock-puppet guidance is counterintuitive: blend in rather than over-engineer. Create accounts via the mobile app (more forgiving signup), from your residential IP without a VPN on a vanilla Chrome browser so you look like an ordinary user, and don't put in more effort than needed. Never reuse other people's headshots/profile photos from around the internet — that will get you flagged. The cleanest method is a disposable phone set up over your home internet.

**When to use:** When you need research accounts to view platforms that require login (e.g., Instagram, Facebook, TikTok).

## Steps
- Prefer the platform's mobile app for signup (more forgiving than web).
- Sign up from your residential IP, no VPN, vanilla Chrome — appear 'normal'.
- Keep the persona minimal; don't over-build it.
- Never use other people's headshots/profile pics scraped from the internet.
- For the cleanest setup, use a disposable mobile phone provisioned over your home connection.

## Signals it's working
- The account survives signup and routine use without verification challenges or bans

## Pitfalls
- Using a VPN/exotic browser that makes the new account look suspicious and gets it flagged
- Reusing someone's real photo as the profile pic (gets you 'in trouble')
- Over-investing effort that increases exposure

_Harvested from `tofm` — methodology only, no case PII. Promote/curate as needed._
