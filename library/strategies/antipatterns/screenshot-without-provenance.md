---
id: screenshot-without-provenance
name: antipattern-screenshot-without-provenance
description: Use as a guardrail at the moment of capture — a screenshot with no source URL, no capture date, and no integrity check is a picture, not evidence, and it can be worthless for the law-enforcement handoff.
type: antipattern
phase: reporting
pivotFrom: [any]
pivotTo: [document-id]
summary: A bare screenshot feels like proof, but a cropped image with no URL, no timestamp, and no integrity hash is unverifiable — a reviewer can't confirm where it came from, when it was true, or that it wasn't altered. Worse, the live source can change or be deleted before law enforcement reviews it, leaving you with an unsupported claim. In missing-persons work the whole point of capture is the handoff; evidence that a judge or detective can't authenticate gets discarded, and you lose the finding even though you "had" it.
missingPersonsRelevance: high
whenToUse: Every time you capture a finding you might submit, cite, or hand to law enforcement — get the provenance at the moment of capture, not later.
steps:
  - Capture the FULL context, not a crop — include the visible URL/address bar, the platform chrome, and the timestamp on the page.
  - Record the source URL and the exact capture date/time alongside the image, in the subject's reference timezone.
  - Prefer full-page capture (and an archival copy, e.g. Wayback "Save Page Now") over a phone-screen crop.
  - Add an integrity anchor — a file hash, an archive URL, or a tool that timestamps the capture — so alteration is detectable.
  - Write the one-line context: how you found it and why it matters, because raw data without context is not intelligence.
signals:
  - Your capture shows the URL, a readable timestamp, and you logged the date/time and a hash or archive link.
  - A later-deleted post is still fully documented and authenticatable from your evidence file.
pitfalls:
  - Cropping to just the post and losing the URL/timestamp that prove origin and date.
  - Relying on a live link that may 404 by the time it's reviewed.
  - No hash/archive, so there's no way to show the image wasn't edited.
  - Submitting a bare image with no note on how it was found or why it matters (gets rejected).
toolsUsed: [Nimbus Screenshot & Screen Video Recorder, Wayback Machine]
evidence: []
trust: trusted
relatedStrategies: [Capture full-page screenshots of every finding for the LE handoff, Export and preserve findings as you go for documentation and handoff, Document the workflow as a flowchart - context turns data into intelligence, phase-reporting, antipattern-misreading-timestamps-and-locale]
tags: [reporting, evidence, chain-of-custody, documentation, safety]
source: ""
---

# Antipattern: Screenshot without provenance

## The tempting wrong move
You find the post, hit screenshot, crop it to just the relevant part, and drop the image into your notes. It clearly shows what you saw — job done. You'll remember where it came from.

## Why it fails
A cropped image with no URL, no capture time, and no integrity check is a **picture, not evidence**. A reviewer looking at it can't answer the three questions that make it usable: *where did this come from, when was it true, and has it been altered?* Without those, it's an unsupported assertion. And the source is volatile — social posts get edited, locked, or deleted, often quickly, so by the time law enforcement reviews your report the live link may 404 and the only thing left is your unauthenticatable crop. In missing-persons work the entire purpose of capture is the **handoff**: a finding a judge or detective can't authenticate gets discarded, and you lose it even though you found it. "Information without context is not intelligence" (`[[Document the workflow as a flowchart - context turns data into intelligence]]`) — and a context-free screenshot is exactly that.

## The fix: provenance at the moment of capture
You can't reconstruct provenance later; capture it with the image:
1. **Full context, not a crop.** Include the visible URL/address bar, platform chrome, and the on-page timestamp. Prefer full-page capture (Nimbus-class tools) over a phone-screen crop — this is the discipline in `[[Capture full-page screenshots of every finding for the LE handoff]]`.
2. **Source URL + exact capture time**, logged beside the image in the subject's reference timezone (and mind `[[antipattern-misreading-timestamps-and-locale]]` when you record it).
3. **Integrity anchor.** A file hash, or an independent archival copy (Wayback "Save Page Now"), so any later alteration is detectable and the page survives deletion — the preservation point of `[[Export and preserve findings as you go for documentation and handoff]]`.
4. **The one-line why.** How you found it and why it matters, so it travels as intelligence, not raw data.

## Tell
If your capture can't answer "where, when, and is it unaltered?", it's not evidence yet. The bar isn't "I can see what it shows" — it's "a stranger reviewing this in six months can authenticate it." Capture provenance at the click, because the source may not be there when you need it. This is the `[[phase-reporting]]` standard.

---
## Metadata
| field | value |
|---|---|
| type | antipattern |
| phase | reporting |
| MP relevance | high |
| related | Capture full-page screenshots of every finding for the LE handoff, phase-reporting |
