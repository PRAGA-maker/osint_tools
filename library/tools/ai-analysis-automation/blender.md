---
id: blender
name: Blender
description: Use when you have `image`s/video of a place and want to reconstruct or test its 3D geometry — returns modeled scenes and sun/shadow simulations to verify `geolocation`.
url: https://www.blender.org/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building 3D reconstructions and sun/shadow simulations to verify locations, sightlines, and event geometry.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open-source (GPL); cross-platform desktop application, no account.
opsec: passive
opsecNote: "Blender runs entirely offline on your machine — reconstructing a scene from imagery you already have touches no target and leaks nothing. It's analyst-side tooling; the only OpSec note is standard evidence hygiene (work on copies, keep source imagery's chain of custody)."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Blender is a mature, widely-used open-source 3D suite (Blender Foundation) featured in the Bellingcat toolkit; it's a modeling tool, so conclusions depend on how faithfully you build the scene.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Blender 3D
- blender.org
tags:
- bellingcat-toolkit
- data-organization-analysis
- 3d-reconstruction
- geolocation
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Blender

> An open-source 3D suite that investigators use to reconstruct scenes and simulate sun position/shadows — a way to test whether an `image` is consistent with a claimed place and time.

## When to use
You have photos/video of a location and need to verify geometry that flat imagery can't settle: does a building's height/shadow match the claimed date and `geolocation`? Are two views consistent with the same 3D space? Blender's sun-position add-on and modeling tools let you reconstruct the scene and check shadows, sightlines, and camera positions (the Bellingcat "shadow analysis"/3D-reconstruction workflow). Specialist verification tooling, so low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Blender from https://www.blender.org/ (Windows/macOS/Linux).
2. Model the scene: place reference geometry (buildings, terrain) from imagery, map coordinates, and set scale.
3. Enable the Sun Position add-on; set the `geolocation` (lat/long) and the claimed date/time to cast accurate shadows.
4. Compare simulated shadows/sightlines against the photo — a mismatch challenges the claimed time or place; a match corroborates it.
5. Import DEM/terrain or drone imagery for landscape reconstructions; export annotated renders as evidence.

## Inputs → Outputs
- **In:** `image`/video of a scene + candidate `geolocation`/date
- **Out:** 3D reconstruction, sun/shadow simulation supporting or refuting a `geolocation`/timestamp
- **Empty/negative result looks like:** an inconclusive model — insufficient reference points or ambiguous geometry mean you can't confirm or refute; that's a limit of the inputs, not a finding.

## Gotchas & OpSec
- Conclusions are only as good as your model — wrong scale, coordinates, or reference geometry produces confident but false results. Document your assumptions.
- Steep learning curve; the sun/shadow method requires accurate lat/long and date/time to be meaningful.
- It's a modeling tool, not a measurement device — treat outputs as corroboration alongside other evidence, not proof on their own.

## Overlaps ("do both")
- Pairs with mapping/satellite tools like [[nasa-firms]] and general geolocation workflows — maps/imagery establish the candidate location, Blender tests the 3D/shadow consistency. Use SunCalc-type tools for a quick shadow check before committing to a full Blender build.

## Trust & verifiability
`trust: trusted` — a mature, transparent open-source suite; reliability rests on your modeling rigor, so publish your reference points and assumptions so others can reproduce the reconstruction.
