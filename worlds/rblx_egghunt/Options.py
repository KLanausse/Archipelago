from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink, OptionGroup

@dataclass
class RobloxEggHuntOptions(PerGameCommonOptions):
    death_link: DeathLink

OPTION_GROUPS = [
    OptionGroup("Game Options", []),
    OptionGroup("Death Link", [DeathLink]),
]

option_presets = {
    "Default": {
        "death_link": True
    }
}