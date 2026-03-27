from collections.abc import Mapping
from typing import Any, Dict

from BaseClasses import MultiWorld, Item, Tutorial
from worlds.AutoWorld import World, WebWorld

# Imports of your world's files must be relative.
from . import Locations, Items, Options, Regions, Rules, Music, Enemies


class InStarsAndTimeWebWorld(WebWorld):
    theme = "grassFlowers"

    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up In Stars And Time for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Lanausse"]
    )]

    option_groups = Options.OPTION_GROUPS

class InStarsAndTimeWorld(World):
    game = "In Stars And Time"
    web = InStarsAndTimeWebWorld()

    item_name_to_id = Items.ITEM_TABLE
    location_name_to_id = Locations.LOCATION_TABLE
    options_dataclass = Options.InStarsAndTimesOptions
    options: Options.InStarsAndTimesOptions

    origin_region_name = "Dormont"

    bgm_map = Dict[str, str]
    #sfx_map = Dict[str, str]
    enemy_map = Dict[str, str]
    troop_map = Dict[str, str]

    def generate_basic(self) -> None:
        Music.randomize_music(self)
        Enemies.randomize_enemies(self)
        Enemies.randomize_troops(self)

    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)

    # Item Creation Funcs
    def create_items(self) -> None:
        Items.create_all_items(self)

    def create_item(self, name: str) -> Items.InStarsAndTimeItem:
        return Items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)

    def set_rules(self) -> None:
        Rules.set_all_rules(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "death_link": self.options.death_link.value,
            "death_link_amnesty": self.options.death_link_amnesty.value,
            "starting_craft": self.options.starting_craft.value,
            "music_rando": self.bgm_map,
            "enemy_rando": self.enemy_map,
            "troop_rando": self.troop_map,
        }
