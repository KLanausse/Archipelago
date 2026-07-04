from __future__ import annotations

import random
from typing import Dict, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .Types import ItemData, RobloxEggHuntItem, baseId

if TYPE_CHECKING:
    from .World import RobloxEggHuntWorld

filler_items: Dict[str, ItemData] = {
    "OOF":           ItemData(1, ItemClassification.filler),
}

SHUFFLED_ITEMS: Dict[str, ItemData] = {
    **filler_items,
}

ALL_ITEMS = {
    **SHUFFLED_ITEMS
}

ITEM_TABLE = {name: data.id+baseId for name, data in ALL_ITEMS.items()}


def get_random_filler_item_name(world: RobloxEggHuntWorld):
    return random.choice([name for name in filler_items]) # Temp

def create_item_with_correct_classification(world: RobloxEggHuntWorld, name: str) -> RobloxEggHuntItem:
    return RobloxEggHuntItem(name, ALL_ITEMS[name].classification, ALL_ITEMS[name].id, world.player)

def create_all_items(world: RobloxEggHuntWorld) -> None:
    itempool: list[Item] = [world.create_item(name) for name, data in SHUFFLED_ITEMS.items()]


    # Based off of APQuest Code
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool