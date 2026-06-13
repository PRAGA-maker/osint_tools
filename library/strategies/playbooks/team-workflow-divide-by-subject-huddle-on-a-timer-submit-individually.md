---
id: team-workflow-divide-by-subject-huddle-on-a-timer-submit-individually
name: 'Team workflow: divide by subject, huddle on a timer, submit individually'
description: Use when Any multi-person investigation with several subjects and a fixed time window.
type: playbook
summary: The highest-performing teams split the subjects across members and let each person investigate deeply until they hit a wall, rather than swarming one subject or hopping around. Roles align to specialties (social media, breach data, web recon, geolocation). The team regroups in short huddles roughly every 60 minutes to share theories and redirect, but each member submits their own findings rather than funneling everything through one bottleneck person. Keep one shared comms/coordination surface (Discord/Slack) but avoid over-engineered tracking systems that slow people down.
missingPersonsRelevance: high
phase: intake
steps:
- Split subjects among members; assign roles by specialty (social, breach, web, geo).
- Have each member investigate their subject deeply until hitting a wall.
- Run a short team huddle roughly hourly to share theories and reallocate effort.
- Let each member submit their own discoveries (no single submission bottleneck).
- Use one shared comms channel; avoid heavyweight tracking tools that bottleneck flow.
- Take periodic breaks to stay sharp across long events.
signals:
- Members are productive in parallel with little duplicated work
- Hourly huddles redirect a stuck member to a fresh angle
pitfalls:
- Everyone piling onto one subject
- Centralizing all submissions through one person (bottleneck)
- Over-engineering with Trello/Sheets that slow people down
- Skipping huddles so the team drifts onto dead ends
toolsUsed:
- Discord
- Slack
tags:
- teamwork
- coordination
- workflow
- division-of-labor
evidence:
- type: writeup
  url: https://shandyman.online/blog/on-a-mission-a-tracelabs-ctf-missing-persons-writeup/
  note: Divide 8 MPs; team huddles every 60 minutes; individual submission beats central bottleneck; abandoned Trello after an hour
- type: writeup
  url: https://www.aaroncti.com/trace-labs-august-2020/
  note: Discord voice + link/image sharing for collaborative decisions
- type: writeup
  url: https://jack.bio/blog/tracelabs
  note: Division of labor by missing person with central cross-verification
trust: community
source: searchparty-writeups
---

# Team workflow: divide by subject, huddle on a timer, submit individually

> The highest-performing teams split the subjects across members and let each person investigate deeply until they hit a wall, rather than swarming one subject or hopping around. Roles align to specialties (social media, breach data, web recon, geolocation). The team regroups in short huddles roughly every 60 minutes to share theories and redirect, but each member submits their own findings rather than funneling everything through one bottleneck person. Keep one shared comms/coordination surface (Discord/Slack) but avoid over-engineered tracking systems that slow people down.

**When to use:** Any multi-person investigation with several subjects and a fixed time window.

## Steps
- Split subjects among members; assign roles by specialty (social, breach, web, geo).
- Have each member investigate their subject deeply until hitting a wall.
- Run a short team huddle roughly hourly to share theories and reallocate effort.
- Let each member submit their own discoveries (no single submission bottleneck).
- Use one shared comms channel; avoid heavyweight tracking tools that bottleneck flow.
- Take periodic breaks to stay sharp across long events.

## Signals it's working
- Members are productive in parallel with little duplicated work
- Hourly huddles redirect a stuck member to a fresh angle

## Pitfalls
- Everyone piling onto one subject
- Centralizing all submissions through one person (bottleneck)
- Over-engineering with Trello/Sheets that slow people down
- Skipping huddles so the team drifts onto dead ends

**Tools:** Discord, Slack

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
