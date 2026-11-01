---
name: genpark-personal-agent-ambient-noise-auditory-focus-masker-skill
version: "1.0.0"
description: "Zero-dependency acoustical Speech Intelligibility Index (SII) distraction auditor, cognitive throughput degradation modeler, and colored noise masking soundscape synthesizer."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Ambient Noise Auditory Focus Masker Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI agents to protect human working memory from acoustical interference, quantify conversational distraction penalties, and synthesize safe colored noise masking profiles (Pink and Brownian noise).

## Agent In-Context Capabilities

- **Speech Intelligibility Index (SII) Distraction Audit**: Detects and penalizes intelligible phonemes (500Hz-4000Hz) that capture the brain's phonological loop.
- **Spectral Energy Slope Tailoring**: Recommends exact 1/f (-3 dB/octave) Pink noise or 1/f^2 (-6 dB/octave) Brown noise based on cognitive workload.
- **Hearing Conservation Enforcement**: Caps sound masking pressure levels to WHO/OSHA safe exposure thresholds.

## Tools Summary

1. `evaluate_acoustic_distraction_risk`: Assesses dBA, speech frequency, and working memory throughput penalties.
2. `synthesize_colored_noise_masking_profile`: Calculates target masking volume and optimal spectral color.
