---
id: timeline-anchoring
name: pattern-timeline-anchoring
description: Use to convert scattered posts into a last-known-activity timeline — order every dated artifact so you can see the most recent signal of life and spot what doesn't fit.
type: pattern
phase: enrichment
pivotFrom:
- social-profile
- image
pivotTo:
- geolocation
summary: A timeline turns a pile of posts, photos, check-ins, and timestamps into a chronological narrative whose most important point is the LAST one — the most recent confirmed signal of activity. Building it surfaces the subject's routine and recent locations, anchors every other claim to a date, and — crucially — exposes contradictions a date can't hide (a "live" post that pre-dates the disappearance, two events that can't both be true). In missing-persons work, last-known-activity is often the single most actionable output.
missingPersonsRelevance: high
whenToUse: As soon as you have a few dated artifacts — during enrichment, and continuously as new dated selectors arrive.
steps:
- Collect every dated artifact — posts, photos, check-ins, comments, login/last-seen indicators, EXIF and chronolocation times.
- Place each on a single timeline with its source and a confidence (an inferred chronolocation time is softer than an explicit post date).
- Find the LAST confirmed activity — the most recent point that genuinely shows the subject acting, not just an old post resurfacing.
- Read the routine — recurring places, posting cadence, day/night patterns; deviations from routine are signals.
- Stress-test for contradictions — anything that can't coexist (a post dated after a known event, two simultaneous locations) flags a wrong selector or a different person.
signals:
- A clear last-known-activity point emerges with a source you trust.
- The timeline is internally consistent — dates, places, and events all coexist without contradiction.
pitfalls:
- Trusting a display "date" that's actually a repost, a scheduled post, or a re-share of old content — verify the artifact is genuinely recent.
- Mixing timezones silently — normalize before ordering, or you'll misplace events.
- Reading a gap as "missing since" when it may just be a privacy change or platform switch.
toolsUsed:
- wayback-machine
- exiftool
evidence: []
trust: trusted
relatedStrategies:
- phase-enrichment
- pivot-exif-and-chronolocation
- pivot-network-triangulation
- phase-reporting
tags:
- timeline
- enrichment
- chronolocation
source: ''
---

# Pattern: Timeline anchoring

## The move
Take every dated artifact you've gathered — posts, photos, check-ins, comments, last-seen indicators, EXIF and chronolocation times — and lay them on one chronological line. The timeline's most valuable point is its **last** one: the most recent moment you can confirm the subject was active. That last-known-activity is often the most actionable thing an investigation produces.

## Three things a timeline gives you
1. **Last-known-activity** — the freshest confirmed signal of life and, frequently, the freshest location. This is what an authority can act on.
2. **Routine** — recurring places, posting cadence, day/night rhythm. Deviation from routine is itself a signal.
3. **A consistency check** — and this is the underrated one. A timeline makes *contradictions* visible that prose hides: a "live" post that actually pre-dates the disappearance, two events that can't both be true, a location that can't coexist with another. A contradiction means a wrong selector or a different person has slipped in — the timeline catches it.

## Date the artifact, not the display
The biggest trap is trusting a surface "date." A post can be a **repost**, a **scheduled** publish, or an old photo **re-shared** today. Before a point earns a recent slot, confirm the artifact is genuinely recent. Likewise, **normalize timezones** before ordering — silent timezone mixing misplaces events and manufactures false contradictions. Inferred times (chronolocation, `[[pivot-exif-and-chronolocation]]`) go on the line softer than explicit post dates; mark the confidence.

## Where it feeds
Timeline anchoring is a core enrichment move (`[[phase-enrichment]]`) and is fed heavily by network triangulation (`[[pivot-network-triangulation]]`) — associates' posts are some of the best dated anchors for a private subject. The result flows straight into `[[phase-reporting]]` as the case's spine.

## A caution on gaps
A silence in the timeline is not automatically "missing since." It can be a privacy change, a platform switch, or just a quiet stretch. Treat a gap as a question, not a conclusion.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | enrichment |
| pivot | social-profile, image → geolocation |
| MP relevance | high |
| tools | wayback-machine, exiftool |
