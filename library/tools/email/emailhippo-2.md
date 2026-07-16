---
id: emailhippo-2
name: EmailHippo
description: Use when you have an `email` and want to check whether it is real/deliverable and how trustworthy it looks — returns a validity verdict, a reliability score, and mailbox/domain diagnostics.
url: https://tools.emailhippo.com/email/
category: email
path:
- email
bestFor: Verifying that an email address exists and is deliverable, with a reliability score, before investing in it.
selectorsIn:
- email
selectorsOut:
- email
- domain
status: live
pricing: freemium
costNote: The web "More" free tool verifies single addresses at no cost; bulk verification and the API require a paid Email Hippo plan/key.
opsec: passive
opsecNote: Passive but not zero-touch — verification typically performs SMTP/MX checks against the address's mail server, which can register a probe in that server's logs (it does NOT email or alert the person). Use a sock-puppet context if you want to avoid your own IP appearing; Email Hippo runs the checks server-side.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Email Hippo is an established commercial email-verification vendor; the deliverability verdict is technically sound, though "valid" means the mailbox accepts mail, not who owns it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Email Hippo
- tools.emailhippo.com
tags:
- Emails
- email-verification
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- email-address-verifier
---

# EmailHippo

> A free single-address email verifier: it tells you whether an address is syntactically valid, whether its domain accepts mail, whether the mailbox exists, and scores overall reliability on a 10-point scale.

## When to use
You have an `email` and need to know if it's real and deliverable before treating it as a live lead — e.g. deciding whether an address recovered from a breach, a form, or a guessed pattern is worth pivoting on. A high reliability score plus "mailbox exists" tells you the address is active; a hard fail tells you not to waste further OSINT on it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tools.emailhippo.com/email/ (the free "More" verification tool).
2. Enter the target `email` and run the check.
3. Read the verdict: syntax, DNS/`domain` MX validity, mailbox existence (SMTP check), disposable/role-address flags, and a reliability score out of 10.
4. Interpret: "valid + high score" = deliverable, active address; "invalid/does-not-exist" = dead or fake; "catch-all" = server accepts everything, so mailbox existence is inconclusive.
5. Pivot: a confirmed-live address is worth running through existence oracles (`[[account-live-com]]`, `[[yahoo-mail]]`) and enrichment (`[[google-account-finder-epieos]]`, `[[gravatar]]`).

## Inputs → Outputs
- **In:** `email`
- **Out:** validity verdict, reliability score (/10), `domain`/MX diagnostics, disposable/role/catch-all flags
- **Empty/negative result looks like:** "does not exist" / low score / hard-bounce — the mailbox isn't deliverable. A "catch-all domain" result is NOT a confirmation; it means the check couldn't prove the specific mailbox exists.

## Gotchas & OpSec
- "Valid/deliverable" ≠ identity — it confirms a mailbox accepts mail, not who owns it. This is a filter, not an attribution tool.
- Catch-all domains and greylisting produce inconclusive results; don't read them as positive.
- Verification does an SMTP/MX probe to the mail server (server-side by Email Hippo) — it does not notify the address owner, but the probe may appear in mail-server logs.
- Free tool is single-address; bulk/automation needs a paid key.

## Overlaps ("do both")
- Pairs with existence oracles `[[account-live-com]]` and `[[yahoo-mail]]` — EmailHippo confirms deliverability generically; those confirm a specific provider account.
- Feed verified-live addresses into enrichment tools `[[google-account-finder-epieos]]` / `[[gravatar]]`.

## Trust & verifiability
`trust: trusted` — Email Hippo is a reputable verification vendor and the technical deliverability signal is reliable. Keep in mind the score measures deliverability/quality, not ownership, and catch-all/greylisting cases are genuinely inconclusive rather than positive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | emailhippo-2 |
| category | email |
| selectorsIn → selectorsOut | email → email, domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
