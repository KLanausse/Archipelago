from collections.abc import Mapping
from typing import Any, Dict

from BaseClasses import MultiWorld, Item, Tutorial
from worlds.AutoWorld import World, WebWorld


from . import Locations, Items, Options, Regions

class RobloxEggHuntWorld(World):
    """
    Placeholder.
    """
    game = "Roblox Egg Hunt"

    item_name_to_id = Items.ITEM_TABLE
    location_name_to_id = Locations.LOCATION_TABLE
    options_dataclass = Options.RobloxEggHuntOptions
    options: Options.RobloxEggHuntOptions

    origin_region_name = "Spawn"

    def generate_basic(self) -> None:
        pass

    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)

        # Item Creation Funcs

    def create_items(self) -> None:
        Items.create_all_items(self)

    def create_item(self, name: str) -> Items.RobloxEggHuntItem:
        return Items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)

    def set_rules(self) -> None:
        pass
        #Rules.set_all_rules(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "death_link": self.options.death_link.value,
        }