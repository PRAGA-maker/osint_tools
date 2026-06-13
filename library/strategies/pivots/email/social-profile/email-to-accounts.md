---
id: email-to-accounts
name: pivot-email-to-accounts
description: Use when you have an email — discover which accounts it registered, mine breach/leak data for linked selectors, and treat the local-part as a username candidate.
type: technique
phase: pivot
pivotFrom: [email]
pivotTo: [social-profile, username, name, phone]
platforms: [gravatar, github, twitter]
summary: An email is a near-unique selector that unlocks two distinct pivots. Account-discovery tools and registration-check techniques reveal where the address has accounts; breach/leak datasets reveal what's been exposed alongside it — names, usernames, phone numbers, hashed passwords, and other emails. The email's local-part is also a strong username candidate. Together these turn one address into a cluster of accounts and identity fragments, making email one of the highest-yield seeds when you have one.
missingPersonsRelevance: high
whenToUse: You hold an email address (from a profile, a leak, a resume, a WHOIS, an account-recovery hint) and want the accounts/identity behind it.
steps:
  - Treat the local-part as a username and run handle enumeration (`[[username-reuse-enumeration]]`) — people reuse the part before the @ as a handle.
  - Run account-discovery / registration checks — which platforms have an account on this email (some sites confirm via signup/reset flows; prefer passive tools).
  - Search breach/leak datasets — these surface linked names, usernames, phones, other emails, and password reuse patterns.
  - Check identity services tied to email — Gravatar and similar return a profile photo/handle straight from an email hash.
  - Harvest and recurse — every new username/email/phone found goes back through its own pivots, verifying as you go.
signals:
  - The local-part is a real reused handle across multiple platforms.
  - A breach record ties the email to a name/phone you independently already hold — convergence.
pitfalls:
  - Active registration-probing that emails the subject (account-exists checks, password resets) tips them off — prefer passive methods (see `[[antipattern-contaminating-the-subject]]`).
  - Breach data is dated and dirty — a name/phone in a 2015 dump may be stale or belong to a co-leaked record; verify.
  - Shared/role emails (family, work) aren't one person — don't assume the address maps to the subject alone.
toolsUsed: [holehe, h8mail, hunter-io, gravatar, dehashed]
evidence: []
trust: trusted
relatedStrategies: [username-reuse-enumeration, pivot-phone-to-identity, antipattern-contaminating-the-subject, phase-verification]
tags: [email, breach, account-discovery, high-yield]
source: ""
---

# Email → Social profiles (email-to-accounts)

## The move
An email address is close to unique, and it forks into two strong pivots: **account discovery** (where does this address have accounts?) and **breach/leak mining** (what's been exposed next to it?). Plus the **local-part** is itself a username candidate. One address routinely expands into a cluster of accounts and identity fragments.

## Account discovery
Tools that check registration across many sites reveal where the email has accounts. Prefer the **passive** methods — ones that query without sending the subject anything. Some "account exists?" techniques rely on signup or password-reset flows that *email the target*; those tip them off and are a contamination risk (`[[antipattern-contaminating-the-subject]]`). Choose tools that determine registration silently. Gravatar and similar identity services map an email hash straight to a profile photo and handle — a clean passive win.

## Breach and leak mining
Leak datasets are an email-pivot superpower: a single address can pull a real **name**, a **phone**, **other emails**, reused **usernames**, and password patterns from old breaches. This is often where a thin email seed suddenly becomes a full identity. Two cautions: the data is **dated and dirty** (a 2015 dump may be stale), and records can co-mingle, so a field next to your email isn't guaranteed to be the subject's. Verify against a second signal.

## Local-part as username
People reuse the string before the `@` as a handle everywhere. Feed it straight into `[[username-reuse-enumeration]]`. This is one of the most reliable cheap pivots off an email.

## Recurse and verify
Every new username, email, and phone you surface goes back through its own pivots — the graph recurses. And every promotion still passes `[[phase-verification]]`: convergence (a breach name matching a name you already had) is your confirmation, not the breach record alone.

---
## Metadata
| field | value |
|---|---|
| type | technique |
| pivot | email → social-profile, username, name, phone |
| platforms | gravatar, github, twitter |
| MP relevance | high |
| tools | holehe, h8mail, hunter-io, gravatar, dehashed |
