from collections.abc import Mapping
from typing import Any

from BaseClasses import MultiWorld, Item, Tutorial
from worlds.AutoWorld import World, WebWorld

# Imports of your world's files must be relative.
from . import Locations, Items, Options, Regions


class InStarsAndTimeWeb(WebWorld):
    # Theres a few different themes so have fun with it
    theme = "grassFlowers"

    # You shouldnt have to change much here except the name at the bottom!
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

    item_name_to_id = Items.item_table
    location_name_to_id = Locations.location_table
    options_dataclass = Options.InStarsAndTimesOptions

    origin_region_name = "Dormont"

    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)

    def create_items(self) -> None:
        itempool: list[Item] = [
            self.create_item("Reminder Note"),
            self.create_item("Drawing"),
            self.create_item("Loop's Coin")
        ]

        self.multiworld.itempool += itempool


    # Our world class must also have a create_item function that can create any one of our items by name at any time.
    # We also put this in a different file, the same one that create_items is in.
    def create_item(self, name: str) -> Items.InStarsAndTimeItem:
        return Items.create_item_with_correct_classification(self, name)


    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "death_link", "death_link_amnesty", "starting_craft", "music_rando", "enemy_rando", "troop_rando"
        )
