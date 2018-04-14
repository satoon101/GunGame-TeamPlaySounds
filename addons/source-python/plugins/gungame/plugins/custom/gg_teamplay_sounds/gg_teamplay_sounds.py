# ../gungame/plugins/custom/gg_teamplay_sounds/gg_teamplay_sounds.py

"""."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from events import Event
from events.hooks import EventAction, PreEvent

# GunGame
from gungame.core.players.dictionary import player_dictionary
from gungame.core.sounds.hooks import SoundHook
from gungame.core.sounds.manager import sound_manager
from gungame.core.teams import team_levels

# Plugin
from .configuration import announce_final_round, dominating_levels, join_team


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
_teams = {
    2: 't',
    3: 'ct',
}


# =============================================================================
# >> GAME EVENTS
# =============================================================================
@Event('round_start')
def _round_start(game_event):
    """Play the "final round" sound, if it's the final round."""
    if not announce_final_round.get_bool():
        return


@Event('player_team')
def _join_team(game_event):
    """Play the appropriate join team sound."""
    if not join_team.get_bool():
        return

    team = game_event['team']
    if team not in _teams:
        return

    player = player_dictionary[game_event['userid']]
    player.play_sound(f'teamplay_join_team_{_teams[team]}')


# =============================================================================
# >> GUNGAME EVENTS
# =============================================================================
@Event('gg_team_level_up')
def _team_level_up(game_event):
    """Play the appropriate team level-up sound."""
    scoring_team = game_event['team']
    if scoring_team not in _teams:
        return

    current_level = team_levels[scoring_team]
    opposing_level = team_levels[5 - scoring_team]
    suffix = _teams[scoring_team]
    if current_level < opposing_level:
        sound = 'levelup'
    elif current_level == opposing_level:
        sound = 'ties'
    elif current_level == opposing_level + 1:
        sound = 'takes_lead'
    elif current_level < opposing_level + dominating_levels.get_int():
        sound = 'increases_lead'
    else:
        sound = 'dominating'
    sound_manager.play_sound(f'teamplay_{sound}_{suffix}')


# =============================================================================
# >> SOUND HOOKS
# =============================================================================
@SoundHook('level_up')
def _suppress_level_up_sound(sound_name):
    """Stop level-up sound from playing at the same time as other sounds."""
    return False


# =============================================================================
# >> PRE-EVENTS
# =============================================================================
@PreEvent('round_end')
def _stop_broadcast(game_event):
    """Stop round_end from broadcasting to clients causing round end sounds."""
    if game_event['reason'] != 15:
        return EventAction.STOP_BROADCAST
