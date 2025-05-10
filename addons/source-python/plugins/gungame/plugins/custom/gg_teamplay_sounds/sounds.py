# ../gungame/plugins/custom/gg_teamplay_sounds/sounds.py

"""Register sounds for gg_teamplay_sounds."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame
from gungame.core.sounds.manager import sound_manager

# =============================================================================
# >> SOUND REGISTRATION
# =============================================================================
sound_manager.register_sound(
    sound_name="teamplay_final_round",
    default="source-python/gungame/default/final_round.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_join_team_t",
    default="source-python/gungame/default/red_team.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_join_team_ct",
    default="source-python/gungame/default/blue_team.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_levelup_t",
    default="source-python/gungame/default/red_round.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_levelup_ct",
    default="source-python/gungame/default/blue_round.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_ties_t",
    default="source-python/gungame/default/red_scores.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_ties_ct",
    default="source-python/gungame/default/blue_scores.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_takes_lead_t",
    default="source-python/gungame/default/red_takes.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_takes_lead_ct",
    default="source-python/gungame/default/blue_takes.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_increases_lead_t",
    default="source-python/gungame/default/red_increase.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_increases_lead_ct",
    default="source-python/gungame/default/blue_increase.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_dominating_t",
    default="source-python/gungame/default/red_dominating.mp3",
)

sound_manager.register_sound(
    sound_name="teamplay_dominating_ct",
    default="source-python/gungame/default/blue_dominating.mp3",
)
