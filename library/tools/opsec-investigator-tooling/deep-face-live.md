---
id: deep-face-live
name: Deep Face Live
description: Use when you have a puppet `face`/`image` and want a real-time face swap on webcam or video calls to protect your own identity — returns a synthetic on-camera `face`.
url: https://github.com/iperov/DeepFaceLive
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Disguising the investigator's own face on live video calls or streams during undercover contact.
selectorsIn:
- face
- image
selectorsOut:
- face
status: degraded
pricing: free
costNote: Free and open-source (GPL-3.0), pre-built portable Windows releases; requires a capable GPU. Repo archived (read-only) Nov 2024 but downloads still work.
opsec: passive
opsecNote: This is a defensive/own-opsec tool — it alters YOUR outbound camera feed, it does not touch the target. Never present a swapped face as a real person's likeness (impersonation/fraud risk); use it only to avoid disclosing your true face during authorised undercover work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: unverified
trustNote: Community deepfake project (iperov); archived and unmaintained. Vet the binary and run it isolated — no data-quality guarantees.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- DeepFaceLive
tags:
- Sock Puppets
- opsec
- deepfake
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Deep Face Live

> Real-time GPU face-swap for webcam and video-call feeds — an investigator sock-puppet/opsec tool for hiding your own face, not a people-finder.

## When to use
You must appear on live video (a video call, a stream, an undercover contact) during an authorised investigation and need to avoid exposing your real face. DeepFaceLive substitutes a chosen puppet face onto your camera feed in real time. It surfaces **no** intelligence about a target — it only protects the operator.

## How to use it (`bestInteractionPattern`: desktop-app)
1. On a Windows machine with a DirectX12 GPU (RTX 2070 / RX 5700 XT class or better), download a portable release from the GitHub releases page.
2. Extract and launch the app; select your webcam as the input device.
3. Load a pre-trained model or a still `image`/`face` (Insight-face mode) as the swap source.
4. Route the app's virtual-camera output into your call/stream software (Zoom, OBS, etc.).
5. There is no pivot into other selectors — output is only your disguised live `face`.

## Inputs → Outputs
- **In:** a puppet `face` or source `image`, plus your live webcam feed
- **Out:** a real-time face-swapped video `face` on your virtual camera
- **Empty/negative result looks like:** poor GPU → dropped frames / no swap; the app simply passes your real face through, which is an opsec failure, not a silent success.

## Gotchas & OpSec
- Repo is **archived/unmaintained** (status: degraded) — no updates or security fixes; sandbox the binary.
- Windows + strong GPU only; unusable on low-end or headless hosts.
- OpSec/legal: using a swapped face to impersonate a real, identifiable person can constitute fraud. Keep it to concealment, never impersonation.

## Overlaps ("do both")
- Complements sock-puppet identity kits and virtual-camera setups; use alongside a separate persona (name, backstory) rather than as your whole cover.

## Trust & verifiability
`trust: unverified` — community deepfake tooling, now archived. Its "output" is your own feed, so the only thing to verify is that the swap actually engages before you go live.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deep-face-live |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | face, image → face |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
