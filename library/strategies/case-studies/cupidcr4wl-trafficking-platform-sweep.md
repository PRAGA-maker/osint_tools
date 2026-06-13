---
id: cupidcr4wl-trafficking-platform-sweep
name: 'Trafficking-risk case: sweep username and phone across adult/dating/escort platforms with a stop-and-report tripwire'
description: Use when an adult or older-teen subject's mainstream profiles are stale and there are trafficking/exploitation indicators, and you need the live footprint mainstream username tools never check.
type: case-study
summary: 'cupidcr4wl is a username/phone enumeration tool built specifically for missing-persons cases touching dating, adult video/photo, and human-trafficking concerns, on the premise that people in trafficking situations or who have run often keep ACTIVE accounts on these platforms even after their mainstream profiles go dark. The worked method: take confirmed usernames and phone numbers, sweep them (with spelling variations, since platforms structure handles differently) across seven categories mainstream tools skip - payment/gifting, social, dating/hookup, fetish, adult video/photo, camming, and escort directories - and export hits to a self-contained HTML report for documentation. A hit on these platforms can be the only live digital footprint and a fresh geolocation source. The tool ships an explicit safety tripwire: if you find suspected illegal content (CSAM/trafficking), STOP investigating and use the bundled law-enforcement reporting resources, operating within your jurisdiction. The lesson: do not skip these platforms out of discomfort, run username AND phone with variants, preserve every hit, and pre-commit to halt-and-report on illegal content.'
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
- Gather confirmed usernames and phone numbers for the subject (validated against the source of truth, not raw tool hits).
- Sweep them - with spelling variations, because platforms structure handles differently - across the seven cupidcr4wl categories mainstream username tools skip.
- Export hits to a self-contained HTML report (--export-results) so the live finding survives takedown.
- If a hit shows recent activity or imagery, treat it as a live lead and a potential geolocation source, and verify it against the subject before trusting it.
- If you encounter suspected illegal content (CSAM/trafficking), STOP active investigation, record only what is needed to report, and escalate via the law-enforcement reporting resources within your jurisdiction.
signals:
- A username or phone returns an active account on a dating/adult/escort platform.
- Recent photos or location hints appear on a platform the mainstream profiles did not show.
pitfalls:
- Skipping these platforms out of discomfort and missing the only live footprint.
- Running only the canonical handle spelling and missing variant forms.
- Continuing to dig on illegal content instead of stopping and reporting it.
- Treating a checker hit as the subject without verifying, or ignoring jurisdictional/legal limits.
toolsUsed:
- cupidcr4wl
tags:
- trafficking
- adult-platforms
- phone-pivot
- username-pivot
- safety
- evidence-preservation
evidence:
- type: other
  url: https://github.com/OSINTI4L/cupidcr4wl
  note: 'Built for missing-persons cases involving dating/adult platforms and trafficking concerns; 7 platform categories; run usernames in variations; --export-results writes hits to cc_results.html; bundled law-enforcement reporting resources for suspected illegal content.'
trust: community
source: osinti4l-user
relatedStrategies:
- Check adult/dating/escort platforms in trafficking-risk missing-persons cases
- Username variation sweep across platforms to catch non-canonical handles
- Stop and report, do not investigate, when you find illegal content
- Export and preserve findings as you go for documentation and handoff
- antipattern-automation-without-verification
---

# Trafficking-risk case: sweep username and phone across adult/dating/escort platforms

> cupidcr4wl is a username/phone enumeration tool built specifically for missing-persons cases touching dating, adult, and trafficking concerns, on the premise that people in trafficking situations or who have run often keep active accounts on these platforms even after their mainstream profiles go dark. The worked method sweeps confirmed usernames and phone numbers (with variations) across seven categories mainstream tools skip, exports every hit for documentation, and ships an explicit stop-and-report tripwire for illegal content.

**When to use:** When an adult or older-teen subject's mainstream profiles are stale and there are trafficking/exploitation indicators, and you need the live footprint mainstream username tools never check.

## The pivot chain that worked
1. **Start from confirmed selectors.** Gather the subject's usernames and phone numbers — validated against the source of truth, not raw checker output.
2. **Sweep where mainstream tools don't look.** Run those selectors, with spelling variations (platforms structure handles differently — `[[Username variation sweep across platforms to catch non-canonical handles]]`), across the seven cupidcr4wl categories: payment/gifting, social, dating/hookup, fetish, adult video/photo, camming, and escort directories. This is the premise of `[[Check adult/dating/escort platforms in trafficking-risk missing-persons cases]]`: a person whose mainstream presence has gone dark may still be active here, making it the *only* live footprint.
3. **Preserve every hit.** Export to a self-contained HTML report so a finding survives the source being deleted or set private (`[[Export and preserve findings as you go for documentation and handoff]]`).
4. **Treat a fresh hit as a live lead.** Recent activity or imagery on these platforms can be a current-contact point and a geolocation source.

## The verification step
A checker hit is a lead, not the subject — verify each against the seed before acting, or you import the tool's false positives (`[[antipattern-automation-without-verification]]`). Phone and username are run *both*, because each catches accounts the other misses.

## The safety tripwire (load-bearing)
This branch touches platforms where illegal material can surface, so the method pre-commits a red line: **on suspected illegal content (CSAM/trafficking), stop active investigation immediately** — do not download or distribute — record only what's needed to report (URL, platform, timestamp), and escalate through the bundled law-enforcement reporting resources, within your jurisdiction's laws (`[[Stop and report, do not investigate, when you find illegal content]]`). Continuing to "investigate" such content is itself illegal and can compromise a prosecution.

## The lesson
Don't skip uncomfortable platforms — in trafficking-risk cases they may hold the only live lead. Run username *and* phone with variants, preserve every hit at the moment of discovery, verify before trusting, and pre-decide the halt-and-report tripwire so you never cross it under momentum.

## Signals it's working
- A username or phone returns an active account on a dating/adult/escort platform.
- Recent photos or location hints appear on a platform the mainstream profiles did not show.

## Pitfalls
- Skipping these platforms out of discomfort and missing the only live footprint.
- Running only the canonical handle spelling and missing variant forms.
- Continuing to dig on illegal content instead of stopping and reporting it.
- Treating a checker hit as the subject without verifying, or ignoring jurisdictional/legal limits.

**Tools:** cupidcr4wl

_Harvested from `osinti4l-user` — methodology only, no case PII. Promote/curate as needed._

---
## Metadata
| field | value |
|---|---|
| type | case-study |
| phase | pivot |
| MP relevance | high |
| related | Check adult/dating/escort platforms in trafficking-risk missing-persons cases; Stop and report, do not investigate, when you find illegal content |
