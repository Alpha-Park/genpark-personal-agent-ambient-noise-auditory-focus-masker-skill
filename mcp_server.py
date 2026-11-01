# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Ambient Noise Auditory Focus Masker Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentAmbientNoiseAuditoryFocusMasker

mcp = FastMCP("PersonalAgentAmbientNoiseAuditoryFocusMasker")
client = PersonalAgentAmbientNoiseAuditoryFocusMasker()

@mcp.tool()
def evaluate_acoustic_distraction_risk(
    ambient_dba: float,
    speech_presence_pct: float = 25.0,
    background_variability_db: float = 8.0
) -> str:
    """Audits room sound pressure, speech intelligibility, and cognitive distraction penalty."""
    import json
    return json.dumps(client.evaluate_acoustic_distraction_risk(
        ambient_dba, speech_presence_pct, background_variability_db
    ), indent=2)

@mcp.tool()
def synthesize_colored_noise_masking_profile(
    ambient_dba: float,
    target_work_type: str = "deep_coding"
) -> str:
    """Synthesizes optimal Pink/Brown noise masking profile and safe decibel targets."""
    import json
    return json.dumps(client.synthesize_colored_noise_masking_profile(
        ambient_dba, target_work_type
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
