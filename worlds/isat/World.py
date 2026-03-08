from collections.abc import Mapping
from typing import Any

from BaseClasses import MultiWorld, Item, Tutorial
from worlds.AutoWorld import World, WebWorld

# Imports of your world's files must be relative.
from . import Locations, Items, Options


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

    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "death_link", "starting_craft"
        )
