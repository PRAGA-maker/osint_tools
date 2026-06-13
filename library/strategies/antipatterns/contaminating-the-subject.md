---
id: contaminating-the-subject
name: antipattern-contaminating-the-subject
description: Use as a hard guardrail before any action that touches the subject or their network — following, messaging, friending, or viewing from a real account tips them off and can endanger them.
type: antipattern
phase: opsec
pivotFrom: [any]
pivotTo: [any]
summary: Contaminating the subject is any action that crosses from passive observation into engagement that the target can detect — following, friending, liking, messaging, joining, story-viewing, adding a phone contact, or browsing from a real/linked account. In a missing-persons case the consequences are not academic: you can alert someone who is hiding, drive them further off-grid, endanger them if a bad actor is involved, or compromise a future law-enforcement approach. This is the most serious opsec failure because the harm lands on the vulnerable person, not on you.
missingPersonsRelevance: high
whenToUse: Before EVERY action — the check is "could the subject or their network detect this?".
steps:
  - Default to passive — assume any interactive action (follow/message/like/join/view) may notify the target.
  - Separate identities completely — never act from a real or subject-linked account; use a clean sock puppet only when login is unavoidable.
  - Watch the silent leaks — story/Reel view lists, "seen" receipts, profile-view notifications, "People You May Know", and contact-upload matching all expose you without an explicit action.
  - Never initiate contact — no DMs, calls, texts, friend/follow requests, or joining the subject's spaces; route any needed contact through the proper authority instead.
  - If you slip, log it — note the contaminating action so downstream reasoning accounts for a possibly-alerted subject.
signals:
  - Every action you've taken is one a passive observer could have taken — zero notifications generated on the target side.
  - Your research identity has no path back to your real identity or into the subject's network.
pitfalls:
  - "I'll just follow to see more" — the single most common contamination; it notifies the target instantly.
  - Logging in with your personal account to peek — view receipts and PYMK graphs leak you.
  - Adding the subject's phone number to contacts to check a messaging app — can surface you to them.
  - Engaging an ASSOCIATE — following/messaging someone in the network ripples straight to the subject.
toolsUsed: [sock-puppet-generator]
evidence: []
trust: trusted
relatedStrategies: [phase-opsec, pivot-phone-to-identity, pivot-network-triangulation, phase-reporting]
tags: [opsec, safety, contamination, sensitive]
source: ""
---

# Antipattern: Contaminating the subject

## The tempting wrong move
You're deep in a profile and you hit a wall — the next posts are friends-only, the story looks relevant, the messaging app might confirm the number. So you do the small thing: follow, send a request, add the contact, "just message to ask." It feels minor and helpful. It is neither.

## Why it fails — and who it harms
Every one of those actions can be **detected by the target**, and the cost lands on the most vulnerable party. Alert someone who is deliberately hiding and they go further off-grid. Tip off a situation involving a bad actor and you may put the subject in danger. Surface yourself to the target and you can compromise a future law-enforcement approach. Unlike most antipatterns, the failure here isn't a wasted hour — it's **harm to a real, vulnerable person**. That's why it's an opsec hard line, not a style preference.

## The silent leaks people forget
Contamination isn't only deliberate contact. Platforms leak the *observer*:
- **Story / Reel view lists** and **"seen" receipts** name you.
- **Profile-view notifications** ("who viewed your profile").
- **"People You May Know" / contact-graph** matching can put *you* in the subject's suggestions — or surface *them* in yours — especially from a real or weakly-separated account.
- **Uploading a phone number** to check a messaging app can match you into the target's contacts.

Browsing from your personal account is contamination even if you never click anything.

## The fix
1. **Passive by default.** Assume any interactive action notifies the target. The whole tree is built around contactless pivots precisely so you never need to cross this line.
2. **Clean separation.** When login is unavoidable, use a sock puppet with no path back to you and no overlap with the subject's network. The puppet protects *your* identity; it does **not** license you to follow or message — a puppet that follows the subject is still contamination.
3. **Never initiate contact** — not the subject, not an associate. The network ripples: messaging a friend reaches the subject (`[[pivot-network-triangulation]]`). Any genuine need to contact goes through the **proper authority**, per `[[phase-reporting]]`.

## Tell
If you're about to take an action and have to wonder "will they see this?", the answer is treat it as yes — and don't. The correct posture is the one in `[[phase-opsec]]`: look without touching.

---
## Metadata
| field | value |
|---|---|
| type | antipattern |
| phase | opsec |
| MP relevance | high |
| related | phase-opsec, pivot-network-triangulation |
