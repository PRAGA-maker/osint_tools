---
id: stop-and-report-do-not-investigate-when-you-find-illegal-content
name: Stop and report, do not investigate, when you find illegal content
description: Use when The moment you encounter suspected illegal content (CSAM, trafficking) while sweeping adult/dating/escort platforms.
type: pattern
summary: 'cupidcr4wl''s documentation builds in an explicit boundary: if you believe you have found a platform hosting illegal content, use the bundled law-enforcement reporting resources to report it, and operate within your jurisdiction''s laws. For missing-persons cases that touch adult/trafficking platforms, this is a critical OPSEC and ethical guardrail - continuing to dig into CSAM or trafficking material can be illegal and can compromise an eventual prosecution. The transferable pattern is to pre-decide a tripwire: on suspected illegal content, halt active investigation and route to the proper auth'
missingPersonsRelevance: high
phase: opsec
pivotFrom: []
platforms:
- adult-platforms
- escort-directories
steps:
- Stop active investigation of the material immediately - do not download or distribute.
- Record only what is necessary to report (URL, platform, timestamp).
- Use the law-enforcement reporting resources to escalate to the appropriate authority.
- Stay within the laws and regulations of your jurisdiction throughout.
signals:
- You encounter content that appears to depict minors or trafficking
pitfalls:
- Continuing to 'investigate' illegal content and exposing yourself to legal liability
- Failing to report through proper channels
- Ignoring jurisdictional limits
toolsUsed:
- cupidcr4wl
tags:
- opsec
- legal
- ethics
- trafficking
- law-enforcement
- guardrail
evidence:
- type: tool
  url: https://github.com/OSINTI4L/cupidcr4wl/blob/main/.github/LEReportingResources.md
  note: README directs users to law-enforcement reporting resources for suspected illegal content; use in accordance with local law
trust: community
source: osinti4l-user
---

# Stop and report, do not investigate, when you find illegal content

> cupidcr4wl's documentation builds in an explicit boundary: if you believe you have found a platform hosting illegal content, use the bundled law-enforcement reporting resources to report it, and operate within your jurisdiction's laws. For missing-persons cases that touch adult/trafficking platforms, this is a critical OPSEC and ethical guardrail - continuing to dig into CSAM or trafficking material can be illegal and can compromise an eventual prosecution. The transferable pattern is to pre-decide a tripwire: on suspected illegal content, halt active investigation and route to the proper auth

**When to use:** The moment you encounter suspected illegal content (CSAM, trafficking) while sweeping adult/dating/escort platforms.

## Steps
- Stop active investigation of the material immediately - do not download or distribute.
- Record only what is necessary to report (URL, platform, timestamp).
- Use the law-enforcement reporting resources to escalate to the appropriate authority.
- Stay within the laws and regulations of your jurisdiction throughout.

## Signals it's working
- You encounter content that appears to depict minors or trafficking

## Pitfalls
- Continuing to 'investigate' illegal content and exposing yourself to legal liability
- Failing to report through proper channels
- Ignoring jurisdictional limits

**Tools:** cupidcr4wl

_Harvested from `osinti4l-user` — methodology only, no case PII. Promote/curate as needed._
