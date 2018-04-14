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
    'announce_final_round',
    'dominating_levels',
    'join_team',
)


# =============================================================================
# >> CONFIGURATION
# =============================================================================
with GunGameConfigManager(info.name) as _config:

    with _config.cvar('announce_final_round', True) as announce_final_round:
        announce_final_round.add_text()

    with _config.cvar('join_team', True) as join_team:
        join_team.add_text()

    with _config.cvar('dominating_levels', 4) as dominating_levels:
        dominating_levels.add_text()
