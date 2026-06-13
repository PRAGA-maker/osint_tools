---
id: check-adult-dating-escort-platforms-in-trafficking-risk-missing-persons-cases
name: Check adult/dating/escort platforms in trafficking-risk missing-persons cases
description: Use when When the missing person is an adult or older teen, mainstream profiles are stale, and there are trafficking/exploitation or sex-work indicators.
type: playbook
summary: 'cupidcr4wl was built specifically for missing-persons investigations where dating, adult video/photo platforms, and human-trafficking concerns are relevant, on the premise that people in trafficking situations or who have run often maintain active accounts on these platforms even when their mainstream profiles go dark. The playbook is to take confirmed usernames and phone numbers and sweep them across payment/gifting, social, dating/hookup, fetish, adult video/photo, camming, and escort directories - categories that mainstream username tools skip. A hit on these platforms can be the only live '
missingPersonsRelevance: high
phase: pivot
pivotFrom:
- username
- phone
pivotTo:
- social-profile
- image
- geolocation
platforms:
- dating-sites
- escort-directories
- camming-sites
- adult-platforms
steps:
- Gather confirmed usernames and phone numbers for the subject.
- 'Sweep them (with variations) across the seven cupidcr4wl categories: payment/gifting, social, dating/hookup, fetish, adult video/photo, camming, escort.'
- Export hits to an HTML report for documentation.
- If a hit reveals recent activity or imagery, treat it as a live lead and a potential geolocation source.
- If illegal content (e.g., CSAM/trafficking) is found, stop and use the law-enforcement reporting resources rather than investigating further yourself.
signals:
- A username/phone returns an active account on a dating/adult/escort platform
- Recent photos or location hints appear on a platform the mainstream profiles did not show
pitfalls:
- Skipping these platforms out of discomfort and missing the only live footprint
- Continuing to dig on illegal content instead of reporting it to law enforcement
- Ignoring jurisdictional/legal limits on accessing these platforms
toolsUsed:
- cupidcr4wl
tags:
- trafficking
- adult-platforms
- phone-pivot
- username-pivot
- safety
- playbook
evidence:
- type: tool
  url: https://github.com/OSINTI4L/cupidcr4wl
  note: Built for missing-persons cases involving dating/adult platforms and trafficking concerns; 7 platform categories; LE reporting resources for illegal content
trust: community
source: osinti4l-user
---

# Check adult/dating/escort platforms in trafficking-risk missing-persons cases

> cupidcr4wl was built specifically for missing-persons investigations where dating, adult video/photo platforms, and human-trafficking concerns are relevant, on the premise that people in trafficking situations or who have run often maintain active accounts on these platforms even when their mainstream profiles go dark. The playbook is to take confirmed usernames and phone numbers and sweep them across payment/gifting, social, dating/hookup, fetish, adult video/photo, camming, and escort directories - categories that mainstream username tools skip. A hit on these platforms can be the only live 

**When to use:** When the missing person is an adult or older teen, mainstream profiles are stale, and there are trafficking/exploitation or sex-work indicators.

## Steps
- Gather confirmed usernames and phone numbers for the subject.
- Sweep them (with variations) across the seven cupidcr4wl categories: payment/gifting, social, dating/hookup, fetish, adult video/photo, camming, escort.
- Export hits to an HTML report for documentation.
- If a hit reveals recent activity or imagery, treat it as a live lead and a potential geolocation source.
- If illegal content (e.g., CSAM/trafficking) is found, stop and use the law-enforcement reporting resources rather than investigating further yourself.

## Signals it's working
- A username/phone returns an active account on a dating/adult/escort platform
- Recent photos or location hints appear on a platform the mainstream profiles did not show

## Pitfalls
- Skipping these platforms out of discomfort and missing the only live footprint
- Continuing to dig on illegal content instead of reporting it to law enforcement
- Ignoring jurisdictional/legal limits on accessing these platforms

**Tools:** cupidcr4wl

_Harvested from `osinti4l-user` — methodology only, no case PII. Promote/curate as needed._
