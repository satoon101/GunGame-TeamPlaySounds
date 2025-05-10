# ../gungame/plugins/custom/gg_teamplay_sounds/configuration.py

"""Creates the gg_teamplay_sounds configuration."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame
from gungame.core.config.manager import GunGameConfigManager

# Plugin
from .info import info

# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    "announce_final_round",
    "dominating_levels",
    "join_team",
)


# =============================================================================
# >> CONFIGURATION
# =============================================================================
with (
    GunGameConfigManager(info.name) as _config,
    _config.cvar("announce_final_round", 1) as announce_final_round,
    _config.cvar("join_team", 1) as join_team,
    _config.cvar("dominating_levels", 4) as dominating_levels,
):
    announce_final_round.add_text()
    join_team.add_text()
    dominating_levels.add_text()
