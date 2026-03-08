from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink


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
    Randomize groups of enemys.
    """

    display_name = "Troop Randomizer"


@dataclass
class InStarsAndTimesOptions(PerGameCommonOptions):
    death_link: DeathLink
    starting_craft: StartingCraft
    music_rando: MusicRando
