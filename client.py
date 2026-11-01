# -*- coding: utf-8 -*-
"""
Personal Agent Ambient Noise Auditory Focus Masker Client
Zero-dependency acoustical Speech Intelligibility Index (SII) distraction auditor,
cognitive throughput degradation modeler, and colored noise masking soundscape synthesizer.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentAmbientNoiseAuditoryFocusMasker:
    """
    Audits environmental soundscapes, quantifies acoustic distraction from intelligible speech
    and variable noise, and calculates optimal colored noise masking curves (Pink/Brown noise).
    """

    def evaluate_acoustic_distraction_risk(
        self,
        ambient_dba: float,
        speech_presence_pct: float = 25.0,
        background_variability_db: float = 8.0
    ) -> Dict[str, Any]:
        """
        Evaluates cognitive performance degradation based on ambient decibel levels
        and speech intelligibility in the 500Hz-4000Hz conversational frequency bands.
        """
        dba = max(30.0, min(105.0, float(ambient_dba)))
        speech_pct = max(0.0, min(100.0, float(speech_presence_pct)))
        variability = max(1.0, min(30.0, float(background_variability_db)))

        # Speech Intelligibility Index (SII) proxy
        # Intelligible phonemes capture the phonological loop in working memory
        sii_factor = min(1.0, (speech_pct / 100.0) * (1.2 if 45.0 <= dba <= 75.0 else 0.8))

        # Cognitive distraction penalty (0 - 100 pts)
        # Steady noise has low distraction, but fluctuating intelligible speech is devastating
        speech_penalty = sii_factor * 60.0
        decibel_penalty = max(0.0, (dba - 55.0) * 1.1)
        fluctuation_penalty = variability * 1.5

        distraction_score = round(min(100.0, speech_penalty + decibel_penalty + fluctuation_penalty), 1)

        # Working memory throughput loss percentage
        memory_throughput_loss_pct = round(min(45.0, distraction_score * 0.42), 1)

        if distraction_score < 25.0:
            env_status = "Acoustic Flow Zone (Low distraction)"
            masking_need = "OPTIONAL: Natural silence or low-volume ambient soundscape."
        elif distraction_score < 60.0:
            env_status = "Moderate Acoustic Friction (Occasional attention hijacking)"
            masking_need = "RECOMMENDED: Pink noise masking to blanket intelligible syllables."
        else:
            env_status = "Severe Auditory Fragmentation (Active cognitive interference)"
            masking_need = "CRITICAL: Brown/Pink noise masking or active noise cancelling headphones required."

        return {
            "ambient_sound_level_dba": dba,
            "speech_presence_percentage": speech_pct,
            "sound_variability_db": variability,
            "distraction_risk_score": f"{distraction_score} / 100",
            "working_memory_throughput_penalty": f"-{memory_throughput_loss_pct}% capacity",
            "acoustic_environment_status": env_status,
            "masking_intervention_urgency": masking_need
        }

    def synthesize_colored_noise_masking_profile(
        self,
        ambient_dba: float,
        target_work_type: str = "deep_coding"
    ) -> Dict[str, Any]:
        """
        Synthesizes optimal spectral masking profile (Pink Noise vs. Brown Noise) and
        calculates target masking sound pressure level (dBA) for hearing safety.
        """
        dba = max(35.0, min(95.0, float(ambient_dba)))
        work = str(target_work_type).lower()

        # Optimal masking level is typically 3-5 dBA above ambient, capped at 70 dBA for OSHA/WHO safety
        target_masking_dba = round(min(70.0, max(50.0, dba + 3.5)), 1)

        # Spectral slope selection:
        # Brown noise (-6 dB / octave, 1/f^2): Deep rumble, excellent for masking high-friction coding
        # Pink noise (-3 dB / octave, 1/f): Equal energy per octave, ideal for linguistic/reading flow
        # White noise (0 dB / octave): Harsh, rarely recommended for prolonged neuro-focus
        if "read" in work or "writ" in work or "linguistic" in work:
            noise_type = "Pink Noise (1/f Spectrum)"
            spectral_slope = "-3.0 dB / octave"
            rationale = "Pink noise balances high and low frequencies, harmonizing the phonological loop during reading and writing."
        elif "anxiet" in work or "calm" in work:
            noise_type = "Brownian Noise (1/f^2 Spectrum)"
            spectral_slope = "-6.0 dB / octave"
            rationale = "Deeper acoustic warmth suppresses sympathetic nervous system arousal and soothes tinnitus."
        else:
            noise_type = "Brownian / Deep Pink Hybrid"
            spectral_slope = "-4.5 dB / octave"
            rationale = "Low-frequency attenuation absorbs keyboard clatter and distant chatter while facilitating sustained algorithmic reasoning."

        # Maximum safe daily continuous headphone exposure (WHO standard: 75 dBA safe for 8 hours)
        if target_masking_dba <= 65.0:
            safe_exposure_hours = 8.0
        elif target_masking_dba <= 70.0:
            safe_exposure_hours = 6.0
        else:
            safe_exposure_hours = 3.0

        return {
            "recommended_noise_color": noise_type,
            "spectral_energy_slope": spectral_slope,
            "target_masking_sound_level_dba": target_masking_dba,
            "hearing_conservation_safety_cap_hours": safe_exposure_hours,
            "neuroacoustic_rationale": rationale,
            "headphone_protocol": f"Set playback volume to exactly {target_masking_dba} dBA. Take 5-minute ear rests every 90 minutes."
        }
