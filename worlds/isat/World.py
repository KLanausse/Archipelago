from collections.abc import Mapping
from typing import Any

from BaseClasses import MultiWorld, Item, Tutorial
from worlds.AutoWorld import World, WebWorld

# Imports of your world's files must be relative.
from . import Locations, Items, Options, Regions, Rules


class InStarsAndTimeWeb(WebWorld):
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

class InStarsAndTimeWorld(World):
    game = "In Stars And Time"

    item_name_to_id = Items.ITEM_TABLE
    location_name_to_id = Locations.LOCATION_TABLE
    options_dataclass = Options.InStarsAndTimesOptions

    origin_region_name = "Dormont"

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
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "death_link", "death_link_amnesty", "starting_craft", "music_rando", "enemy_rando", "troop_rando"
        )
