---
id: email2phonenumber
name: email2phonenumber
description: Use when you have an `email` and want to recover the target's phone number by harvesting masked digits from services' password-reset flows — returns a reconstructed phone.
url: https://github.com/martinvigo/email2phonenumber
category: email
path:
- email
bestFor: Reconstructing a target's full phone number from the masked hints that websites' password-recovery flows reveal for a known email.
selectorsIn:
- email
selectorsOut:
- phone
status: degraded
pricing: free
costNote: Free and open-source (Python). No paid tier; effectiveness depends on which services still leak masked digits for the email.
opsec: active
opsecNote: The tool triggers password-recovery flows on third-party services using the target's email to scrape masked phone digits. This can generate account-security notifications to the owner and leaves a footprint on those services. It is NOT passive — use only with authorisation, from a controlled environment, and expect it may alert the target.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: cli
trust: community
trustNote: Well-known PoC by Martin Vigo demonstrating the masked-digit-harvesting technique; the concept is sound, but many services have since changed their reset flows/masking, so results are inconsistent.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- email2phonenumber
- martinvigo/email2phonenumber
tags:
- email
- phone-recovery
- password-reset
- cli
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# email2phonenumber

> A proof-of-concept that reconstructs a phone number from an email — by collecting the masked digits (e.g. `••• ••• ••89`) that different sites reveal in their password-recovery flows and stitching them together.

## When to use
You have an `email` and no phone, and you want to derive the associated `phone` number. Many services, in their "forgot password" flow, show partial masked phone digits tied to an account. Because different services mask different positions, email2phonenumber queries several, harvests the exposed digits, and reconstructs candidate numbers — then can validate them by generating and checking possibilities. Reach for it when a phone is the missing link and you're authorised to probe.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install dependencies (Python).
2. **Scrape:** run the scrape mode with the target `email` to collect masked digits from supported services.
3. **Bruteforce/generate:** use the tool's generation mode to build candidate numbers consistent with the harvested masks.
4. **Validate:** narrow candidates using area-code/format logic and, cautiously, verification checks.
5. Pivot: a recovered phone feeds phone-OSINT (`[[whatsapp-checkleaked]]`, PhoneInfoga, carrier/HLR lookups) and reverse-number people-search.

## Inputs → Outputs
- **In:** `email`
- **Out:** `phone` (reconstructed candidate number)
- **Empty/negative result looks like:** no masked digits harvested, or too few to reconstruct — increasingly common as services changed their reset masking, so a failure often reflects tooling drift, not that the email has no phone.

## Gotchas & OpSec
- **Degraded:** many target services altered reset flows/masking since the tool's release; supported-site coverage has decayed — verify it still works before relying on it.
- **Active and alerting:** triggering password-recovery can notify the account owner; only run with authorisation and from a controlled environment.
- Reconstruction yields candidates, not a confirmed number — validate before use.

## Overlaps ("do both")
- Pairs with `[[whatsapp-checkleaked]]` and PhoneInfoga — once you have a candidate number, confirm it's live (WhatsApp) and enrich it (carrier/owner) with those.

## Trust & verifiability
`trust: community` — a respected PoC demonstrating a real technique, but its site coverage has aged; treat outputs as candidate numbers to validate, and mind the active/alerting nature.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email2phonenumber |
| category | email |
| selectorsIn → selectorsOut | email → phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (captcha) |
