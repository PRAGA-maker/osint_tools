---
id: alerting-the-subject
name: antipattern-alerting-the-subject
description: Use as a hard guardrail around the SILENT ways platforms tip off the subject — story views, read receipts, follow-suggestion (PYMK) leakage — which alert the target even when you never click a single button.
type: antipattern
phase: opsec
pivotFrom: [social-profile, any]
pivotTo: [any]
summary: Alerting the subject is the passive-looking cousin of overt contact. You never follow, message, or friend — but the platform still tells the target you were there, through story/Reel view lists, "seen" read receipts, profile-view notifications, and "People You May Know" / contact-graph suggestions that surface YOU to THEM or THEM to you. These leaks fire from a real or weakly-separated account during ordinary browsing. In a missing-persons case, tipping off someone who is hiding can drive them further off-grid or, if a bad actor is involved, escalate danger — so the harm lands on the vulnerable person, not on you.
missingPersonsRelevance: high
whenToUse: Before and during any logged-in viewing of the subject or their network — assume the platform is broadcasting your presence unless you've proven otherwise.
steps:
  - Enumerate the leak surfaces for the platform you're on — story/Reel views, read receipts, "viewed your profile", PYMK/contact-graph — BEFORE you browse.
  - Never view stories/Reels or open messages from a research account that could match into the subject's graph.
  - Strip the account's contact-graph footing — no uploaded contacts, no phone tied to the subject's circle, so PYMK can't cross-suggest.
  - Default to logged-out or cached/archived views where the platform can't attribute the visit.
  - If a leak may have fired, LOG it so downstream reasoning accounts for a possibly-alerted subject.
signals:
  - You completed the viewing with zero artifacts that could appear in any view-list, receipt, or suggestion feed on the target side.
  - Your research account has no contact-graph or mutual path that could surface it in the subject's PYMK.
pitfalls:
  - "Just glancing at their story" — story/Reel view lists name you instantly.
  - Opening a DM thread to read it — the "seen" receipt tells them you read it.
  - Browsing from an account whose uploaded contacts or phone number put you in the subject's "People You May Know".
  - Assuming "I didn't click anything" means you're invisible — passive viewing still emits signals.
toolsUsed: [sock-puppet-generator]
evidence: []
trust: trusted
relatedStrategies: [antipattern-contaminating-the-subject, Passive-only reconnaissance with sock puppets and no subject contact, Build clean sock-puppet accounts that look normal, phase-opsec]
tags: [opsec, safety, contamination, sensitive, passive-recon]
source: ""
---

# Antipattern: Alerting the subject

## The tempting wrong move
You're being careful — you'd never follow or message. But you tap their story to see what's there, you open the DM thread to read it, you browse their profile from your research login. No buttons pressed that say "contact." You feel passive.

## Why it fails — the platform contacts them for you
`[[antipattern-contaminating-the-subject]]` covers the overt actions; this one is about the **silent** leaks, which are easier to miss precisely because you didn't *do* anything obvious:

- **Story / Reel view lists** put your account name in a list the owner can read. Viewing is not passive on these surfaces.
- **Read / "seen" receipts** tell the target the moment you open a thread.
- **"Viewed your profile" notifications** name visitors on some platforms.
- **"People You May Know" / contact-graph matching** can surface *you* in the subject's suggestions — or *them* in yours — from an account whose contacts or phone number touch their circle, with no action on your part at all.

In a missing-persons case the cost is not a wasted hour. Alert someone who is deliberately hiding and they go further off-grid; tip off a situation with a bad actor and you may escalate the danger. The harm lands on the vulnerable person.

## The fix: assume broadcast, then prove silence
1. **Map the leaks first.** Before browsing, know which surfaces on this platform emit signals — views, receipts, profile-view, PYMK — and avoid them.
2. **Prefer attribution-free views.** Logged-out browsing and cached/archived copies can't be tied to you. When login is unavoidable, use a clean sock puppet (`[[Build clean sock-puppet accounts that look normal]]`) with no contact-graph footing in the subject's network — a puppet that views a story still names the puppet.
3. **Never open stories, Reels, or message threads** of the subject or close associates from any attributable account.
4. **Log a slip.** If a leak may have fired, record it so the rest of the case assumes a possibly-alerted subject. This is the standing posture of `[[Passive-only reconnaissance with sock puppets and no subject contact]]`.

## Tell
If you have to wonder "could this show up on their side?", treat the answer as yes and don't. "I didn't click anything" is not the bar — *zero detectable artifacts* is. The `[[phase-opsec]]` rule holds: look without being seen looking.

---
## Metadata
| field | value |
|---|---|
| type | antipattern |
| phase | opsec |
| MP relevance | high |
| related | antipattern-contaminating-the-subject, phase-opsec |
