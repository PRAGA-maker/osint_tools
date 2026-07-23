---
id: crontab-guru
name: Crontab guru
description: Use when you need to write or decode a cron schedule expression for automating recurring OSINT jobs — returns a plain-English reading and next-run times for a cron string.
url: https://crontab.guru/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Building and validating cron schedule expressions for automated/recurring collection jobs.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web editor by Cronitor; no account.
opsec: passive
opsecNote: A syntax helper — you type a schedule expression, not any target data; fully passive with no OSINT-target exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Well-known free utility from Cronitor; deterministically parses/explains cron syntax, so its output is reliable by construction.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- crontab.guru
tags:
- opsec-investigator-tooling
- automation
- cron
- utility
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Crontab guru

> A tiny but essential utility — write a cron schedule and see it explained in plain English with the next run times. Plumbing for automating recurring collection.

## When to use
You're setting up automated/recurring OSINT jobs (a scheduled scrape, a monitoring script, a periodic archive run) and need to get the cron timing right — or you've inherited a crontab and need to decode what an expression actually does and when it next fires.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://crontab.guru/.
2. Type or edit a cron expression (e.g. `*/15 * * * *`); it live-explains the schedule and shows upcoming run times.
3. Adjust until the plain-English reading matches your intent.
4. Pivot: paste the validated expression into your scheduler/crontab for the automation (e.g. running `[[ddgr]]`/`[[auto-archiver]]` on a schedule).

## Inputs → Outputs
- **In:** a cron schedule expression (no personal selector)
- **Out:** plain-English explanation + next scheduled run times
- **Empty/negative result looks like:** an invalid expression is flagged rather than explained — fix the syntax it points at.

## Gotchas & OpSec
- It validates *timing* only — it doesn't run anything or know your server's timezone/crontab specifics.
- Beware timezone differences between crontab.guru and your actual host.
- Purely a helper — no OSINT data involved.

## Overlaps ("do both")
- Supports any scheduled tooling — pair with the tools you're automating (e.g. `[[auto-archiver]]`, `[[dnsrecon]]`); crontab.guru just gets the schedule right.

## Trust & verifiability
`trust: trusted` — a reliable, deterministic syntax tool from a reputable vendor; its explanation is correct by construction.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crontab-guru |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
