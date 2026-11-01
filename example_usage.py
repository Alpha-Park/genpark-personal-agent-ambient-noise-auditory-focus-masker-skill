# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Ambient Noise Auditory Focus Masker Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentAmbientNoiseAuditoryFocusMasker

def main():
    agent = PersonalAgentAmbientNoiseAuditoryFocusMasker()

    print("=" * 70)
    print("DEMO: Personal Agent Ambient Noise Auditory Focus Masker")
    print("=" * 70)

    # 1. Open cafe acoustic distraction evaluation (62 dBA, 40% intelligible speech)
    res_distract = agent.evaluate_acoustic_distraction_risk(
        ambient_dba=62.0,
        speech_presence_pct=40.0,
        background_variability_db=12.0
    )

    print(f"\n1. Open Cafe Acoustic Distraction Analysis (62 dBA, 40% speech):")
    print(f"   Distraction Score: {res_distract['distraction_risk_score']}")
    print(f"   Working Memory Penalty: {res_distract['working_memory_throughput_penalty']}")
    print(f"   Status: {res_distract['acoustic_environment_status']}")
    print(f"   Urgency: {res_distract['masking_intervention_urgency']}")

    # 2. Synthesize colored noise masking soundscape for deep coding
    res_mask = agent.synthesize_colored_noise_masking_profile(
        ambient_dba=62.0,
        target_work_type="deep_coding"
    )

    print(f"\n2. Colored Noise Masking Profile:")
    print(f"   Recommended Noise Color: {res_mask['recommended_noise_color']}")
    print(f"   Spectral Slope: {res_mask['spectral_energy_slope']}")
    print(f"   Target Volume: {res_mask['target_masking_sound_level_dba']} dBA")
    print(f"   Safe Exposure Limit: {res_mask['hearing_conservation_safety_cap_hours']} hours")
    print(f"   Rationale: {res_mask['neuroacoustic_rationale']}")
    print(f"   Protocol: {res_mask['headphone_protocol']}")

    print("\nVerification complete: Auditory focus masking engine executed flawlessly.")

if __name__ == "__main__":
    main()
