# ../gungame/plugins/custom/gg_teamplay_sounds/gg_teamplay_sounds.py

"""Play team based sounds for TeamPlay."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from events import Event
from events.hooks import EventAction, PreEvent
from listeners.tick import Delay
from players.teams import teams_by_number

# GunGame
from gungame.core.players.dictionary import player_dictionary
from gungame.core.plugins.manager import gg_plugin_manager
from gungame.core.sounds.hooks import SoundHook
from gungame.core.sounds.manager import sound_manager
from gungame.core.teams import team_levels
from gungame.core.weapons.manager import weapon_order_manager

# Plugin
from .configuration import announce_final_round, dominating_levels, join_team

# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
GAME_START_REASON = 15


# =============================================================================
# >> GAME EVENTS
# =============================================================================
@Event("round_start")
def _round_start(game_event):
    """Play the "final round" sound, if it's the final round."""
    levels = set(team_levels.values())
    if (
        "gg_teamplay" not in gg_plugin_manager or
        not announce_final_round.get_bool() or
        len(levels) != 1 or
        list(levels)[0] != weapon_order_manager.max_levels
    ):
        return EventAction.CONTINUE

    from gungame.plugins.included.gg_teamplay.manager import teamplay_manager
    if teamplay_manager.current_module == "deathmatch":
        return EventAction.CONTINUE

    from gungame.plugins.included.gg_teamplay.manager import team_dictionary
    instances = team_dictionary.values()
    current_multi_kills = {team.multi_kill for team in instances}
    if len(current_multi_kills) != 1:
        return EventAction.CONTINUE

    if list(current_multi_kills)[0] + 1 == list(instances)[0].level_multi_kill:
        Delay(
            delay=1,
            callback=sound_manager.play_sound,
            args=("teamplay_final_round",),
        )
        return EventAction.STOP_BROADCAST

    return EventAction.CONTINUE


@Event("player_team")
def _join_team(game_event):
    """Play the appropriate join team sound."""
    if not join_team.get_bool():
        return

    team = game_event["team"]
    if team not in team_levels:
        return

    player = player_dictionary[game_event["userid"]]
    Delay(
        delay=1,
        callback=player.play_gg_sound,
        args=(f"teamplay_join_team_{teams_by_number[team]}",),
    )


# =============================================================================
# >> GUNGAME EVENTS
# =============================================================================
@Event("gg_team_level_up")
def _team_level_up(game_event):
    """Play the appropriate team level-up sound."""
    scoring_team = game_event["team"]
    if scoring_team not in team_levels:
        return

    current_level = team_levels[scoring_team]
    opposing_level = team_levels[5 - scoring_team]
    suffix = teams_by_number[scoring_team]
    if current_level < opposing_level:
        sound = "levelup"
    elif current_level == opposing_level:
        sound = "ties"
    elif current_level == opposing_level + 1:
        sound = "takes_lead"
    elif current_level < opposing_level + dominating_levels.get_int():
        sound = "increases_lead"
    else:
        sound = "dominating"
    Delay(
        delay=1,
        callback=sound_manager.play_sound,
        args=(f"teamplay_{sound}_{suffix}",),
    )


# =============================================================================
# >> SOUND HOOKS
# =============================================================================
@SoundHook("level_up")
def _suppress_level_up_sound(sound_name):
    """Stop level-up sound from playing at the same time as other sounds."""
    return False


# =============================================================================
# >> PRE-EVENTS
# =============================================================================
@PreEvent("round_end")
def _stop_broadcast(game_event):
    """Stop round_end from broadcasting to clients causing round end sounds."""
    if game_event["reason"] != GAME_START_REASON:
        return EventAction.STOP_BROADCAST

    return EventAction.CONTINUE
