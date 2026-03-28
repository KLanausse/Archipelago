from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink, OptionGroup


class StartingCraft(Choice):
    """Dictates what craft skills you start with."""
    display_name = "Starting Craft"
    option_all = 0
    option_none = 1
    default = 0


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
    Randomize groups of enemys. Unimplemented.
    """

    display_name = "Troop Randomizer"

# Taken from V6's options
class DeathLinkAmnesty(Range):
    """Amount of Deaths to take before sending a DeathLink signal, for balancing difficulty."""
    display_name = "Death Link Amnesty"
    range_start = 1
    range_end = 30
    default = 5

class UnavoidableDeaths(Toggle):
    """Lets unavoidable deaths trigger Death Link."""
    display_name = "Unavoidable Deaths"

class SkipIntro(Toggle):
    """Skips the intro cutscene."""
    display_name = "Skip Intro"

@dataclass
class InStarsAndTimesOptions(PerGameCommonOptions):
    death_link: DeathLink
    unavoidable_deaths: UnavoidableDeaths
    death_link_amnesty: DeathLinkAmnesty
    starting_craft: StartingCraft
    music_rando: MusicRando
    enemy_rando: EnemyRando
    troop_rando: TroopRando
    skip_intro: SkipIntro

OPTION_GROUPS = [
    OptionGroup("Game Options", [StartingCraft, MusicRando, EnemyRando, SkipIntro]),
    OptionGroup("Death Link", [DeathLink, DeathLinkAmnesty, UnavoidableDeaths]),
    OptionGroup("Unimplemented Stubs", [TroopRando])
]

option_presets = {
    "Death For All": {
        "death_link": True,
        "unavoidable_deaths": True,
        "death_link_amnesty": 1,
        "starting_craft": StartingCraft.option_none,
        "music_rando": True,
        "enemy_rando": True,
        "troop_rando": True,
        "skip_intro": True
    }
}