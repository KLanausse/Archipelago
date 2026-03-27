from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink, OptionGroup


class StartingCraft(Choice):
    """Dictates what craft skills you start with"""
    display_name = "Starting Craft"
    option_all = 0
    option_bestOne = 1
    option_none = 2
    default = 1


class MusicRando(Toggle):
    """
    Randomize the in-game music tracks.
    """

    display_name = "Music Randomizer"


class EnemyRando(Toggle):
    """
    Randomize individual enemys.
    """

    display_name = "Enemy Randomizer"


class TroopRando(Toggle):
    """
    Randomize groups of enemys. Unimplemented
    """

    display_name = "Troop Randomizer"

# Taken from V6's options
class DeathLinkAmnesty(Range):
    """Amount of Deaths to take before sending a DeathLink signal, for balancing difficulty"""
    display_name = "Death Link Amnesty"
    range_start = 1
    range_end = 30
    default = 5

# Taken from V6's options
class UnavoidableDeaths(Toggle):
    """Lets unavoidable deaths trigger Death Link"""
    display_name = "Unavoidable Deaths"


@dataclass
class InStarsAndTimesOptions(PerGameCommonOptions):
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty
    unavoidable_deaths: UnavoidableDeaths
    starting_craft: StartingCraft
    music_rando: MusicRando
    enemy_rando: EnemyRando
    troop_rando: TroopRando

OPTION_GROUPS = [
    OptionGroup("Game Options", [StartingCraft, MusicRando, EnemyRando]),
    OptionGroup("Death Link", [DeathLink, DeathLinkAmnesty, UnavoidableDeaths]),
    OptionGroup("Unimplemented Stubs", [TroopRando])
]